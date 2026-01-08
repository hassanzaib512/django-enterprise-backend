# django-enterprise-backend

## Project Overview

This is a Django enterprise backend starter with JWT auth, RBAC, audit logging, and health/readiness endpoints.
It includes OpenAPI docs, Docker Compose for Django + Postgres, GitHub Actions CI, structured JSON logs,
and production security defaults that activate when debug is off.

## Features

- Health: `/health`
- Readiness: `/ready` (DB probe)
- API: `/api/v1/ping`
- OpenAPI: `/api/schema`, `/api/docs`, `/api/redoc`
- Auth: `/api/v1/auth/register`, `/api/v1/auth/login`, `/api/v1/auth/refresh`, `/api/v1/auth/me`
- RBAC roles: `ADMIN`, `MANAGER`, `USER`
- Admin endpoints: `/api/v1/admin/ping`, `/api/v1/admin/audit-logs`
- Audit logging middleware + `X-Request-ID`
- JSON structured logging
- Docker Compose (Django + Postgres)
- GitHub Actions CI (ruff + pytest)
- Security baseline when `DJANGO_DEBUG=0`

## Architecture

- Src layout with apps under `src/apps`: `accounts`, `api`, `audit`, `core`
- Audit logging implemented as middleware that records each request/response

## Quick Start (Local)

1. Create and activate a virtual environment.
2. Install dependencies:
   `pip install -r requirements.txt`
3. Configure environment:
   `cp .env.example .env`
4. Run migrations:
   `python src/manage.py migrate`
5. Start the server:
   `python src/manage.py runserver`

Endpoints:
- http://localhost:8000/health
- http://localhost:8000/ready
- http://localhost:8000/api/v1/ping
- http://localhost:8000/api/docs

## Quick Start (Docker)

1. `cp .env.example .env`
2. `docker compose up --build`

Endpoints:
- http://localhost:8000/health
- http://localhost:8000/ready
- http://localhost:8000/api/v1/ping
- http://localhost:8000/api/docs

## Testing & Linting

- `ruff check .`
- `pytest -q`

## Docs

- `docs/DECISIONS.md`
- `docs/THREAT_MODEL.md`
- `docs/OPERATIONS.md`

## Roles & Access

- Registering a user assigns the `USER` role by default.
- To set an admin role for now, use Django shell:
  `python src/manage.py shell` and update `user.profile.role = "ADMIN"`.

## Production Security Notes

- Setting `DJANGO_DEBUG=0` enables secure cookies, HSTS, and SSL redirect.
- In real deployments, terminate TLS at a reverse proxy and forward HTTPS to the app.
