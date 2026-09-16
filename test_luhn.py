import subprocess
import sys
import unittest
from pathlib import Path

from luhn import append_check_digit, calculate_check_digit, checksum, is_valid


class LuhnTests(unittest.TestCase):
    def test_valid_known_numbers(self):
        self.assertTrue(is_valid("79927398713"))
        self.assertTrue(is_valid("4539 1488 0343 6467"))
        self.assertTrue(is_valid("6011-1111-1111-1117"))

    def test_invalid_numbers(self):
        self.assertFalse(is_valid("79927398714"))
        self.assertFalse(is_valid("4539 1488 0343 6468"))
        self.assertFalse(is_valid("abc"))
        self.assertFalse(is_valid(""))

    def test_checksum(self):
        self.assertEqual(checksum("79927398713"), 0)
        self.assertEqual(checksum("79927398714"), 1)

    def test_calculate_check_digit(self):
        self.assertEqual(calculate_check_digit("7992739871"), 3)
        self.assertEqual(calculate_check_digit(7992739871), 3)

    def test_append_check_digit(self):
        self.assertEqual(append_check_digit("7992739871"), "79927398713")

    def test_generated_numbers_have_valid_checksums(self):
        for payload in ("0", "7", "12", "000", "7992739871", 7992739871):
            with self.subTest(payload=payload):
                number = append_check_digit(payload)
                self.assertTrue(is_valid(number))
                self.assertEqual(checksum(number), 0)

    def test_other_check_digits_are_invalid(self):
        for payload in ("0", "12", "7992739871"):
            number = append_check_digit(payload)

            for digit in "0123456789":
                if digit == number[-1]:
                    continue

                with self.subTest(payload=payload, check_digit=digit):
                    self.assertFalse(is_valid(number[:-1] + digit))

    def test_supported_separators_are_removed(self):
        for separator in (" ", "-", ".", "/", "\\", ","):
            with self.subTest(separator=separator):
                self.assertTrue(is_valid("799" + separator + "27398713"))
                self.assertEqual(
                    append_check_digit("799" + separator + "2739871"),
                    "79927398713",
                )

        self.assertTrue(is_valid(" 799-273.987/1\\3, "))
        self.assertEqual(append_check_digit(" 799-273.987/1\\, "), "79927398713")
        self.assertEqual(append_check_digit("000"), "0000")

    def test_separator_only_input_is_rejected(self):
        value = " -./\\, "
        self.assertFalse(is_valid(value))

        for function in (checksum, calculate_check_digit, append_check_digit):
            with self.subTest(function=function.__name__), self.assertRaises(
                ValueError
            ):
                function(value)

    def test_rejects_non_digit_payloads(self):
        expected_message = (
            "value must contain digits only, with optional spaces, hyphens, "
            "dots, slashes, backslashes, or commas"
        )

        with self.assertRaisesRegex(ValueError, expected_message):
            calculate_check_digit("123x")

    def test_rejects_unsupported_types(self):
        unsupported_values = (7992739871.3, 0.0, True, None)

        for value in unsupported_values:
            with self.subTest(value=value):
                self.assertFalse(is_valid(value))

                for function in (checksum, calculate_check_digit, append_check_digit):
                    with self.assertRaises(TypeError):
                        function(value)

    def test_cli_exit_status_reflects_validity(self):
        script = Path(__file__).with_name("luhn.py")

        for number, expected_output, expected_status in (
            ("79927398713", "valid", 0),
            ("79927398714", "invalid", 1),
            ("abc", "invalid", 1),
        ):
            with self.subTest(number=number):
                result = subprocess.run(
                    [sys.executable, str(script), number],
                    capture_output=True,
                    text=True,
                    check=False,
                )

                self.assertEqual(result.stdout.strip(), expected_output)
                self.assertEqual(result.returncode, expected_status)

    def test_cli_requires_a_number(self):
        script = Path(__file__).with_name("luhn.py")
        result = subprocess.run(
            [sys.executable, str(script)],
            capture_output=True,
            text=True,
            check=False,
        )

        self.assertEqual(result.returncode, 2)
        self.assertEqual(result.stdout, "")
        self.assertIn("required", result.stderr)


if __name__ == "__main__":
    unittest.main()
