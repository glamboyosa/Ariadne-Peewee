from ariadne import QueryType
from models.book import Book
query = QueryType()
@query.field("getBooks")
def getBooksResolver(_, info): 
    # should append .join(Genre) to avoid 'N +1' problem
    books = Book.select()
    return books
    
