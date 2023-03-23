import sqlalchemy
from sqlalchemy import Column, Integer, String

from book_store.db import base

metadata = sqlalchemy.MetaData()


class Books(base):
    __tablename__ = "books"

    id = Column(Integer, primary_key=True, index=True)
    isbn = Column(Integer, index=True)
    title = Column(String, index=True)
    description = Column(String)
    author = Column(String, index=True)
    genre = Column(String)

