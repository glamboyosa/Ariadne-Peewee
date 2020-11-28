from .user import *
class Genre(Model):
    type = CharField(max_length=100)
    
    class Meta:
        database = db
