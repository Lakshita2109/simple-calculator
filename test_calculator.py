import unittest

from calculator import add, divide, multiply, subtract


class CalculatorTests(unittest.TestCase):
    def test_basic_operations(self):
        self.assertEqual(add(2, 3), 5)
        self.assertEqual(subtract(7, 4), 3)
        self.assertEqual(multiply(6, 7), 42)

    def test_divide_rounds_to_4_places(self):
        self.assertEqual(divide(10, 3), 3.3333)

    def test_divide_by_zero_raises(self):
        with self.assertRaises(ValueError):
            divide(1, 0)


if __name__ == "__main__":
    unittest.main()
