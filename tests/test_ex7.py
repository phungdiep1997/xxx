import unittest
from tests.base import TestExercise

import exercises.ex7_1 as ex7_1
import exercises.ex7_2 as ex7_2
import exercises.ex7_3 as ex7_3
import exercises.ex7_4 as ex7_4
import exercises.ex7_5 as ex7_5
import exercises.ex7_6 as ex7_6
import exercises.ex7_7 as ex7_7


class TestExercise7(TestExercise):
    def test_ex7_1(self):
        self.assertEqual(ex7_1.solve('1/3', '6/9'), 1.0)
        self.assertEqual(ex7_1.solve('1/10', '1/10', '1/10'), 0.3)

    def test_ex7_2(self):
        name, HP = ex7_2.solve(ex7_2.Fighter('PyMi', 100),
                               ex7_2.Fighter('Foo', 100))
        self.assertTrue(name in ('PyMi', 'Foo'))
        self.assertTrue(HP > 0)

    def test_ex7_3(self):
        result = ex7_3.solve(100)
        self.assertEqual(len(result), 100)
        self.assertTrue(isinstance(result[-1], float))
        self.assertTrue(0 <= result[-1] <= 1)

    def test_ex7_4(self):
        cases = [('a', 'a'),
                 ('aa', 'aa2'),
                 ('abbbccccdddd', 'abb3cc4dd4'),
                 ('xxyyyxyyx', 'xx2yy3xyy2x')]
        self._test_all(ex7_4.solve, cases)

    def test_ex7_5(self):
        import os
        result = ex7_5.solve()
        self.assertEqual(os.__file__, result[0])

    def test_ex7_6(self):
        import string
        res = ex7_6.solve(12)
        self.assertEqual(len(res), 12)
        self.assertTrue(
            all([
                any(map(lambda s: s.isdigit(), res)),
                any(map(lambda s: s.islower(), res)),
                any(map(lambda s: s.isupper(), res)),
                any(map(lambda s: s in string.punctuation, res)),
                ])
            )
        self.assertFalse(res == ex7_6.solve(12))

    def test_ex7_7(self):
        res = ex7_7.solve(ex7_7.data)
        self.assertTrue(isinstance(res, list))
        self.assertTrue(isinstance(res[0], tuple))
        self.assertTrue(('Singapore', 4) in res)


if __name__ == "__main__":
    unittest.main()
