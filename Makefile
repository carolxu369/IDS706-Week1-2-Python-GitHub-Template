setup:
    python -m venv venv
    source venv/bin/activate
    pip install -r requirements.txt

test:
    python -m pytest

lint:
    pylint descriptive.py

clean:
    rm -rf venv __pycache__