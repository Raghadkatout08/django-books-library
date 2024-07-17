# django-books-library

Welcome to the Django Books Library project! This project is designed to manage a library of books with user authentication and basic CRUD operations.

## Getting Started
These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

- Python 3.x
- Django
- Virtualenv

### Installation

1. Clone the repository:
   ```bash
   git clone git@github.com:Raghadkatout08/django-books-library.git
   cd django-books-library

2. Create a virtual environment:
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`

3. Install dependencies:
    ```bash
    pip install -r requirements.txt

4. Apply migrations:
    ```bash
    python manage.py migrate

5. Create a superuser (admin):
    ```bash
    python manage.py createsuperuser

6. Run the development server:
    ```bash
    python manage.py runserver


### Running Tests
To run the tests for this project:
    ```bash
    python manage.py test


### Contributing
Feel free to fork this project and submit pull requests. Contributions, suggestions, and improvements are welcome!