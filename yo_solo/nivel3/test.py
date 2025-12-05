from shape_collection import ShapeCollection
from circle import Circle
from rectangle import Rectangle
from triangle import Triangle

collection = ShapeCollection()
collection.add_shape(Rectangle(4.0, 6.0))
collection.add_shape(Circle(5.0))
collection.add_shape(Circle(6.0))

collection.add_shape(Triangle(3.0, 4.0, 5.0))

print(len(collection))              # 3
print(collection.get_total_area())  # Suma de todas las áreas
print(collection.get_largest_shape())  # Retorna el Circle

# Iterar
for shape in collection:
    print(shape.get_info())

# Acceder por índice
print(collection[0])  # Primera forma

# Filtrar
circles = collection.filter_by_type(Circle)
print(len(circles))  # 1