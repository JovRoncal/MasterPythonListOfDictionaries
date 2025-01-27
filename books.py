book_list = [
    {"id": 1, "title": "The Great Gatsby", "author": "F. Scott Fitzgerald", "genre": "Fiction", "published_year": 1925, "isbn": "978-0743273565", "stock": 20, "price": 15.99},
    {"id": 2, "title": "To Kill a Mockingbird", "author": "Harper Lee", "genre": "Fiction", "published_year": 1960, "isbn": "978-0060935467", "stock": 35, "price": 10.99},
    {"id": 3, "title": "1984", "author": "George Orwell", "genre": "Dystopian", "published_year": 1949, "isbn": "978-0451524935", "stock": 40, "price": 9.99},
    {"id": 4, "title": "The Catcher in the Rye", "author": "J.D. Salinger", "genre": "Fiction", "published_year": 1951, "isbn": "978-0316769488", "stock": 25, "price": 8.99},
    {"id": 5, "title": "A Brief History of Time", "author": "Stephen Hawking", "genre": "Non-fiction", "published_year": 1988, "isbn": "978-0553380163", "stock": 10, "price": 18.99}
]

# Printing book details
for book in book_list:
    print(f"Book Title: {book['title']}, Author: {book['author']}, Genre: {book['genre']}, Published Year: {book['published_year']}, ISBN: {book['isbn']}, Stock: {book['stock']}, Price: {book['price']}")