import math
class Fraction:
    """A fraction with a numerator and denominator and arithmetic operations.

    Fractions are always stored in proper form, without common factors in 
    numerator and denominator, and denominator >= 0.
    Since Fractions are stored in proper form, each value has a
    unique representation, e.g. 4/5, 24/30, and -20/-25 have the same
    internal representation.
    """
    
    def __init__(self, numerator, denominator=1):
        """Initialize a new fraction with the given numerator
           and denominator (default 1).
        """
        self.numerator = int(numerator)
        self.denominator = int(denominator)

        if self.numerator >= 1 and self.denominator == 0:
            self.numerator = 1
            self.denominator = 0
        elif self.numerator == 0 and self.denominator != 0:
            self.numerator = 0
            self.denominator = 1
        elif self.numerator < 0 and self.denominator < 0 :
            self.numerator = -self.numerator
            self.denominator = -self.denominator
        elif self.denominator < 0 :
            self.numerator = -self.numerator
            self.denominator = abs(self.denominator)

        if self.numerator == 0 and self.denominator == 0:
            self.numerator = 0
            self.denominator = 0
        else:
            gcd = math.gcd(int(self.numerator),int(self.denominator))
            self.numerator = self.numerator/gcd
            self.denominator = self.denominator/gcd

    #TODO Write the __add__ method, and remove this TODO comment.
    def __add__(self, frac):
        """Return the sum of two fractions as a new fraction.
           Use the standard formula  a/b + c/d = (ad+bc)/(b*d)
        """
        numerator = (self.numerator * frac.denominator) + (frac.numerator* self.denominator)
        denominator = self.denominator * frac.denominator
        number_of_gcd = math.gcd(int(numerator),int(denominator))
        numerator = numerator/number_of_gcd
        denominator = denominator/number_of_gcd
        return Fraction(numerator,denominator)
        
        

    #TODO write __mul__ and __str__.  Verify __eq__ works with your code.
    #Optional have fun and overload other operators such as 
    # __sub__ for f-g
    # __gt__  for f > g
    # __neg__ for -f (negation)

    def __sub__(self, frac):
        """Return the sum of two fractions as a new fraction.
           Use the standard formula  a/b - c/d = (ad-bc)/(b*d)
        """
        numerator = (self.numerator * frac.denominator) - (frac.numerator* self.denominator)
        denominator = self.denominator * frac.denominator
        number_of_gcd = math.gcd(int(numerator),int(denominator))
        numerator = numerator/number_of_gcd
        denominator = denominator/number_of_gcd
        return Fraction(numerator,denominator)

    def __mul__(self, frac):
        """Return the sum of two fractions as a new fraction.
           Use the standard formula  a/b * c/d = (a*c)/(b*d)
        """
        numerator = self.numerator * frac.numerator
        denominator = self.denominator * frac.denominator
        number_of_gcd = math.gcd(int(numerator),int(denominator))
        numerator = numerator/number_of_gcd
        denominator = denominator/number_of_gcd
        return Fraction(numerator,denominator)

    def __truediv__(self, frac):
        """Return the sum of two fractions as a new fraction.
           Use the standard formula  (a/b) / (c/d) = (a*d)/(b*c)
        """
        numerator = self.numerator * frac.denominator
        denominator = self.denominator * frac.numerator
        number_of_gcd = math.gcd(int(numerator),int(denominator))
        numerator = numerator/number_of_gcd
        denominator = denominator/number_of_gcd
        return Fraction(numerator,denominator)

    def __eq__(self, frac):
        """Two fractions are equal if they have the same value.
           Fractions are stored in proper form so the internal representation
           is unique (3/6 is same as 1/2).
        """
        gcd1 = math.gcd(int(self.numerator),int(self.denominator))
        self.numerator = self.numerator/gcd1
        self.denominator = self.denominator/gcd1
        gcd2 = math.gcd(int(frac.numerator),int(frac.denominator))
        frac.numerator = frac.numerator / gcd2
        frac.denominator = frac.denominator / gcd2
        
        return self.numerator == frac.numerator and self.denominator == frac.denominator

    def __str__(self):
        if self.denominator == 1:
            return f"{int(self.numerator)}"
        elif self.numerator == 0 and self.denominator == 0:
            return "0/0"
        else:
            return f"{int(self.numerator)}/{int(self.denominator)}"