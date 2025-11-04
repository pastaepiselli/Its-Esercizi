class Shape:
    def area(self):
        raise NotImplementedError

class Circle(Shape):
    def __init__(self, r) -> None:
        self.r = r
    def area(self) -> float:
        return (3.141592653589793*(self.r**2))

class Rect(Shape):
    def __init__(self, w, h) -> None:
        self.w = w
        self.h = h
    def area(self):
        return self.w * self.h

a = {'palle': {'culo': 2, 'sperma': 3}}

b = a['nuova'] = {'chiave': 2, 'pazza': 4}
print(b)