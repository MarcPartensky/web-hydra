run:
	poetry run python .
build:
	podman compose build
update:
	poetry update
	poetry run pip freeze > requirements.txt
