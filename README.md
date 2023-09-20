# Individual Project 1: Continuous Integration using GitHub Actions of Python Data Science Project
### By Daniel Medina

#### Summary
In this project I use Continuous Integration and Github Actions for a Python-based data science project.
#### Project Structure
- Jupyter Notebook
- Python Script
- lib.py file: holds shared code between the Jupyter notebook and the Python script.
- Makefile:
    - Runs all tests
    - Formats code with Python black
    - Lints code with Ruff
    - Installs code via pip install -r requirements.txt
- test_script.py to test script
- test_lib.py to test library
- Pinned requirements.txt
- GitHub Actions performs all four Makefile commands with badges for each one in the README.mds
