setup:
    pip install -r requirements.txt

test:
    python test_python_script.py

lint:
    pylint python_script.py