import math
import unittest
from calculator import Calculator


class TestCalculator(unittest.TestCase):

    def setUp(self):
        self.calculator = Calculator()

    def test_add(self):
        self.assertEqual(self.calculator.addition(1, 2), 3)


class TestCalculatorAddition(unittest.TestCase):

    def setUp(self) -> None:
        self.calculator = Calculator()

    def testNormalCase(self):
        self.assertEqual(self.calculator.addition(3, 3), 6)
        self.assertEqual(self.calculator.addition(2, 3), 5)

    def testAdditionWithNegative(self):
        self.assertEqual(self.calculator.addition(10, -3), 7)
        self.assertEqual(self.calculator.addition(11, -10), 1)

    def testAdditionToNegative(self):
        self.assertEqual(self.calculator.addition(-10, 3), -7)
        self.assertEqual(self.calculator.addition(-532, 500), -32)

    def testAdditionNegativeToNegative(self):
        self.assertEqual(self.calculator.addition(-10, -3), -13)
        self.assertEqual(self.calculator.addition(-235, -454), -689)

    def testAdditionFloat(self):
        self.assertEqual(self.calculator.addition(5.4, 6.4), 11.8)
        self.assertEqual(self.calculator.addition(51.9, 32.6), 84.5)

    def testBadRequestSecondArgument(self):
        self.assertRaises(TypeError, self.calculator.addition, 54, '123')
        self.assertRaises(TypeError, self.calculator.addition, 54, '234')
        self.assertRaises(TypeError, self.calculator.addition, 54, [1, 3, 5])
        self.assertRaises(TypeError, self.calculator.addition, 54, {1, 2, 3})
        self.assertRaises(TypeError, self.calculator.addition, 54, {1: '123', 2: '456', 3: '789'})

    def testBadRequestFirstArgument(self):
        self.assertRaises(TypeError, self.calculator.addition, '54', 123)
        self.assertRaises(TypeError, self.calculator.addition, '234', 123)
        self.assertRaises(TypeError, self.calculator.addition, [1, 3, 5], 123)
        self.assertRaises(TypeError, self.calculator.addition, {1, 2, 3}, 123)
        self.assertRaises(TypeError, self.calculator.addition, {1: '123', 2: '456', 3: '789'}, 123)

    def testBadRequestTwoArguments(self):
        self.assertEqual(self.calculator.addition('54', '123'), '54123')
        self.assertEqual(self.calculator.addition([456], [123]), [456, 123])
        self.assertRaises(TypeError, self.calculator.addition, {1, 2, 3}, {1, 2, 3})
        self.assertRaises(TypeError, self.calculator.addition, {1, 2, 3}, [1, 2])
        self.assertRaises(TypeError, self.calculator.addition, [1, 2], {1, 2, 3})
        self.assertRaises(TypeError, self.calculator.addition, {1: '123', 2: '456', 3: '789'}, {4: '123'})


class TestCalculatorMultiplication(unittest.TestCase):

    def setUp(self) -> None:
        self.calculator = Calculator()

    def testMultiplicationNormal(self):
        self.assertEqual(self.calculator.multiplication(734, 344), 734*344)
        self.assertEqual(self.calculator.multiplication(-734, 344), -734*344)
        self.assertEqual(self.calculator.multiplication(734, -344), -734*344)
        self.assertEqual(self.calculator.multiplication(-734, -344), 734*344)
        self.assertEqual(self.calculator.multiplication(-734.6, -344), 734.6*344)

    def testMultiplicationBadArguments(self):
        self.assertRaises(TypeError, self.calculator.multiplication, 'a', 'b')
        self.assertRaises(TypeError, self.calculator.multiplication, 3.5, 'b')
        self.assertRaises(TypeError, self.calculator.multiplication, 'a', 6.7)
        self.assertRaises(TypeError, self.calculator.multiplication, [1, 2, 3], 6.7)
        self.assertRaises(TypeError, self.calculator.multiplication, {1, 2, 3}, 6.7)
        self.assertRaises(TypeError, self.calculator.multiplication, {1: 34, 2: 56, 3: 78}, 6.7)


class TestCalculatorSubtraction(unittest.TestCase):

    def setUp(self) -> None:
        self.subtraction = Calculator().subtraction

    def testSubtractionNormal(self):
        self.assertEqual(self.subtraction(5, 4), 1)
        self.assertEqual(self.subtraction(-5, 4), -9)
        self.assertEqual(self.subtraction(50, 4.5), 45.5)
        self.assertEqual(self.subtraction(50, 51), -1)

    def testSubtractionBadArguments(self):
        self.assertRaises(TypeError, self.subtraction, 'a', 'b')
        self.assertRaises(TypeError, self.subtraction, 3.5, 'b')
        self.assertRaises(TypeError, self.subtraction, 'a', 6.7)
        self.assertRaises(TypeError, self.subtraction, [1, 2, 3], 6.7)
        self.assertRaises(TypeError, self.subtraction, {1, 2, 3}, 6.7)
        self.assertRaises(TypeError, self.subtraction, {1: 34, 2: 56, 3: 78}, 6.7)


class TestCalculatorDivision(unittest.TestCase):

    def setUp(self) -> None:
        self.division = Calculator().division

    def testDivisionNormal(self):
        self.assertEqual(self.division(5, 4), 5/4)
        self.assertEqual(self.division(-5, 4), -5/4)
        self.assertEqual(self.division(50, 4.5), 50/4.5)
        self.assertEqual(self.division(50, 51), 50/51)
        self.assertEqual(self.division(50, 0), None)

    def testDivisionBadArguments(self):
        self.assertRaises(TypeError, self.division, 'a', 'b')
        self.assertRaises(TypeError, self.division, 3.5, 'b')
        self.assertRaises(TypeError, self.division, 'a', 6.7)
        self.assertRaises(TypeError, self.division, [1, 2, 3], 6.7)
        self.assertRaises(TypeError, self.division, {1, 2, 3}, 6.7)
        self.assertRaises(TypeError, self.division, {1: 34, 2: 56, 3: 78}, 6.7)


class TestCalculatorAbsolute(unittest.TestCase):

    def setUp(self) -> None:
        self.absolute = Calculator().adsolute

    def testAbsoluteNormal(self):
        self.assertEqual(self.absolute(5), 5)
        self.assertEqual(self.absolute(-4), 4)
        self.assertEqual(self.absolute(-45), 45)
        self.assertEqual(self.absolute(-45.6), 45.6)
        self.assertEqual(self.absolute(55.4), 55.4)

    def testAbsoluteBadArguments(self):
        self.assertRaises(TypeError, self.absolute, 'a')
        self.assertRaises(TypeError, self.absolute, [1, 2, 3])
        self.assertRaises(TypeError, self.absolute, {1, 2, 3})
        self.assertRaises(TypeError, self.absolute, {1: 34, 2: 56, 3: 78})


class TestCalculatorDegree(unittest.TestCase):

    def setUp(self) -> None:
        self.degree = Calculator().degree

    def testDegreeNormal(self):
        self.assertEqual(self.degree(5, 4), 5**4)
        self.assertEqual(self.degree(5, 4.1233), 5**4.1233)
        self.assertEqual(self.degree(5.3, 4.1233), 5.3**4.1233)
        self.assertEqual(self.degree(5, -4), 5**-4)
        self.assertEqual(self.degree(-5, -4), (-5)**-4)
        self.assertEqual(self.degree(-5, 0), 1)
        self.assertEqual(self.degree(0, 0), 1)
        self.assertEqual(self.degree(5, 0), 1)

    def testDegreeBadArguments(self):
        self.assertRaises(TypeError, self.degree, 'a')
        self.assertRaises(TypeError, self.degree, [1, 2, 3])
        self.assertRaises(TypeError, self.degree, {1, 2, 3})
        self.assertRaises(TypeError, self.degree, {1: 34, 2: 56, 3: 78})


class TestCalculatorLn(unittest.TestCase):

    def setUp(self) -> None:
        self.ln = Calculator().ln

    def testLnNormal(self):
        self.assertEqual(self.ln(5), math.log(5))
        self.assertEqual(self.ln(8), math.log(8))
        self.assertEqual(self.ln(19), math.log(19, math.e))
        self.assertEqual(self.ln(math.e), 1)
        self.assertEqual(self.ln(math.e**3), 3)
        self.assertEqual(self.ln(math.e**(1/3)), 1/3)
        self.assertEqual(self.ln(math.e**-5), -5)
        self.assertEqual(self.ln(1), 0)

    def testLnBadArguments(self):
        self.assertRaises(TypeError, self.ln, 'a')
        self.assertRaises(TypeError, self.ln, [1, 2, 3])
        self.assertRaises(TypeError, self.ln, {1, 2, 3})
        self.assertRaises(TypeError, self.ln, {1: 34, 2: 56, 3: 78})
        self.assertRaises(ValueError, self.ln, -5)
        self.assertRaises(ValueError, self.ln, 0)


class TestCalculatorLog(unittest.TestCase):

    def setUp(self) -> None:
        self.log = Calculator().log

    def testLogNormal(self):
        self.assertEqual(self.log(5,2), math.log(5, 2))
        self.assertEqual(self.log(5,5), 1)
        self.assertEqual(self.log(8,2), 3)
        self.assertEqual(self.log(math.e**3, math.e), 3)
        self.assertEqual(self.log(math.e, math.e), 1)
        self.assertEqual(self.log(9**4, 9), 4)
        self.assertEqual(self.log(5**(1/3), 5), 1/3)
        self.assertEqual(self.log(5**-5, 5), -5)
        self.assertEqual(self.log(1, 5), 0)

    def testLogBadArguments(self):
        self.assertRaises(TypeError, self.log, 'a', 'ad')
        self.assertRaises(TypeError, self.log, [1, 2, 3], [1, 2, 3])
        self.assertRaises(TypeError, self.log, {1, 2, 3}, {1, 2, 3})
        self.assertRaises(TypeError, self.log, {1: 34, 2: 56, 3: 78}, {1: 34, 2: 56, 3: 78})
        self.assertRaises(ValueError, self.log, -5, 3)
        self.assertRaises(ValueError, self.log, 0, 3)
        self.assertRaises(ValueError, self.log, 3, 0)
        self.assertRaises(ValueError, self.log, 3, -5)


class TestCalculatorSqrt(unittest.TestCase):

    def setUp(self) -> None:
        self.sqrt = Calculator().sqrt

    def testSqrtNormal(self):
        self.assertEqual(self.sqrt(5), math.sqrt(5))
        self.assertEqual(self.sqrt(25), 5)
        self.assertEqual(self.sqrt(-7*-7), 7)
        self.assertEqual(self.sqrt(0), 0)
        self.assertEqual(self.sqrt(1), 1)
        self.assertEqual(self.sqrt(-5), (-5)**0.5)

    def testSqrtBadArguments(self):
        self.assertRaises(TypeError, self.sqrt, 'a')
        self.assertRaises(TypeError, self.sqrt, [1, 2, 3])
        self.assertRaises(TypeError, self.sqrt, {1, 2, 3})
        self.assertRaises(TypeError, self.sqrt, {1: 34, 2: 56, 3: 78})


class TestCalculatorNthRoot(unittest.TestCase):

    def setUp(self) -> None:
        self.nth_root = Calculator().nth_root

    def testNthRootNormal(self):
        self.assertEqual(self.nth_root(5, 4), math.pow(5, 1.0 / 4))
        self.assertEqual(self.nth_root(25, 3), math.pow(25, 1.0 / 3))
        self.assertEqual(self.nth_root(-7*-7, 6), math.pow(-7*-7, 1.0 / 6))
        self.assertEqual(self.nth_root(0, 4), 0)
        self.assertEqual(self.nth_root(1, 4), 1)
        self.assertEqual(self.nth_root(-5, 4), (-5)**(1. / 4))
        self.assertEqual(self.nth_root(-5, -4), (-5)**(1. / -4))
        self.assertEqual(self.nth_root(5, -4), 5**(1. / -4))

    def testNthRootBadArguments(self):
        self.assertRaises(TypeError, self.nth_root, 'a', 'a')
        self.assertRaises(TypeError, self.nth_root, [1, 2, 3], [1, 2, 3])
        self.assertRaises(TypeError, self.nth_root, {1, 2, 3}, {1, 2, 3})
        self.assertRaises(TypeError, self.nth_root, {1: 34, 2: 56, 3: 78}, {1: 34, 2: 56, 3: 78})


if __name__ == "__main__":
    unittest.main()
