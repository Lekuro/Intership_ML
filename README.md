lesson 04

c1 = Circle()

print(c1.get_area()) # 3.14159

c2 = Circle(2, 3, 4)

print(c2.get_area()) # 12.56636

print(Shape.get_distance(c1, c2)) #5.0

c2.move(4, 3)

print(c2.get_center()) # (7, 7)

t1 = Triangle()

print(t1.get_area()) # 0.4330127018922193

t1.move(3, 4)

print(t1.get_center()) # (3, 4)

t2 = Triangle(2, 3, 3)

print(t2.get_area()) # 1.7320508075688772

print(Triangle.get_distance(t1, t2)) # 1.0

print(t2.get_vertex()) # 3

s1 = Square(3)

s1.move(1, 1)

print(s1.get_center()) # (1, 1)

print(s1.get_vertex()) # 4

print(s1.get_area()) # 3

print(Square.get_distance(s1, t1)) # 3.605551275463989
