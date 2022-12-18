format:
	python -m autoflake --recursive --in-place --remove-all-unused-imports --ignore-init-module-imports app
	python -m isort app
	python -m black -l 160 app