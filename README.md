# Luhn Algorithm

A small, dependency-free Python implementation of the
[Luhn algorithm](https://en.wikipedia.org/wiki/Luhn_algorithm) for validating
and generating check digits.

The Luhn algorithm is commonly used for credit-card-like numbers, IMEI numbers,
and other identifiers that need a simple typo-detection check. This project only
checks the Luhn checksum; it does not verify issuers, account status, number
lengths, or whether an identifier is real.

## Features

- Validate complete numbers with `is_valid`
- Calculate the checksum for a complete number with `checksum`
- Generate a check digit with `calculate_check_digit`
- Append a valid check digit with `append_check_digit`
- Accept strings or integers
- Ignore common separators: spaces, hyphens, dots, slashes, backslashes, and
  commas

## Requirements

- Python 3.8+
- No third-party packages

## Quick Start

Validate a number from the command line:

```bash
python3 luhn.py 79927398713
```

Output:

```text
valid
```

Invalid numbers print:

```text
invalid
```

Run the test suite:

```bash
python3 -m unittest -v
```

## Python Usage

```python
from luhn import append_check_digit, calculate_check_digit, checksum, is_valid

print(is_valid("79927398713"))
# True

print(checksum("79927398713"))
# 0

print(calculate_check_digit("7992739871"))
# 3

print(append_check_digit("7992739871"))
# "79927398713"
```

Formatted values are normalized before validation:

```python
is_valid("4539 1488 0343 6467")  # True
is_valid("6011-1111-1111-1117")  # True
```

## API

| Function | Returns | Description |
| --- | --- | --- |
| `is_valid(value)` | `bool` | Returns `True` when a complete value has a valid Luhn checksum. Invalid input, such as letters or an empty string, returns `False`. |
| `checksum(value)` | `int` | Returns the Luhn checksum for a complete value. A result of `0` means the value is valid. |
| `calculate_check_digit(payload)` | `int` | Calculates the digit that should be appended to a payload that does not include a check digit yet. |
| `append_check_digit(payload)` | `str` | Returns the payload with its calculated check digit appended. |

## Input Rules

All public functions accept `str` and `int` values. The implementation removes
these separators before processing:

```text
space  -  .  /  \  ,
```

After normalization, the value must contain at least one digit and no other
characters. `checksum`, `calculate_check_digit`, and `append_check_digit` raise
`ValueError` for invalid input. `is_valid` catches that error and returns
`False`, which makes it convenient for validation checks.

## Examples

Create a valid identifier from a payload:

```python
payload = "7992739871"
identifier = append_check_digit(payload)

assert identifier == "79927398713"
assert is_valid(identifier)
```

Inspect an invalid number:

```python
value = "79927398714"

assert checksum(value) == 1
assert not is_valid(value)
```

## Project Layout

```text
.
├── luhn.py       # implementation and command-line entry point
├── test_luhn.py  # unittest coverage
└── README.md
```
