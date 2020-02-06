FROM python:3.6-alpine

RUN mkdir -p /flask_docker

COPY /flask_docker /flask_docker

RUN apk add --no-cache git gcc python3-dev gpgme-dev libc-dev

RUN pip install -r flask_docker/requirements.txt

EXPOSE 5011

# CMD ["python", "flask_docker/flask_docker.py"]
