all : setup

setup: ## Install dependencies
	python3 -m venv venv
	./venv/bin/python -m pip install --upgrade pip
	./venv/bin/python -m pip install -r requirements.txt

run: ## Run the Wave App (run `make setup` first)
	./venv/bin/wave run src.app

bundle: ## wave app bundle for H2O AI Hybrid Cloud
	h2o bundle

submission: # Create a compressed archive file for submission
	cp -r ../notebook/ ./notebook/
	tar cvf ../submission.tar ./notebook/ *.wave
	rm -rf ./notebook/

clean:
	rm -rf venv/
	rm ../submission.tar
