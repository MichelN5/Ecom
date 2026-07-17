# Ecom Frontend

This is the Vue frontend for the Ecom project. It connects to the Django backend API at `http://127.0.0.1:8000/`.

## Tech Stack

- Vue 3
- Vue Router
- Vuex
- Axios
- Bulma
- Bulma Toast

## Requirements

- Node.js
- npm
- Backend running at `http://127.0.0.1:8000/`

## Setup

### With Docker

From the project root:

```bash
docker compose up --build frontend
```

Open the frontend in your browser:

```text
http://127.0.0.1:8080/
```

### Without Docker

Install dependencies:

```bash
npm install
```

Start the development server:

```bash
npm run serve
```

Open the frontend in your browser:

```text
http://localhost:8080/
```

Build for production:

```bash
npm run build
```

## Important Files

- `src/main.js` configures Axios and mounts the Vue app.
- `src/router/index.js` defines frontend routes.
- `src/store/index.js` stores cart and authentication state.
- `src/views/` contains the main pages.
- `src/components/` contains reusable UI components.

## Available Pages

- Home
- Product category
- Product details
- Search
- Cart
- Checkout
- Login
- Sign up
- My account

## API Connection

Axios is configured in `src/main.js`:

```js
axios.defaults.baseURL = process.env.VUE_APP_API_URL || 'http://127.0.0.1:8000/'
```

If you run the backend on another port or host, set `VUE_APP_API_URL`.

## Notes

- Product browsing and authentication use the current Django backend APIs.
- Checkout and order history views are in the frontend, but their matching backend endpoints are not included yet.
