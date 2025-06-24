import json, os

def write(file_name: str, data: dict):
    path = os.path.abspath(__file__ + f"/../../static/{file_name}")
    with open(path, "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4, ensure_ascii=False)