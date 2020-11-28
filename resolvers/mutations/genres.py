from ariadne import MutationType
from models.genre import * 
mutation = MutationType()
@mutation.field("createGenres")
def createGenres(_,info, type):
    genre = Genre.create(type=type)
    genre.save()
    return genre