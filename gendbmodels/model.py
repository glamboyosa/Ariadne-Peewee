from peewee import *

database = PostgresqlDatabase('ariadne-books', **{'user': 'postgres', 'password': 'postgres'})

class UnknownField(object):
    def __init__(self, *_, **__): pass

class BaseModel(Model):
    class Meta:
        database = database

class Genre(BaseModel):
    type = TextField()

    class Meta:
        table_name = 'genre'

class Book(BaseModel):
    agerating = TextField()
    genre = ForeignKeyField(column_name='genre', field='id', model=Genre)
    title = TextField()

    class Meta:
        table_name = 'book'

class User(BaseModel):
    email = TextField()
    password = TextField()
    username = TextField()

    class Meta:
        table_name = 'user'

