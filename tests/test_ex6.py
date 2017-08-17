import unittest
from .base import TestExercise

import exercises.ex6_1 as ex6_1
import exercises.ex6_2 as ex6_2
import exercises.ex6_3 as ex6_3
import exercises.ex6_4 as ex6_4
import exercises.ex6_5 as ex6_5
import exercises.ex6_6 as ex6_6
import exercises.ex6_7 as ex6_7
import exercises.ex6_8 as ex6_8
import exercises.ex6_9 as ex6_9


class TestExercise6(TestExercise):
    @unittest.skip
    def test_ex6_0(self):
        pass

    def test_ex6_1(self):
        expected = [1230, 35670, 2165110, 90570, 138000]
        len_expected = len(expected)
        res = ex6_1.solve(
            {'usages': [1, 29, 1235, 69, 100], 'prices': ex6_1.data}
        )
        self.assertTrue(isinstance(res, list))
        self.assertEqual(
            len(res),
            len_expected,
            "Số lượng phần tử không đúng"
        )
        self.assertEqual(res, expected)

    def test_ex6_2(self):
        data = ['meo', 'bo', 'ga', 'cho', 'chim', 'gau', 'voi']
        # https://docs.python.org/3/library/functions.html#zip
        expected = list(zip(*[iter(data)]*2))
        res = ex6_2.solve(data, 2)
        self.assertTrue(isinstance(res, list))
        self.assertTrue(isinstance(res[0], tuple))
        self.assertEqual(res, expected)

        self.assertEqual(ex6_2.solve(data, 3), list(zip(*[iter(data)]*3)))

    def test_ex6_3(self):
        expected = ('2017-05-25', 76454277.83)
        res = ex6_3.solve()
        self.assertEqual(res, expected)

    def test_ex6_4(self):
        res = ex6_4.solve()
        self.assertEqual(res, sum(range(1, 7)))

    def test_ex6_5(self):
        res = ex6_5.solve(ex6_5.data)
        self.assertTrue(isinstance(res, list), 'Must returns a list')
        self.assertTrue(isinstance(res[0], dict), 'List member must be dict')
        self.assertTrue('hvnsweeting' in [n['login'] for n in res])

    def test_ex6_6(self):
        cases = [({'func': lambda x: x**2, 'data': [1, 2, 3, 4]},
                  [1, 4, 9, 16]),
                 ({'func': lambda x: x % 2 == 0, 'data': [4, 3, 2, 1]},
                  [True, False, True, False])
                 ]

        self._test_all(ex6_6.solve, cases)

    def test_ex6_7(self):
        res = ex6_7.solve(([], ''))
        self.assertTrue(isinstance(res, list))
        self.assertTrue('__setitem__' in res)
        self.assertFalse('extend' in res)

    def test_ex6_8(self):
        import string
        res = ex6_8.solve(12)
        self.assertEqual(len(res), 12)
        self.assertTrue(
            all([
                any(map(lambda s: s.isdigit(), res)),
                any(map(lambda s: s.islower(), res)),
                any(map(lambda s: s.isupper(), res)),
                any(map(lambda s: s in string.punctuation, res)),
                ])
            )
        self.assertFalse(res == ex6_8.solve(12))

    def test_ex6_9(self):
        res = ex6_9.solve(ex6_9.data)
        self.assertTrue(isinstance(res, list))
        self.assertTrue(isinstance(res[0], tuple))
        self.assertTrue(('Singapore', 4) in res)

    @unittest.skip
    def test_ex6_10(self):
        pass


if __name__ == "__main__":
    unittest.main()
