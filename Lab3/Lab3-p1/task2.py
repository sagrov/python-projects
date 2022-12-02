# TI-01
# Create a class CALENDAR. Define methods for creating and working with a CALENDAR instances and overload operations^
# "+=, -=" - for adding and subtracting days, months, years to a given date
# "==, !=, >, >=, <, <=" - for comparing dates.


MIN_YEAR = 1
MAX_YEAR = 99999
DAYS_IN_MONTH = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
DAYS_BEFORE_MONTH = [0]


class Calendar:
    __slots__ = '_year', '_month', '_day'

    def __init__(self, year, month, day):
        if not all(isinstance(i, int) for i in (year, month, day)):
            raise ValueError('incorrect input')
        if not MIN_YEAR <= year <= MAX_YEAR:
            raise ValueError('year must be in 1 - 99999')
        if not 1 <= month <= 12:
            raise ValueError('month must be in 1 - 12')
        days_in_month = 29 if month == 2 and year % 4 == 0 and \
                            (year % 100 != 0 and year % 400 == 0) else DAYS_IN_MONTH[month]
        if not 1 <= day <= days_in_month:
            raise ValueError('day must be in 1 - %d' % days_in_month)
        self._year = year
        self._month = month
        self._day = day

    @property
    def year(self):
        return self._year

    @property
    def month(self):
        return self._month

    @property
    def day(self):
        return self._day

    @property
    def _date(self):
        return self.year, self._month, self._day

    @year.setter
    def year(self, y):
        self._year = y

    @month.setter
    def month(self, m):
        self._month = m

    @day.setter
    def day(self, d):
        self._day = d

    def _cmp(a, b):
        return 0 if a._date == b._date else 1 if a._date > b._date else -1

    def __eq__(self, other):
        if not isinstance(other, Calendar):
            raise ValueError('Invalid data type')
        return self._cmp(other) == 0

    def __le__(self, other):
        if not isinstance(other, Calendar):
            raise ValueError('Invalid data type')
        return self._cmp(other) <= 0

    def __lt__(self, other):
        if not isinstance(other, Calendar):
            raise ValueError('Invalid data type')
        return self._cmp(other) < 0

    def __ge__(self, other):
        if not isinstance(other, Calendar):
            raise ValueError('Invalid data type')
        return self._cmp(other) >= 0

    def __gt__(self, other):
        if not isinstance(other, Calendar):
            raise ValueError('Invalid data type')
        return self._cmp(other) > 0

    def __ne__(self, other):
        if not isinstance(other, Calendar):
            raise ValueError('Invalid data type')
        return self._cmp(other) != 0

    def __iadd__(self, other):
        if not isinstance(other, Calendar):
            raise ValueError('Invalid data type')
        _day = self._day + other._day
        _month = self._month + other._month
        _year = self._year + other._year

        if _day > DAYS_IN_MONTH[self._month]:
            _day %= DAYS_IN_MONTH[self._month]
            _month += 1
        if _month > 12:
            _month %= 12
            _year += 1

        return Calendar(_year, _month, _day)

    def __isub__(self, other):
        if not isinstance(other, Calendar):
            raise ValueError('Invalid data type')
        _day = self._day - other._day
        _month = self._month - other._month
        _year = self._year - other._year
        if _day < 0:
            _month -= 1
            _day = DAYS_IN_MONTH[_month] + _day

        if _month < 1:
            _year -= 1
            _month = 12
        return Calendar(_year, _month, _day)

    def __str__(self):
        return f'{self._year}/{self._month}/{self._day}'


A = Calendar(2020, 2, 12)
B = Calendar(2020, 2, 5)
C = Calendar(2020, 2, 5)
D = Calendar(2021, 12, 2)
E = Calendar(2022, 1, 10)
F = Calendar(1, 1, 20)
print(A)
print(A == B, A <= B, A < B, A > B)
print(A >= B, A != B, C != B)
print(D)
D += F
print(D)
D -= F
print(D)

