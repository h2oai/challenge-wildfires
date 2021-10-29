all : setup

setup: ## Install dependencies
	python3 -m venv venv
	./venv/bin/python -m pip install --upgrade pip
	./venv/bin/python -m pip install -r requirements.txt

run: ## Run the Wave App (run `make setup` first)
	./venv/bin/wave run src.app

bundle: # Create a compressed archive file for submission
	tar -czf ../bundle.tgz ./

clean:
	rm -rf venv/
	rm ../bundle.tgz