# BeeWare Theme Templates

A collection of template files to override the Furo Sphinx theme with a BeeWare theme.

## Usage
These template files are designed to override the Furo Sphinx theme, and will therefore only work if the Furo theme is enabled. The following is required to enable these theme elements on a BeeWare repository's Read the Docs documentation. 

1. Update the `core/pyproject.toml` `[docs]` list to include the following:

```toml
"beeware_theme @ git+https://github.com/beeware/beeware-theme",
```

2. Add the following to `docs/conf.py`:

```python
import beeware_theme


templates_path = []
html_static_path = []

beeware_theme.init_templates(templates_path)
beeware_theme.init_static(html_static_path)
```