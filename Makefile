# Setup virtual environment and install dependencies
setup:
    python -m venv venv
    source venv/bin/activate && pip install -r requirements.txt

# Run tests
test:
    source venv/bin/activate && pytest

# Lint the code
lint:
    source venv/bin/activate && flake8 .

# Clean up virtual environment and generated files
clean:
    deactivate || true
    rm -rf venv
