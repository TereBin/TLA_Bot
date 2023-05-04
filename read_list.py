import json

async def read_list(json_path):
    with open(json_path, 'r', encoding='utf-8') as f:
        dictionary = json.load(f)  # make streamer_json to streamer_dict
    return dictionary
