Project Quick Start
====================

To quickly start with the Orange County Lettings site project, follow these steps:

Prerequisites
-------------

- A GitHub account with read access to this repository
- Git CLI installed
- SQLite3 CLI installed
- Python interpreter, version 3.6 or higher

Setup
-----

1. **Clone the repository**
   - Navigate to the directory where you want to place the project:
     ::
     
       cd /path/to/put/project/in
     
   - Clone the repository:
     ::
     
       git clone https://github.com/clementboloch/OCR_P13

2. **Create a virtual environment**
   - Navigate to the project directory:
     ::
     
       cd /path/to/Python-OC-Lettings-FR
     
   - Create a virtual environment:
     ::
     
       python -m venv venv
       
   - Activate the virtual environment:
     ::
     
       source venv/bin/activate
     
   - Confirm that the `python` command executes the Python interpreter in the virtual environment:
     ::
     
       which python
     
   - Confirm that the Python interpreter version is 3.6 or higher:
     ::
     
       python --version
     
   - Confirm that the `pip` command executes the pip executable in the virtual environment:
     ::
     
       which pip
     
   - To deactivate the environment, use:
     ::
     
       deactivate

Running the Site Locally
-------------------------

- Ensure you are in the project directory and the virtual environment is activated.
- Install the required dependencies:
  ::
  
    pip install -r requirements.txt
  
- Start the development server:
  ::
  
    python manage.py runserver
  
- Open `http://localhost:8000` in a web browser to view the site.

Additional Commands
-------------------

- **Linting**: To check the code quality, run:
  ::
  
    flake8
  
- **Unit Tests**: To run unit tests, execute:
  ::
  
    pytest
  
- **Coverage Report**: To generate a coverage report, use:
  ::
  
    coverage run --source='.' manage.py test
    coverage report
  
- **Database Operations**: To interact with the SQLite database:
  - Open a SQLite shell session:
    ::
    
      sqlite3
    
  - Connect to the database:
    ::
    
      .open oc-lettings-site.sqlite3
    
  - Display tables in the database:
    ::
    
      .tables
    
  - Display columns in the profiles table:
    ::
    
      pragma table_info(profiles_profile);
    
  - Query the profiles table:
    ::
    
      select user_id, favorite_city from profiles_profile where favorite_city like 'B%';
    
  - Exit the SQLite session:
    ::
    
      .quit
