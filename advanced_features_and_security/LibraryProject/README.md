# Permissions and Groups Implementation

This project utilizes Django's built-in permissions and groups system to manage user access to various parts of the application.

## Custom Permissions

Custom permissions were defined on the `Book` model within the `bookshelf` app to control specific actions:

- `can_view`: Allows a user to view the list of books.
- `can_create`: Allows a user to add a new book.
- `can_edit`: Allows a user to edit an existing book.
- `can_delete`: Allows a user to delete an existing book.

## Groups and Assigned Permissions

The following user groups were created in the Django Admin to enforce these permissions:

- **Admins:** Assigned all four custom permissions (`can_view`, `can_create`, `can_edit`, `can_delete`).
- **Editors:** Assigned `can_view`, `can_create`, and `can_edit` permissions.
- **Viewers:** Assigned only the `can_view` permission.

## Implementation in Views

The `permission_required` decorator is used in `bookshelf/views.py` and `relationship_app/views.py` to protect specific views and enforce these permissions based on a user's group membership.
