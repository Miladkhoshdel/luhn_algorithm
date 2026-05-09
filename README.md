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
from luhn import append_check_digit, calculate_check_digit, is_valid

print(is_valid("79927398713"))
print(calculate_check_digit("7992739871"))
print(append_check_digit("7992739871"))
```

## Test

Run the test suite with:

```bash
python3 -m unittest -v
```
