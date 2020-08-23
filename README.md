# Flask-base

[![Test Status](https://github.com/bgildson/flask-base/workflows/Test%20and%20Report%20Coverage/badge.svg)](https://github.com/bgildson/flask-base/actions?workflow=test)
[![Coverage Status](https://coveralls.io/repos/github/bgildson/flask-base/badge.svg?branch=master)](https://coveralls.io/github/bgildson/flask-base?branch=master)

This project contains a boilerplate for a basic Flask application.

## Running the app

**To follow the steps bellow, you should have installed [Docker](https://docs.docker.com/get-docker/) and [docker-compose](https://docs.docker.com/compose/install/).**

Build and run the necessary services
```sh
docker-compose up --build
```

In another terminal, apply the app migrations
```sh
docker-compose exec app flask db upgrade
```

**The application will be running on [http://localhost:5000](http://localhost:5000/hello/) with [hello](http://localhost:5000/hello/) and [todos](http://localhost:5000/todos/) available.**
