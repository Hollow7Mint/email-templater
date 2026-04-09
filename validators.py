import re
from typing import Any, Callable

EMAIL_RE = re.compile(r'^[\w.+-]+@[\w-]+\.[\w.-]+$')
PHONE_RE = re.compile(r'^\+?[\d\s\-().]{7,20}$')

Rule = Callable[[str, Any], str | None]


def required(field: str, value: Any) -> str | None:
    if value is None or (isinstance(value, str) and not value.strip()):
        return f"{field} is required"
    return None


def min_len(n: int) -> Rule:
    def check(field: str, value: Any) -> str | None:
        if value is not None and len(str(value)) < n:
            return f"{field} must be at least {n} characters"
        return None
    return check


def max_len(n: int) -> Rule:
    def check(field: str, value: Any) -> str | None:
        if value is not None and len(str(value)) > n:
            return f"{field} must be at most {n} characters"
        return None
    return check


def is_email(field: str, value: Any) -> str | None:
    if value and not EMAIL_RE.match(str(value)):
        return f"{field} is not a valid email"
    return None


def is_phone(field: str, value: Any) -> str | None:
    if value and not PHONE_RE.match(str(value)):
        return f"{field} is not a valid phone number"
    return None


def is_positive(field: str, value: Any) -> str | None:
    try:
        if float(value) <= 0:
            return f"{field} must be positive"
    except (TypeError, ValueError):
        return f"{field} must be a number"
    return None


def one_of(*choices: Any) -> Rule:
    def check(field: str, value: Any) -> str | None:
        if value not in choices:
            opts = ", ".join(map(str, choices))
            return f"{field} must be one of: {opts}"
        return None
    return check


def validate(data: dict[str, Any], rules: dict[str, list[Rule]]) -> list[str]:
    errors: list[str] = []
    for field, checks in rules.items():
        for rule in checks:
            err = rule(field, data.get(field))
            if err:
                errors.append(err)
    return errors
