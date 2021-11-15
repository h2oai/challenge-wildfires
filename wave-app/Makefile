#
# Parameters
#

# Name of created virtual environment
VENV_NAME ?= venv
# Python to use to build virtual environment
PYTHON    ?= python3
# Location of h2o cli
H2O_CLI   ?= h2o

#
# Internal
#
PYTHON_BIN := $(VENV_NAME)/bin/python
WAVE_BIN   := $(VENV_NAME)/bin/wave

all: setup

$(PYTHON_BIN):
	$(PYTHON) -m venv $(VENV_NAME)
	$(PYTHON_BIN) -m pip install --upgrade pip

$(WAVE_BIN): $(PYTHON_BIN) requirements.txt
	$(PYTHON_BIN) -m pip install -r requirements.txt

setup: $(PYTHON_BIN) $(WAVE_BIN)

run: $(WAVE_BIN)
	$(WAVE_BIN) run src.app

generate-cloud-config:
	cp h2o_wildfire_cli_config_template.toml h2o_wildfire_cli_config.toml
	$(H2O_CLI) config update-token --conf h2o_wildfire_cli_config.toml

publish-cloud-private:
	$(H2O_CLI) bundle deploy --conf h2o_wildfire_cli_config.toml

publish-cloud-public:
	$(H2O_CLI) bundle import -v ALL_USERS --conf h2o_wildfire_cli_config.toml

bundle: ## Wave app bundle for H2O AI Hybrid Cloud
	$(H2O_CLI) bundle

submission: # Create a compressed archive file for submission
	cp -r ../notebook/ ./notebook/
	tar cvf ../submission.tar ./notebook/ *.wave
	rm -rf ./notebook/

clean:
	rm -f ../submission.tar
	rm -f *.wave

mrproper: clean
	rm -rf $(VENV_NAME)

.PHONY: all setup run bundle submission clean
