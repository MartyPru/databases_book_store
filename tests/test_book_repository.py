from lib.book_repository import *
from lib.book import *
"""
When calling #all
returns array of Book objects
"""
def test_returns_list_of_book_objects(db_connection):
    db_connection.seed("seeds/book_store.sql")
    repo = BookRepository(db_connection)
    books = repo.all()
    assert books == [
        Book(1, "Nineteen Eighty-Four", 'George Orwell'),
        Book(2, "Mrs Dalloway", 'Virginia Woolf'),
        Book(3, "Emma", 'Jane Austen'),
        Book(4, "Dracula", 'Bram Stoker'),
        Book(5, "The Age of Innocence", 'Edith Wharton')
    ]