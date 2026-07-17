# Ecom

Ecom is a small full-stack ecommerce project with a Django REST API backend and a Vue frontend.

## Project Structure

```text
Ecom/
|-- ecom_django/   # Django backend API
|-- ecom_vue/      # Vue frontend app
|-- docker-compose.yml
`-- README.md
```

## Tech Stack

- Backend: Django, Django REST Framework, Djoser, SQLite
- Frontend: Vue 3, Vue Router, Vuex, Axios, Bulma
- Tooling: Docker Compose

## Run With Docker

Requirements:

- Docker Desktop
- Docker Compose

From the project root:

```bash
docker compose up --build
```

Open the app:

```text
http://127.0.0.1:8080/
```

Backend API:

```text
http://127.0.0.1:8000/
```

The backend container runs migrations, seeds starter `cat1` and `cat2` product categories, and stores its SQLite database in a Docker volume.

## Run Without Docker

Start the backend first:

```bash
cd ecom_django
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

Then start the frontend in a second terminal:

```bash
cd ecom_vue
npm install
npm run serve
```

## Main API Routes

- `GET /api/v1/latest-products/`
- `GET /api/v1/products/<category_slug>/`
- `GET /api/v1/products/<category_slug>/<product_slug>/`
- `POST /api/v1/products/search/`
- `POST /api/v1/users/`
- `POST /api/v1/token/login/`
- `POST /api/v1/token/logout/`

## Environment

Example environment files are included:

- `ecom_django/.env.example`
- `ecom_vue/.env.example`

The Docker setup already provides the needed development values.

## Notes

- The frontend reads the API URL from `VUE_APP_API_URL`.
- The backend reads Django settings from environment variables.
- Local databases, virtual environments, Python cache files, uploaded media, build output, and dependency folders are ignored by Git.
- Checkout and account order pages are present in the frontend, but the current backend only includes product and authentication APIs.
