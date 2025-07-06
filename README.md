# User Profile MicroService

This project is a Python-based backend service for managing user profiles. It provides an API endpoint to update user profile information, including their description, preferences, and type. The service uses a MySQL database to store profile data and JWT for authenticating requests.

## Folder Structure

The project is organized using a layer-based folder structure:

-   **`.github/workflows/`**: Contains CI/CD pipeline definitions, specifically for Docker image publishing (`docker-publish.yml`).
-   **`conections/`**: Handles database connectivity.
    -   `mysql.py`: Contains the logic to connect to the MySQL database using SQLAlchemy, configured via environment variables.
-   **`main.py`**: The main entry point of the Flask application. It defines API routes, handles request authentication (JWT), and delegates business logic to the service layer.
-   **`models/`**: Defines the SQLAlchemy ORM models that map to database tables.
    -   `models.py`: Contains `Profile`, `Type`, and `Preference` table definitions.
-   **`services/`**: Contains the core business logic of the application.
    -   `functions.py`: Includes functions like `edit_user` which encapsulate operations on user profiles.
-   **`tests/`**: Contains test scripts for the application.
    -   `route_test.py`: An example script for testing the `/update-profile` endpoint.
    -   `test_edit.py`: (Likely contains unit tests for service functions, though its content was not inspected).
-   **`dockerfile`**: Instructions for building a Docker image for the application.
-   **`.gitignore`**: Specifies intentionally untracked files that Git should ignore.
-   **`requirements.txt`**: Lists the Python dependencies for the project.

## Backend Design Pattern

The service employs a **Service Layer Pattern**.
-   The API layer (`main.py`) is responsible for handling HTTP requests, validating authentication (JWT), and formatting responses.
-   The Service layer (`services/functions.py`) encapsulates the business logic. For example, the `edit_user` function handles the logic for updating a user's profile. This layer interacts with the data access components.

This pattern promotes separation of concerns, making the codebase more modular and maintainable.

## Communication Architecture

The communication architecture is a **RESTful API** with **direct database interaction**:

-   **RESTful API**: The application exposes HTTP endpoints (e.g., `/update-profile`) managed by Flask. Clients interact with these endpoints using standard HTTP methods (like PATCH) and JSON for data exchange.
-   **Direct Database Interaction**: The service layer (`services/functions.py`) uses the `conections/mysql.py` module to establish a session with the MySQL database. It performs CRUD operations directly using SQLAlchemy ORM. There is no intermediary messaging system or separate Data Access Object (DAO) layer beyond the ORM and connection management.

## Endpoint Instructions

### Update User Profile

-   **Endpoint:** `PATCH /update-profile`
-   **Purpose:** Allows an authenticated user to update their profile information.
-   **Authentication:**
    -   Requires a `Bearer` token in the `Authorization` header.
    -   The token is a JWT which must decode successfully and contain a `user_id` claim.
-   **Request Body:**
    -   Content-Type: `application/json`
    -   The body can contain any combination of the following optional fields:
        ```json
        {
            "Description": "A new bio or status update.",
            "Id_preferences": 1,
            "Id_type": 2
        }
        ```
        -   `Description` (string, optional): The new description for the user's profile.
        -   `Id_preferences` (integer, optional): The ID of the user's new preference (foreign key to `Preferences` table).
        -   `Id_type` (integer, optional): The ID of the user's new type (foreign key to `Types` table).
-   **Responses:**
    -   **`200 OK`**: Profile updated successfully.
        ```json
        {
            "message": "Profile updated successfully"
        }
        ```
    -   **`401 Unauthorized`**:
        -   Token missing or invalid format: `{"error": "Token missing or invalid"}`
        -   Token expired: `{"error": "Token expired"}`
        -   Invalid token (e.g., bad signature, missing `user_id`): `{"error": "Invalid token"}` or `{"error": "Invalid token data"}`
    -   **`404 Not Found`**:
        -   Active profile not found for the user: `{"error": "Active profile not found"}` (This occurs if the user specified by `user_id` in the token does not have an active account (`Status_account=1`)).

## Setup and Running

(This section would typically include instructions on setting up environment variables, installing dependencies, and running the application. Based on the files, it would involve creating a `.env` file for database credentials and `SECRET_KEY`, running `pip install -r requirements.txt`, and then `python main.py`.)

*Note: Setup instructions are inferred and may need specific details from the project owner.*
