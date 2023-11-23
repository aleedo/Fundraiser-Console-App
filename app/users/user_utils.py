import os
import hashlib
from ..utils import write_json, read_json
from ..const import DATA_FILE_PATH


def decrypt_password(password):
    pwd_hash = hashlib.sha224(str.encode(password)).hexdigest()
    return pwd_hash


def get_registered_users():
    if not os.path.exists(DATA_FILE_PATH):
        write_json({}, DATA_FILE_PATH)
    return read_json(DATA_FILE_PATH)
