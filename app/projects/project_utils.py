import os
from ..utils import write_json, read_json
from ..const import PROJECT_FILE_PATH


def get_all_projects():
    if not os.path.exists(PROJECT_FILE_PATH):
        write_json({}, PROJECT_FILE_PATH)
    return read_json(PROJECT_FILE_PATH)
