# project_dustbin / trashify

A user friendly app for both normal users and organizations that bridges the gap between them and waste
collectors to provide easy and organized waste collection.

## Prerequisites

- Python 3.8 or higher
- [Auth0 account](<https://auth0.com/>)
- [Docker](<https://www.docker.com/>)

## Installation

1. Clone the repository

You need to first clone the [repository](<https://github.com/thatboyreegan/project_dustbin>) repository.

```Bash
git clone https://github.com/thatboyreegan/project_dustbin.git
```

Then move into the `project_dustbin` directory.

```Bash
cd project_dustbin
```

2. Install `pipenv`

```Bash
pip install pipenv
```

The Python version used is vital for the `pipenv` to work as intended and for the `Dockerfile` to build appropriately. This repository used `Python 3.10.12`.

If you'd like to use another Python version, change the `python_version` and `python_full_version` in [Pipfile](Pipfile) to match your Python version.

>Your Python version must be 3.8 or higher

```YAML
# Pipfile

[requires]
python_version = "3.10" # Change here
python_full_version = "3.10.12" # Change here
```

3. Create environment

Create a new project environment using your Python version. If you changed the Python version above, then replace 3.10 with the Python version you are using.

```Bash
pipenv --python 3.10
```

4. Install packages and dependencies.

```Bash
pipenv install --dev
```

## Usage

The web app uses [Auth0](<https://auth0.com/>) for user authentication.
Therefore you need to have an Auth0 account and create a regular web application that can be used by this web app.
The `Client ID`, `Client Secret` and `Domain` of your Auth0 application will be required.

### Set environment variables

The following environment variables need to be set before proceeding to start the web app.

| Variable name | Description|
|---|---|
| `AUTH0_CLIENT_ID` | `Client ID` of the auth0 application |
| `AUTH0_CLIENT_SECRET` | `Client Secret` of the auth0 application |
| `AUTH0_DOMAIN` | `Domain` where the auth0 application is found. It is of the format `<tenant>.<region>auth0.com` eg. `infinity.us.auth0.com` |
| `APP_SECRET_KEY` | String of random bytes used in flask session encryption |

You can include the variables in a file such as `.env` in the root of this repo after cloning.

```Bash
# .env

AUTH0_CLIENT_ID=Client ID
AUTH0_CLIENT_SECRET=Client Secret
AUTH0_DOMAIN=Domain
APP_SECRET_KEY=Secret Key
```

If the file is names `.env`, the flask app will load the environment variables during execution. Otherwise, if you give your file a different name, then you must `source <filename>` in the current shell instance so as to load the variables.

### Starting app locally

After cloning the repo, installing dependencies and setting the environment variables, you can run the app by executing `bootstrap.sh`.

```Bash
chmod +x bootstrap.sh && ./bootstrap.sh
```

This runs the app on [`http://localhost:5000`](<http://localhost:5000>)

### Starting app in container

You need to install docker to use the app in a container. Follow the this [installation guide](<https://docs.docker.com/engine/install/>) to install. Continue with setting up the container after installing docker.

If you changed the Python version in `Pipfile` change the base image tag in `Dockerfile` to match your `python_full_version`.

```Dockerfile
# Dockerfile

FROM python:3.10.12-alpine # Change the 3.10.12 to your python_full_version as in Pipfile
```

The file [`exec.sh`](exec.sh) builds a container called `trashify` as per the [`Dockerfile`](Dockerfile) instructions and runs a new instance of the container mapping port `5000` of the local machine to `5000` of the container.

When running the container instance, the environment file is provided so that the environment variables can be loaded in the container. In this case, the env file is `.env`. If you named yours differently, then change the value for `--env-file` to match your env file.

```Bash
# exec.sh

docker build -t trashify .

docker run --name trashify-1 -p 5000:5000 --env-file ./.env -d trashify
```

The command below executes the same way as the two above.

```Bash
chmod +x exec.sh && ./exec.sh
```

This app instance can be accessed on [`http://localhost:5000`](<http://localhost:5000>)
