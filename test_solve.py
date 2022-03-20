import unittest
from solve import solve


class SolveTest(unittest.TestCase):

    def test_no_sqrt(self):
        """Тест на проверку что корней нет"""
        self.assertEqual([], solve(1, 0, 1))

    def test_two_sqrt(self):
        """Тест на проверку что корня два"""
        self.assertEqual([1, -1], solve(1, 0, -1))

    def test_one_sqrt(self):
        """Тест на проверку что корень один"""
        self.assertEqual([-1], solve(1, 2, 1))

    def test_a_no_equal_zero(self):
        """Тест на проверку что аргумент а не равен 0"""
        with self.assertRaises(Exception):
            solve(0, 1, 1)

    def test_type(self):
        """Тест на проверку передаваемых типов"""
        with self.assertRaises(TypeError):
            solve('a', 0, 3)

        with self.assertRaises(TypeError):
            solve('a', 0x31, None)


if __name__ == '__main__':
    unittest.main()
