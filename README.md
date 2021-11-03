# challenge-wildfires
Starter kit for H2O.ai competition.

### Wave App Development

#### Requirements

1. Python 3.6+, and pip3
2. h2o_wave v0.19.0 (python package)
3. H2O Wave SDK for your platform
   https://wave.h2o.ai/docs/installation
4. H2O AI Cloud cli (to debug and bundle your H2O Wave app)
   https://h2oai-cloud-release.s3.amazonaws.com/releases/ai/h2o/h2o-cloud/latest/index.html
5. `tar` (or an alternative, to create a compressed archive file for submission)

#### 1. Run the H2O Wave Server

Go to your H2O Wave SDK directory and run the server

```bash
./waved
```
> https://wave.h2o.ai/docs/installation#step-4-run


#### 2. Clone the H2O.ai challenge-wildfires GitHub repo

```bash
git clone https://github.com/h2oai/challenge-wildfires.git
```

#### 3. Setup your Python environment

```bash
cd wave-app
make setup
```

#### 4. Run your Wave app

```bash
cd wave-app
make run
```

#### 5. Bundle your Wave app to run on H2O AI Cloud

```bash
cd wave-app
make bundle
```

This will create a new archive file in the root directory of the repo called `bundle.tgz`. This archive file contains your wave app files for submission. These include:
- app.toml; the platform config file for H2O.ai Hybrid Cloud
- source code (in `src/`)
- static assets (in `static/`)
- requirements.txt; pip-managed dependencies of the app


### Submission

**Make a compressed archive file for submission**

```bash
cd wave-app
make submission
```
