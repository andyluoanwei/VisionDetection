# !/bin/python

import unittest

class TestMathFunc(unittest.TestCase):
    def test_add(self):
        self.assertEqual(3, 1+2)
        self.assertEqual(4, 2+2)
        self.assertNotEqual(3, 1+3)

    def runTest(self):
        self.test_add()


suite = unittest.TestSuite()
testCase = [TestMathFunc()]
suite.addTests(testCase)
runner = unittest.TextTestRunner(verbosity=2)
runner.run(suite)

