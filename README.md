# SWAPI Planets CRUD API

This Django project provides a RESTful API to interact with planet data from the Star Wars API (SWAPI).

## Setup

1. Clone this repository.
2. Install dependencies: `pip install -r requirements.txt`
3. Run migrations: `python manage.py migrate`
4. Populate the database: `python manage.py populate_planets`
5. Start the development server: `python manage.py runserver`

## API Endpoints

* **GET /planets/**: List all planets
* **GET /planets/<id>/**: Retrieve a specific planet
* **POST /planets/**: Create a new planet
* **PUT /planets/<id>/**: Update a planet
* **DELETE /planets/<id>/**: Delete a planet
