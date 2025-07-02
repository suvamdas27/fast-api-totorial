install:
	pip install --upgrade pip &&  pip install -r requirements.txt
lint:
	pylint basicApp/*.py
test:
	# python -m pytest --cov=app --cov-report=xml --cov-report=html
format:
	black basicApp/*.py
all: install lint test format