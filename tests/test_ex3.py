import unittest

from exercises.ex3_0 import squared
from exercises.ex3_1 import solve_3_1
from exercises.ex3_2 import solve_3_2
MESSAGE_FMT = 'Kết quả đúng là `{0}`, nhận được `{1}`'


class TestExercise3(unittest.TestCase):
    def _test_all(self, func, cases):
        for input, expect in cases:
            msg = MESSAGE_FMT.format(expect, input)
            self.assertEqual(func(input), expect, msg)

    def test_ex3_0(self):
        res = squared(5)
        self.assertEqual(res, 25, MESSAGE_FMT.format(25, res))

    def test_ex3_1(self):
        cases = [(1, 1), (5, 1), (9, 1), (24, 1000), (10, 10)]
        self._test_all(solve_3_1, cases)

    def test_ex3_2(self):
        cases = [(-4, "this is negative number"),
                 (0, "this is zero"),
                 (10000, "this is positive number")
                 ]
        self._test_all(solve_3_2, cases)

    def test_ex3_3(self):
        # TODO
        pass

    def test_ex3_4(self):
        # TODO
        pass

    def test_ex3_5(self):
        # TODO
        pass

    def test_ex3_6(self):
        # TODO
        pass

    def test_ex3_7(self):
        # TODO
        pass

    def test_ex3_8(self):
        # TODO
        pass

    def test_ex3_9(self):
        # TODO
        pass


if __name__ == "__main__":
    unittest.main()
