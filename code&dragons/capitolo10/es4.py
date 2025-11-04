class Stack:
    def __init__(self) -> None:
        self.zaino = []
    def is_empty(self) -> bool:
        return len(self.zaino) == 0
    def push(self, x) -> None:
        self.zaino.append(x)
    def pop(self):
        if self.is_empty():
            raise IndexError
        return self.zaino.pop()
    
        
    