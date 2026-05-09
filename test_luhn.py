import unittest

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

    def test_rejects_non_digit_payloads(self):
        with self.assertRaises(ValueError):
            calculate_check_digit("123x")


if __name__ == "__main__":
    unittest.main()
