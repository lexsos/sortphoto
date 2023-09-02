clean:
	rm -fr build/
	rm -fr dist/
	rm -fr .eggs/
	rm -fr *.egg-info
	find . -iname '*.egg' -delete
	find . -iname '*.pyc' -delete
	find . -iname '*.pyo' -delete
	find . -iname '*~' -delete
	find . -iname '__pycache__' -delete

develop: clean
	python3.11 -m venv env
	env/bin/pip install -U pip wheel
	env/bin/pip install -Ue '.[develop]'
	env/bin/pip check
