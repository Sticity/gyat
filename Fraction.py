class Fraction(object):

    def __init__(self, numerator=0, denominator=1):
        self.numerator = numerator
        self.denominator = denominator

    def gcd(a, b):
        if (b == 0 or a == 0): 
            return 0 
        while b: 
            a, b = b, a % b
        return a

    def get_numerator(self):
        lowest = self.numerator / self.gcd(self.numerator, self.denominator)
        
        return '' + lowest

    def get_denominator(self):
        lowest = self.denominator / self.gcd(self.numerator, self.denominator)
        
        return '' + self.denominator

    def get_fraction(self):
        return 'f{self.numerator}/{self.denominator}'
