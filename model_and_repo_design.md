# {{TABLE NAME}} Model and Repository Classes Design Recipe

_Copy this recipe template to design and implement Model and Repository classes for a database table._

## 1. Design and create the Table

If the table is already created in the database, you can skip this step.

Otherwise, [follow this recipe to design and create the SQL schema for your table](./single_table_design_recipe_template.md).

*In this template, we'll use an example table `students`*

```
# EXAMPLE
table: books

id | title | author_name

```

## 2. Create Test SQL seeds

Your tests will depend on data stored in PostgreSQL to run.

If seed data is provided (or you already created it), you can skip this step.

```sql

```

Run this SQL file on the database to truncate (empty) the table, and insert the seed data. Be mindful of the fact any existing records in the table will be deleted.

```bash
psql -h 127.0.0.1 your_database_name < seeds_{table_name}.sql
```

## 3. Define the class names

Usually, the Model class name will be the capitalised table name (single instead of plural). The same name is then suffixed by `Repository` for the Repository class name.

```python
#model class
class Book():

#repository class
class BookRepository():

```

## 4. Implement the Model class

Define the attributes of your Model class. You can usually map the table columns to the attributes of the class, including primary and foreign keys.

```python
class Book():
    self.id = 0
    self.title = ''
    self.author_name = ''

```

*You may choose to test-drive this class, but unless it contains any more logic than the example above, it is probably not needed.*

## 5. Define the Repository Class interface

Your Repository class will need to implement methods for each "read" or "write" operation you'd like to run against the database.

Using comments, define the method signatures (arguments and return value) and what they do - write up the SQL queries that will be used by each method.

```python
class BookRepository():
    def all():
        #executes SQL query: "SELECT * FROM books"
        #returns array of Book objects
```

## 6. Write Test Examples

Write Python code that defines the expected behaviour of the Repository class, following your design from the table written in step 5.

These examples will later be encoded as Pytest tests.

```python
#MODEL CLASS TESTS
#test init
# book = Book(1, 'Title 1', 'Author 1')
# book.id == 1
# book.title == Title 1
# book.author_name == Author 1

#test __eq__
# book_1 = Book(1, 'Title 1', 'Author 1')
# book_2 = Book(1, 'Title 1', 'Author 1')
# book_1 == book_2

#test str formatting
# book_1 = Book(1, 'Title 1', 'Author 1')
# str(book_1) => 'Book(1, Title 1, Author 1)'



#REPO TEST
# repository = BookRepository()
# books = repository.all()
# books => [Book(1, Nineteen Eighty-Four, George Orwell), Book(2, Mrs Dalloway, Virginia Woolf), etc.] 
```

Encode this example as a test.


## 7. Test-drive and implement the Repository class behaviour

_After each test you write, follow the test-driving process of red, green, refactor to implement the behaviour._
