import unittest
from calculatorv24 import evaluateCalc

class AdditionTestCase(unittest.TestCase):

    def test_addition(self):
        calcAnswer = evaluateCalc("1+2")
        self.assertEqual(calcAnswer, 3)

class SubtractionTestCase(unittest.TestCase):

    def test_subtraction(self):
        calcAnswer = evaluateCalc("2-1")
        self.assertEqual(calcAnswer, 1)

class MultiplicationTestCase(unittest.TestCase):

    def test_subtraction(self):
        calcAnswer = evaluateCalc("2*3")
        self.assertEqual(calcAnswer, 6)

class DivisionTestCase(unittest.TestCase):

    def test_division(self):
        calcAnswer = evaluateCalc("3/2")
        self.assertEqual(calcAnswer, 1.5)

class DifficultTestCase(unittest.TestCase):

    def test_no_brackets(self):
        calcAnswer = evaluateCalc("1+1*5")
        self.assertEqual(calcAnswer, 6)

    def test_brackets(self):
        calcAnswer = evaluateCalc("(1+1)*5")
        self.assertEqual(calcAnswer, 10)

    def test_more_brackets(self):
        calcAnswer = evaluateCalc("(1*2)-(3*4)")
        self.assertEqual(calcAnswer, -10)

unittest.main()
