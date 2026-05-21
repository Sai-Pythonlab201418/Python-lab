class Circle:
    def __init__(self, radius):
        self.radius = radius
        self.pi = 3.14159
    def self_area(self):
        return self.pi * (self.radius ** 2)
    def self_perimeter(self):
        return 2 * self.pi * self.radius
my_circle = Circle(5)
print("Area: %s" % my_circle.self_area())
print("Perimeter: %s" % my_circle.self_perimeter())
