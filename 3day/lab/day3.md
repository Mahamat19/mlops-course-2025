# Day 3 Lab: Data Version Control (DVC)

**Table of contents:**

- [Day 3 Lab: Data Version Control (DVC)](#day-3-lab-data-version-control-dvc)
  - [Theory Overview](#theory-overview)
    - [What is DVC?](#what-is-dvc)
    - [Why DVC?](#why-dvc)
  - [Part 1: Version Control Data and Models with DVC](#part-1-version-control-data-and-models-with-dvc)
    - [Task 1: Initialize DVC and Track Data](#task-1-initialize-dvc-and-track-data)
    - [`[BONUS]` Task 2: Storing DVC Data Remotely](#bonus-task-2-storing-dvc-data-remotely)
    - [Task 3: Make Local Changes to the Dataset](#task-3-make-local-changes-to-the-dataset)
  - [Part 2: Reproducing Pipelines](#part-2-reproducing-pipelines)
    - [Task 3: Create a Simple DVC Pipeline](#task-3-create-a-simple-dvc-pipeline)
  - [Lab Wrap-Up](#lab-wrap-up)
  - [Bonus Material](#bonus-material)

## Theory Overview

### What is DVC?

- **Data Version Control (DVC)** is an open-source tool for versioning data, models, and ML pipelines.
- Works alongside Git:
  - Git tracks code and metadata files.
  - DVC tracks large data files and models using lightweight `.dvc` metafiles and a content-addressed cache.
- Enables **reproducibility** and **collaboration** in ML projects.

### Why DVC?

- Traditional Git cannot handle large datasets or binaries efficiently.
- DVC decouples **data storage** from **code versioning**.
- Supports **remote storage backends** (local, S3, Azure, GCS, SSH, etc.).

## Part 1: Version Control Data and Models with DVC

### Task 1: Initialize DVC and Track Data

**Objective**: Learn how to use DVC to version control datasets.

**Instructions**:

  1. Install DVC:

  2. Initialize DVC in your Git repository (make sure to be in the root folder) and commit the changes:

  3. Start tracking a local [dataset](https://figshare.com/articles/dataset/Iris_DataSet/878028?file=1315364) with DVC (add it to DVC + push changes to git):

**Note**: You can look into the `name_of_your_dataset.dvc` metafile created for you local dataset. It contains a md5 hash value that is used for referencing the file. If you check the cache inside the `.dvc` directory you can see the file there with the name of the hash value. On GitHub only the metafile is stored/tracked. The actual data is stored in `.dvc/cache`.

### `[BONUS]` Task 2: Storing DVC Data Remotely

**Objective**: Understand how to store and retrieve data using DVC remote storage.

**Instructions:**

  1. Create a "local remote" folder (i.e., a directory in the local file system) to serve as storage. Make sure it is ignored by `.gitignore` if set inside the git repo.

  2. Add it as a DVC remote and commit the DVC config.

  3. Push the data to the "local remote". And check out the local remote now (it should contain a folder of md5 hash names and file contents):

  4. Test the storage. Delete the data from your repo data folder and `.dvc` cache, then pull it from 'remote' (the local that serves as remote):

  5. Check that the data was correctly pulled from the local folder that serves as storage.

**Note**: The `-d` flag of the `dvc remote add` flag sets the `--default` remote to be used when executing `push`, `pull`, `status`, etc. If you want to use a different remote with these functions you can always provide the `--remote` (`-r`) flag to them.

### Task 3: Make Local Changes to the Dataset

**Objective**: Learn how to manage dataset versions with DVC after making changes.

**Instructions:**

  1. Make some changes to the local data (e.g., duplicate/remove a row).

  2. Track the latest version:

  3. Push the changes to the remote and commit the new metafile to git:

## Part 2: Reproducing Pipelines

### Task 3: Create a Simple DVC Pipeline

**Objective:** Learn how to track preprocessing/training steps with DVC.

  1. Write a preprocessing script (e.g., `src/preprocess.py`) that takes raw data and outputs modified data (e.g., multiply one of the features with 2).

  2. Add a training script (e.g., `src/train.py`) that trains a simple model.  

  3. Create DVC pipeline stages with `dvc stage add`. And commit the pipeline files (`dvc.yaml`, `dvc.lock`) to Git.

**Note:** `dvc.yaml` contains pipeline definition; `dvc.lock` records exact versions.

  4. Run the pipeline with `dvc repro`.

**Check:** data/iris_clean.csv and data/model.pkl are created.

---

## Lab Wrap-Up

- Learned how to version datasets and models with DVC.  
- Configured remote storage for collaboration.  
- Built a reproducible pipeline with `dvc repro`.  

---

## Bonus Material

- Try integrating with **cloud storage**: S3, Azure, or GCS.  
- Explore `dvc exp run` for experiment management.  
- Useful links:
  - [DVC Docs](https://dvc.org/doc)
  - [DVC Pipelines](https://dvc.org/doc/start/data-pipelines)
