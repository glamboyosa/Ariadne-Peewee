from ariadne import QueryType
query = QueryType()

@query.field("hello")
def helloResolver(_, info):
    return [{"title": "The Lord of The Rings", "ageRating": "PG-13", "genre": {
        "type": "fantasy"
    }}]