"""Book class"""
# name, author, pages, required


class Book:
    #book class for keep track of books
    def __init__(self, name="", author="", pages=0, required=""):
        self.name = name
        self.author = author
        self.pages = pages
        self.required = required

    def __str__(self):
        return "{self.name}, {self.author}, {self.pages}, {self.required}".format(self=self)


def run_tests():
    d1 = Book()
    print(d1)

    d2 = Book("My Book", "Greg Taylor", 123, "r")
    print(d2)

    total_pages = 0
    books = [d2, d2]
    for book in books:
        total_pages += book.pages
    print(total_pages)

if __name__ == '__main__':
    run_tests()