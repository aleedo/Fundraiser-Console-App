import os

BASE_PATH = "app/data"

if not os.path.exists(BASE_PATH):
    os.makedirs(BASE_PATH)

DATA_FILE_PATH = os.path.join(BASE_PATH, "fundraiser.json")
PROJECT_FILE_PATH = os.path.join(BASE_PATH, "projects.json")
