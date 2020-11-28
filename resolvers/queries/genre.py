from ariadne import QueryType
from models.genre import Genre
query = QueryType()

@query.field("getGenres")
def genreResolver(_, info):
    genres = Genre.select()
    return genres