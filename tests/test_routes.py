
# Get /books/1 with NO data in test database (no fixture) returns a 404
def test_get_one_planet_with_no_data(client):
    # Act
    response = client.get("/planets/1")

    # Assert
    assert response.status_code == 404

# Get one book by id test
def test_get_one_planet(client, three_saved_planets):
    # Act
    response = client.get('/planets/1')
    response_body = response.get_json()

    # Assert
    assert response.status_code == 200
    assert response_body == {
        "id": 1,
        "name": "Jupiter",
        "description": "King of the Roman gods, aka Zeus"
    }

# test Get all books in database
def test_get_all_planets(client, three_saved_planets):
    # Act
    response = client.get('/books')
    response_body = response.get_json()

    # Assert
    assert response.status_code == 200
    assert response_body == [{"id": 2, "name": "Mars", "description": "Roman god of war, aka Ares"},
        {"id": 3, "name": "Venus", "description": "Roman goddess of love, aka Aphrodite"}
        ]

# Create one book
def test_create_one_planet(client):
    # Act
    response = client.post("/planets", json={
        "name": "New planet",
        "description": "The Best!"
    })
    response_body = response.get_data(as_text=True)

    # Assert
    assert response.status_code == 201
    assert response_body == "Planet New planet successfully created"


