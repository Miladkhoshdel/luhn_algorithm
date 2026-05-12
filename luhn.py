"""Utilities for validating and generating Luhn check digits."""

from __future__ import annotations

from typing import Union

NumberLike = Union[str, int]
REMOVE_CHARS = " -./\\,"
DIGIT_CLEANUP_TABLE = str.maketrans("", "", REMOVE_CHARS)


def _digits(value: NumberLike) -> str:
    """Return only digits, allowing spaces, hyphens, dots, slashes, backslashes, and commas as separators."""
    cleaned = str(value).strip().translate(DIGIT_CLEANUP_TABLE)

    if not cleaned or not cleaned.isdigit():
        raise ValueError(
            "value must contain digits only, with optional spaces or hyphens"
        )

    return cleaned


def checksum(value: NumberLike) -> int:
    """Return the Luhn validation checksum for a complete number."""
    digits = _digits(value)

    total = 0
    should_double = False

    for digit in reversed(digits):
        number = int(digit)

        if should_double:
            number *= 2

            if number > 9:
                number -= 9

        total += number
        should_double = not should_double

    return total % 10


def is_valid(value: NumberLike) -> bool:
    """Return whether the value satisfies the Luhn algorithm."""

    try:
        is_valid_checksum = checksum(value) == 0
    except ValueError:
        return False

    return is_valid_checksum


def calculate_check_digit(payload: NumberLike) -> int:
    """Return the Luhn check digit to append to the payload."""

    digits = _digits(payload)
    total = 0
    should_double = True

    for digit in reversed(digits):
        number = int(digit)

        if should_double:
            number *= 2

            if number > 9:
                number -= 9

        total += number
        should_double = not should_double

    return (10 - total % 10) % 10


def append_check_digit(payload: NumberLike) -> str:
    """Return the payload with a valid Luhn check digit appended."""
    payload = _digits(payload)
    return f"{payload}{calculate_check_digit(payload)}"


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(
        description="Validate a number with the Luhn algorithm."
    )
    parser.add_argument("number", help="number to validate")
    args = parser.parse_args()

    print("valid" if is_valid(args.number) else "invalid")
