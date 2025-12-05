#!/usr/bin/python3

from abc import ABC, abstractmethod


class Shape(ABC):
    def __init__(self, name: str, color: str):
        self.name = name
        self.color = color

    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass

    def get_info(self):
        return f"{self.name} (color: {self.color}) - Area: {self.area():.2f}, Perimeter: {self.perimeter():.2f}"

    def __str__(self):
        return self.name

    def __repr__(self):
        return f"Shape(name='{self.name}', color='{self.color}')"
