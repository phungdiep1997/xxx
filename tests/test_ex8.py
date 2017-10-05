import unittest
from tests.base import TestExercise

import exercises.ex8_1 as ex8_1
import exercises.ex8_2 as ex8_2
import exercises.ex8_3 as ex8_3
import exercises.ex8_4 as ex8_4
import exercises.ex8_7 as ex8_7
import exercises.ex8_8 as ex8_8
import exercises.ex8_9 as ex8_9


class TestExercise8(TestExercise):
    @unittest.skip
    def test_ex8_0(self):
        pass

    def test_ex8_1(self):
        N = 3
        times, total_time = ex8_1.solve(N)
        self.assertEqual(len(times), N,
                         "Chưa thực hiện đủ số lần in ra màn hình")
        self.assertTrue(N <= total_time)

    def test_ex8_2(self):
        res = ex8_2.solve('-h', __file__)
        self.assertEqual(10, len(res), "Số lượng phần tử không đúng")
        with open(__file__) as f:
            line = f.readline()
        self.assertEqual(line.strip(), res[0].strip())

    def test_ex8_3(self):
        res = ex8_3.solve(ex8_3.data)
        self.assertEqual(len(res), len(ex8_3.data),
                         "Số lượng phần tử không đúng")
        self.assertEqual(res[0], ex8_3.data[0].upper())

    def test_ex8_4(self):
        timer_res = ex8_4.solve()
        self.assertTrue(timer_res > 1.0)

    def test_ex8_7(self):
        res = ex8_7.solve()
        self.assertTrue(
            all([
                (res[0].startswith('INFO')),
                (res[1].startswith('ERROR')),
                (res[2].startswith('DEBUG')),
            ]),
        )

    def test_ex8_8(self):
        cases = [('02/03/16', '19.0.2'), ('09/06/16', '11.1.3')]
        self._test_all(ex8_8.solve, cases)

    def _total_line_suffix(self, path):
        '''
        :param path: path folder
        :rtype dict:
        '''
        import os
        file_suffix = {}
        for root, _, files in os.walk(path):
            for file in files:
                path_file = os.path.join(root, file)
                try:
                    _suffix = path_file[path_file.rfind('.'):]
                    if _suffix not in file_suffix:
                        file_suffix.update({_suffix: 0})
                    with open(file) as f:
                        file_suffix[_suffix] += sum(1 for _ in f)
                except Exception:
                    continue
        return file_suffix

    def test_ex8_9(self):
        expected = self._total_line_suffix(ex8_9.PATH)
        res = ex8_9.solve(ex8_9.PATH)
        self.assertTrue(
            expected == res,
            self.MESSAGE_FMT.format(expected, res)
        )

    @unittest.skip
    def test_ex8_10(self):
        pass


if __name__ == "__main__":
    unittest.main()
