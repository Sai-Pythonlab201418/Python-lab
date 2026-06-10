class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
    def borrow(self):
        print("You have borrowed the book: " + self.title + " by " + self.author)
    def return_book(self):
        print("You have returned the book: " + self.title + " by " + self.author)
book1 = Book("Harry Potter and the philosopher's stone", "J.K. Rowling")
book2 = Book("Famous Five: Five on a Treasure Island", "Enid Blyton")
book3 = Book("Matilda", "Roald Dahl")

print("Welcome to the library!")
book1.borrow()
book2.borrow()
book3.borrow()
book1.return_book()
book2.return_book()
book3.return_book()