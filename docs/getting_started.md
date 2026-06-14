# Getting Started

Generate a project:

```bash
uvx copier copy --trust gh:mgaitan/django-unfold-copier-template my-internal-app
cd my-internal-app
make install
make migrate
make seed
make run
```

Open <http://127.0.0.1:8000/>. It redirects to the private Unfold admin.

The `language_code` prompt defaults to `en-us` and can be set to `es-ar` for
Spanish projects. The generated `.env.example` keeps the value configurable via
`DJANGO_LANGUAGE_CODE`.

The default demo user is:

```text
admin / admin123
```
