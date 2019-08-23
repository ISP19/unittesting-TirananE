import math
import time
import unittest
from fraction import Fraction


class FractionTest(unittest.TestCase):
    """Test the methods and constructor of the Fraction class. """

    def test_init(self):
        f = Fraction(0,0)
        self.assertEqual(0, f.numerator)
        self.assertEqual(0, f.denominator)
        f = Fraction(0,1)
        self.assertEqual(0, f.numerator)
        self.assertEqual(1, f.denominator)
        f = Fraction(-1,0)
        self.assertEqual(-1, f.numerator)
        self.assertEqual(0, f.denominator)
        f = Fraction(5,10)
        self.assertEqual(1, f.numerator)
        self.assertEqual(2, f.denominator)
        f = Fraction(-1,30)
        self.assertEqual(-1, f.numerator)
        self.assertEqual(30, f.denominator)
        f = Fraction(-100, -100)
        self.assertEqual(1, f.numerator)
        self.assertEqual(1, f.denominator)
        f = Fraction(-2)
        self.assertEqual(-2, f.numerator)
        self.assertEqual(1, f.denominator)
        

    def test_str(self):
        f = Fraction(3, -1)
        self.assertEqual("-3", f.__str__())
        f = Fraction(0, 5)
        self.assertEqual("0", f.__str__())
        f = Fraction(60, 90)
        self.assertEqual("2/3", f.__str__())
        f = Fraction(1500, 60)
        self.assertEqual("25", f.__str__())
        f = Fraction(1500, 90)
        self.assertEqual("50/3", f.__str__())
        f = Fraction(-80, 20)
        self.assertEqual("-4", f.__str__())
        f = Fraction(36, -60)
        self.assertEqual("-3/5", f.__str__())
        f = Fraction(99)
        self.assertEqual("99", f.__str__())
        f = Fraction(0,0)
        self.assertEqual("0/0", f.__str__())

    def test_add(self):
        # 3/4 = 2/3 + 1/12
        self.assertEqual(Fraction(3,4), Fraction(1,12)+Fraction(2,3))
        self.assertEqual(Fraction(-1,5),Fraction(-3,5)+Fraction(2,5))
        self.assertEqual(Fraction(-1),Fraction(-2,5)+Fraction(-3,5))
        self.assertEqual(Fraction(-1),Fraction(2,-5)+Fraction(3,-5))
        self.assertEqual(Fraction(1,10),Fraction(8,100)+Fraction(2,100))
        self.assertEqual(Fraction(2,3),Fraction(18,27)+Fraction(0))
        self.assertEqual(Fraction(0),Fraction(0,4)+Fraction(0,-1))
        self.assertEqual(Fraction(0),Fraction(0)+Fraction(0))

    def test_sub(self):
        # -1/5 = 2/5 - 3/5
        self.assertEqual(Fraction(-1,5),Fraction(2,5)-Fraction(3,5))
        self.assertEqual(Fraction(1,5),Fraction(-2,5)-Fraction(-3,5))
        self.assertEqual(Fraction(3,50),Fraction(8,100)-Fraction(2,100))
        self.assertEqual(Fraction(2,3),Fraction(18,27)-Fraction(0))
        self.assertEqual(Fraction(-2,3),Fraction(0)-Fraction(18,27))
        self.assertEqual(Fraction(0),Fraction(0,4)-Fraction(0,-1))
        self.assertEqual(Fraction(0),Fraction(0)-Fraction(0))

    def test_mul(self):
        # 5/27 = 5/9 * 1/3
        self.assertEqual(Fraction(0),Fraction(0)*Fraction(0))
        self.assertEqual(Fraction(0),Fraction(0)*Fraction(18,27))
        self.assertEqual(Fraction(5,27),Fraction(5,9)*Fraction(1,3))
        self.assertEqual(Fraction(-8,15),Fraction(2,3)*Fraction(4,-5))
        self.assertEqual(Fraction(-8,15),Fraction(2,3)*Fraction(4,-5))

    def test_div(self):
        with self.assertRaises(ZeroDivisionError):
            Fraction(0,0)/Fraction(0,0)
            Fraction(0)/Fraction(0)
            Fraction(3)/Fraction(0)
            Fraction(-1,0)/Fraction(3,0)
        self.assertEqual(Fraction(100,343), Fraction(20,49)/Fraction(7,5))
        self.assertEqual(Fraction(0),Fraction(0)/Fraction(18,27))
        self.assertEqual(Fraction(3),Fraction(5,9)/Fraction(5,27))
        self.assertEqual(Fraction(3),Fraction(-5,9)/Fraction(-5,27))
        self.assertEqual(Fraction(-3),Fraction(-5,9)/Fraction(5,27))
        self.assertEqual(Fraction(1,0), Fraction(1,0)/Fraction(2,3))
        self.assertEqual(Fraction(-1,0), Fraction(323,-23)/Fraction(0))

        
    def test_eq(self):
        f = Fraction(1,2)
        g = Fraction(-40,-80)
        h = Fraction(10000,20001) # not quite 1/2
        self.assertTrue(f == g)
        self.assertTrue(f.__eq__(g))  # same thing
        self.assertFalse(f == h)
        self.assertFalse(f.__eq__(h))
        self.assertTrue(Fraction(3,0) == (Fraction(1,0)))
        self.assertFalse(Fraction(-1,0) == Fraction(1,0))
        self.assertFalse(Fraction(43,23) == Fraction(1,2))
        self.assertTrue(Fraction(-100,50) == Fraction(-2))
        self.assertTrue(Fraction(8) == Fraction(16,2))

        

            

