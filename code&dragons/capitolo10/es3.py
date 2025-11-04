class Rectangle:
    def __init__(self, w, h) -> None:
        self.w = w
        self.h = h
    def area(self) -> int:
        return self.w * self.h
    def perimeter(self) -> int:
        return (self.w + self.h) * 2
    def __eq__(self, other) -> bool:
        return self.area() == other.area()