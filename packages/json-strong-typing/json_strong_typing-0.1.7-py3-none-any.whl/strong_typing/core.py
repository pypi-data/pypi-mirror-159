from __future__ import annotations

from typing import Dict, List, Union


class JsonObject:
    "Placeholder type for an unrestricted JSON object."


class JsonArray:
    "Placeholder type for an unrestricted JSON array."


# a JSON type with possible `null` values
JsonType = Union[
    None,
    bool,
    int,
    float,
    str,
    Dict[str, "JsonType"],
    List["JsonType"],
]

# a JSON type that cannot contain `null` values
StrictJsonType = Union[
    bool,
    int,
    float,
    str,
    Dict[str, "StrictJsonType"],
    List["StrictJsonType"],
]

# a meta-type that captures the object type in a JSON schema
Schema = Dict[str, "StrictJsonType"]
