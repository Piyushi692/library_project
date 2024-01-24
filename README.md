# Django Rest Framework - Bookstore Management

This Django Rest Framework project is a bookstore management system, allowing administrators to perform various tasks such as adding genres, managing authors and books, and efficiently exporting book data.

## Features

1. **Common Login and Signup:**
   - Unified login for Authors and administrators.
   - Author signup functionality.

2. **Admin APIs:**
   - Add genre for books.
   - Retrieve all details of all authors, including their books.
   - Fetch details of a specific author.
   - Retrieve books of a specific author.
   - Delete genre from the system.

3. **Author APIs:**
   - Add a new book to the system.
   - Edit details of an existing book.

4. **Export API for Admin:**
   - Efficiently export all book data for a specific genre in structured formats like CSV or JSON.
   - Includes details such as Book name, Author name, Number of pages, and other relevant information.

## Getting Started

Follow these instructions to set up the project locally:

### Prerequisites

- Python 3.x
- Django
- Django Rest Framework

### Installation

1. **Clone the Repository:**
   ```bash
  git clone https://github.com/Piyushi692/library_project.git

2. **Create a Virtual Environment**
3. cd library_project
  python -m venv venv

4.**Activate the virtual environment**
  .\venv\Scripts\activate

5. **Install Dependencies**
     pip install -r requirements.txt

6.**Apply Migrations**
  python manage.py migrate

7.**Run the Development Server**
  python manage.py runserver


