run: build
	poetry run python .
build:
	npm --prefix ./front run build
docker:
	podman compose build
	podman compose push
update:
	poetry update
	poetry run pip freeze > requirements.txt
