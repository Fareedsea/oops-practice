class Library():
    def __init__(self, name, location):
        self.books = []
        self.name = name
        self.location = location

    def add_book(self, new_book_name):
        return self.books.append(new_book_name)
    
    def remove_book(self, remove_book):
        return self.books.remove(remove_book)
    
    def get_book(self):
        return self.books

class Book():
    def __init__(self, book_name, author_name, availability):
        self.book_name = book_name
        self.author_name = author_name
        self.availability = availability

mylib2 = Library("The Library", "Karachi")    
book1 = Book("Poetry", "Alama Iqbal", True)
book2 = Book("Pretty", "Eleven", True)
book3 = Book("Rainy", "Micheal", True)

mylib2.add_book(book1.book_name)
mylib2.add_book(book2.book_name)
mylib2.add_book(book3.book_name)
print(mylib2.get_book())
# print(lib1.name)
# print(lib1.location)
# print(book1.name, book2.name)
# print(book1.author, book2.author)
# print(book1.availability, book2.availability)

mylib2.remove_book('Poetry')
print(mylib2.get_book)

        
        