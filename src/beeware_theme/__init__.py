from pathlib import Path


def init(project_name, templates, context, static, css, theme_options):
    context["github_project_name"] = project_name

    templates.append(str(Path(__file__).parent / "_templates"))
    static.append(str(Path(__file__).parent / "_static"))
    css.append("beeware-theme.css")

    theme_options.setdefault("light_css_variables", {}).update({
        "toc-title-font-size": "var(--font-size--small--3)",  # Increase size
        "toc-font-size": "var(--font-size--small--2)",  # Increase size
        "sidebar-item-font-size": "var(--font-size--normal)",  # Increase size
    })
