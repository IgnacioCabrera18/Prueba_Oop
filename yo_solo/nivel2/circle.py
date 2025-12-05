#!/usr/bin/python3

from math import pi
from shape import Shape


class Circle(Shape):
    def __init__(self, radius: float, name="Circle", color="blue"):
        super().__init__(name, color)
        self._radius = radius
    
    @property
    def radius(self):
        return self._radius
    
    @radius.setter
    def radius(self, value):
        if value < 0:
            raise ValueError("Radius must be positive")
        self._radius = value
    
    def area(self):
        return pi * (self._radius ** 2)
    
    def perimeter(self):
        return 2 * pi * self._radius
    
    def __str__(self):
        return f"{self.__class__.__name__}(radius={self._radius})"

circle = Circle(5.0, name="My Circle", color="red")
print(circle.radius)      # 5.0
circle.radius = 10.0      # Funciona
circle.radius = -5.0      # ValueError: Radius must be positive
print(circle.get_info())  # My Circle (color: red) - Area: 78.54, Perimeter: 31.42
