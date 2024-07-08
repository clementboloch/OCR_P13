Project Setup
=============

To set up and run this project locally, follow these steps:

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

3. Install Dependencies
------------------------

With the virtual environment activated, install the required dependencies using pip. Run:

.. code-block:: sh

   pip install -r requirements.txt

4. Run Database Migrations
---------------------------

Apply the necessary database migrations to set up the database schema. Run:

.. code-block:: sh

   python manage.py migrate

5. Run the Development Server
------------------------------

Start the Django development server to run the application locally. Run:

.. code-block:: sh

   python manage.py runserver

This command starts the application and binds it to port 8000 on your local machine. You can access it by navigating to `http://localhost:8000` in your web browser.

6. Running Tests Locally (Optional)
-----------------------------------

To test the application locally before deployment, you can pull the Docker image from Docker Hub and run a container locally.

.. code-block:: sh

   docker login
   docker pull clementboloch/ocr_p13:latest
   docker run -d -p 8000:8000 clementboloch/ocr_p13:latest

Access `http://localhost:8000` in your browser to see the application.

7. Deployment
-------------

The project uses a CI/CD pipeline for deployment. Pushing changes to the master branch or merging a pull request into master triggers the pipeline, which automatically builds a Docker image, pushes it to Docker Hub, and deploys it to the production server on Render.
