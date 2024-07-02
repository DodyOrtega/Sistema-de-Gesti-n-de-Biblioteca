class Book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.is_checked_out = False

class Member:
    def __init__(self, name, member_id):
        self.name = name
        self.member_id = member_id
        self.borrowed_books = []

    def borrow_book(self, book):
        if not book.is_checked_out:
            book.is_checked_out = True
            self.borrowed_books.append(book)
        else:
            print(f"El libro '{book.title}' ya está prestado.")

    def return_book(self, book):
        if book in self.borrowed_books:
            book.is_checked_out = False
            self.borrowed_books.remove(book)
        else:
            print(f"El libro '{book.title}' no fue prestado a {self.name}.")

class Library:
    def __init__(self):
        self.books = []
        self.members = []

    def add_book(self, book):
        self.books.append(book)

    def add_member(self, member):
        self.members.append(member)

    def list_books(self):
        for book in self.books:
            status = 'Disponible' if not book.is_checked_out else 'Prestado'
            print(f"{book.title} por {book.author} - {status}")

    def list_members(self):
        for member in self.members:
            print(f"Miembro: {member.name}, ID: {member.member_id}")

# Ejemplo de uso
library = Library()
library.add_book(Book("1984", "George Orwell", "1234567890"))
library.add_book(Book("To Kill a Mockingbird", "Harper Lee", "092260764"))
member1 = Member("Alice", "001")
library.add_member(member1)

library.list_books()
member1.borrow_book(library.books[0])
library.list_books()
member1.return_book(library.books[0])
library.list_books()
