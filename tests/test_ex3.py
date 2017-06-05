import unittest

from exercises.ex3_0 import squared
from exercises.ex3_1 import solve_3_1
from exercises.ex3_2 import solve_3_2
from exercises.ex5_1 import solve_5_1, data as ex5_colors
import exercises.ex5_2 as ex5_2


class TestExercise(unittest.TestCase):
    MESSAGE_FMT = 'Kết quả đúng là `{0}`, nhận được `{1}`'

    def _test_all(self, func, cases):
        for input, expect in cases:
            output = func(input)
            msg = self.MESSAGE_FMT.format(expect, output)
            self.assertEqual(output, expect, msg)


class TestExercise3(TestExercise):

    def test_ex3_0(self):
        res = squared(5)
        self.assertEqual(res, 25, self.MESSAGE_FMT.format(25, res))

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


class TestExercise5(TestExercise):
    def test_ex5_1(self):
        res = solve(ex5_colors)
        self.assertEqual(len(res), len('Google'),
                         'Kết quả không đủ các chữ cái')
        self.assertEqual(res[0], ('G', '#4885ed'), 'Sai màu')

    def test_ex5_2(self):
        res = ex5_2.solve([])
        self.assertTrue(isinstance(res, list))
        # TODO

    def test_ex5_3(self):
        # TODO
        pass

    def test_ex5_4(self):
        # TODO
        pass

    def test_ex5_5(self):
        # TODO
        pass

    def test_ex5_6(self):
        # TODO
        pass

    def test_ex5_7(self):
        # TODO
        pass

    def test_ex5_8(self):
        # TODO
        pass

    def test_ex5_9(self):
        # TODO
        pass


if __name__ == "__main__":
    unittest.main()
