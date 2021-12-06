
# Twitter ShadowBan Test (Backend)

Frontend:   
[tsukumijima/shadowban-eu-frontend](https://github.com/tsukumijima/shadowban-eu-frontend)

Backend (this repository):   
[tsukumijima/shadowban-eu-backend](https://github.com/tsukumijima/shadowban-eu-backend)

## Setup

Run the following commands in order.

```bash
# Clone this repository
$ git@github.com:tsukumijima/shadowban-eu-frontend.git
$ cd shadowban-eu-backend
# Dependencies installation
$ pip install --no-cache-dir -r requirements.txt
# Copy .env.example to .env
$ cp .env.example .env
```

Run the api server with the following command.  
By default, the API server is listening on port 9001.

```bash
# Specify the name of the .env file as an argument
$ ./docker-entry.sh .env
```

## Setup with Docker

Run the following commands in order.

```bash
# Clone this repository
$ git@github.com:tsukumijima/shadowban-eu-frontend.git
$ cd shadowban-eu-backend
# Copy .env.example to .env
$ cp .env.example .env
```

If you use Docker, you need to change `MONGO_HOST` in .env from `localhost` to `mongo` .  
Please edit the .env file in an editor.

Run the api server with the following command.  
By default, the API server is listening on port 9001.

```bash
# The first time you run it, the container will be created automatically
$ docker-compose up -d
```
