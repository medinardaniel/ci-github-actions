install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt

test:
	python3 -m pytest --nbval src/*.ipynb
	python3 -m pytest -vv --cov=lib

format:	
	black ./*.py
	nbqa black src/*.ipynb 

lint:
	nbqa ruff src/*.ipynb
	ruff check ./*.py
		
all: install lint test format
