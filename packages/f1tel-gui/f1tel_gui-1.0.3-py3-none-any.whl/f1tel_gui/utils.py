from email.policy import default
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

    dir_path = path.dirname(path.realpath(__file__))
    default_file_name = "graph_layout.json"
    default_path = path.join(dir_path, default_file_name)

    if not pathlib.Path(default_path).is_file():
        pathlib.Path(default_path).touch()

    return default_path

def get_img_path(img_name):
    return pathlib.Path(__file__).parent.absolute().joinpath("img").joinpath(img_name).as_posix()

def get_current_season():
    return date.today().year