import json


def write_json(data, file_path):
    with open(file_path, "w") as fw:
        json.dump(data, fw, indent=4)


def read_json(file_path):
    with open(file_path, "r") as fr:
        return json.load(fr)
