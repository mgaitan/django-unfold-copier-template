# Django Unfold Copier Template

[![Copier](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/copier-org/copier/master/img/badge/badge-grayscale-inverted-border-purple.json)](https://github.com/copier-org/copier)
[![CI](https://github.com/mgaitan/django-unfold-copier-template/actions/workflows/ci.yml/badge.svg)](https://github.com/mgaitan/django-unfold-copier-template/actions/workflows/ci.yml)
[![Docs](https://github.com/mgaitan/django-unfold-copier-template/actions/workflows/pages.yml/badge.svg)](https://mgaitan.github.io/django-unfold-copier-template/)

Copier template for minimalist internal management systems built with Django,
`django-unfold`, `uv`, `pytest`, and Ruff.

This template is inspired by
[`mgaitan/python-package-copier-template`](https://github.com/mgaitan/python-package-copier-template)
and adapts its conventions to Django projects.

Documentation: <https://mgaitan.github.io/django-unfold-copier-template/>

## Generate a project

```bash
uvx copier copy --trust gh:mgaitan/django-unfold-copier-template my-internal-app
cd my-internal-app
make run
```

By default, the generated project includes:

- Django settings split into `base`, `development`, `test`, and `production`.
- `django-unfold` configured with a light theme and green accent `#00a651`.
- `/` redirecting directly to the private Unfold admin.
- Django admin as the application shell and primary CRUD surface.
- A sample `WorkItem` model to demonstrate list, filters, search, and detail/edit views in admin.
- Language selection at copy time, defaulting to English with Spanish available.
- Dependency cooldowns and malware checks through `uv`.
- `pytest-django`, Ruff with a broad rule set including `flake8-django`, and a small Makefile.

## Local template development

```bash
make install
make qa
make smoke
```
