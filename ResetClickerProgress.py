import json

with open("score.json", "w", encoding="utf-8") as file:
    data = {
        "score": 0,
        "power_click": 1
    }
    json.dump(data, file, indent=4)