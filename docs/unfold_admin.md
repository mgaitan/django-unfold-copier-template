# Unfold Admin

The template configures `django-unfold` as the admin skin and uses `#00a651` as
the default primary accent.

Admin classes should inherit from `unfold.admin.ModelAdmin`:

```python
from unfold.admin import ModelAdmin


class MyModelAdmin(ModelAdmin):
    list_display = (...)
    search_fields = (...)
    list_filter = (...)
```

The generated starter disables global command and modal overlays via template
overrides:

- `templates/unfold/helpers/command.html`
- `templates/unfold/helpers/modal.html`

This keeps the admin direct and predictable for internal systems.

Keep custom screens inside the admin/Unfold experience. The generated project
does not include a separate public app shell: `/` redirects to `/admin/`, and
the admin login is the only public page by default.
