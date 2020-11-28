from ariadne import gql;

type_defs = gql("""
type Genre {
    type: String!
    book: Book
}
type Book {
    title: String!
    agerating: String!
    genre: Genre!
}
type User {
    email: String!
    username: String!
    password: String!
}
input BookInput {
    title: String!
    ageRating: String!
    genreId: Float!
}
input CreateUserInput {
    email: String!
    username: String!
    password: String!
}
type Query {
    getBooks: [Book]!
    getGenres: [Genre]!
    hello: [Book]!
}
type Mutation {
    createBooks(bookInput: BookInput!) : Book!
    register(registerInput: CreateUserInput!): User!
    createGenres(type: String!): Genre!
}
""")