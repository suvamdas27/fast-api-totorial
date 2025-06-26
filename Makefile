install:
	pip install --upgrade pip &&  pip install -r requirements.txt
lint:
	pylint .
test:
	# python -m pytest --cov=app --cov-report=xml --cov-report=html
format:
	black .
all: install lint test format