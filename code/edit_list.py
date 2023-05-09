import json


async def edit_list(streamer_json_path, i, is_live):
    streamer_json = json.load(open(streamer_json_path, 'r', encoding='utf-8'))

    if is_live:
        streamer_json[str(i)]["4_signal"] = "True"
        with open(streamer_json_path, 'w', encoding='utf-8') as file:
            json.dump(streamer_json, file, indent="\t")
        return True

    elif not is_live:
        streamer_json[str(i)]["4_signal"] = "False"
        with open(streamer_json_path, 'w', encoding='utf-8') as file:
            json.dump(streamer_json, file, indent="\t")
        return False

    else:
        return False
