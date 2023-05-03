# test get all books with no records
def test_get_all_books_with_no_records(client):
    # Arrange is inside Conftest
    # Act
    response = client.get("/books")
    response_body = response.get_json()

    # Assert
    assert response.status_code == 200
    assert response_body == []

# Get /books/1 with NO data in test database (no fixture) returns a 404
def test_get_one_book_with_no_data(client):
    # Act
    response = client.get("/books/1")
    print(response)
    print(client)

    # Assert
    assert response.status_code == 404

# Get one planet by id test
def test_get_one_book(client, two_saved_books):
    # Act
    response = client.get('/books/1')
    response_body = response.get_json()

    # Assert
    assert response.status_code == 200
    assert response_body == {
        "id": 1,
        "title": "Ocean Book",
        "description": "watr 4evr"
    }

# test Get all planets in database
def test_get_all_books(client, two_saved_books):
    # Act
    response = client.get('/books')
    response_body = response.get_json()

    # Assert
    assert response.status_code == 200
    assert response_body == [{"id": 1, "title": "Ocean Book", "description": "watr 4evr"},
        {"id": 2, "title": "Mountain Book", "description": "i luv to climb rocks"}
        ]

# Create one book
def test_create_one_book(client):
    # Act
    response = client.post("/books", json={
        "title": "New Book",
        "description": "The Best!"
    })
    response_body = response.get_data(as_text=True)

    # Assert
    assert response.status_code == 201
    assert response_body == "Book New Book successfully created"