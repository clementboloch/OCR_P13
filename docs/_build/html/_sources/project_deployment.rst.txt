Project Deployment and Management Procedures
============================================

The project API deployment and management procedures are outlined through a combination of the Continuous Integration/Continuous Deployment (CI/CD) pipeline, Docker containerization, and deployment to Render. Here's a summary of the procedures based on the provided workspace information:

CI/CD Pipeline
--------------

1. Compilation and Testing
   -----------------------
   Upon each push, changes undergo a compilation and testing phase to ensure the code is functional, adheres to coding standards, and maintains a test coverage above 80%. This is automated through GitHub Actions as specified in the `.github/workflows/ci.yml` file.

2. Containerization
   ----------------
   If tests pass and the push is made to the master branch, a Docker image is built, tagged with the commit hash, and pushed to Docker Hub. This process is likely defined in the `Dockerfile` and possibly further configured in `docker-compose.yml`.

3. Deployment to Production
   ------------------------
   When an update is pushed to the master branch, the Docker image is retrieved and automatically deployed to the Render server to update the production site. This is automated through a deployment step in the GitHub Actions workflow, which uses a POST request to Render's API for deploying the service, as seen in the deployment step in the `.github/workflows/ci.yml` file.

Docker Management
-----------------

- Local Testing: Before deployment, the Docker image can be tested locally by pulling the latest image from Docker Hub and running a container. This is documented in the `README.md` under the section "Tester Localement (Optionnel)".

- Commands for Local Testing:

  .. code-block:: sh

     docker login
     docker pull clementboloch/ocr_p13:latest
     docker run -d -p 8000:8000 clementboloch/ocr_p13:latest

  Access the application at `http://localhost:8000` in a browser to verify functionality.

Deployment Options
------------------

1. Pushing Changes to Master
   -------------------------
   Commit and push changes locally, then push to the master branch of the remote repository. This triggers the CI/CD pipeline for deployment.

2. Merging into Master
   -------------------
   If working on a feature or fix branch, create a Pull Request (PR) on GitHub from your branch to master. Once the PR is approved and merged into master, it triggers the CI/CD pipeline for deployment.

Additional Management Procedures
--------------------------------

- Database Management: Instructions for interacting with the SQLite database, including opening a shell session, connecting to the database, and querying tables, are provided in the `README.md`.

- Linting and Unit Testing: Procedures for linting with `flake8` and running unit tests with `pytest` are documented, ensuring code quality and functionality before deployment.

- Virtual Environment Setup: Detailed steps for setting up a Python virtual environment for local development are included in the `README.md`, ensuring a consistent development environment.

This documentation provides a comprehensive overview of the deployment and management procedures for the project API, leveraging automation, containerization, and cloud deployment to streamline the process.
