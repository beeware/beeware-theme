from pathlib import Path


def init(templates, static, css):
    templates.append(str(Path(__file__).parent / "_templates"))
    static.append(str(Path(__file__).parent / "_static"))
    css.append("beeware-theme.css")
