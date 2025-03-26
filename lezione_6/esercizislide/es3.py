class Animal:
    def __init__(self, name, legs):
        self.name = name
        self.legs = legs
    
    def set_legs(self, new_legs):
        self.legs = new_legs

    def get_legs(self):
        return self.legs
    
    def printinfo(self):
        print(self.name, self.legs)

cat = Animal('popa', 4)
print(cat.name)
cat.legs = 5
print(cat.legs)
        