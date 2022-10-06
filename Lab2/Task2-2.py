import math


class Rational:
    def __init__(self, numerator, denominator=1):
        # checking the correction of the arguments' type
        if not (isinstance(numerator, int) or isinstance(denominator, int)):
            raise TypeError("Type Error")
        # classical check
        if denominator == 0:
            raise ZeroDivisionError(f'Rational({numerator}, 0)')
            # if all demands are met
        common_divisor = math.gcd(numerator, denominator)
        self._numerator = numerator // common_divisor
        self._denominator = denominator // common_divisor

    # function for arithmetic operations on fractions
    def __str__(self):
        return f'{self._numerator}' if self._denominator == 1 else f'{self._numerator}/{self._denominator}'

    def __add__(a, b):
        return Rational(a._numerator * b._denominator + a._denominator * b._numerator, a._denominator * b._denominator)

    def __sub__(a, b):
        return Rational(a._numerator * b._denominator - a._denominator * b._numerator, a._denominator * b._denominator)

    def __mul__(a, b):
        return Rational(a._numerator * b._numerator, a._denominator * b._denominator)

    def __truediv__(a, b):
        return Rational(a._numerator * b._denominator, b._numerator * a._denominator)

    # functions for formatted displaying of a fraction
    def get_normal_format(self):
        return f'{self._numerator}' if self._denominator == 1 else f'{self._numerator}/{self._denominator}'

    def get_float_format(self):
        return f'{round(self._numerator / self._denominator, 2)}'


fraction_1 = Rational(8, 10)
fraction_2 = Rational(5, 12)
print(fraction_1, fraction_2)
print(fraction_1.get_normal_format())
print(fraction_1 + fraction_2, fraction_1 - fraction_2)
print(fraction_1 * fraction_2, fraction_1 / fraction_2)
print(fraction_2.get_float_format())

