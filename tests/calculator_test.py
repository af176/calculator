import unittest

from server import calculate_formula


class TestCalculateFormula(unittest.TestCase):
    def test_valid_formulas(self):
        valid_formulas = [
            ("1 + 2", 3),
            ("2*A1+2Z", 6),
            ("3*A5+2*2Z + 7", 34),
            ("-1*A6+3Z", -9),
            ("10+20Z","Invalid formula: Invalid brackets"),
            ("A2Z", "Invalid formula: Invalid brackets"),
            ("A5/0Z", "Invalid formula: Division by zero"),
            ("$@#", "Error: Invalid characters in the formula"),
        ]

        for formula, expected_result in valid_formulas:
            result = calculate_formula(formula)
            self.assertEqual(result, expected_result)

if __name__ == '__main__':
    unittest.main()
