# Makefile untuk pipeline RAG PDF

venv:
	python3 -m venv .venv
	. .venv/bin/activate && pip install -r requirements.txt

install:
	pip install -r requirements.txt

run:
	. .venv/bin/activate && python app/main.py

test:
	. .venv/bin/activate && pytest tests/

lint:
	. .venv/bin/activate && flake8 app/ tests/

migrate:
	. .venv/bin/activate && python scripts/migrate.py

clean:
	rm -rf .venv __pycache__ *.pyc .mypy_cache .pytest_cache
