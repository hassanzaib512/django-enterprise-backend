# Decisions

## 01. Django + DRF
We use Django for mature auth, ORM, admin, and migrations.
DRF adds standardized API patterns without extra glue code.
This keeps the starter aligned with common enterprise stacks.

## 02. SimpleJWT for tokens
SimpleJWT provides stateless JWT access/refresh tokens.
It integrates cleanly with DRF authentication settings.
We avoid custom token logic until real requirements emerge.

## 03. Role stored in profile model
Roles live in `UserProfile` to keep the core User model intact.
This avoids a custom user model for a small RBAC surface.
The profile is extensible for future attributes.

## 04. Audit log middleware
Middleware captures method, path, status, duration, and user.
It does not capture request bodies or query params to avoid sensitive data.
Request ID correlation enables traceability without deep logging.

## 05. JSON logging with request_id
Structured JSON logs are easy to ingest by log pipelines.
Request IDs tie application logs to audit entries.
The formatter uses stdlib logging to keep dependencies minimal.

## 06. Docker + Postgres with sqlite fallback
Compose provides a realistic Postgres dev environment.
SQLite remains the default for tests and simple local runs.
This balances accuracy with low friction.

## 07. Security settings gated by DJANGO_DEBUG
Production defaults (HSTS, secure cookies, SSL redirect) enable when debug is off.
Local dev stays simple with debug on and no forced HTTPS.
CI tests explicitly disable SSL redirect.
