#!/usr/bin/python3

from math import sqrt
from shape import Shape

class Triangle(Shape):
    def __init__(self, side_a: float, side_b: float, side_c: float, name="Triangle", color="yellow"):
        super().__init__(name, color)
        self._side_a = side_a
        self._side_b = side_b
        self._side_c = side_c

    @property
    def side_a(self):
        return self._side_a
    
    @side_a.setter
    def side_a(self, value):
        if value < 0:
            raise ValueError("side_a must be positive")
        aux = self._side_a
        self._side_a = value
        if not self.is_valid():
            self._side_a = aux


    @property
    def side_b(self):
        return self._side_b
    
    @side_b.setter
    def side_b(self, value):
        if value < 0:
            raise ValueError("side_b must be positive")
        aux = self._side_b
        self._side_b = value
        if not self.is_valid():
            self._side_b = aux

    @property
    def side_c(self):
        return self._side_c
    
    @side_c.setter
    def side_c(self, value):
        if value < 0:
            raise ValueError("side_c must be positive")
        aux = self._side_c
        self._side_c = value
        if not self.is_valid():
            self._side_c = aux

    def area(self):
        s = (self._side_a + self._side_b + self._side_c) / 2
        return sqrt(s * (s - self._side_a) * (s - self._side_b) * (s - self._side_c))
    
    def perimeter(self):
        return self._side_a + self._side_b + self._side_c

    def is_valid(self):
        return self._side_a + self._side_b > self._side_c and self._side_a + self._side_c > self._side_b and self._side_b + self._side_c > self._side_a
    
    def __str__(self):
        return f"{self.__class__.__name__}(side_a={self._side_a}, side_b={self._side_b}, side_c={self._side_c})"

    def triangle_type(self):
        if self._side_a == self._side_b and self._side_b == self._side_c:
            return "equilateral"
        elif self._side_a == self._side_b or self._side_b == self._side_c or self._side_a == self._side_c:
            return "isosceles"
        else:
            return "scalene"
