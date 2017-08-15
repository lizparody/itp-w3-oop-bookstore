class Bookstore(object):
    def __init__(self, name):
        self.name = name
        self.books = []
   
    def add_book(self, book):
        self.books.append(book)
        
    def get_books(self):
        return self.books
        
    def search_books(self, title = None, author = None):
      result = []
      if (title == None) and author:
        for book in self.books:
          if author.name == book.author.name:
            result.append(book)
      elif title and (author == None):
        for book in self.books:
          if title.lower() in book.title.lower():
            result.append(book)
      return result
      
        
class Author(object):
    def __init__(self, name, nationality):
        self.name = name
        self.nationality = nationality
        self.books = []
        
    def add_book(self, book):
        self.books.append(book)
        
    def get_books(self):
        return self.books
        
class Book(object):
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.author.add_book(self)
        


