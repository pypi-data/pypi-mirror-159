from __future__ import annotations

import dataclasses
import datetime
import decimal
import re
import uuid
from collections.abc import Callable
from typing import Any, Generic, Literal, NewType, TypeVar, Union, cast

FieldName = NewType("FieldName", str)
ObjectName = NewType("ObjectName", str)


@dataclasses.dataclass(frozen=True)
class SerDeError:
    locator: FieldName | ObjectName
    problem: Problem


Problem = Union[str, frozenset[SerDeError]]

T = TypeVar("T")
V = TypeVar("V")
E = TypeVar("E")


@dataclasses.dataclass(frozen=True)
class Ok(Generic[T]):
    value: T
    type: Literal["ok"] = "ok"


@dataclasses.dataclass(frozen=True)
class Error(Generic[E]):
    error: E
    type: Literal["error"] = "error"


Result = Union[Ok[T], Error[E]]


def map_result(result: Result[T, E], mapper: Callable[[T], V]) -> Result[V, E]:
    if result.type == "ok":
        return Ok(mapper(result.value))
    return cast(Result[V, E], result)


def get_field(
    data: dict[str, Any],
    field: str,
    delegate: Callable[[Any], Result[T, Problem]],
    *,
    nullable: bool = False,
) -> Result[T, SerDeError]:
    raw_value = data.get(field, None)
    if not nullable and raw_value is None:
        return Error(SerDeError(locator=FieldName(field), problem="Missing required field"))
    result = delegate(raw_value)
    if result.type == "ok":
        return cast(Result[T, SerDeError], result)
    return Error(SerDeError(FieldName(field), problem=result.error))


def get_optional_field(
    data: dict[str, Any], field: str, delegate: Callable[[Any], Result[T, Problem]]
) -> Result[T | None, SerDeError]:
    raw_value = data.get(field, None)
    if raw_value is None:
        return Ok(None)
    result = delegate(raw_value)
    if result.type == "ok":
        return cast(Result[Union[T, None], SerDeError], result)
    return Error(SerDeError(FieldName(field), problem=result.error))


def get_enum(
    raw_value: Any, enum_factory: Callable[..., Result[T, SerDeError]]
) -> Result[T, Problem]:
    if not isinstance(raw_value, str):
        return _type_mismatch_error("string", raw_value)

    result = enum_factory(raw_value)
    if result.type == "ok":
        return cast(Result[T, Problem], result)
    return Error(frozenset((result.error,)))


def get_object(
    raw_value: Any,
    object_factory: Callable[..., Result[T, SerDeError]],
    *,
    ignore_unknown_properties: bool,
) -> Result[T, Problem]:
    if not isinstance(raw_value, dict):
        return _type_mismatch_error("object", raw_value)

    result = object_factory(raw_value, ignore_unknown_properties=ignore_unknown_properties)
    if result.type == "ok":
        return cast(Result[T, Problem], result)
    return Error(frozenset((result.error,)))


def _as_int32(value: int) -> Result[int, Problem]:
    if -(2**31) <= value <= (2**31 - 1):
        return Ok(value)

    return Error(f"{value} must be in int32 range [{-2**31}, {2**31 - 1}]")


def _as_int(value: Any) -> Result[int, Problem]:
    if isinstance(value, int):
        return _as_int32(value)
    else:
        if isinstance(value, str) and re.fullmatch("-?\\d+", value):
            try:
                return _as_int32(int(value))
            except Exception:
                pass

    return _type_mismatch_error("int", value)


def get_int(
    raw_value: Any,
    *,
    allow_number: bool = False,
    inclusive_min: int | None = None,
    inclusive_max: int | None = None,
    exclusive_min: int | None = None,
    exclusive_max: int | None = None,
) -> Result[int, Problem]:
    if allow_number:
        float_value = get_number(raw_value)
        if float_value.type == "ok":
            raw_value = int(float_value.value)

    int_result = _as_int(raw_value)
    if int_result.type == "error":
        return int_result

    int_value = int_result.value
    if inclusive_min is not None and int_value < inclusive_min:
        return Error(f"{int_value} must be at least {inclusive_min} inclusive")
    elif exclusive_min is not None and int_value <= exclusive_min:
        return Error(f"{int_value} must be at least {exclusive_min} exclusive")
    if inclusive_max is not None and int_value > inclusive_max:
        return Error(f"{int_value} must be at most {inclusive_max} inclusive")
    elif exclusive_max is not None and int_value >= exclusive_max:
        return Error(f"{int_value} must be at most {exclusive_max} exclusive")

    return Ok(int_value)


# TODO(forozco): reconcile decimal
def get_number(
    value: Any,
    *,
    inclusive_min: float | None = None,
    inclusive_max: float | None = None,
    exclusive_min: float | None = None,
    exclusive_max: float | None = None,
) -> Result[float, Problem]:
    if isinstance(value, float):
        float_value = value
    else:
        try:
            float_value = float(value)
        except:
            return _type_mismatch_error("float", value)

    if inclusive_min is not None and float_value < inclusive_min:
        return Error(f"{float_value} must be at least {inclusive_min} inclusive")
    elif exclusive_min is not None and float_value <= exclusive_min:
        return Error(f"{float_value} must be at least {exclusive_min} exclusive")
    if inclusive_max is not None and float_value > inclusive_max:
        return Error(f"{float_value} must be at most {inclusive_max} inclusive")
    elif exclusive_max is not None and float_value >= exclusive_max:
        return Error(f"{float_value} must be at most {exclusive_max} exclusive")

    return Ok(float_value)


def get_string(value: Any) -> Result[str, Problem]:
    if isinstance(value, str):
        return Ok(value)
    elif isinstance(value, int) or isinstance(value, float):
        return Ok(str(value))

    return _type_mismatch_error("string", value)


def get_uuid(value: Any) -> Result[uuid.UUID, Problem]:
    if isinstance(value, str):
        try:
            return Ok(uuid.UUID(value))
        except:
            return Error(f"{value} is not a valid UUID")
    return _type_mismatch_error("uuid", value)


def get_date(value: Any) -> Result[datetime.date, Problem]:
    if isinstance(value, str):
        try:
            return Ok(datetime.date.fromisoformat(value))
        except:
            return Error(f"{value} is not a valid date (dates must be in format yyyy-mm-dd)")
    return _type_mismatch_error("date", value)


def get_datetime(value: Any) -> Result[datetime.datetime, Problem]:
    if isinstance(value, str):
        try:
            return Ok(datetime.datetime.fromisoformat(value))
        except:
            return Error(
                f"{value} is not a valid datetime (dates must be in format yyyy-mm-dd'T'HH:mm:ss.sss)"
            )
    return _type_mismatch_error("datetime", value)


def get_boolean(value: Any) -> Result[bool, Problem]:
    if isinstance(value, bool):
        return Ok(value)

    return _type_mismatch_error("boolean", value)


def check_string_literal(value: Any, *, literal: str) -> Result[None, Problem]:
    result = get_string(value)
    if result.type == "ok":
        if not result.value == literal:
            return Error("foo")
    return cast(Result[None, Problem], result)


def get_list(
    raw_value: Any | None,
    *,
    element_deser: Callable[[Any], Result[T, Problem]],
    allow_single_value: bool = False,
    min_count: int | None = None,
    max_count: int | None = None,
) -> Result[list[T], Problem]:
    elements: list[T] | None = None
    if raw_value is None:
        elements = []
    elif isinstance(raw_value, list):
        elements = []
        errors: set[SerDeError] = set()
        for i, element in enumerate(raw_value):
            element_value = element_deser(element)
            if element_value.type == "error":
                errors.add(
                    SerDeError(locator=FieldName(f"Element {i}"), problem=element_value.error)
                )
            else:
                elements.append(element_value.value)
        if len(errors) > 0:
            return Error(frozenset(errors))
    elif allow_single_value:
        single_element = element_deser(raw_value)
        if single_element.type == "ok":
            elements = [single_element.value]
        else:
            return Error(single_element.error)

    if elements is None:
        return _type_mismatch_error("list", raw_value)

    if min_count is not None and len(elements) < min_count:
        return Error(
            f"Must contain at least {min_count} item{_pluralize(min_count)} (found {len(elements)} item{_pluralize(len(elements))})"
        )
    if max_count is not None and len(elements) > max_count:
        return Error(
            f"May contain at most {max_count} item{_pluralize(max_count)} (found {len(elements)} item{_pluralize(len(elements))})"
        )
    return Ok(elements)


def _pluralize(value: int | float) -> str:
    if value == 1:
        return ""
    return "s"


def get_dict(
    raw_value: Any | None,
    *,
    value_deser: Callable[[Any], Result[T, Problem]],
    min_count: int | None = None,
    max_count: int | None = None,
) -> Result[dict[str, T], Problem]:
    if raw_value is None:
        return Ok(dict())

    if isinstance(raw_value, dict):
        elements: dict[str, T] = {}
        errors: set[SerDeError] = set()
        for key, value in raw_value.items():
            parsed_value = value_deser(value)
            if parsed_value.type == "error":
                errors.add(SerDeError(locator=FieldName(f"Key {key}"), problem=parsed_value.error))
            else:
                elements[key] = parsed_value.value
        if len(errors) > 0:
            return Error(frozenset(errors))

        if min_count is not None and len(elements) < min_count:
            return Error(f"Dict with size {len(elements)} must have at least {min_count} elements")
        if max_count is not None and len(elements) > max_count:
            return Error(f"Dict with size {len(elements)} must have at most {max_count} elements")
        return Ok(elements)

    return _type_mismatch_error("dict", raw_value)


def normalize_error_details(serde_error: SerDeError) -> list[str]:
    if isinstance(serde_error.problem, str):
        return [serde_error.locator + ": " + serde_error.problem]

    result = []
    for problem in serde_error.problem:
        for inner_problem in normalize_error_details(problem):
            result.append(serde_error.locator + "." + inner_problem)

    return result


def _type_mismatch_error(target_type: str, value: Any) -> Error[Problem]:
    return Error(
        f"Unable to interpret value of type '{_to_human_readable_type(value)}' as a '{target_type}'"
    )


def _to_human_readable_type(value: Any) -> str:
    if isinstance(value, str):
        return "string"
    if isinstance(value, int):
        return "int"
    elif isinstance(value, float) or isinstance(value, decimal.Decimal):
        return "float"
    elif isinstance(value, bool):
        return "boolean"
    elif isinstance(value, list):
        return "list"
    elif isinstance(value, dict):
        return "object"

    return str(type(value))
