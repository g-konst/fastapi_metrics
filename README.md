[![python_version](https://img.shields.io/badge/python-3.8-brightgreen.svg?logo=Python&logoColor=white)](https://www.python.org/)


## fastAPI metrics service

Simple fastAPI service to store metrics from other services to database

### Gettings Started

This project uses some of the new features of the python language introduced in `python3.8`, so first of all make sure that your version is at least.

### Prepare environment

First of all you need to create a virtual environment and activate it:

```bash
$ python3 -m venv .venv
$ source .venv/bin/activate
```

And then install all of the dependencies:

```bash
$ pip install -r requirements.txt
```

### Configure the app

The app uses environment variables to configure itself, so you need to create `.env` file in the root of the project and fill it with the following variables (you can change the values if you want):

```bash
DB_HOST=localhost
DB_PORT=5432
DB_USER=postgres
DB_PASS=postgres
DB_NAME=postgres
```

### Run the app

Now you can start the app (you can add `--reload` flag to enable hot-reload, but it's not recommended for production, see [docs](https://www.uvicorn.org/deployment/#running-with-gunicorn) for more info):

```bash
$ uvicorn app.main:app --reload
```

### Testing

First of all you need to create a test database called `test`

```bash
$ sudo -u postgres psql -c 'create database test;'
```

To run the tests run the following command:

```bash
$ pytest -v
```
