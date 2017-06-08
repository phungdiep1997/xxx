import unittest

import exercises.ex6_1 as ex6_1
import exercises.ex6_2 as ex6_2


class TestExercise(unittest.TestCase):
    MESSAGE_FMT = 'Kết quả đúng là `{0}`, nhận được `{1}`'

    def _test_all(self, func, cases):
        for input, expect in cases:
            output = func(input)
            msg = self.MESSAGE_FMT.format(expect, output)
            self.assertEqual(output, expect, msg)


class TestExercise6(TestExercise):
    def test_ex6_1(self):
        # [1, 29, 1235, 69, 100] = >
        # [1230, 35670, 2165110, 90570, 138000]
        expected = [1230, 35670, 2165110, 90570, 138000]
        len_expected = len(expected)
        res = ex6_1.solve()
        self.assertTrue(isinstance(res, list))
        self.assertEqual(
            len(res),
            len_expected,
            "Số lượng phần tử không đúng"
        )
        self.assertEqual(res[0], expected[0], "Phần tử đầu tiên chưa đúng")
        self.assertEqual(res[4], expected[4], "Phần tử cuối chưa đúng")

    def test_ex6_2(self):
        # li = ['meo', 'bo', 'ga', 'cho', 'chim', 'gau'] = >
        # [('meo', 'bo'), ('ga', 'cho'), ('chim', 'gau')]
        expected = [('meo', 'bo'), ('ga', 'cho'), ('chim', 'gau')]
        len_expected = len(expected)
        res = ex6_2.solve()
        self.assertTrue(isinstance(res, list))
        self.assertEqual(isinstance(res[0], tuple))
        self.assertEqual(
            len(res),
            len_expected,
            "Số lượng phần tử không đúng"
        )
        self.assertEqual(res[0], expected[0], "Phần tử đầu tiên chưa đúng")
        self.assertEqual(res[1], expected[1], "Phần tử giữa chưa đúng")
        self.assertEqual(res[2], expected[2], "Phần tử cuối chưa đúng")


if __name__ == "__main__":
    unittest.main()
