from pydantic import BaseModel


class BookBase(BaseModel):
    isbn: int
    isbn: int
    author: str | None = None
    genre: str | None = None
    title: str
    description: str | None = None


class BookCreate(BookBase):
    pass


class Book(BookBase):
    id: int

    class Config:
        orm_mode = True


class BookUpdate(BookBase):
    pass


class BookResponse(BookBase):
    isbn: int
    author: str | None = None
    genre: str | None = None
    title: str
    description: str | None = None

    class Config:
        orm_mode = True
