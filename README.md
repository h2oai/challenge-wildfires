# Wildfire Challenge Starter Kit

Starter kit for H2O.ai [Wildfire Challenge](https://www.h2o.ai/wildfire).

## Wave App Development

### Requirements

1. Install Python 3.6+, and pip3

2. Install H2O Wave SDK - follow instructions for your platform at https://wave.h2o.ai/docs/installation

3. Install H2O AI Cloud CLI (v0.9.1-rc1) to debug, bundle and execute your H2O Wave app: 
   https://h2oai-cloud-release.s3.amazonaws.com/releases/ai/h2o/h2o-cloud/v0.9.1-rc1/index.html

4. Install `tar` (or an alternative, to create a compressed archive file for submission)

### 1. Run the H2O Wave Server

Go to your H2O Wave SDK directory and run the Wave server:

```bash
cd $HOME/wave && ./waved
```
> INFO: On Windows, run `waved.exe` to start the server.


### 2. Clone the H2O.ai Wildfire Challenge GitHub repo

```bash
git clone https://github.com/h2oai/challenge-wildfires.git
```

### 3. Search for Datasets
 * Use the provided [sample for Australia](https://github.com/h2oai/challenge-wildfires/tree/main/notebook/data/australia_fire_daily.csv.gz)
 * Download the [global raw data](https://github.com/h2oai/challenge-wildfires/tree/main/notebook/data)
 * Search for other useful external datasets

### 4. Setup your Python environment

```bash
cd wave-app
make setup
```
or simply
```bash
cd wave-app
python3 -m venv venv
./venv/bin/python -m pip install --upgrade pip
./venv/bin/python -m pip install -r requirements.txt
```

### 5. Run your Wave app

This step is using installed h2o-wave package to run the application.

```bash
cd wave-app
make run
```
or
```bash
cd wave-app
./venv/bin/wave run src.app
```

Point your web browser to http://localhost:10101/ to access the app.

### 6. Bundle your Wave app to run on H2O AI Cloud

This step prepares the Wave app for submission.

```bash
cd wave-app
make bundle
```
or
```bash
cd wave-app
h2o bundle
```

## Debug or Publish your Wave app on H2O AI Cloud

H2O.ai Wildfire & Bushfire Challenge enables participants to deploy, debug, and upload their H2O Wave apps on a managed H2O AI Cloud instance. H2O AI Cloud's Appstore operationalizes AI/ML applications built with H2O Wave. https://challenge.h2o.ai/ is a H2O AI cloud instance managed by H2O.ai and is available for use for Callenge Wildfire.

> Developer Guide is available here: https://h2oai.github.io/h2o-ai-cloud/docs/userguide/developer-guide

Wildfire Challenge allows two usage modes for the participants on the cloud:

1. **publish-cloud-private**: immediately run your current app source in the platform. This command will automatically package your current directory into a .wave bundle, import it into the platform, and run it privately (only visible to you). In the output you will be able to find a URL where you can reach the instance, or visit the "My Instances" in the UI.

2. **publish-cloud-public**: publish an app to the platform. This command will automatically package your current directory into a .wave bundle and import it into the platform. The app will be visible and available to run for all participants. Participants will be run an instance on H2OAIC Appstore.

To get started, please follow the steps below:

### 1. Configure your h2o cli to run your Wave apps on H2O AI Cloud

> Note: For ease of use, config setup steps have been automated for you. When you get to the token portion, you will need to visit https://challenge.h2o.ai/auth/get-token in order to obtain your token. After entering the token here, you are all set.

> _WARNING:_ please ensure that the newly generated config file, `h2o_wildfire_cli_config.toml`, is confidential.

```bash
cd wave-app
make generate-cloud-config
```


### 2. Deploy wave app and view privately

```bash
cd wave-app
make publish-cloud-private
```

### 3. Upload wave app and make it visible to other users

> _WARNING:_ this mode will allow all participants to view and launch an instance of your H2O Wave app on the Appstore.

```bash
cd wave-app
make publish-cloud-public
```

## Submission

This operation is going to create a new archive file in the root directory of the repo called `submission.tar`. The archive follows challenge rules and contains the wave app, Python notebook, and this README.

```bash
cd wave-app
make submission
```


## Starter kit H2O Wave app in action

https://user-images.githubusercontent.com/64787868/140529424-1a9b9c5c-3a64-44ee-8aed-b67625b93e8f.mp4


## Community

There are several communities to discuss topics related to AI/ML or application development:

- H2O.ai Community Slack: http://h2oai-community.slack.com/ provides a space to discuss AI/ML related topics or questions related to H2O.ai open source tools.
- H2O.ai Challenge Forum: https://discuss.challenge.h2o.ai/ is a space to discuss challenges, tools, dataset, and ideas.
- H2O.ai Wave Discussions: https://github.com/h2oai/wave/discussions includes technical topics about Wave and Wave applications development.
