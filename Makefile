
lint:
	autoflake --in-place --remove-all-unused-imports -r .
	isort . -w 120
	black -l 120 .

test:
	mypy ./suffuse_log --ignore-missing-imports
	pytest ./suffuse_log