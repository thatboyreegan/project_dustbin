#!/bin/sh

docker build -t trashify .

docker run --name trashify-1 -p 5000:5000 -d trashify
