# Task 1. Modify the class Rational of Lab No1 to perform the following tasks:
# - adding two Rational numbers. The result should be stored in reduced form;
# - subtracting two Rational numbers. The result should be stored in reduced form;
# - multiplying two Rational numbers. The result should be stored in reduced form;
# - dividing two Rational numbers. The result should be stored in reduced form;
# - comparison two Rational numbers.

import math


class Rational:
    def __init__(self, numerator, denominator=1):
        if not (isinstance(numerator, int) or isinstance(denominator, int)):
            raise TypeError("Type Error")
        if denominator == 0:
            raise ZeroDivisionError(f'Rational({numerator}, 0)')
        self._numerator = numerator
        self._denominator = denominator
        g = math.gcd(numerator, denominator)
        self._numerator = numerator // g
        self._denominator = denominator // g

    @property
    def numerator(self):
        return self._numerator

    @property
    def denominator(self):
        return self._denominator

    @numerator.setter
    def numerator(self, num):
        self._numerator = num

    @denominator.setter
    def denominator(self, num):
        self._denominator = num

    def _reducing(self):
        g = math.gcd(self._numerator, self._denominator)
        return self._numerator // g, self._denominator // g

    def __add__(a, b):
        return Rational(a._numerator * b._denominator + a._denominator * b._numerator, a._denominator * b._denominator)

    def __sub__(a, b):
        return Rational(a._numerator * b._denominator - a._denominator * b._numerator, a._denominator * b._denominator)

    def __mul__(a, b):
        return Rational(a._numerator * b._numerator, a._denominator * b._denominator)

    def __truediv__(a, b):
        return Rational(a._numerator * b._denominator, b._numerator * a._denominator)

    def compare(a, b):
        if a._denominator == b._denominator:
            return 0 if a._numerator == b._numerator else 1 if a._numerator > b._numerator else -1
        if a._numerator == b._numerator:
            return 0 if a._numerator == b._numerator else 1 if a._numerator < b._numerator else -1
        g = math.lcm(a._denominator, b._denominator)
        A_num = a.numerator * (g / a.denominator)
        B_num = b.numerator * (g / b.denominator)
        return 0 if A_num == B_num else 1 if A_num > B_num else -1

    def __eq__(a, b):
        if not isinstance(b, Rational):
            raise ValueError('Invalid data type')
        return a.compare(b) == 0

    def __le__(a, b):
        if not isinstance(b, Rational):
            raise ValueError('Invalid data type')
        return a.compare(b) <= 0

    def __lt__(a, b):
        if not isinstance(b, Rational):
            raise ValueError('Invalid data type')
        return a.compare(b) < 0

    def __ge__(a, b):
        if not isinstance(b, Rational):
            raise ValueError('Invalid data type')
        return a.compare(b) >= 0

    def __gt__(a, b):
        if not isinstance(b, Rational):
            raise ValueError('Invalid data type')
        return a.compare(b) > 0

    def __ne__(a, b):
        if not isinstance(b, Rational):
            raise ValueError('Invalid data type')
        return a.compare(b) != 0

    def __str__(self):
        return f'{self._numerator}/{self._denominator}'

    def float_point_format(self):
        return f'{round(self._numerator / self._denominator, 2)}'


fraction_1 = Rational(9, 10)
fraction_2 = Rational(1, 3)
fraction_3 = Rational(25, 27)
fraction_4 = Rational(0, 1)
fraction_5 = Rational(19)

print(fraction_1, fraction_2, fraction_5)

print(fraction_1 + fraction_2, fraction_1 - fraction_2, fraction_1 * fraction_2, fraction_1 / fraction_2)

print(fraction_1, fraction_1.float_point_format())

print(fraction_1 < fraction_2, fraction_1 > fraction_2, fraction_1 == fraction_2, fraction_1 != fraction_2, fraction_2 == fraction_3)
