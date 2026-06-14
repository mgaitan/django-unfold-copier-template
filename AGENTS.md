# Working with This Template

You are assisting on `mgaitan/django-unfold-copier-template`, a Copier template
for internal Django applications powered by `django-unfold`.

## Purpose

- Generate small, modern Django projects for internal business systems.
- Use Django admin plus Unfold as the primary CRUD and model-management surface.
- Keep the generated app server-rendered, light, and operationally boring.
- Use `uv`, `pytest`, Ruff, and a Makefile by default.

## Relationship to the Python Package Template

This project is a sibling template inspired by
`mgaitan/python-package-copier-template`, not a branch of it. When changing
Copier mechanics, QA conventions, documentation shape, or Makefile ergonomics,
compare against that template and preserve the same spirit where it fits.

## Key Files

- `copier.yml`: prompts, defaults, and post-copy tasks.
- `project/`: generated project skeleton.
- `project/AGENTS.md.jinja`: instructions emitted into generated projects.
- `project/{{project_slug}}/config/settings/`: Django settings split by environment.
- `project/{{project_slug}}/apps/core/`: sample internal app and demo model.
- `docs/`: template documentation.
- `tests/`: template smoke tests.

## Editing Rules

- Prefer minimal, Copier-friendly changes.
- Preserve Jinja syntax in generated files.
- Run `make qa` after template changes.
- Run `make smoke` after changes to `copier.yml` or `project/`.
- Do not add frontend complexity unless it directly supports Unfold/admin usage.
- Avoid hand-built CRUD surfaces when Django admin and Unfold already provide them.

## Django/Unfold Preferences

- Admin is the source of truth for list, create, update, delete, detail, search, filters, permissions, and history.
- `/` should redirect to `/admin/`; do not introduce a parallel public app shell.
- Custom views should be private admin-integrated dashboards, summaries, or workflows that are awkward in standard model admin.
- Keep Unfold configuration explicit in settings.
- Use the default green accent `#00a651` unless the user changes `brand_color`.
- Avoid global command palettes or overlays in the generated starter unless requested.
- Keep `skills/django-unfold-admin/SKILL.md` aligned with generated-project guidance.

## Generated Project QA

Generated projects should pass:

```bash
make lint
make test
make check
```
