# BeeWare Theme Templates

A collection of template files to override the [Furo Sphinx theme](https://github.com/pradyunsg/furo) with BeeWare header and sidebar branding.

## Usage

These template files are designed to override the Furo Sphinx theme, and will therefore only work if the Furo theme is enabled. The following is required to enable these theme elements on a BeeWare repository's Read the Docs documentation.

1. Update the `pyproject.toml` `[docs]` extra list to include the following:

```toml
"beeware_theme @ git+https://github.com/beeware/beeware-theme",
```

2. Add the following to `docs/conf.py`:

```python
import beeware_theme


templates_path = []
html_static_path = []
html_css_files = []
html_context = {}

beeware_theme.init(
    project_name="my_project",
    templates=templates_path,
    context=html_context,
    static=html_static_path,
    css=html_css_files,
)
```
In this configuration, ``my_project`` is the GitHub project name. You can put
any other content in ``template_paths``, ``html_static_path``,
``html_css_files`` or ``html_context`` as is required by the local project.

## Testing

To test this theme, create a virtual environment, and run:
```
(venv) $ pip install -e ".[dev]"
(venv) $ tox -e docs-live
```

This will serve a test project with the theme applied.
