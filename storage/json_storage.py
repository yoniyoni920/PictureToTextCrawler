import json

class JSONStorage:
    def save(self, data: dict, filename: str):
        with open(filename, "w") as f:
            json.dump(data, f, indent=4)
