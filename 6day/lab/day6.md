# Day 6 Lab: CI/CD for FastAPI Applications

## Table of Contents

- [Day 6 Lab: CI/CD for FastAPI Applications](#day-6-lab-cicd-for-fastapi-applications)
  - [Table of Contents](#table-of-contents)
  - [Overview](#overview)
  - [Theoretical Concepts](#theoretical-concepts)
    - [Continuous Integration and Continuous Deployment (CI/CD)](#continuous-integration-and-continuous-deployment-cicd)
    - [Writing Tests for FastAPI](#writing-tests-for-fastapi)
    - [GitHub Actions](#github-actions)
  - [Learning Objectives](#learning-objectives)
  - [Lab Instructions](#lab-instructions)
    - [Part 1: Writing Tests for FastAPI](#part-1-writing-tests-for-fastapi)
      - [Task 1.1: Setting up Pytest](#task-11-setting-up-pytest)
      - [Task 1.2: Writing Unit Tests for FastAPI](#task-12-writing-unit-tests-for-fastapi)
    - [Part 2: Setting Up GitHub Actions for CI/CD](#part-2-setting-up-github-actions-for-cicd)
      - [Task 2.1: Creating a GitHub Actions Workflow](#task-21-creating-a-github-actions-workflow)
      - [Task 2.2: Running Automated Tests](#task-22-running-automated-tests)
      - [Task 2.4: Run CICD on python changes](#task-24-run-cicd-on-python-changes)
      - [Task 2.3: Manual Dispatch with Inputs](#task-23-manual-dispatch-with-inputs)
    - [`BONUS` Part 3: Using GitHub Secrets and Variables](#bonus-part-3-using-github-secrets-and-variables)
      - [Task 3.1: Demonstrate using GitHub Secrets and Variables in Workflows](#task-31-demonstrate-using-github-secrets-and-variables-in-workflows)
      - [Task 3.2: Extract GitHub Secrets with a Workflow job](#task-32-extract-github-secrets-with-a-workflow-job)
  - [Conclusion](#conclusion)
  - [Useful Links](#useful-links)

## Overview

In this lab, we will explore how to implement a continuous integration and continuous deployment (CI/CD) pipeline for your FastAPI application. We'll write tests using **pytest**, set up a GitHub Actions workflow to automate the testing process, and build and push Docker images automatically when code is pushed to the repository.

## Theoretical Concepts

### Continuous Integration and Continuous Deployment (CI/CD)

CI/CD is a software development practice where code changes are automatically tested, built, and deployed to a production or staging environment. It involves two key processes:

- **Continuous Integration (CI)**: Automates the testing and integration of new code into the main branch. Developers frequently commit code, which triggers automated tests to ensure new changes don’t break existing functionality.
- **Continuous Deployment (CD)**: Automatically deploys the application to a production environment after the code passes the CI phase. This ensures that new features or bug fixes are delivered quickly and reliably.

### Writing Tests for FastAPI

FastAPI supports testing using the **TestClient** from **Starlette**, which provides a simple interface for testing endpoints. Automated tests ensure that changes to the codebase do not introduce new bugs. In this lab, you'll use **pytest** and **pytest-mock** to test FastAPI routes.

Key concepts for testing:

- **Unit Tests**: Small, isolated tests that verify the correctness of individual units of code (e.g., functions, routes).
- **Mocking**: Replacing parts of the system under test with mock objects that simulate the behavior of real components. This allows us to test a system independently of external dependencies, such as databases or external services.

### GitHub Actions

GitHub Actions is a CI/CD platform integrated into GitHub repositories. It allows you to define workflows in a YAML file to automate testing, building, and deploying your application. In this lab, you’ll use GitHub Actions to run tests on every code push, ensuring that your FastAPI app works as expected.

## Learning Objectives

By the end of this lab, students will:

- Write automated tests for FastAPI applications using **pytest**.
- Set up a GitHub Actions pipeline to run tests on each push/commit.
- Work with secrets, variables, manual dispatch.

## Lab Instructions

### Part 1: Writing Tests for FastAPI

Before setting up CI/CD, it's essential to write tests for your application. In this section, you'll write unit tests for your FastAPI app.

#### Task 1.1: Setting up Pytest

1. Install **pytest** and **pytest-mock** if not already installed

2. Create a file named `test_main.py` for your tests

#### Task 1.2: Writing Unit Tests for FastAPI

You’ll write tests for your FastAPI application. You can always check out the [documentation](https://fastapi.tiangolo.com/tutorial/testing/#using-testclient) on how it can be done.

If needed, mock/patch the models (predict function) to return default values.

1. Test the endpoints: `root`, `health_check`, `list_models`.
2. Test prediction with an invalid model name.
3. Test prediction with a valid model name. Make sure to mock the models, no need to load them and do actual predictions.
4. Run `python -m pytest ./tests/test_main.py` to execute the tests.

### Part 2: Setting Up GitHub Actions for CI/CD

In this part, you'll create a CI/CD pipeline using GitHub Actions that runs your tests every time you push code.

#### Task 2.1: Creating a GitHub Actions Workflow

1. In your project, create a `.github/workflows` directory

2. Create a file named `cic.yml` inside the `.github/workflows` directory

3. Fill in the `yml` file such that:
   - define name of your workflow
   - define rules when to trigger (e.g., on push to main, on pull request to main, etc.)
   - define a `test` job that will include the steps of:
     - setting up python 3.11
     - installing dependencies and upgrading pip
     - running tests

#### Task 2.2: Running Automated Tests

1. Push your code to GitHub:

2. Go to the `Actions` tab of your GitHub repository and you should see the workflow running.

3. Fail the pipeline:
    - Update your code in such a way to make the tests pipeline fail.
    - Push your code to GitHub or create a new PullRequest.
    - Notice how the pipeline failed and examine the logs.
    - Fix the introduced error.

#### Task 2.4: Run CICD on python changes

- Run the testing pipeline only when there is changes to python files, requirements or any workflow files.
- Push to Github.
- Change some non-python files and see if pipeline gets triggered.

#### Task 2.3: Manual Dispatch with Inputs

1. Create a new pipeline that will be triggered manually (on manual dispatch).
2. You should accept an input that will be printed in the job.
3. Add an additional boolean input, if true run another step with an additional print.

### `BONUS` Part 3: Using GitHub Secrets and Variables

#### Task 3.1: Demonstrate using GitHub Secrets and Variables in Workflows

1. Define one **secret** and one **variable** in your GitHub project:
   - In `Settings` of the Repo go to `Secrets and variables` and then `Actions`
   - Add `New repository secret`
   - Add `New repository variable`
2. Write a simple **workflow** where you will attempt to print these two values (the secret value should print as `***`).

#### Task 3.2: Extract GitHub Secrets with a Workflow job

1. Write a **workflow** that extracts the secret saved on GitHub and makes it 'visible' to the person who reads the **workflow** (job runner) logs.

## Conclusion

In this lab, you’ve learned how to implement a robust CI/CD pipeline for FastAPI applications. You started by writing automated tests for your FastAPI app using **pytest** and integrating these tests into a GitHub Actions workflow.

By setting up automated testing and continuous deployment, you’ve streamlined the process of releasing new features, ensuring code quality, and minimizing manual effort. This CI/CD workflow is essential for developing scalable, production-ready ML or web applications.

---

## Useful Links

- [FastAPI Documentation](https://fastapi.tiangolo.com/)
- [Pytest Documentation](https://docs.pytest.org/en/6.2.x/)
- [GitHub Actions Documentation](https://docs.github.com/en/actions)
