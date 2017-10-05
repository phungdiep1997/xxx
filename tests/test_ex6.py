import unittest
from tests.base import TestExercise

import exercises.ex6_1 as ex6_1
import exercises.ex6_2 as ex6_2
import exercises.ex6_3 as ex6_3
import exercises.ex6_4 as ex6_4
import exercises.ex6_5 as ex6_5
import exercises.ex6_8 as ex6_8
import exercises.ex6_9 as ex6_9


class TestExercise6(TestExercise):
    @unittest.skip
    def test_ex6_0(self):
        pass

    def test_ex6_1(self):
        expected = [('Nam', 1230), ('Pikalong', 35670),
                    ('Phan Quan', 2165110), ('Maria', 90570),
                    ('Trump', 138000)]
        len_expected = len(expected)
        res = ex6_1.solve(
            {'usages': [('nam', '1'), ('pikalong', '29'),
                        ('phan quan', '1235'), ('maria', '69'),
                        ('trump', '100')],
             'prices': ex6_1.data}
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
        self.assertEqual(res, sum(range(1, 7)) + .5)

    def test_ex6_5(self):
        res = ex6_5.solve(ex6_5.data)
        self.assertTrue(isinstance(res, list), 'Must returns a list')
        self.assertTrue(isinstance(res[0], dict), 'List member must be a dict')
        self.assertTrue('hvnsweeting' in [n['login'] for n in res])
        self.assertTrue(
            'https://github.com/thedrow' in [n['html_url'] for n in res]
        )
        self.assertTrue(
            'https://github.com/hvnsweeting' in [n['html_url'] for n in res]
        )

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
