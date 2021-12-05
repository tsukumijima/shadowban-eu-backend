
# Use Python 3.9 as a base image
FROM python:3.9-slim-buster

# Package installation
RUN apt-get update -y && apt-get upgrade -y
RUN apt install gcc python3-dev -y

# Dependencies installation
COPY requirements.txt /tmp/
RUN pip install --no-cache-dir -r /tmp/requirements.txt && rm /tmp/requirements.txt

# Working directory
WORKDIR /app/

# entry point
ENTRYPOINT /bin/bash docker-entry.sh .env
