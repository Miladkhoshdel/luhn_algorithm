# Luhn Algorithm

A small, dependency-free Python implementation of the Luhn algorithm.

## Features

- Validate complete numbers with `is_valid`
- Calculate a checksum with `checksum`
- Generate a check digit with `calculate_check_digit`
- Append a valid check digit with `append_check_digit`
- Accept digits with optional spaces or hyphens

## Requirements

- Python 3.8+

## Run

Validate a number from the command line:

```bash
python3 luhn.py 79927398713
```

Expected output:

```text
valid
```

Invalid numbers print:

```text
invalid
```

## Use In Python

```python
from luhn import append_check_digit, calculate_check_digit, checksum, is_valid

print(is_valid("79927398713"))
print(checksum("79927398713"))
print(calculate_check_digit("7992739871"))
print(append_check_digit("7992739871"))
```

## Function Use Cases

| Function | Use case | Example |
| --- | --- | --- |
| `is_valid(value)` | Check whether a complete number already has a valid Luhn check digit. Useful before accepting account numbers, card-like identifiers, or other Luhn-protected values. | `is_valid("4539 1488 0343 6467")` returns `True` |
| `checksum(value)` | Inspect the Luhn checksum for a complete number. A checksum of `0` means the full value is valid; any other result can help with debugging or custom validation flows. | `checksum("79927398714")` returns `1` |
| `calculate_check_digit(payload)` | Generate the check digit for a payload that does not include one yet. Use this when creating a new identifier that should pass Luhn validation after the digit is appended. | `calculate_check_digit("7992739871")` returns `3` |
| `append_check_digit(payload)` | Build the final valid value in one step by appending the calculated check digit to the payload. | `append_check_digit("7992739871")` returns `"79927398713"` |

The module also includes `_digits(value)`, an internal helper used by the public
functions to normalize input by removing spaces and hyphens. Application code
should normally use the public functions above instead of calling `_digits`
directly.

## Test

Run the test suite with:

```bash
python3 -m unittest -v
```
