# Individual Project 1: Continuous Integration using GitHub Actions of Python Data Science Project
### By Daniel Medina

![format workflow](https://github.com/medinardaniel/ci-github-actions/actions/workflows/format.yml/badge.svg)
![install workflow](https://github.com/medinardaniel/ci-github-actions/actions/workflows/install.yml/badge.svg)
![lint workflow](https://github.com/medinardaniel/ci-github-actions/actions/workflows/lint.yml/badge.svg)
![test workflow](https://github.com/medinardaniel/ci-github-actions/actions/workflows/test.yml/badge.svg)

#### YouTube Walkthrough Link
https://youtu.be/GnCb82L9MPg

#### Summary
In this project I use Continuous Integration and Github Actions for a Python-based data science project.
#### Project Structure
- Jupyter Notebook: Analyzes student_mental_health.csv. Produces some general statistics on the dataset.
- Python Script: Analyzes student_mental_health.csv. Produces some general statistics on the dataset. Same content as Jupyter Notebook.
- lib.py file: Holds shared code between the Jupyter notebook and the Python script.
- Makefile:
    - Runs all tests
    - Formats code with Python black
    - Lints code with Ruff
    - Installs code via pip install -r requirements.txt
- test_script.py to test script
- test_lib.py to test library
- Pinned requirements.txt
- GitHub Actions performs all four Makefile commands with badges for each one in the README.mds
