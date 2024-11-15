class TestDivide(TestCase):
    def test_both_positive(self):
        a, b = 4, 2
        answer = 2
        self.assertEqual(divide(a, b), answer)

    def test_positive_and_negative(self):
        a, b = 4, -2
        answer = -2
        self.assertEqual(divide(a, b), answer)

    def test_negative_and_positive(self):
        a, b = -4, 2
        answer = -2
        self.assertEqual(divide(a, b), answer)

    def test_both_negative(self):
        a, b = -4, -2
        answer = 2
        self.assertEqual(divide(a, b), answer)

    def test_both_equal(self):
        a, b = 1, 1
        answer = 1
        self.assertEqual(divide(a, b), answer)

    def test_fraction(self):
        a, b = 1, 2
        answer = 0.5
        self.assertEqual(divide(a, b), answer)

    def test_infinite_fraction(self):
        a, b = 1, 3
        answer = 1 / 3
        self.assertEqual(divide(a, b), answer)

    def test_division_by_zero(self):
        a, b = 4, 0
        answer = "Can't divide by zero"
        self.assertEqual(divide(a, b), answer)

    def test_zero_divided(self):
        a, b = 0, 4
        answer = 0
        self.assertEqual(divide(a, b), answer)

    def test_both_zero(self):
        a, b = 0, 0
        answer = "Can't divide by zero"
        self.assertEqual(divide(a, b), answer)

    def test_first_big(self):
        a, b = 10**16, 10
        answer = 10**15
        self.assertEqual(divide(a, b), answer)

    def test_second_big(self):
        a, b = 10, 10**16
        answer = 10**-15
        self.assertEqual(divide(a, b), answer)

    def test_both_big(self):
        a, b = 10**16, 10**15
        answer = 10
        self.assertEqual(divide(a, b), answer)

    def test_first_small(self):
        a, b = 10**-16, 10
        answer = 10**-17
        self.assertAlmostEqual(divide(a, b), answer, places=10)

    def test_second_small(self):
        a, b = 10, 10**-16
        answer = 10**17
        self.assertEqual(divide(a, b), answer)

    def test_both_small(self):
        a, b = 10**-16, 10**-15
        answer = 10**-1
        self.assertAlmostEqual(divide(a, b), answer, places=10)

    def test_big_and_small(self):
        a, b = 10**16, 10**-15
        answer = 10**31
        self.assertAlmostEqual(divide(a, b), answer, places=10)

    def test_small_and_big(self):
        a, b = 10**-16, 10**15
        answer = 10**-31
        self.assertAlmostEqual(divide(a, b), answer, places=10)

    def test_first_fractional(self):
        a, b = 0.5, 2
        answer = 0.25
        self.assertEqual(divide(a, b), answer)

    def test_second_fractional(self):
        a, b = 2, 0.5
        answer = 4
        self.assertEqual(divide(a, b), answer)

    def test_both_fractional(self):
        a, b = 0.5, 0.25
        answer = 2
        self.assertEqual(divide(a, b), answer)

    def test_non_numeric_input(self):
        with self.assertRaises(TypeError):
            divide("a", 5)
        with self.assertRaises(TypeError):
            divide(5, "b")