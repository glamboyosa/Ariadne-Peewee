# Ariadne + Peewee Demo

This is a feeler project experimenting with [Ariadne](https://ariadnegraphql.org) and [Peewee ORM](http://docs.peewee-orm.com/en/latest/index.html)

## To Install

There are two possible ways to install dependencies

- ### Docker:

  run `docker build .`

- ### Pip
  run `pip install -r requirements.txt`

## To Run

- create a database named `ariande-books` in `PGAdmin`
- run `uvicorn index:app`
