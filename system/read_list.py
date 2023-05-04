import json

async def read_list(streamer_json_path):
    with open(streamer_json_path, 'r', encoding='utf-8') as f:
        streamer_dict = json.load(f)  # make streamer_json to streamer_dict
    return streamer_dict
