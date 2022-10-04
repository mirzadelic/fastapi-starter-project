# FastAPI Starter Project

Project includes:

-   `fastapi`
-   `sqlmodel`
-   `alembic`

##

## Models

Check db/models and migrations, there is one example.

## Using docker

Setup env variables in `app/core/.env` using `app/core/.env-example`

#### Install and run

```bash
docker-compose up -d web

# you can track logs with:
docker-compose logs -f --tail=100 web
```

Go to: http://localhost:8000/api/docs/

#### Migrations

Create migrations

```bash
docker-compose exec web alembic revision --autogenerate -m "Example model"
```

Apply migrations

```bash
docker-compose exec web alembic upgrade head
```

#### Tests

Run tests

```bash
docker-compose exec web pytest .
```

## Without docker

#### Install

```bash
cd app/
pip install -r requirements/development.txt
```

Setup env variables in `app/core/.env`.

#### Run

```bash
cd app/
python app/server.py
```

Go to: http://localhost:8000/api/docs/

#### Migrations

Create migrations

```bash
alembic revision --autogenerate -m "Example model"
```

Apply migrations

```bash
alembic upgrade head
```

#### Tests

Run tests

```bash
pytest .
```

## Environment Variables

To run this project, you will need to add the following environment variables to your app/core/.env file

`BASE_URL` - default: http://localhost:8000

`RELOAD` - default: false

`DB_HOST` - default: localhost

`DB_PORT` - default: 5432

`DB_USER` - default: postgres

`DB_PASS` - default: postgres

`DB_BASE` - default: db

`DB_ECHO` - default: false
