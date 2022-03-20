import unittest
from solve import solve


class SolveTest(unittest.TestCase):

    def test_no_sqrt(self):
        """Тест, который проверяет, что для уравнения x^2+1 = 0 корней нет"""
        self.assertEqual([], solve(1, 0, 1))

    def test_two_sqrt(self):
        """Тест, который проверяет, что для уравнения x^2-1 = 0 есть два корня"""
        self.assertEqual([1, -1], solve(1, 0, -1))

    def test_one_sqrt(self):
        """Тест, который проверяет, что для уравнения есть один корень.
        если дискриминант ровно равен 0, и если дискриминант не ноль, но меньше заданного epsilon"""
        self.assertEqual([-1], solve(1, 2, 1))
        self.assertEqual([-1], solve(1, 2, 1.000000001))

    def test_a_no_equal_zero(self):
        """Тест, который проверяет, что коэффициент a не может быть равен 0
        с учетом, что a - число с плавающей точкой, успешно выполняется"""
        with self.assertRaises(Exception):
            solve(0, 1, 2)
        solve(0.0001, 1, 2)

    def test_type(self):
        """Тест, который проверяет, что solve не может принимать значения, отличные от чиcел"""
        with self.assertRaises(TypeError):
            solve('a', 0, 3)

        with self.assertRaises(TypeError):
            solve('a', 0x31, None)


if __name__ == '__main__':
    unittest.main()
