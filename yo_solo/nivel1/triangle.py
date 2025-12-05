#!/usr/bin/python3

from math import sqrt

class Triangle:
    def __init__(self, side_a: float, side_b: float, side_c: float):
        self.side_a = side_a
        self.side_b = side_b
        self.side_c = side_c

    @property
    def side_a(self):
        return self._side_a
    
    @side_a.setter
    def side_a(self, value):
        if value < 0:
            raise ValueError("side_a must be positive")
        self._side_a = value

    @property
    def side_b(self):
        return self._side_b
    
    @side_b.setter
    def side_b(self, value):
        if value < 0:
            raise ValueError("side_b must be positive")
        self._side_b = value

    @property
    def side_c(self):
        return self._side_c
    
    @side_c.setter
    def side_c(self, value):
        if value < 0:
            raise ValueError("side_c must be positive")
        self._side_c = value

    def area(self):
        s = (self.side_a + self.side_b + self.side_c) / 2
        return sqrt(s * (s - self.side_a) * (s - self.side_b) * (s - self.side_c))
    
    def perimeter(self):
        return self.side_a + self.side_b + self.side_c

    def is_valid(self):
        if self.side_a + self.side_b > self.side_c and self.side_a + self.side_c > self.side_b and self.side_b + self.side_c > self.side_a:
            return True
        else:
            raise ValueError("The Triangle is not valid")
    
    def __str__(self):
        return f"{self.__class__.__name__}(side_a={self.side_a}, side_b={self.side_b}, side_c={self.side_c})"

triangle = Triangle(3.0, 4.0, 5.0)
print(triangle.area())      # 6.0
print(triangle.perimeter()) # 12.0
print(triangle.is_valid())  # True
triangle.side_a  = 10
print(triangle)             # Triangle(side_a=3.0, side_b=4.0, side_c=5.0)