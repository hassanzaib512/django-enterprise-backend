# django-enterprise-backend

## Local Run (Docker)

1. `cp .env.example .env`
2. `docker compose up --build`
3. Open http://localhost:8000

## Production Security Notes

- Security settings activate when `DJANGO_DEBUG=0`.
- For local dev, keep debug on or override `SECURE_SSL_REDIRECT` if needed.
