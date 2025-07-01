from pathlib import Path


def init(
    project_name,
    templates=None,
    context=None,
    static=None,
    css=None,
    theme_options=None,
):
    templates = [] if templates is None else templates
    context = {} if context is None else context
    static = [] if static is None else static
    css = [] if css is None else css
    theme_options = {} if theme_options is None else theme_options

    context["github_project_name"] = project_name

    templates.append(str(Path(__file__).parent / "_templates"))
    static.append(str(Path(__file__).parent / "_static"))
    css.append("beeware-theme.css")

    theme_options.setdefault("light_css_variables", {}).update({
        "toc-title-font-size": "var(--font-size--small--3)",  # Increase size
        "toc-font-size": "var(--font-size--small--2)",  # Increase size
        "sidebar-item-font-size": "var(--font-size--normal)",  # Increase size
    })
