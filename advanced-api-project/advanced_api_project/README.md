# Advanced API Project

This is a Django REST Framework API for managing a library's authors and books, created as a learning exercise. It demonstrates the use of custom serializers, generic views, and advanced query features like filtering, searching, and ordering.

## API Endpoints

The API provides the following endpoints for managing books.

### `/api/books/` (List and Create)

- **Description**: This endpoint allows you to retrieve a list of all books or create a new one.
- **Methods**:
  - `GET`: Retrieves a list of all books.
  - `POST`: Creates a new book. Requires authentication.
- **Query Parameters**:
  - `search`: Perform a text search on `title` and `author__name`. Example: `?search=pride`
  - `publication_year`: Filter books by publication year. Example: `?publication_year=1980`
  - `ordering`: Order results by a specific field. Use a minus sign for descending order. Example: `?ordering=-publication_year`

### `/api/books/<int:pk>/` (Detail)

- **Description**: This endpoint retrieves the details of a single book.
- **Methods**:
  - `GET`: Retrieves a single book by ID.
  - `PUT`: Updates an existing book. Requires authentication.
  - `DELETE`: Deletes a book. Requires authentication.

### `/api/books/create/`

- **Description**: A dedicated endpoint for creating a new book. Requires authentication.

### `/api/books/<int:pk>/update/`

- **Description**: A dedicated endpoint for updating a specific book. Requires authentication.

### `/api/books/<int:pk>/delete/`

- **Description**: A dedicated endpoint for deleting a specific book. Requires authentication.
