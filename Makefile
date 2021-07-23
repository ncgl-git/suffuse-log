
lint:
	autoflake --in-place --remove-all-unused-imports -r .
	isort . -w 120
	black -l 120 .

test:
	pytest