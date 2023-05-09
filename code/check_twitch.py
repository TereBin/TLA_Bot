import requests
from err_logging import err_logging

async def check_twitch(streamer_id, app_key, auth_token):
    try:
        headers = {'client-id': app_key, 'Authorization': auth_token}
        stream_req = requests.get(f'https://api.twitch.tv/helix/search/channels?query={streamer_id}', headers=headers)
        stream_data_json = stream_req.json()["data"]

        i = 0
        is_live = None
        category = None
        title = None

        for stream_data in stream_data_json:
            if stream_data["broadcaster_login"] == streamer_id:
                is_live = stream_data["is_live"]
                category = stream_data["game_name"]
                title = stream_data["title"]
                print("\n" + stream_data["display_name"], "(" + streamer_id + ")")
                break
            else:
                pass

        if i == len(stream_data_json):
            print("error : 트위치 채널 정보 없음")
            return None, None, None

        elif is_live:
            print("online")
            return is_live, category, title

        else:
            print("offline")
            return is_live, category, title

    except Exception as err_data:
        await err_logging(err_data)
        print("req error! twitch 연결 불가")
        pass
