class Shape:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def get_center(self):
        return (self.x, self.y)

    def move(self, x, y):
        self.x += x
        self.y += y

    @staticmethod
    def get_distance(fig1, fig2):
        return ((fig1.x-fig2.x) ** 2+(fig1.y-fig2.y) ** 2) ** 0.5


class Circle(Shape):
    PI = 3.14159

    def __init__(self, radius=1, x=0, y=0):
        super().__init__(x, y)
        self.radius = radius

    def get_area(self):
        return self.radius ** 2 * self.PI


class Square(Shape):
    def __init__(self, side=1, x=0, y=0):
        super().__init__(x, y)
        self.side = side

    def get_area(self):
        return self.side**2

    def get_vertex(self):
        return 4


class Triangle(Shape):
    def __init__(self, side=1, x=0, y=0):
        super().__init__(x, y)
        self.side = side

    def get_area(self):
        const = 0.25*(3**0.5)
        return const*(self.side**2)

    def get_vertex(self):
        return 3


c1 = Circle()
print(c1.get_area())
c2 = Circle(2, 3, 4)
print(c2.get_area())
print(Shape.get_distance(c1, c2))
c2.move(4, 3)
print(c2.get_center())
t1 = Triangle()
print(t1.get_area())
t1.move(3, 4)
print(t1.get_center())
t2 = Triangle(2, 3, 3)
print(t2.get_area())
print(Triangle.get_distance(t1, t2))
print(t2.get_vertex())
s1 = Square(3)
s1.move(1, 1)
print(s1.get_center())
print(s1.get_vertex())
print(s1.get_area())
print(Square.get_distance(s1, t1))
