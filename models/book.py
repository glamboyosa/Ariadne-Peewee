from .user import *
from .genre import *
class Book(Model): 
    title = CharField(max_length=100)
    agerating = CharField(max_length=20)
    genre = ForeignKeyField(column_name='genre', model=Genre)
    
    class Meta: 
        database = db
    