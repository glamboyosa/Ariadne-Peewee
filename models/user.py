from peewee import * 
db = PostgresqlDatabase('ariadne-books', user="postgres", password="postgres", host="localhost", port=5432)
class User(Model):
    username = CharField(max_length=200, unique=True)
    password = CharField( max_length=200)
    email = CharField(max_length=200, unique=True)
    
    class Meta:
        database = db