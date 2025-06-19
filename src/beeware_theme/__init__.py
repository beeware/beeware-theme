from pathlib import Path


def init(project_name, templates, context, static, css):
    context["github_project_name"] = project_name

    templates.append(str(Path(__file__).parent / "_templates"))
    static.append(str(Path(__file__).parent / "_static"))
    css.append("beeware-theme.css")
