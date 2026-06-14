# Generated Project

The generated project is intentionally small:

- `manage.py`
- `config/settings/` split into base, development, test, and production
- `apps/core/` with a demo `WorkItem` model
- `templates/` for Unfold overrides
- `tests/` with pytest-django coverage

`/` redirects to `/admin/`. The Unfold admin is the private application shell
and primary CRUD interface; only the admin login is public by default.

Language is chosen by the `language_code` Copier prompt and can later be
overridden with `DJANGO_LANGUAGE_CODE`.
