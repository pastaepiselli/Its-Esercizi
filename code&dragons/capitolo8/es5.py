import json

def to_json_lines(records: list[dict]) -> list[str]:
    new_list = []
    for d in records:
        new_list.append(json.dumps(d))
    return new_list