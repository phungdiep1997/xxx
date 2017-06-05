import unittest

import exercises.ex3_0 as ex3_0
import exercises.ex3_1 as ex3_1
import exercises.ex3_2 as ex3_2
import exercises.ex5_1 as ex5_1
import exercises.ex5_2 as ex5_2
import exercises.ex5_3 as ex5_3
import exercises.ex5_4 as ex5_4
import exercises.ex5_5 as ex5_5
import exercises.ex5_6 as ex5_6
import exercises.ex5_7 as ex5_7
import exercises.ex5_8 as ex5_8
import exercises.ex5_9 as ex5_9


class TestExercise(unittest.TestCase):
    MESSAGE_FMT = 'Kết quả đúng là `{0}`, nhận được `{1}`'

    def _test_all(self, func, cases):
        for input, expect in cases:
            output = func(input)
            msg = self.MESSAGE_FMT.format(expect, output)
            self.assertEqual(output, expect, msg)


class TestExercise3(TestExercise):

    def test_ex3_0(self):
        res = ex3_0.squared(5)
        self.assertEqual(res, 25, self.MESSAGE_FMT.format(25, res))

    def test_ex3_1(self):
        cases = [(1, 1), (5, 1), (9, 1), (24, 1000), (10, 10)]
        self._test_all(ex3_1.solve, cases)

    def test_ex3_2(self):
        cases = [(-4, "this is negative number"),
                 (0, "this is zero"),
                 (10000, "this is positive number")
                 ]
        self._test_all(ex3_2.solve, cases)

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
        res = ex5_1.solve(ex5_1.data)
        self.assertEqual(len(res), len('Google'),
                         'Kết quả không đủ các chữ cái')
        self.assertEqual(res[0], ('G', '#4885ed'), 'Sai màu')

    def test_ex5_2(self):
        res = ex5_2.solve(ex5_2.data)
        self.assertTrue(isinstance(res, list))
        self.assertTrue(("Hoang", "") in res)
        self.assertTrue(("Duy", "Maria") in res)

    def test_ex5_3(self):
        res = ex5_3.solve(ex5_3.data)
        self.assertTrue(("be", 5) in res,
                        "Không tìm thấy cặp ('be', 5) trong kết quả")
        self.assertTrue(("can", 4) in res,
                        "Không tìm thấy cặp ('can', 4) trong kết quả")

    def test_ex5_4(self):
        expected = [
            '111111111111111111111111111111\n',
            '59999984\n',
            '111111111111111111111111111111\n',
            '59999988\n',
            '111111111111111111111111111111\n',
            '59999992\n',
            '111111111111111111111111111111\n',
            '59999996\n',
            '111111111111111111111111111111\n',
            '60000000\n'
        ]
        import tempfile
        _, fn = tempfile.mkstemp()
        self.assertEqual(ex5_4.solve(fn), expected)

    def test_ex5_5(self):
        res = ex5_5.solve(ex5_5.data)
        self.assertEqual([('Dai', 5), ('Dung', 5), ('Duong', 5)], res[:3])

    def test_ex5_6(self):
        term1, term2 = ex5_6.data
        res = ex5_6.solve(term1, term2)
        self.assertEqual(res['python'], 9)
        self.assertEqual(res['math'], 7)
        self.assertEqual(res['data'], 2)

    def test_ex5_7(self):
        prefix = ('       1       1     0o1     0x1\n'
                  '       2      10     0o2     0x2\n')
        suffix = ('      18   10010    0o22    0x12\n'
                  '      19   10011    0o23    0x13\n')
        res = ex5_7.solve(range(1, 20))

        self.assertTrue(res.startswith(prefix))
        self.assertTrue(res.endswith(suffix))

    def test_ex5_8(self):
        ascii_, unicodes, tabcp, newlinecp, spacecp = ex5_8.solve()
        self.assertEqual(ascii_[:3], [(33, '!'), (34, '"'), (35, '#')])
        self.assertEqual(
            ascii_[-4:],
            [(49, '1'), (50, '2'), (51, '3'), (52, '4')]
        )
        self.assertEqual(tabcp, ord('\t'))
        self.assertEqual(spacecp, ord(' '))
        self.assertEqual(newlinecp, ord('\n'))

    def test_ex5_9(self):
        provinces, populations = ex5_9.solve(ex5_9.data)
        self.assertEqual(provinces[-2:], ['Hải Phòng', 'Hậu Giang'],)
        self.assertEqual(populations[:3], [7681700, 6844100, 3426600])


if __name__ == "__main__":
    unittest.main()
