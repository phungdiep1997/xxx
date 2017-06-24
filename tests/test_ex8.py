import unittest
from base import TestExercise

import exercises.ex8_1 as ex8_1
import exercises.ex8_2 as ex8_2
import exercises.ex8_3 as ex8_3
import exercises.ex8_4 as ex8_4
import exercises.ex8_5 as ex8_5
import exercises.ex8_6 as ex8_6
import exercises.ex8_7 as ex8_7
import exercises.ex8_8 as ex8_8
# import exercises.ex8_9 as ex8_9


class TestExercise8(TestExercise):
    @unittest.skip
    def test_ex8_0(self):
        pass

    def test_ex8_1(self):
        res = ex8_1.solve()
        len_expected = 4
        self.assertEqual(len(res), len_expected, "Không đủ số phần tử")
        with open('../exercises/ex8_1.py') as f:
            data = f.read()
            self.assertTrue(
                all([
                    (True if data.find(i) != -1 else False)
                    for i in (
                        "yaml.load(", "json.dump(", "pickle.dump(", "wb"
                    )
                ]),
                "Chưa thực hiện đúng yêu cầu"
            )

    def test_ex8_2(self):
        res = ex8_2.solve(ex8_2.words)
        len_expected = 10
        self.assertEqual(
            len(res),
            len_expected,
            "Số lượng phần tử không đúng"
        )
        self.assertTrue(
            all([
                (True if res[i].endswith('\n') else False)
                for i in range(1, len_expected)
            ]),
            "Chưa thực hiện đủ số lần in ra file"
        )

    def test_ex8_3(self):
        res = ex8_3.solve(ex8_3.words)
        len_expected = 4
        self.assertEqual(
            len(res),
            len_expected,
            "Số lượng phần tử không đúng"
        )
        self.assertTrue(res[0] == 'nhung\n',
                        "Phần tử đầu tiên không đúng")
        self.assertTrue(res[-1] in ('nho\n', 'nho'),
                        "Phần tử cuối cùng không đúng")

    def test_ex8_4(self):
        res = ex8_4.solve(ex8_4.words)
        self.assertTrue(
            res is None,
            "Chưa set gía trị cho biến `result`"
        )

    def test_ex8_5(self):
        times, total_time = ex8_5.solve()
        self.assertTrue(
            all([
                (len(times) == 60),
                (60 <= total_time),
            ]),
            "Chưa thực hiện đủ số lần in ra màn hình"
        )

    def test_ex8_6(self):
        word_frequency, most_common = ex8_6.solve()
        len_expected = 42
        cases = [('counts', 3), ('is', 3), ('are', 3)]
        self.assertEqual(
            len(word_frequency),
            len_expected,
            "Không đủ số từ"
        )
        self.assertTrue(
            all([
                (word_frequency["a"] == 2),
                (word_frequency["counts"] == 3),
                (word_frequency["languages"] == 1),
            ]),
            "Số lượng từ đếm chưa đúng"
        )
        for case in cases:
            self.assertTrue(
                case in most_common,
                "Thiếu bộ {}".format(case)
            )

    def test_ex8_7(self):
        res = ex8_7.solve()
        len_expected = 14
        self.assertEqual(
            len(res),
            len_expected,
            "Không đủ số dòng, số dòng yêu cầu là %d" % len_expected
        )
        self.assertTrue(
            all([
                (res[0].startswith('INFO:')),
                (res[1].startswith('ERROR:')),
                (res[2].startswith('DEBUG:')),
                (res[-1].startswith('DEBUG:')),
            ]),
        )

    def test_ex8_8(self):
        cases = [('02/03/16', '19.0.2'), ('09/06/16', '11.1.3')]
        self._test_all(ex8_8.solve, cases)

    def test_ex8_9(self):
        pass

    @unittest.skip
    def test_ex8_10(self):
        pass


if __name__ == "__main__":
    unittest.main()
