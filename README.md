
# Twitter ShadowBan Test (Backend)

Frontend:   
[tsukumijima/shadowban-eu-frontend](https://github.com/tsukumijima/shadowban-eu-frontend)

Backend (this repository):   
[tsukumijima/shadowban-eu-backend](https://github.com/tsukumijima/shadowban-eu-backend)

## About this fork

In this fork, we have made various improvements, including tidying up the code, incorporating other branches, and updating dependencies.

Python has been updated to Python 3.9. Also, the miscellaneous shell scripts have been tidy up and put into docker-entry.sh.  
In addition, the unmerged [dev branch](https://github.com/shadowban-eu/shadowban-eu-backend/tree/dev) and the code from the [testing repository](https://github.com/shadowban-eu/testing/tree/dev), which is being developed as a future version and has been heavily refactored, have been merged and the code has been tidy up.

In addition, the Dockerfile has been improved and Docker Compose is now supported.   
With support for Docker Compose, which is very useful as it allows you to run the server with just `docker-compose up` without having to build an environment.

## Setup

Beforehand, Python 3.9 and MongoDB must be installed.

Run the following commands in order.

```bash
# Clone this repository
$ git@github.com:tsukumijima/shadowban-eu-frontend.git
$ cd shadowban-eu-backend

# Copy .env.example to .env
$ cp .env.example .env

# Dependencies installation
$ pip install --no-cache-dir -r requirements.txt
```

You need to modify `MONGO_DB`, `MONGO_USERNAME`, `MONGO_PASSWORD` in the .env file to suit your environment.  
Please edit the .env file in an editor.

Run the api server with the following command.  
By default, the API server is listening on port 9100.

```bash
# Specify the name of the .env file as an argument
$ ./docker-entry.sh .env
```

## Setup with Docker

Beforehand, Docker and Docker-Compose must be installed.

Run the following commands in order.

```bash
# Clone this repository
$ git@github.com:tsukumijima/shadowban-eu-frontend.git
$ cd shadowban-eu-backend

# Copy .env.example to .env
$ cp .env.example .env
```

If you use Docker, you need to modify `MONGO_HOST` in the .env file from `localhost` to `mongo` .  
Please edit the .env file in an editor.

Run the api server with the following command.  
By default, the API server is listening on port 9100.

```bash
# The first time you run it, the container will be created automatically
$ docker-compose up -d
```

## Notes

The default is to test without login.

You can also test with login. Copy accounts.example.json to accounts.json and set the username (screen name) and password.  
But, doesn't work at this time because the login API for the Twitter Web App has changed.
