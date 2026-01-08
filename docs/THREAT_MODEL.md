# Threat Model

## Assets
- Credentials (passwords during registration)
- JWT access and refresh tokens
- Audit logs (user actions and request metadata)
- PII (email, names)

## Threats
- Token theft from clients or logs
- Authentication bypass or token forgery
- Privilege escalation via role manipulation
- Log leakage or over-collection of sensitive data
- Injection attacks against API inputs

## Mitigations in this repo
- JWT auth with DRF permissions and RBAC checks
- Secure defaults when `DJANGO_DEBUG=0` (HSTS, secure cookies, SSL redirect)
- No request body logging; audit logs capture only metadata
- Request ID correlation for traceability without exposing payloads

## TODOs (future)
- Rate limiting and brute-force protection
- Refresh token rotation and revocation
- CSP and additional security headers
- Secrets management (vault or cloud KMS)
- SSO integration and 2FA
