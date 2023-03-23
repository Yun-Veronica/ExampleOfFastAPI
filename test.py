import pytest
from fastapi.testclient import TestClient
from appl import app

client = TestClient(app)

# @pytest.mark.fastapi
def test_create_book():
    response = client.post("/book/", json={"isbn": "1",
                                           "title": "Foo Bar",
                                           "description": "The Foo Barters",
                                           "author": "fooooobar f f",
                                           "genre": "fantasy"})
    assert response.status_code == 200
    assert response.json() == {
        "isbn": "1",
        "title": "Foo Bar",
        "description": "The Foo Barters",
        "author": "fooooobar f f",
        "genre": "fantasy"
    }


def test_update_book():
    response = client.put("/book/1", json={"isbn": "1",
                                           "title": "Foo Bar",
                                           "description": "The Foo Barters",
                                           "author": "fooooobar f f",
                                           "genre": "sci-fi"
                                           })
    assert response.status_code == 200
    assert response.json() == {
        "isbn": "1",
        "title": "Foo Bar",
        "description": "The Foo Barters",
        "author": "fooooobar f f",
        "genre": "sci-fi"}


def test_read_book():
    response = client.get("/book/1")
    assert response.status_code == 200
    assert response.json() == {
        "isbn": "1",
        "title": "Foo Bar",
        "description": "The Foo Barters",
        "author": "fooooobar f f",
        "genre": "fantasy"
    }


def test_delete_book():
    response = client.delete("/book/1")
    assert response.status_code == 200
    assert response.json() == {"message": f"Book '1' deleted"}


def test_read_nonexisting_item():
    response = client.get("/book/5")
    assert response.status_code == 404


def test_create_existing_item():
    response = client.post(
        "/book/",
        json={
            "isbn": "1",
            "title": "Foo Bar",
            "description": "The Foo Barters",
            "author": "fooooobar f f",
            "genre": "fantasy"
        },
    )
    assert response.status_code == 400
    assert response.json() == {"detail": "Item already exists"}
