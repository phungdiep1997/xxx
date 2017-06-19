import unittest


class TestExercise(unittest.TestCase):
    MESSAGE_FMT = 'Kết quả đúng là `{0}`, nhận được `{1}`'

    def _test_all(self, func, cases):
        for input, expect in cases:
            output = func(input)
            msg = self.MESSAGE_FMT.format(expect, output)
            self.assertEqual(output, expect, msg)
