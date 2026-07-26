# Template Maintenance

Run local checks:

```bash
make qa
```

Run a generated-project smoke test:

```bash
make smoke
```

This repository is inspired by `mgaitan/python-package-copier-template`. Keep
tooling and documentation conventions aligned where they make sense, but prefer
Django and Unfold defaults for generated application code.

The Ruff configuration follows that template's broad selector baseline and adds
the `DJ` family from `flake8-django`. Both the template repository and generated
projects must keep that baseline covered by tests.
