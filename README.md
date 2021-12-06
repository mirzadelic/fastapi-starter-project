
# FastAPI Starter Project

Project includes:
- fastapi - 0.70.0
- sqlmodel - 0.0.4
- alembic - 1.7.5


##


## Installation

Install my-project with npm

```bash
  pip install -r requirements/development.txt
```

Setup env variables in `app/core/.env`.

Check db/models and migrations, there is one example.
## Run


```bash
cd app/
python server.app
```

Go to: http://localhost:8000/api/docs/

### Migrations

Create migrations
```bash
alembic revision --autogenerate -m "Example model"
```

Apply migrations
```bash
alembic upgrade head
```
## Environment Variables

To run this project, you will need to add the following environment variables to your app/core/.env file

`BASE_URL` - default: http://localhost:8000

`RELOAD` -  default: false

`DB_HOST` - default: localhost

`DB_PORT` - default: 5432

`DB_USER`

`DB_PASS`

`DB_BASE`

`DB_ECHO` - default: false
