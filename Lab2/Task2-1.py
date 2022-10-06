class Rectangle:
    def __init__(self, width = 1, length = 1):
        self.length = length
        self.width = width

    @property
    def width(self):
        return self._width

    @property
    def length(self):
        return self._length

    @width.setter
    def width(self, width_new):
        if not (isinstance(width_new, (int, float))):
            raise Exception("Width isn't a float")
        if width_new <= 0 or width_new > 20:
            raise Exception("Width is not in range 0 <-> 20")
        self._width = width_new

    @length.setter
    def length(self, length_new):
        if not (isinstance(length_new, (int, float))):
            raise Exception("Height isn't a float")
        if length_new <= 0 or length_new > 20:
            raise Exception("Height is not in range 0 <-> 20")
        self._length = length_new

    def perimeter(self):
        return f'Perimeter: {(self.length + self.width) * 2}'

    def area(self):
        return f'Area: {self.length * self.width}'


length = float(input('Length: '))
width = float(input('Width: '))
rectangle = Rectangle(length, width)
print (rectangle.area(), rectangle.perimeter())

