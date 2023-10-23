FROM python:3.10.12-alpine

RUN apk update
RUN pip install --no-cache-dir pipenv

WORKDIR /home/app
COPY bootstrap.sh Pipfile Pipfile.lock setup.py ./
COPY trashify ./trashify

RUN pipenv install --system --deploy

EXPOSE 5000
ENTRYPOINT [ "/home/app/bootstrap.sh" ]
