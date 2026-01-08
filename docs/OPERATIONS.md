# Operations

## Local run
- `python -m venv .venv` and activate it
- `pip install -r requirements.txt`
- `cp .env.example .env`
- `python src/manage.py migrate`
- `python src/manage.py runserver`

## Docker run
- `cp .env.example .env`
- `docker compose up --build`

## Audit logs (admin only)
- Endpoint: `GET /api/v1/admin/audit-logs?limit=50`
- Requires JWT access token for an `ADMIN` user

## Request ID usage
- Every response includes `X-Request-ID`.
- Use it to correlate client reports with audit logs and JSON logs.

## Logging
- Logs are emitted as JSON to stdout.
- Ops teams typically ingest stdout via container runtime or platform logs.

## Troubleshooting
- Migrations: run `python src/manage.py migrate`
- Missing env vars: copy `.env.example` to `.env`
- DB connection: confirm Postgres is up when `DB_HOST` is set
