#!/usr/bin/python3

from shape import Shape

class Rectangle(Shape):
    def __init__(self, width: float, height: float, name="Rectangle", color="green"):
        super().__init__(name, color)
        self._width = width
        self._height = height

    @property
    def width(self):
        return self._width
    
    @width.setter
    def width(self, value):
        if value < 0:
            raise ValueError("width must be positive")
        self._width = value
    
    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, value):
        if value < 0:
            raise ValueError("height must be positive")
        self._height = value
    
    def area(self):
        return self._width * self._height
    
    def perimeter(self):
        return 2 * (self._width + self._height)
    
    def __str__(self):
        return f"{self.__class__.__name__}(width={self._width}, height={self._height})"

    def is_square(self):
        return self._width == self._height

rect = Rectangle(4.0, 6.0)
print(rect.area())      # 24.0
print(rect.perimeter()) # 20.0
print(rect)             # Rectangle(width=4.0, height=6.0)
print(rect.is_square())
rect._width = 6.0
print(rect.is_square())
print(rect.get_info())
