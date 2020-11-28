from ariadne import MutationType
from models.book import *
from models.genre import *
mutation = MutationType()
@mutation.field("createBooks")
def createBooks(_, info, bookInput):
    genre = Genre.get(Genre.id==bookInput.get("genreId"))
    print(genre)
    book = Book.create(title=bookInput.get("title"), agerating=bookInput.get("ageRating"), genre=genre)
    book.save()
    return book
    
    