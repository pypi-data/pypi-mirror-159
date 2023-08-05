from __future__ import annotations

import dataclasses
import datetime
import decimal
import enum
import functools
import inspect
import json
import re
import typing
import uuid
from copy import deepcopy
from typing import (
    Any,
    Callable,
    ClassVar,
    Dict,
    List,
    Literal,
    Optional,
    Tuple,
    Type,
    TypeVar,
    Union,
    overload,
)

import jsonschema

from . import docstring
from .auxiliary import (
    Alias,
    IntegerRange,
    MaxLength,
    MinLength,
    Precision,
    get_auxiliary_format,
)
from .core import JsonArray, JsonObject, JsonType, Schema, StrictJsonType
from .inspection import (
    get_annotation,
    get_class_properties,
    is_dataclass_type,
    is_type_enum,
    is_type_optional,
    unwrap_optional_type,
)
from .name import python_type_to_name
from .serialization import object_to_json

# determines the maximum number of distinct enum members up to which a Dict[EnumType, Any] is converted into a JSON
# schema with explicitly listed properties (rather than employing a pattern constraint on property names)
OBJECT_ENUM_EXPANSION_LIMIT = 4


T = TypeVar("T")


def check_type(data_type: type) -> None:
    """
    Checks if the object is a type or type-like object (e.g. generic type).

    :param data_type: The object to validate.
    """

    if isinstance(data_type, type):
        # a standard type
        return
    elif typing.get_origin(data_type) is not None:
        # a generic type such as `List`, `Dict` or `Set`
        return
    elif hasattr(data_type, "__forward_arg__"):
        # an instance of `ForwardRef`
        return
    elif data_type is Any:
        # the special form `Any`
        return

    raise TypeError(
        f"expected a type but got an instance of {type(data_type)}: {data_type}"
    )


def get_class_docstrings(data_type: type) -> Tuple[Optional[str], Optional[str]]:
    check_type(data_type)
    docstr = docstring.parse_type(data_type)

    # check if class has a doc-string other than the auto-generated string assigned by @dataclass
    if is_dataclass_type(data_type) and re.match(
        f"^{re.escape(data_type.__name__)}[(].*[)]$", data_type.__doc__
    ):
        return None, None

    return docstr.short_description, docstr.long_description


def get_class_property_docstrings(
    data_type: type, transform_fun: Callable[[type, str, str], str] = None
) -> Dict[str, str]:
    """
    Extracts the documentation strings associated with the properties of a composite type.

    :param data_type: The object whose properties to iterate over.
    :param transform_fun: An optional function that maps a property documentation string to a custom tailored string.
    :returns: A dictionary mapping property names to descriptions.
    """

    check_type(data_type)
    result = {}
    for base in inspect.getmro(data_type):
        docstr = docstring.parse_type(base)
        for param in docstr.params.values():
            if param.name in result:
                continue

            if transform_fun:
                description = transform_fun(data_type, param.name, param.description)
            else:
                description = param.description

            result[param.name] = description
    return result


def docstring_to_schema(data_type: type) -> Schema:
    check_type(data_type)
    short_description, long_description = get_class_docstrings(data_type)
    schema = dict()
    if short_description:
        schema["title"] = short_description
    if long_description:
        schema["description"] = long_description
    return schema


class _TypeCatalogAuto:
    "Marker object for a type whose schema is automatically generated on the fly."


@dataclasses.dataclass
class TypeCatalogEntry:
    schema: Schema
    identifier: str
    examples: Optional[JsonType] = None


class TypeCatalog:
    "Maintains an association of well-known Python types to their JSON schema."

    _by_type: Dict[type, TypeCatalogEntry]
    _by_name: Dict[str, TypeCatalogEntry]

    def __init__(self):
        self._by_type = {}
        self._by_name = {}

    def __contains__(self, data_type: type) -> bool:
        if isinstance(data_type, typing.ForwardRef):
            fwd: typing.ForwardRef = data_type
            name = fwd.__forward_arg__
            return name in self._by_name
        else:
            return data_type in self._by_type

    def add(
        self,
        data_type: type,
        schema: Schema,
        identifier: str,
        examples: List[JsonType] = None,
    ) -> None:

        if isinstance(data_type, typing.ForwardRef):
            raise TypeError("forward references cannot be used to register a type")

        if data_type in self._by_type:
            raise ValueError(f"type {data_type} is already registered in the catalog")

        entry = TypeCatalogEntry(schema, identifier, examples)
        self._by_type[data_type] = entry
        self._by_name[identifier] = entry

    def get(self, data_type: type) -> TypeCatalogEntry:
        if isinstance(data_type, typing.ForwardRef):
            fwd: typing.ForwardRef = data_type
            name = fwd.__forward_arg__
            return self._by_name[name]
        else:
            return self._by_type[data_type]


@dataclasses.dataclass
class SchemaOptions:
    definitions_path: str = "#/definitions/"
    use_descriptions: bool = True
    use_examples: bool = True
    property_description_fun: Callable[[type, str, str], str] = None


class JsonSchemaGenerator:
    "Creates a JSON schema with user-defined type definitions."

    type_catalog: ClassVar[TypeCatalog] = TypeCatalog()
    types_used: Dict[str, type]
    options: SchemaOptions

    def __init__(self, options: SchemaOptions = None):
        if options is None:
            self.options = SchemaOptions
        else:
            self.options = options
        self.types_used = {}

    @functools.singledispatchmethod
    def _metadata_to_schema(self, arg) -> Schema:
        # unrecognized annotation
        return {}

    @_metadata_to_schema.register
    def _(self, arg: IntegerRange) -> Schema:
        return {"minimum": arg.minimum, "maximum": arg.maximum}

    @_metadata_to_schema.register
    def _(self, arg: Precision) -> Schema:
        return {
            "multipleOf": 10 ** (-arg.decimal_digits),
            "exclusiveMinimum": -(10**arg.integer_digits),
            "exclusiveMaximum": (10**arg.integer_digits),
        }

    @_metadata_to_schema.register
    def _(self, arg: MinLength) -> Schema:
        return {"minLength": arg.value}

    @_metadata_to_schema.register
    def _(self, arg: MaxLength) -> Schema:
        return {"maxLength": arg.value}

    def _with_metadata(
        self, type_schema: Schema, metadata: Optional[Tuple[Any, ...]]
    ) -> Schema:
        if metadata:
            for m in metadata:
                type_schema.update(self._metadata_to_schema(m))
        return type_schema

    def _simple_type_to_schema(self, typ: type) -> Schema:
        "Returns the JSON schema associated with a simple, unrestricted type."

        if typ is type(None):
            return {"type": "null"}
        elif typ is bool:
            return {"type": "boolean"}
        elif typ is int:
            return {"type": "integer"}
        elif typ is float:
            return {"type": "number"}
        elif typ is str:
            return {"type": "string"}
        elif typ is bytes:
            return {"type": "string", "contentEncoding": "base64"}
        elif typ is datetime.datetime:
            # 2018-11-13T20:20:39+00:00
            return {
                "type": "string",
                "format": "date-time",
            }
        elif typ is datetime.date:
            # 2018-11-13
            return {"type": "string", "format": "date"}
        elif typ is datetime.time:
            # 20:20:39+00:00
            return {"type": "string", "format": "time"}
        elif typ is decimal.Decimal:
            return {"type": "number"}
        elif typ is uuid.UUID:
            # f81d4fae-7dec-11d0-a765-00a0c91e6bf6
            return {"type": "string", "format": "uuid"}
        elif typ is Any:
            return {
                "oneOf": [
                    {"type": "null"},
                    {"type": "boolean"},
                    {"type": "number"},
                    {"type": "string"},
                    {"type": "array"},
                    {"type": "object"},
                ]
            }
        elif typ is JsonObject:
            return {"type": "object"}
        elif typ is JsonArray:
            return {"type": "array"}
        else:
            # not a simple type
            return None

    def type_to_schema(self, data_type: type, force_expand: bool = False) -> Schema:
        """
        Returns the JSON schema associated with a type.

        :param data_type: The Python type whose JSON schema to return.
        :param force_expand: Forces a JSON schema to be returned even if the type is registered in the catalog of known types.
        :returns: The JSON schema associated with the type.
        """

        # short-circuit for common simple types
        schema = self._simple_type_to_schema(data_type)
        if schema is not None:
            return schema

        # types registered in the type catalog of well-known types
        if not force_expand and data_type in __class__.type_catalog:
            # user-defined type
            identifier = __class__.type_catalog.get(data_type).identifier
            self.types_used[identifier] = data_type
            return {"$ref": f"{self.options.definitions_path}{identifier}"}

        # unwrap annotated types
        metadata = getattr(data_type, "__metadata__", None)
        if metadata is not None:
            # type is Annotated[T, ...]
            typ = typing.get_args(data_type)[0]

            schema = self._simple_type_to_schema(typ)
            if schema is not None:
                # recognize well-known auxiliary types
                fmt = get_auxiliary_format(data_type)
                if fmt is not None:
                    schema.update({"format": fmt})
                    return schema
                else:
                    return self._with_metadata(schema, metadata)

        else:
            # type is a regular type
            typ = data_type

        if isinstance(typ, typing.ForwardRef):
            fwd: typing.ForwardRef = typ
            identifier = fwd.__forward_arg__
            typ = eval(identifier)
            self.types_used[identifier] = typ
            return {"$ref": f"{self.options.definitions_path}{identifier}"}

        if is_type_enum(typ):
            enum_type: Type[enum.Enum] = typ
            enum_values = [e.value for e in enum_type]
            enum_value_types = list(dict.fromkeys(type(value) for value in enum_values))
            if len(enum_value_types) != 1:
                raise ValueError(
                    f"enumerations must have a consistent member value type but several types found: {enum_value_types}"
                )

            enum_value_type = enum_value_types[0]
            if enum_value_type is bool:
                enum_schema_type = "boolean"
            elif enum_value_type is int:
                enum_schema_type = "integer"
            elif enum_value_type is float:
                enum_schema_type = "number"
            elif enum_value_type is str:
                enum_schema_type = "string"
            else:
                raise ValueError(
                    f"unsupported enumeration member value type: {enum_value_type}"
                )

            enum_schema = {"type": enum_schema_type, "enum": enum_values}
            if self.options.use_descriptions:
                enum_schema.update(docstring_to_schema(typ))
            return enum_schema

        origin_type = typing.get_origin(typ)
        if origin_type is list:
            (list_type,) = typing.get_args(typ)  # unpack single tuple element
            return {"type": "array", "items": self.type_to_schema(list_type)}
        elif origin_type is dict:
            key_type, value_type = typing.get_args(typ)
            if not (key_type is str or key_type is int or is_type_enum(key_type)):
                raise ValueError(
                    "`dict` with key type not coercible to `str` is not supported"
                )

            value_schema = self.type_to_schema(value_type)
            if is_type_enum(key_type):
                enum_values = [e.value for e in key_type]
                if len(enum_values) > OBJECT_ENUM_EXPANSION_LIMIT:
                    dict_schema = {
                        "propertyNames": {
                            "pattern": "^(" + "|".join(enum_values) + ")$"
                        },
                        "additionalProperties": value_schema,
                    }
                else:
                    dict_schema = {
                        "properties": dict(
                            (str(value), value_schema) for value in enum_values
                        ),
                        "additionalProperties": False,
                    }
            else:
                dict_schema = {"additionalProperties": value_schema}

            schema = {"type": "object"}
            schema.update(dict_schema)
            return schema
        elif origin_type is set:
            (set_type,) = typing.get_args(typ)  # unpack single tuple element
            return {
                "type": "array",
                "items": self.type_to_schema(set_type),
                "uniqueItems": True,
            }
        elif origin_type is tuple:
            args = typing.get_args(typ)
            return {
                "type": "array",
                "minItems": len(args),
                "maxItems": len(args),
                "prefixItems": [
                    self.type_to_schema(member_type) for member_type in args
                ],
            }
        elif origin_type is Union:
            return {
                "oneOf": [
                    self.type_to_schema(union_type)
                    for union_type in typing.get_args(typ)
                ]
            }
        elif origin_type is Literal:
            (literal_value,) = typing.get_args(typ)  # unpack value of literal type
            schema = self.type_to_schema(type(literal_value))
            schema["const"] = literal_value
            return schema
        elif origin_type is type:
            (concrete_type,) = typing.get_args(typ)  # unpack single tuple element
            return {"const": self.type_to_schema(concrete_type, force_expand=True)}

        # dictionary of class attributes
        members = dict(inspect.getmembers(typ, lambda a: not inspect.isroutine(a)))

        property_docstrings = get_class_property_docstrings(
            typ, self.options.property_description_fun
        )

        properties: Dict[str, Schema] = {}
        required: List[Schema] = []
        for property_name, property_type in get_class_properties(typ):
            # rename property if an alias name is specified
            alias = get_annotation(property_type, Alias)
            if alias:
                output_name = alias.name
            else:
                output_name = property_name

            if is_type_optional(property_type):
                optional_type = unwrap_optional_type(property_type)
                property_def = self.type_to_schema(optional_type)
            else:
                property_def = self.type_to_schema(property_type)
                required.append(output_name)

            # check if attribute has a default value initializer
            if members.get(property_name) is not None:
                def_value = members[property_name]
                # check if value can be directly represented in JSON
                if isinstance(
                    def_value,
                    (
                        bool,
                        int,
                        float,
                        str,
                        enum.Enum,
                        datetime.datetime,
                        datetime.date,
                        datetime.time,
                    ),
                ):
                    property_def["default"] = object_to_json(def_value)

            # add property docstring if available
            property_doc = property_docstrings.get(property_name)
            if property_doc:
                property_def["title"] = property_doc
                property_def.pop("description", None)

            properties[output_name] = property_def

        schema = {"type": "object"}
        if len(properties) > 0:
            schema["properties"] = properties
            schema["additionalProperties"] = False
        if len(required) > 0:
            schema["required"] = required
        if self.options.use_descriptions:
            schema.update(docstring_to_schema(typ))
        return schema

    def _type_to_schema_with_lookup(self, data_type: type) -> Schema:
        """
        Returns the JSON schema associated with a type that may be registered in the catalog of known types.

        :param data_type: The type whose JSON schema we seek.
        :returns: The JSON schema associated with the type.
        """

        entry = __class__.type_catalog.get(data_type)
        if entry.schema is None:
            type_schema = self.type_to_schema(data_type, force_expand=True)
        else:
            type_schema = deepcopy(entry.schema)

        # add descriptive text (if present)
        if self.options.use_descriptions:
            type_schema.update(docstring_to_schema(data_type))

        # add example (if present)
        if self.options.use_examples and entry.examples:
            type_schema["examples"] = entry.examples

        return type_schema

    def classdef_to_schema(
        self, data_type: type, force_expand: bool = False
    ) -> Tuple[Schema, Dict[str, Schema]]:
        """
        Returns the JSON schema associated with a type and any nested types.

        :param data_type: The type whose JSON schema to return.
        :param force_expand: True if a full JSON schema is to be returned even for well-known types; false if a schema
        reference is to be used for well-known types.
        :returns: A tuple of the JSON schema, and a mapping between nested type names and their corresponding schema.
        """

        self.types_used = {}
        try:
            type_schema = self.type_to_schema(data_type, force_expand=force_expand)

            types_defined = {}
            while len(self.types_used) > len(types_defined):
                # make a snapshot copy; original collection is going to be modified
                types_undefined = {
                    sub_name: sub_type
                    for sub_name, sub_type in self.types_used.items()
                    if sub_name not in types_defined
                }

                # expand undefined types, which may lead to additional types to be defined
                for sub_name, sub_type in types_undefined.items():
                    types_defined[sub_name] = self._type_to_schema_with_lookup(sub_type)

            type_definitions = dict(sorted(types_defined.items()))
        finally:
            self.types_used = {}

        return type_schema, type_definitions


class Validator(enum.Enum):
    "Defines constants for JSON schema standards."

    Draft7 = jsonschema.Draft7Validator
    Draft201909 = jsonschema.Draft201909Validator
    Draft202012 = jsonschema.Draft202012Validator
    Latest = jsonschema.Draft202012Validator


def classdef_to_schema(
    data_type: type,
    options: SchemaOptions = None,
    validator: Validator = Validator.Latest,
) -> Schema:
    """
    Returns the JSON schema corresponding to the given type.

    :param data_type: The Python type used to generate the JSON schema
    :returns: A JSON object that you can serialize to a JSON string with json.dump or json.dumps
    :raises TypeError: Indicates that the generated JSON schema does not validate against the desired meta-schema.
    """

    # short-circuit with an error message when passing invalid data
    check_type(data_type)

    generator = JsonSchemaGenerator(options)
    type_schema, type_definitions = generator.classdef_to_schema(data_type)

    class_schema = {}
    if type_definitions:
        class_schema["definitions"] = type_definitions
    class_schema.update(type_schema)

    validator_id = validator.value.META_SCHEMA["$id"]
    try:
        validator.value.check_schema(class_schema)
    except jsonschema.exceptions.SchemaError:
        raise TypeError(
            f"schema does not validate against meta-schema <{validator_id}>"
        )

    schema = {"$schema": validator_id}
    schema.update(class_schema)
    return schema


def validate_object(data_type: type, json_dict: JsonType) -> None:
    """
    Validates if the JSON dictionary object conforms to the expected type.

    :param data_type: The type to match against.
    :param json_dict: A JSON object obtained with `json.load` or `json.loads`.
    :raises jsonschema.exceptions.ValidationError: Indicates that the JSON object cannot represent the type.
    """

    check_type(data_type)
    schema_dict = classdef_to_schema(data_type)
    jsonschema.validate(
        json_dict, schema_dict, format_checker=jsonschema.FormatChecker()
    )


def print_schema(data_type: type) -> None:
    """Pretty-prints the JSON schema corresponding to the type."""

    s = classdef_to_schema(data_type)
    print(json.dumps(s, indent=4))


def get_schema_identifier(data_type: type) -> Optional[str]:
    if data_type in JsonSchemaGenerator.type_catalog:
        return JsonSchemaGenerator.type_catalog.get(data_type).identifier
    else:
        return None


def register_schema(
    data_type: Type[T],
    schema: Schema = None,
    name: str = None,
    examples: List[JsonType] = None,
) -> Type[T]:
    """
    Associates a type with a JSON schema definition.

    :param data_type: The type to associate with a JSON schema.
    :param schema: The schema to associate the type with. Derived automatically if omitted.
    :param name: The name used for looking uo the type. Determined automatically if omitted.
    :returns: The input type.
    """

    check_type(data_type)
    JsonSchemaGenerator.type_catalog.add(
        data_type,
        schema,
        name if name is not None else python_type_to_name(data_type),
        examples,
    )
    return data_type


@overload
def json_schema_type(cls: Type[T], /) -> Type[T]:
    ...


@overload
def json_schema_type(cls: None, /) -> Callable[[Type[T]], Type[T]]:
    ...


def json_schema_type(cls: Type[T] = None, /, *, schema: Schema = None):
    """Decorator to add user-defined schema definition to a class."""

    def wrap(cls: Type[T]) -> Type[T]:
        return register_schema(cls, schema)

    # see if decorator is used as @json_schema_type or @json_schema_type()
    if cls is None:
        # called with parentheses
        return wrap
    else:
        # called as @json_schema_type without parentheses
        return wrap(cls)


register_schema(JsonObject, name="JsonObject")
register_schema(JsonArray, name="JsonArray")

register_schema(
    JsonType,
    name="JsonType",
    examples=[
        {
            "property1": None,
            "property2": True,
            "property3": 64,
            "property4": "string",
            "property5": ["item"],
            "property6": {"key": "value"},
        }
    ],
)
register_schema(
    StrictJsonType,
    name="StrictJsonType",
    examples=[
        {
            "property1": True,
            "property2": 64,
            "property3": "string",
            "property4": ["item"],
            "property5": {"key": "value"},
        }
    ],
)
