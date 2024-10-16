import math

# Base class
class Shape:
    """A base class for shapes that requires derived classes to implement an area method."""

    def area(self):
        """Method to calculate the area of the shape. Must be overridden by derived classes."""
        raise NotImplementedError("The area() method must be overridden in derived classes.")


# Derived class for Rectangle
class Rectangle(Shape):
    """A class representing a rectangle, derived from Shape."""

    def __init__(self, length, width):
        """Initialize the rectangle with length and width."""
        self.length = length
        self.width = width

    def area(self):
        """Calculate and return the area of the rectangle (length × width)."""
        return self.length * self.width


# Derived class for Circle
class Circle(Shape):
    """A class representing a circle, derived from Shape."""

    def __init__(self, radius):
        """Initialize the circle with a radius."""
        self.radius = radius

    def area(self):
        """Calculate and return the area of the circle (π × radius²)."""
        return math.pi * self.radius ** 2


# Polymorphism demonstration
def polymorphism_demo():
    """Function to demonstrate polymorphism by calculating areas of different shapes."""
    shapes = [
        Rectangle(5, 10),  # Rectangle with length 5 and width 10
        Circle(7),         # Circle with radius 7
        Rectangle(3, 4),   # Rectangle with length 3 and width 4
        Circle(2)          # Circle with radius 2
    ]

    for shape in shapes:
        print(f"The area of the {type(shape).__name__} is: {shape.area()}")

if __name__ == "__main__":
    polymorphism_demo()
