install:
	pip install --upgrade pip --user --no-cache-dir &&\
		pip install -r requirements.txt --user --no-cache-dir

test:
	#python -m pytest -vv --cov=myrepolib tests/*.py
	#python -m pytest --nbval notebook.ipynb


lint:
	pylint --disable=R,C,E1120 animal.py

all: install lint test