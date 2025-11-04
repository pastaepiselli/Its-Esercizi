class Counter:
    def __init__(self) -> None:
        self.conta = 0
    def inc(self) -> None:
        self.conta += 1
    def value(self) -> int:
        return self.conta
         