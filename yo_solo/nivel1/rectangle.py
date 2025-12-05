#!/usr/bin/python3

class Rectangle:
    def __init__(self, width: float, height: float):
        self.width = width
        self.height = height

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
        return self.width * self.height
    
    def perimeter(self):
        return 2 * (self.width + self.height)
    
    def __str__(self):
        return f"{self.__class__.__name__}(width={self.width}, height={self.height})"

rect = Rectangle(4.0, 6.0)
print(rect.area())      # 24.0
print(rect.perimeter()) # 20.0
print(rect)             # Rectangle(width=4.0, height=6.0)
