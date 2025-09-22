# Day 1 Lab: Introduction to MLOps

**Table of contents:**

- [Day 1 Lab: Introduction to MLOps](#day-1-lab-introduction-to-mlops)
  - [Theory Overview](#theory-overview)
    - [Repository and Version Control](#repository-and-version-control)
    - [Git and `.gitignore`](#git-and-gitignore)
    - [Python Virtual Environment and `requirements.txt`](#python-virtual-environment-and-requirementstxt)
    - [`.env` Files and Environment Variables](#env-files-and-environment-variables)
    - [Branching Strategies in Git](#branching-strategies-in-git)
    - [Introduction to Testing in ML](#introduction-to-testing-in-ml)
  - [Part 1: Repository Setup and Version Control](#part-1-repository-setup-and-version-control)
    - [Task 1: Create a New Repository](#task-1-create-a-new-repository)
    - [Task 2: Initialize Git and Set Up `.gitignore`](#task-2-initialize-git-and-set-up-gitignore)
  - [Part 2: Setting Up Python Environment](#part-2-setting-up-python-environment)
    - [Task 1: Create and Activate Python Virtual Environment](#task-1-create-and-activate-python-virtual-environment)
    - [Task 2: Create and Populate `requirements.txt`](#task-2-create-and-populate-requirementstxt)
  - [Part 3: Build a Simple ML Pipeline](#part-3-build-a-simple-ml-pipeline)
    - [Task 1: Load and Explore the Iris Dataset](#task-1-load-and-explore-the-iris-dataset)
    - [Task 2: Train a Logistic Regression Model](#task-2-train-a-logistic-regression-model)
    - [Task 3: Write and Run a Simple Unit Test](#task-3-write-and-run-a-simple-unit-test)
    - [Task 4: Visualize Data and Model Performance](#task-4-visualize-data-and-model-performance)
  - [Part 4: Collaborate Using Branches and Pull Requests](#part-4-collaborate-using-branches-and-pull-requests)
    - [Task 1: Partner Repository Review and Pull Request](#task-1-partner-repository-review-and-pull-request)
  - [`[BONUS]` Part 5: Handling Secret Files](#bonus-part-5-handling-secret-files)
    - [Task 1: Accidentally Push a Secret File and Remove It](#task-1-accidentally-push-a-secret-file-and-remove-it)
  - [Lab Wrap-Up: What We Learned](#lab-wrap-up-what-we-learned)
  - [Bonus Material](#bonus-material)
    - [Best Practices and Useful Links](#best-practices-and-useful-links)
    - [Practice Git Skills](#practice-git-skills)

## Theory Overview

### Repository and Version Control

- **Repository**: A repository (or repo) is a central place where all the files for a particular project are stored. It contains the project's code, configuration files, documentation, and version history. GitHub and GitLab are platforms that host repositories and provide version control services.
  - **Example**: You can create a repository for your MLOps project where you track changes to your code and collaborate with others.

### Git and `.gitignore`

- **Git**: Git is a distributed version control system that allows multiple people to work on a project simultaneously. It tracks changes to files and enables collaboration through branches and commits.
  - **Example**: You use Git to commit changes to your code, allowing you to keep a history of modifications and collaborate with others.
- **`.gitignore`**: This file tells Git which files or directories to ignore when committing changes. It prevents unnecessary files from being tracked.
  - **Example**: You might add `__pycache__/` to `.gitignore` to avoid tracking Python bytecode files.

### Python Virtual Environment and `requirements.txt`

- **Python Virtual Environment**: A virtual environment is an isolated environment in which you can install packages separately from the system-wide Python installation. It helps manage dependencies and avoid conflicts.
  - **Example**: By creating a virtual environment, you ensure that the libraries used in your project do not affect other Python projects.
- **`requirements.txt`**: This file lists all the Python packages required for a project. It allows others to replicate the environment easily.
  - **Example**: A `requirements.txt` file might include packages like `scikit-learn` and `pandas`, which are needed to run your ML code.

### `.env` Files and Environment Variables

- **Environment Variables**: Environment variables are used to store configuration values and secrets (like API keys or database credentials) that your application needs to run. These variables are typically stored in a `.env` file in your project directory.
  - **Example**: A `.env` file might contain a variable like `SECRET_KEY=mysecretkey123` that your application uses for security.
- **`.env` Files in Git**: It's important to ensure that `.env` files are not tracked by Git to prevent sensitive information from being exposed. This is typically managed by adding `.env` to your `.gitignore` file.
  - **Example**: Adding `.env` to `.gitignore` ensures that your environment variables are not accidentally committed to your repository.

### Branching Strategies in Git

- **Branching**: Branching allows you to create a separate line of development in your repository. It enables you to work on features or fixes without affecting the main codebase.
  - **Example**: You can create a branch named `feature/new-model` to develop a new machine learning model, keeping the main branch clean.
- **Merging**: Merging is the process of integrating changes from one branch into another. It is commonly used to bring feature changes back into the main branch after development is complete.
  - **Example**: Once you finish developing a new model on a feature branch, you can merge it into the main branch.

### Introduction to Testing in ML

- **Testing**: Testing ensures that code works as expected and helps identify bugs or issues early. In ML, testing can include checking model performance, data integrity, and code functionality.
  - **Example**: Writing a test to verify that your model achieves a minimum accuracy ensures that any changes don't degrade model performance.

## Part 1: Repository Setup and Version Control

### Task 1: Create a New Repository

- **Objective**: Introduce version control using GitHub.
- **Instructions:**
  1. Go to [GitHub](https://github.com/).
  2. Create a new repository titled `mlops-introduction`.
  3. Clone the repository to your local machine:

     ```bash
     git clone https://github.com/YOUR_USERNAME/mlops-introduction.git
     cd mlops-introduction
     ```

### Task 2: Initialize Git and Set Up `.gitignore`

- **Objective**: Initialize Git and set up a `.gitignore` file.
- **Instructions:**
  1. Initialize Git if necessary:

     ```bash
     git init
     ```

  2. Create a `.gitignore` file with:

     ```
     __pycache__/
     ```

  3. Add, commit, and push changes:

     ```bash
     git add .
     git commit -m "Initial commit"
     git push origin main
     ```

## Part 2: Setting Up Python Environment

### Task 1: Create and Activate Python Virtual Environment

- **Objective**: Set up a clean Python environment using `virtualenv`.
- **Instructions:**
  1. Install `virtualenv` if not installed:

     ```bash
     pip install virtualenv
     ```

  2. Create and activate environment:

     ```bash
     virtualenv mlops-lab1
     source mlops-lab1/bin/activate  # On Windows, use `mlops-lab1\Scripts\activate`
     ```

### Task 2: Create and Populate `requirements.txt`

- **Objective**: Document project dependencies using `requirements.txt`.
- **Instructions:**
  1. Create a `requirements.txt` file in the project directory:

     ```bash
     touch requirements.txt
     ```

  2. Add the required libraries to `requirements.txt`:

     ```
     scikit-learn
     pandas
     numpy
     matplotlib
     ```

  3. Install dependencies from `requirements.txt`:

     ```bash
     pip install -r requirements.txt
     ```

  4. Verify installation:

     ```bash
     python -c "import sklearn, pandas, numpy, matplotlib; print('Libraries installed successfully')"
     ```

## Part 3: Build a Simple ML Pipeline

If you find it easier, you can initially write and test your code in a Jupyter Notebook (`.ipynb`). This allows for interactive coding and testing. Once you have verified your code works correctly, copy it into Python functions and create a working script (`.py`).

### Task 1: Load and Explore the Iris Dataset

- **Objective**: Load and examine a public dataset. Then, train a simple model.
- **Instructions:**

  1. Create a new branch for this task:

     ```bash
     git checkout -b feature/load-data
     ```

  2. Create `iris_pipeline.py` with:

     ```python
     import pandas as pd
     from sklearn.datasets import load_iris

     def load_dataset():
         iris = load_iris()
         df = pd.DataFrame(iris.data, columns=iris.feature_names)
         df['species'] = iris.target
         df["species_name"] = df.apply(
             lambda x: str(iris.target_names[int(x["species"])]), axis=1
         )
         return df

     if __name__ == "__main__":
         iris_df = load_dataset()
         print(iris_df.head())
     ```

  3. Add, commit, and push your changes:

     ```bash
     git add iris_pipeline.py
     git commit -m "Load and explore Iris dataset"
     git push origin feature/load-data
     ```

  4. Open a pull request on GitHub to merge your changes into the `main` branch and review it before merging.

### Task 2: Train a Logistic Regression Model

- **Objective**: Build and evaluate a simple model.
- **Instructions:**

  1. Create a new branch for this task:

     ```bash
     git checkout -b feature/train-model
     ```

  2. Extend `iris_pipeline.py` to include:

     ```python
     from sklearn.model_selection import train_test_split
     from sklearn.linear_model import LogisticRegression
     from sklearn.metrics import accuracy_score

     def train(df):
         X_train, X_test, y_train, y_test = train_test_split(
             df.iloc[:, :-1], df["species"], test_size=0.2, random_state=42
         )

         model = LogisticRegression(max_iter=200)
         model.fit(X_train, y_train)

         return model, X_train, X_test, y_train, y_test

     def get_accuracy(model, X_test, y_test):
         predictions = model.predict(X_test)
         accuracy = accuracy_score(y_test, predictions)

         return accuracy

     if __name__ == "__main__":
         iris_df = load_dataset()
         model, X_train, X_test, y_train, y_test = train(iris_df)
         accuracy = get_accuracy(model, X_test, y_test)
         print(f"Accuracy: {accuracy:.2f}")
     ```

  3. Update `requirements.txt` if new dependencies are required:

     ```
     scikit-learn
     ```

  4. Add, commit, and push your changes:

     ```bash
     git add iris_pipeline.py requirements.txt
     git commit -m "Train logistic regression model"
     git push origin feature/train-model
     ```

  5. Open a pull request on GitHub to merge your changes into the `main` branch and review it before merging.

### Task 3: Write and Run a Simple Unit Test

- **Objective**: Introduce the concept of testing in ML pipelines.
- **Note**: The tests provided here are basic/dummy examples to demonstrate the concept of testing.
- **Instructions:**
  1. Create a new branch for this task:

     ```bash
     git checkout -b feature/add-tests
     ```

  2. Create a test script named `test_iris_pipeline.py`.

  3. Write test functions for each major component in your script. For example:
     ```python
     from iris_pipeline import load_dataset, train, get_accuracy

     def test_load_dataset():
         df = load_dataset()
         assert not df.empty, "The DataFrame should not be empty after loading the dataset."

     def test_model_accuracy():
         df = load_dataset()
         model, X_train, X_test, y_train, y_test = train(df)
         accuracy = get_accuracy(model, X_test, y_test)
         assert accuracy > 0.8, "Model accuracy is below 80%."
     ```

  4. Run the tests using a testing framework like `pytest`:

     ```bash
     pytest test_iris_pipeline.py
     ```

  5. Add, commit, and push your changes:

     ```bash
     git add test_iris_pipeline.py
     git commit -m "Add unit tests for data loading, training, and model accuracy"
     git push origin feature/add-tests
     ```

  6. Open a pull request on GitHub to merge your changes into the `main` branch and review it before merging.

### Task 4: Visualize Data and Model Performance

- **Objective**: Visualize data and model outputs.
- **Instructions:**

  1. Create a new branch for this task:

     ```bash
     git checkout -b feature/add-visualizations
     ```

  2. Update your `iris_pipeline.py` script to include functions for data visualization using `matplotlib`.

  3. Add the following visualization functions to `iris_pipeline.py`:

     ```python
     import matplotlib.pyplot as plt
     from sklearn.metrics import ConfusionMatrixDisplay

     def plot_feature(df, feature):
         # Plot a histogram of one of the features
         df[feature].hist()
         plt.title(f"Distribution of {feature}")
         plt.xlabel(feature)
         plt.ylabel("Frequency")
         plt.show()

     def plot_features(df):
         # Plot scatter plot of first two features.
         scatter = plt.scatter(
             df["sepal length (cm)"], df["sepal width (cm)"], c=df["species"]
         )
         plt.title("Scatter plot of the sepal features (width vs length)")
         plt.xlabel(xlabel="sepal length (cm)")
         plt.ylabel(ylabel="sepal width (cm)")
         plt.legend(
             scatter.legend_elements()[0],
             df["species_name"].unique(),
             loc="lower right",
             title="Classes",
         )
         plt.show()

     def plot_model(model, X_test, y_test):
         # Plot the confusion matrix for the model
         ConfusionMatrixDisplay.from_estimator(estimator=model, X=X_test, y=y_test)
         plt.title("Confusion Matrix")
         plt.show()
     ```

  4. Call these functions in the `__main__` block to visualize the data and model performance:

     ```python
     if __name__ == "__main__":
         iris_df = load_dataset()
         model, X_train, X_test, y_train, y_test = train(iris_df)
         accuracy = get_accuracy(model, X_test, y_test)
         print(f"Accuracy: {accuracy:.2f}")

         plot_feature(iris_df, "sepal length (cm)")
         plot_features(iris_df)
         plot_model(model, X_test, y_test)
     ```

  5. Update `requirements.txt` if new dependencies are required:

     ```
     matplotlib
     ```

  6. Add, commit, and push your changes:

     ```bash
     git add iris_pipeline.py requirements.txt
     git commit -m "Add data visualization functions and update script"
     git push origin feature/add-visualizations
     ```

  7. Open a pull request on GitHub to merge your changes into the `main` branch and review it before merging.


## Part 4: Collaborate Using Branches and Pull Requests

### Task 1: Partner Repository Review and Pull Request

- **Objective**: Gain hands-on experience with branching, pull requests, and collaboration.
- **Instructions:**

  1. Pair up with a classmate and fork their repository:
     - Navigate to your partner's repository on GitHub.
     - Fork the repository to your own GitHub account.
  2. Clone your forked repository:

     ```bash
     git clone https://github.com/YOUR_USERNAME/partner-repo.git
     cd partner-repo
     ```

  3. Create a new branch for your changes:

     ```bash
     git checkout -b add-readme
     ```

  4. Create a `README.md` file in your partner's repository with:

     ```markdown
     # MLOps Introduction - Iris ML Pipeline

     ## Project Overview

     This project demonstrates the basics of setting up an MLOps pipeline using the Iris dataset and logistic regression.

     ## Setup Instructions

     1. Clone the repository.
     2. Create and activate a Python environment.
     3. Install the necessary libraries from `requirements.txt`.
     4. Run the `iris_pipeline.py` script to train and evaluate the model.

     ## How to Use

     - `iris_pipeline.py` contains the ML pipeline for the Iris dataset.
     - Use the script to train and evaluate a logistic regression model.
       ...
     ```

  5. Add, commit, and push your changes:

     ```bash
     git add README.md
     git commit -m "Add README.md for partner's repository"
     git push origin add-readme
     ```

  6. Open a pull request on GitHub to merge your changes into the main branch of your partner's repository.
     - Go to your forked repository on GitHub.
     - Click on "Compare & pull request" to create a pull request.
     - Fill out the pull request form and submit it.
  7. **Review and Collaboration**: Your partner will review your pull request, leave comments, and discuss changes if necessary. They will also need to merge your pull request into their main branch after reviewing.

## `[BONUS]` Part 5: Handling Secret Files

### Task 1: Accidentally Push a Secret File and Remove It

- **Objective**: Learn how to handle and remove sensitive data that has been accidentally pushed to a repository.
- **Instructions:**
  1. Create a `.env` file containing a mock secret key:

     ```bash
     echo "SECRET_KEY=mysecretkey123" > .env
     ```

  2. Add and commit the `.env` file to your repository by mistake:

     ```bash
     git add .env
     git commit -m "Accidentally add .env file with secret key"
     git push origin main
     ```

  3. **Task**: Remove the `.env` file from the repository and all commit history:
     - First, remove the file from your local commit history:

       ```bash
       git rm --cached .env
       echo ".env" >> .gitignore
       git add .gitignore
       git commit -m "Remove .env file and add to .gitignore"
       ```

     - Use `git filter-branch` to clean the history:

       ```bash
       git filter-branch --force --index-filter "git rm --cached --ignore-unmatch .env" --prune-empty --tag-name-filter cat -- --all
       ```

     - Push the rewritten history to GitHub:

       ```bash
       git push origin --force --all
       git push origin --force --tags
       ```

     - Clean up your local repository to remove the old references:

       ```bash
       rm -rf .git/refs/original/
       git reflog expire --expire=now --all
       git gc --prune=now --aggressive
       ```

  4. Revoke any leaked credentials.
     - As with any method, if your `.env` file contained sensitive information, revoke and regenerate those credentials immediately.

## Lab Wrap-Up: What We Learned

- **Repository and Version Control**: We learned how to create and manage a repository using GitHub, initialize version control, and set up `.gitignore` to exclude unnecessary files.
- **Python Environment Setup**: We set up a Python virtual environment to isolate project dependencies and documented these dependencies using `requirements.txt`.
- **Building ML Pipelines**: We built a simple ML pipeline using the Iris dataset, performed data exploration, trained a logistic regression model, and added simple unit tests to ensure our model's performance.
- **Git Branching and Merging**: We explored how to create branches for new features and merge them back into the main branch.
- **Collaboration Using Pull Requests**: We practiced forking repositories, creating branches, and making pull requests. We also learned about the importance of reviewing and merging changes in a collaborative environment.
- **Handling Secrets in Git**: We learned how to handle and permanently remove sensitive data from a Git repository to ensure security.

## Bonus Material

### Best Practices and Useful Links

- **Branching Strategy**: Use branches for new features, bug fixes, or experiments. This keeps the main branch clean and stable.
  - [GitHub Flow](https://guides.github.com/introduction/flow/) is a popular branching strategy.
- **Commit Messages**: Write clear and descriptive commit messages. This helps others understand the purpose of each change.
  - [How to Write a Commit Message](https://chris.beams.io/posts/git-commit/) provides guidelines for effective commit messages.
- **Pull Request Reviews**: Always review pull requests carefully. Leave constructive feedback and ensure code quality and functionality.
- **Useful links**:
  - [Generate .gitignore files](https://www.toptal.com/developers/gitignore)
  - [Remove Leaked Files](https://dev.to/kodebae/how-to-remove-a-leaked-env-file-from-github-permanently-3lei?ref=dailydev)
  - [How to work with multiple GitHub accounts on a single machine?](https://gist.github.com/rahularity/86da20fe3858e6b311de068201d279e3).
  - [Requirements.txt File Format](https://pip.pypa.io/en/stable/reference/requirements-file-format/)

### Practice Git Skills

- **Git Exercises and Tutorials**: Additional exercises to improve your Git skills.
  - [Git Immersion](http://gitimmersion.com/)
- **Learn Git Branching**: An interactive tool to practice Git branching and merging.
  - [Learn Git Branching](https://learngitbranching.js.org/)
