import pathlib
import os.path as path
from datetime import date

def get_design_path(design_name):
    return pathlib.Path(__file__).parent.absolute().joinpath("design").joinpath(design_name)

def get_cache_path():

    if not pathlib.Path(__file__).parent.absolute().joinpath("cache").exists():
        pathlib.Path(__file__).parent.absolute().joinpath("cache").mkdir()

    return pathlib.Path(__file__).parent.absolute().joinpath("cache")

def get_json_layout_path():

    if not pathlib.Path(__file__).parent.absolute().joinpath("graph_layout.json").is_file():
        pathlib.Path(__file__).parent.absolute().joinpath("graph_layout.json").touch()

    return path.join(pathlib.Path(__file__).parent.absolute(),("graph_layout.json"))

def get_current_season():
    return date.today().year