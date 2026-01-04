class Book:
    def __init__(self, title: str, author: str, isbn: str) -> None:
        self.title = title
        self.author = author
        self.isbn = isbn

    def __str__(self) -> str:
        return f"Title: {self.title}, Author: {self.author}, Isbn: {self.isbn}"

    @classmethod
    def from_string(cls, book_str):
        title, author, isbn = book_str.split(", ")
        return cls(title, author, isbn)


if __name__ == "__main__":
    book_str: str = "La Divina Commedia, D. Alighieri, 999000666"
    divina_commedia: Book = Book.from_string(book_str)

    print(divina_commedia)
