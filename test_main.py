
import unittest

from main import (
    calculate_total,
    calculate_average,
    calculate_grade,
    calculate_result
)


class TestStudentGradeSystem(unittest.TestCase):

    def test_total(self):
        self.assertEqual(
            calculate_total([80, 90, 70, 60, 100]),
            400
        )

    def test_average(self):
        self.assertEqual(
            calculate_average([80, 90, 70, 60, 100]),
            80
        )

    def test_grade(self):
        self.assertEqual(calculate_grade(95), "A+")
        self.assertEqual(calculate_grade(85), "A")
        self.assertEqual(calculate_grade(75), "B")

    def test_pass(self):
        self.assertEqual(
            calculate_result([80, 90, 70, 60, 100]),
            "PASS"
        )

    def test_fail(self):
        self.assertEqual(
            calculate_result([80, 90, 30, 60, 100]),
            "FAIL"
        )


if __name__ == "__main__":
    unittest.main()
