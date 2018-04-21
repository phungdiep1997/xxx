import unittest
from tests.base import TestExercise

import exercises.ex3_0 as ex3_0
import exercises.ex3_1 as ex3_1
import exercises.ex3_2 as ex3_2
import exercises.ex3_3 as ex3_3
import exercises.ex3_4 as ex3_4
import exercises.ex3_5 as ex3_5
import exercises.ex3_6 as ex3_6
import exercises.ex3_7 as ex3_7
import exercises.ex3_8 as ex3_8
import exercises.ex3_9 as ex3_9
import exercises.ex3_10 as ex3_10

import exercises.ex4_1 as ex4_1
import exercises.ex4_2 as ex4_2
import exercises.ex4_3 as ex4_3
import exercises.ex4_4 as ex4_4
import exercises.ex4_5 as ex4_5
import exercises.ex4_6 as ex4_6
import exercises.ex4_7 as ex4_7
import exercises.ex4_8 as ex4_8
import exercises.ex4_9 as ex4_9

import exercises.ex5_1 as ex5_1
import exercises.ex5_2 as ex5_2
import exercises.ex5_3 as ex5_3
import exercises.ex5_4 as ex5_4
import exercises.ex5_5 as ex5_5
import exercises.ex5_6 as ex5_6
import exercises.ex5_7 as ex5_7
import exercises.ex5_8 as ex5_8
import exercises.ex5_9 as ex5_9

import exercises.ex35_1 as ex35_1
import exercises.ex35_2 as ex35_2
import exercises.ex35_3 as ex35_3
import exercises.ex35_4 as ex35_4
import exercises.ex35_5 as ex35_5
import exercises.ex35_6 as ex35_6
import exercises.ex35_7 as ex35_7
import exercises.ex35_8 as ex35_8
import exercises.ex35_9 as ex35_9


class TestExercise3(TestExercise):

    def test_ex3_0(self):
        res = ex3_0.squared(5)
        self.assertEqual(res, 25, self.MESSAGE_FMT.format(5, 25, res))

    def test_ex3_1(self):
        cases = [(1, 1), (5, 1), (9, 1), (24, 1000), (10, 10)]
        self._test_all(ex3_1.solve, cases)

    def test_ex3_2(self):
        text = 'P\nY\nM\nI'
        self.assertEqual(ex3_2.solve(text), 'Pymi')
        self.assertEqual(ex3_2.solve(ex3_2.data), 'Crossmyheart')

    def test_ex3_3(self):
        res = ex3_3.solve()
        self.assertIsInstance(
            res, list,
            "Expect list, got: {0}".format(type(res))
        )
        self.assertEqual(
            len(res),
            len(range(1, 101)),
            "Số lượng phần tử không đúng"
        )
        cases = [(1, 1), (2, 2), (3, "Fizz"), (5, "Buzz"), (15, "FizzBuzz")]
        for num, value in cases:
            msg = self.MESSAGE_FMT.format(num, value, res[num - 1])
            self.assertEqual(res[num - 1], value, msg)

    def test_ex3_4(self):
        cases = [("....slsslslsls...sls", "....slsslslsls.."),
                 ("maria.data.mp9", "maria.data"),
                 ]
        self._test_all(ex3_4.solve, cases)

    def test_ex3_5(self):
        len_expected = len(ex3_5.data)
        res = ex3_5.solve(ex3_5.data)
        self.assertIsInstance(res, list)
        self.assertEqual(len(res), len_expected, "Số lượng phần tử không đúng")
        self.assertEqual(res[0][0], 1, 'Index phần tử đầu tiên không đúng')
        self.assertEqual(
            res[-1][0],
            len_expected,
            'Index phần tử cuối cùng không đúng'
        )

    def test_ex3_6(self):
        res = ex3_6.solve(2)
        self.assertIsInstance(res, tuple)
        self.assertEqual(len(res), 2, "Số lượng phần tử không đúng")
        cases = [(1, ("January", 31)),
                 (2, ("February", 28)),
                 (3, ("March", 31)),
                 (4, ("April", 30)),
                 (7, ("July", 31)),
                 (8, ("August", 31)),
                 (9, ("September", 30))
                 ]
        for input_data, expect in cases:
            res = ex3_6.solve(input_data)
            msg = self.MESSAGE_FMT.format(input_data, expect, res)
            self.assertEqual(res, expect, msg)

    def test_ex3_7(self):
        len_expected = 19
        res = ex3_7.solve()
        self.assertEqual(len(res), len_expected, "Số lượng phần tử không đúng")
        self.assertEqual(res[0], '5 == 1 * 5', "Phần tử đầu tiên chưa đúng")
        self.assertEqual(res[-1], '95 == 19 * 5', "Phần tử cuối chưa đúng")

    def test_ex3_8(self):
        cases = [('ana', True),
                 ('Civic', True),
                 ('Python', False),
                 ('', False),
                 ('P', False),
                 (' P  ', False),
                 (' P ', False),
                 ('Able was I ere I saw Elba', True)]
        self._test_all(ex3_8.solve, cases)

    def test_ex3_9(self):
        len_expected = 23
        res = ex3_9.solve()
        msg = self.MESSAGE_FMT.format(None, len_expected, len(res))
        self.assertEqual(len(res), len_expected, "Số bộ không đủ: " + msg)
        self.assertEqual(res[0], [9, 1, 1], "Bộ số đầu tiên chưa chính xác")
        self.assertEqual(res[-1], [1, 9, 1], "Bộ số cuối cùng chưa chính xác")

    def test_ex3_10(self):
        res = ex3_10.solve(*ex3_10.data)
        res.sort()
        self.assertEqual(res, [4, 5])


class TestExercise4(TestExercise):
    def test_ex4_1(self):
        cases = [
            ('0.0.0.0', '00000000.00000000.00000000.00000000'),
            ('192.168.1.1', '11000000.10101000.00000001.00000001'),
            ('208.67.222.222', '11010000.01000011.11011110.11011110'),
        ]

        self._test_all(ex4_1.solve, cases)

    def test_ex4_2(self):
        cases = [(0o644, 0o133), (0o755, 0o022)]
        self._test_all(ex4_2.solve, cases)

    def test_ex4_3(self):
        cases = [
            (['knowledge', 'hardwork', 'discipline', 'attitude'],
             [96, 98, 100, 100])
        ]
        self._test_all(ex4_3.solve, cases)

    def test_ex4_4(self):
        self.assertEqual(ex4_4.solve(), 453542)

    def test_ex4_5(self):
        cases = [
            ([1, 2, 3], (6, 6)),
            ([0, 1, 2], (3, 0))
        ]

        self._test_all(ex4_5.solve, cases)

    def test_ex4_6(self):
        ss3 = '10 Bé học lớp 3 lên lớp 4'
        ss = ', 60năm cuộc đời, 20 năm đầu, sung sướng0bao lâu'
        ss2 = '6năm0 cuộc đời, 20 năm đầu, sung sướng0bao lâu'

        import re
        pattern = re.compile('\d+')

        def _solve(ss):
            return [int(i) for i in pattern.findall(ss)]

        cases = [(i, _solve(i)) for i in [ss, ss2, ss3]]

        self._test_all(ex4_6.solve, cases)

    def test_ex4_7(self):
        cases = [(2008, 'Mậu Tý'), (2009, 'Kỷ Sửu'), (2010, 'Canh Dần'),
                 (2011, 'Tân Mão'), (2012, 'Nhâm Thìn'), (2013, 'Quý Tị'),
                 (2014, 'Giáp Ngọ'), (2015, 'Ất Mui'), (2016, 'Bính Thân'),
                 (2017, 'Đinh Dậu'), (2018, 'Mậu Tuất'), (2019, 'Kỷ Hợi'),
                 (2020, 'Canh Tý'), (1990, 'Canh Ngọ')]
        cases = [(i[0], i) for i in cases]
        self._test_all(ex4_7.solve, cases)

    def test_ex4_8(self):
        result = ex4_8.solve()
        self.assertIn((6, 8, 10), result)
        self.assertEqual(len(result), 2)

    def test_ex4_9(self):
        cases = [
            ([1, 3, 2], 3),
            ([42], 42),
        ]
        self._test_all(ex4_9.solve, cases)


class TestExercise5(TestExercise):
    def test_ex5_1(self):
        res = ex5_1.solve(ex5_1.data)
        self.assertEqual(len(res), len('Google'),
                         'Kết quả không đủ các chữ cái')
        self.assertEqual(res[0], ('G', '#4885ed'), 'Sai màu')

    def test_ex5_2(self):
        res = ex5_2.solve(ex5_2.data)
        self.assertIsInstance(res, list)
        hoang, duy, dai, tu = ex5_2.data
        self.assertNotIn('languages', duy)

        newhoang, newduy, newdai, newtu = res

        self.assertEqual(hoang['languages'], newduy['languages'])
        self.assertEqual(hoang['languages'], newdai['languages'])
        self.assertEqual(hoang['languages'], newtu['languages'])
        self.assertIn('Elixir', newhoang['languages'])
        self.assertEqual(newtu['girl_friend'], 'Do Anh')
        self.assertNotIn('girl_friend', newduy)

    def test_ex5_3(self):
        res = ex5_3.solve(ex5_3.data)
        self.assertIn(("be", 5), res,
                      "Không tìm thấy cặp ('be', 5) trong kết quả")
        self.assertIn(("can", 4), res,
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
        msv, name, year, room = res[0]
        self.assertLess(msv, ex5_5.MAGIC_NUMBER,
                        "Mã sinh viên phải nhỏ hơn số MAGIC_NUMBER")
        self.assertEqual(year, 1990, "Các học viên phải có năm sinh là 1990")
        self.assertEqual([('Dai', 5), ('Dung', 5), ('Duong', 5)],
                         [(e[1], e[-1]) for e in res[:3]])

    def test_ex5_6(self):
        term1, term2 = ex5_6.data
        res = ex5_6.solve(term1, term2)
        self.assertIsInstance(res, dict)
        self.assertEqual(res['python'], 9)
        self.assertEqual(res['math'], 7)
        self.assertEqual(res['data'], 2)

    def test_ex5_7(self):
        prefix = ('       1       1     0o1     0x1\n'
                  '       2      10     0o2     0x2\n')
        suffix = ('      18   10010    0o22    0x12\n'
                  '      19   10011    0o23    0x13\n')
        res = ex5_7.solve(range(1, 20))

        self.assertEqual(prefix, res[:len(prefix)])
        self.assertEqual(suffix, res[-len(suffix):])

    def test_ex5_8(self):
        ascii_, _, tabcp, newlinecp, spacecp = ex5_8.solve()
        self.assertEqual(ascii_[:3], [(33, '!'), (34, '"'), (35, '#')])
        self.assertEqual(
            ascii_[-4:],
            [(49, '1'), (50, '2'), (51, '3'), (52, '4')]
        )
        self.assertEqual(tabcp, ord('\t'))
        self.assertEqual(spacecp, ord(' '))
        self.assertEqual(newlinecp, ord('\n'))

    def test_ex5_9(self):
        start_with_h, more_than_1mil = ex5_9.solve(ex5_9.data)
        self.assertEqual(start_with_h[-2:],
                         [('Hải Phòng', 1904100), ('Hậu Giang', 769700)])
        self.assertEqual(
            more_than_1mil[:2],
            [('TP. Hồ Chí Minh', 7681700), ('Hà Nội', 6844100)]
        )

    def test_ex35_1(self):
        result = ex35_1.solve(10)
        self.assertEqual(len(result), 10)
        self.assertEqual(list(set(result))[0], 2)

    def test_ex35_2(self):
        result = ex35_2.solve(5)
        self.assertEqual(len(result), 5)
        new_result = ex35_2.solve(5)
        # They are random, should be different
        self.assertNotEqual(result, new_result)
        self.assertIn(result[0], range(0, 10))

        # do the same with 10
        result = ex35_2.solve(10)
        self.assertEqual(len(result), 10)
        new_result = ex35_2.solve(10)
        self.assertNotEqual(result, new_result)

    def test_ex35_3(self):
        result = ex35_3.solve(10)
        self.assertEqual(result[:2], [2, 4])
        self.assertEqual(len(result), 10)

    def test_ex35_4(self):
        result = ex35_4.solve(5)
        self.assertEqual(len(result), 5)
        new_result = ex35_4.solve(5)
        self.assertNotEqual(result, new_result, 'Output should be random')

    def test_ex35_5(self):
        result = ex35_5.solve(12)
        self.assertEqual(result[-1], '111111111111')
        self.assertEqual(result[0], '111111')

    def test_ex35_6(self):
        result = ex35_6.solve(1000)
        self.assertEqual(result, sum(int(i) for i in str(2**1000)))

    def test_ex35_7(self):
        result = ex35_7.solve(10)
        self.assertEqual(result, 23)
        result = ex35_7.solve(1000)
        self.assertEqual(result, 233168)

    def test_ex35_8(self):
        result = ex35_8.solve(10)
        self.assertEqual(result[:2], '0*')
        self.assertEqual(result[-2:], '*9')

        N = 10
        matrix = [list(range(N)) for i in range(N)]
        for rowidx, row in enumerate(matrix):
            for idx, _ in enumerate(row):
                if idx == rowidx or idx == N - rowidx - 1:
                    row[idx] = str(rowidx)
                else:
                    row[idx] = '*'
        matrix = '\n'.join([''.join(line) for line in matrix])

        self.assertEqual(result, matrix)

    def test_ex35_9(self):
        res = ex35_9.solve(([], ''))
        self.assertIsInstance(res, list)
        self.assertIn('__setitem__' in res)
        self.assertIn('extend' in res)


if __name__ == "__main__":
    unittest.main()
