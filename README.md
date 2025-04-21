# SWAPI Planets API

This is a simple Django-based API to manage planets, available at:

**`/swapi/planets`**

## Features

- Full CRUD operations on planets
- Add a single planet or multiple planets as an array

---

## Getting Started

Follow these steps to set up and run the project locally:

### 1. Clone the repository

```bash
git clone <your-repo-url>
cd <your-project-folder>
```

### 2. Create a virtual environment

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Run migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### 5. Start the server

```bash
python manage.py runserver
```

---

## Populating Data from SWAPI GraphQL

You can use the `populate_swapi_planets.py` script to fetch planets from the SWAPI GraphQL endpoint and insert them into your local Django REST API.

**GraphQL Endpoint:**

`https://swapi-graphql.netlify.app/graphql`

**GraphQL Query Used:**

```graphql
query {
  allPlanets {
    planets {
      name
      population
      terrains
      climates
    }
  }
}
```

---

### Running the script

Make sure your local server is running at `http://localhost:8000` and then execute:

```bash
python populate_swapi_planets.py
```
