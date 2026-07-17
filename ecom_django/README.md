# Ecom Backend

This is the Django backend API for the Ecom project. It provides product, category, search, media, and authentication endpoints for the Vue frontend.

## Tech Stack

- Django
- Django REST Framework
- Djoser
- django-cors-headers
- Pillow
- SQLite

## Requirements

- Python 3.9+
- pip

## Setup

### With Docker

From the project root:

```bash
docker compose up --build backend
```

The backend runs at:

```text
http://127.0.0.1:8000/
```

### Without Docker

Create and activate a virtual environment:

```bash
python -m venv .venv
.venv\Scripts\activate
```

Install dependencies:

```bash
pip install django djangorestframework django-cors-headers djoser pillow
```

Or use the included requirements file:

```bash
pip install -r requirements.txt
```

Run migrations:

```bash
python manage.py migrate
```

Seed starter categories and products:

```bash
python manage.py seed_demo_data
```

Start the development server:

```bash
python manage.py runserver
```

The backend runs at:

```text
http://127.0.0.1:8000/
```

## Admin

Create a Django admin user:

```bash
python manage.py createsuperuser
```

Then open:

```text
http://127.0.0.1:8000/admin/
```

## API Routes

Product routes:

- `GET /api/v1/latest-products/`
- `GET /api/v1/products/<category_slug>/`
- `GET /api/v1/products/<category_slug>/<product_slug>/`
- `POST /api/v1/products/search/`

Authentication routes from Djoser:

- `POST /api/v1/users/`
- `POST /api/v1/token/login/`
- `POST /api/v1/token/logout/`

## Media

Product images are stored in:

```text
media/uploads/
```

During development, Django serves media files from:

```text
/media/
```

## Notes

- The project uses SQLite.
- Docker stores SQLite data in a named volume.
- Local `db.sqlite3` files are ignored by Git.
- CORS is currently open for development through `CORS_ALLOW_ALL=1`.
- `DEBUG` is enabled by default for development, so update settings before deploying this backend publicly.
- Checkout and order endpoints are not currently implemented in the backend.
