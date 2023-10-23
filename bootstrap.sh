#!/bin/sh

export FLASK_APP=trashify

pipenv run flask --debug run -h 0.0.0.0 --port 5000
