from pathlib import Path


def init_templates(templates_path_list):
    templates_path_list.append(str(Path(__file__).parent / "_templates"))


def init_static(static_path_list):
    static_path_list.append(str(Path(__file__).parent / "_static"))
