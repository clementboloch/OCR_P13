Project Setup
=============

To set up and run this project locally, follow these steps:

1. Clone the Repository
------------------------

First, clone the repository to your local machine using Git. Open your terminal and run:

.. code-block:: sh

   git clone <repository-url>

Replace `<repository-url>` with the actual URL of the repository.

2. Install Docker and Docker Compose
------------------------------------

Ensure that Docker and Docker Compose are installed on your machine. These are required for building and running the application in a containerized environment. Visit the official Docker documentation for installation instructions: `Install Docker <https://docs.docker.com/get-docker/>`_ and `Install Docker Compose <https://docs.docker.com/compose/install/>`_.

3. Build the Docker Image
-------------------------

Navigate to the project directory and build the Docker image using the provided `Dockerfile`. Run:

.. code-block:: sh

   docker build -t ocr_p13 .

This command builds a Docker image named `ocr_p13` based on the instructions in the `Dockerfile`.

4. Run the Application
----------------------

After the image is built, you can run the application using Docker Compose. The `docker-compose.yml` file defines the services, networks, and volumes for the application. Start the application by running:

.. code-block:: sh

   docker-compose up

This command starts the application and binds it to port 8000 on your local machine.

5. Access the Application
-------------------------

Once the application is running, you can access it by navigating to `http://localhost:8000` in your web browser.

6. Running Tests Locally (Optional)
-----------------------------------

To test the application locally before deployment, you can pull the Docker image from Docker Hub and run a container locally. Replace `commit_hash` with the hash of the latest commit as described in the `README.md`:

.. code-block:: sh

   docker login
   docker pull clementboloch/ocr_p13:latest
   docker run -d -p 8000:8000 clementboloch/ocr_p13:latest

Access `http://localhost:8000` in your browser to see the application.

7. Deployment (Optional)
------------------------

The project uses a CI/CD pipeline for deployment. Pushing changes to the master branch or merging a pull request into master triggers the pipeline, which automatically builds a Docker image, pushes it to Docker Hub, and deploys it to the production server on Render.

For more detailed instructions, refer to the `README.md` file in the project repository.
