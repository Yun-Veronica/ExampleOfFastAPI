from fastapi import FastAPI, HTTPException
from book_store.custom_models import Books
from book_store.custom_schemas import BookResponse, Book, BookUpdate, BookCreate
from sqlalchemy.exc import SQLAlchemyError

from book_store.db import Session

app = FastAPI()


@app.post("/books/")
async def create_book(book: Book) -> Book:
    with Session() as session:
        db_book = Books(**book.dict())
        session.add(db_book)
        try:
            session.commit()
            session.refresh(db_book)
            return db_book
        except SQLAlchemyError as e:
            session.rollback()
            raise HTTPException(status_code=500, detail="Database Error: " + str(e))


# @app.get("/books/{book_id}", response_model=Book)
@app.get("/books/{book_id}")
async def read_book(book_id: int) -> Book:
    with Session() as session:
        db_book = session.query(Books).filter(Books.id == book_id).first()
        if db_book is None:
            raise HTTPException(status_code=404, detail="Book not found")
        return db_book


@app.put("/books/{book_id}")
async def update_book(book_id: int, book: Book) -> Book:
    with Session() as session:
        db_book = session.query(Books).filter(Books.id == book_id).first()
        if db_book is None:
            raise HTTPException(status_code=404, detail="Book not found")
        for field, value in book:
            setattr(db_book, field, value)
        try:
            session.commit()
            session.refresh(db_book)
            return db_book
        except  SQLAlchemyError as e:
            session.rollback()
            raise HTTPException(status_code=500, detail="Database Error: " + str(e))


@app.delete("/books/{book_id}")
async def delete_book(book_id: int):
    with Session() as session:
        db_book = session.query(Books).filter(Books.id == book_id).first()
        if db_book is None:
            raise HTTPException(status_code=404, detail="Book not found")
        try:
            session.delete(db_book)
            session.commit()
        except  SQLAlchemyError as e:
            session.rollback()
            raise HTTPException(status_code=500, detail="Database Error: " + str(e))


@app.get("/books/")
async def read_books() -> list:
    with Session() as session:
        db_books = session.query(Books).all()
        return db_books
