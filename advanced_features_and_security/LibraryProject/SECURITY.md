Security measures:
- DEBUG=False in production; set ALLOWED_HOSTS appropriately.
- SESSION_COOKIE_SECURE / CSRF_COOKIE_SECURE set to True (requires HTTPS).
- SECURE_BROWSER_XSS_FILTER, SECURE_CONTENT_TYPE_NOSNIFF, X_FRAME_OPTIONS set.
- Use django-csp to set CSP headers.
- All templates using forms include {% csrf_token %}.
- Use ModelForms and ORM; raw SQL uses parameterized queries.
