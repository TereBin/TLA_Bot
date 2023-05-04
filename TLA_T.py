import asyncio
import requests
import time

from read_list import read_list
from err_logging import err_logging
from check_twitch import check_twitch
from edit_list import edit_list
from send_tweet import send_tweet
from send_chat import send_chat

streamer_json_path = "../data/streamer_list.json"
twitch_api_path = "../data/twitch_api_data.txt"
discord_bot_path = "../data/discord_bot_data.txt"


async def main(_twitch_key, _auth_token):
    try:
        streamer_data = await read_list(streamer_json_path)

        i = 1
        while i < len(streamer_data):
            try:
                ind_streamer_data = streamer_data[str(i)]
                is_live, category, title = await check_twitch(ind_streamer_data["1_twitch_id"], _twitch_key, _auth_token)
                signal_sent = ind_streamer_data["4_signal"]

                if signal_sent == "True":
                    signal_sent = True
                elif signal_sent == "False":
                    signal_sent = False

                if is_live is None:
                    print()
                elif is_live != signal_sent:  # stream status changed
                    if is_live:  # changed to online
                        print("방송 시작")
                        await send_tweet(ind_streamer_data, category, title)
                        await send_chat(ind_streamer_data["1_twitch_id"])
                    else:  # changed to offline
                        print("방송 종료")

                    await edit_list(streamer_json_path, i, is_live)
                else:
                    print("상태 유지")
                i += 1

            except Exception as err_data:
                print("error under main.")
                await err_logging(err_data)

    except Exception as err_data:
        print("error under main.")
        await err_logging(err_data)


while True:  # biggest loop in case of error
    try:
        print("initializing")
        print("="*50)

        with open(twitch_api_path, 'r') as f:
            twitch_api_data = f.read().splitlines()
            twitch_key = twitch_api_data[0]
            twitch_secret = twitch_api_data[1]

        auth_req = requests.post('https://id.twitch.tv/oauth2/token?client_id=' + twitch_key + '&client_secret=' + twitch_secret + '&grant_type=client_credentials')
        auth_req_json = auth_req.json()
        access_token = auth_req_json["access_token"]
        token_type = auth_req_json["token_type"]
        token_type = token_type[0].upper() + token_type[1:]
        auth_token = token_type + " " + access_token

        print("initializing complete")
        print("="*50)

        while True:  # every minute loop
            print(time.strftime('%y/%m/%d %H:%M', time.localtime(time.time())))
            start_time = time.time()
            asyncio.run(main(twitch_key, auth_token))
            print("-" * 50)
            end_time = time.time()
            time.sleep(60 - (end_time - start_time) % 60)

    except Exception as err_data:
        asyncio.run(err_logging(err_data))
