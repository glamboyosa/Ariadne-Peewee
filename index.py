from ariadne import make_executable_schema
from ariadne.asgi import GraphQL
from schema.schema import *
from resolvers.mutations.book import mutation as BookMutation
from resolvers.mutations.genres import mutation  as GenreMutation
from resolvers.queries.hello import query as HelloQuery
from resolvers.queries.book import query as BookQuery
from resolvers.queries.genre import query as GenreQuery
from models.user import *
from models.genre import *
from models.book import *
db.connect()
# the line below creates maps entities to tables but I used PWIZ to map existing DB tables to code
db.create_tables([User, Genre, Book])
schema = make_executable_schema(type_defs, [BookQuery,HelloQuery, GenreQuery, GenreMutation, BookMutation])
app = GraphQL(schema, debug=True)
# def demo_function(word: str, union: Union[int, str]) -> str:
#     print(word)
#     print(union)
#     return word

# demo_function(False, "a boy")
