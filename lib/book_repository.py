from lib.book import Book

class BookRepository():
    def __init__(self, connection):
        self.connection = connection

    def all(self):
        result_set = self.connection.execute("SELECT * FROM books;")
        books = []
        for result in result_set:
            book = Book(result['id'], result['title'], result['author_name'])
            books.append(book)
        return books