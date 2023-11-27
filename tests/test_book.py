from lib.book import Book
"""
When creating instance of Book
correctly stores attributes
"""
def test_init_attributes():
    book = Book(1, 'Title 1', 'Author 1')
    assert book.id == 1
    assert book.title == 'Title 1'
    assert book.author_name == 'Author 1'


"""
If two instances of Book have same fields
They are equal
"""
def test_equality():
    book_1 = Book(1, 'Title 1', 'Author 1')
    book_2 = Book(1, 'Title 1', 'Author 1')
    assert book_1 == book_2


"""
When formatted as string
Prints easy-to-read string
"""
def test_str_formatting():
    book = Book(1, 'Title 1', 'Author 1')
    assert str(book) == 'Book(1, Title 1, Author 1)'