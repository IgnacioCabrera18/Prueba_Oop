#!/usr/bin/python3

from shape import Shape


class ShapeCollection():
    def __init__(self):
        self._shapes = []
    
    def add_shape(self, shape):
        if not isinstance(shape, Shape):
            raise TypeError("Only Shape instances can be added")
        self._shapes.append(shape)
    
    def remove_shape(self, shape):
        if shape in self._shapes:
            self._shapes.remove(shape)
            return True
        else:
            return False
    
    def get_total_area(self):
        sum = 0
        for shape in self._shapes:
            sum += shape.area()
        return sum
    
    def get_total_perimeter(self):
        sum = 0
        for shape in self._shapes:
            sum += shape.perimeter()
        return sum

    def get_largest_shape(self):
        if self._shapes == []:
            return None
        largest = self._shapes[0]
        for shape in self._shapes:
            if shape.__gt__(largest):
                largest = shape
        return largest

    def get_smallest_shape(self):
        if self._shapes == []:
            return None
        smallest = self._shapes[0]
        for shape in self._shapes:
            if shape.__lt__(smallest):
                smallest = shape
        return smallest

    def __len__(self):
        return len(self._shapes)
    
    def __iter__(self):
        return iter(self._shapes)
    
    def __getitem__(self, index):
        if index < 0 and index > self.__len__():
            raise IndexError("a casa pt 2")
        return self._shapes[index]

    def __str__(self):
        return f"ShapeCollection with {self.__len__()} shapes"

    def filter_by_type(self, shape_type):
        new_list = []
        for shape in self._shapes:
            if isinstance(shape, shape_type):
                new_list.append(shape)
        return new_list