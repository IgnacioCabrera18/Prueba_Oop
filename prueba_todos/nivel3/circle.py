#!/usr/bin/python3

from math import pi


class Circle():
    def __init__(self, radius:float):
        self.radius = radius
    
    @property
    def radius(self):
        return self._radius
    
    @radius.setter
    def radius(self, value):
        if value < 0:
            raise ValueError("sos un boludo ingresa un valor positivo")
        self._radius = value

    def area(self):
        return (pi * (self.radius ** 2))
            
    def perimeter(self):
        return (2 * pi * self.radius)

    def __str__(self):
        return f"{self.__class__.__name__}(radius={self.radius})"
