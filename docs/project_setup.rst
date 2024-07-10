Project Setup
=============

To set up and run this project locally, follow these steps:

Prerequisites
-------------

- A GitHub account with read access to this repository
- Git CLI installed
- SQLite3 CLI installed
- Python interpreter, version 3.6 or higher


1. Clone the Repository
------------------------

First, clone the repository to your local machine using Git. Open your terminal and run:

.. code-block:: sh

   git clone https://github.com/clementboloch/OCR_P13.git

2. Set Up a Virtual Environment
-------------------------------

Navigate to the project directory and set up a virtual environment to manage dependencies. Run:

.. code-block:: sh

   cd OCR_P13
   python -m venv env

Activate the virtual environment:

- On Windows, run:

  .. code-block:: sh

     .\env\Scripts\activate

- On macOS and Linux, run:

  .. code-block:: sh

     source env/bin/activate

Confirm that the `python` command executes the Python interpreter in the virtual environment:

.. code-block:: sh

   which python

Confirm that the Python interpreter version is 3.6 or higher:

.. code-block:: sh

   python --version

Confirm that the `pip` command executes the pip executable in the virtual environment:

.. code-block:: sh

   which pip

To deactivate the environment, use:

.. code-block:: sh

   deactivate

3. Install Dependencies
------------------------

With the virtual environment activated, install the required dependencies using pip. Run:

.. code-block:: sh

   pip install -r requirements.txt

4. Run Database Migrations
---------------------------

Apply the necessary database migrations to set up the database schema. Run:

.. code-block:: sh

   python manage.py makemigrations
   python manage.py migrate

1. Run the Development Server
------------------------------

Start the Django development server to run the application locally. Run:

.. code-block:: sh

   python manage.py runserver

This command starts the application and binds it to port 8000 on your local machine. You can access it by navigating to `http://localhost:8000` in your web browser.

6. Additional Commands
----------------------

- **Linting**: To check the code quality, run:
  
  .. code-block:: sh
  
   flake8
  
- **Unit Tests**: To run unit tests, execute:
  
  .. code-block:: sh
  
   pytest
  
- **Coverage Report**: To generate a coverage report, use:
  
  .. code-block:: sh
  
   coverage run --source='.' manage.py test
   coverage report
  
- **Database Operations**: To interact with the SQLite database:
  - Open a SQLite shell session:
   
   .. code-block:: sh
    
      sqlite3
    
  - Connect to the database:
   
   .. code-block:: sh
    
      .open oc-lettings-site.sqlite3
    
  - Display tables in the database:
   
   .. code-block:: sh
    
      .tables
    
  - Display columns in the profiles table:
   
   .. code-block:: sh
    
      pragma table_info(profiles_profile);
    
  - Query the profiles table:
   
   .. code-block:: sh
    
      select user_id, favorite_city from profiles_profile where favorite_city like 'B%';
    
  - Exit the SQLite session:
   
   .. code-block:: sh
    
      .quit
