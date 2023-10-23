# project_dustbin / trashify

A user friendly app for both normal users and organizations that bridges the gap between them and waste
collectors to provide easy and organized waste collection.

## Installation

```
### Prerequisites

- Python 3.8 or higher
```

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

### Starting app locally

After cloning the repo and installing dependencies, you can run the app by executing `bootstrap.sh`.

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

```Bash
# exec.sh

docker build -t trashify .

docker run --name trashify-1 -p 5000:5000 -d trashify
```

You can execute the above commands individually just execute `exec.sh` to build and run an instance.

```Bash
chmod +x exec.sh && ./exec.sh
```

This app instance can be accessed on [`http://localhost:5000`](<http://localhost:5000>)
