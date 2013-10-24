build:
	virtualenv .
	bash -c "source bin/activate && bin/pip install -r freeze.txt"
