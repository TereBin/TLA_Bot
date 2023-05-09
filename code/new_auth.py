import tweepy
import json

twitter_api_path = "../data/twitter_api_data.txt"
streamer_json_path = "../data/streamer_list.json"

with open(twitter_api_path, 'r') as f:
    twitter_api_data = f.read().splitlines()
    api_key = twitter_api_data[0]
    api_secret = twitter_api_data[1]

streamer_dict = json.load(
        open(streamer_json_path, 'r', encoding='utf-8'))  # readable dict

oauth1_user_handler = tweepy.OAuth1UserHandler(api_key, api_secret, callback='oob')
print(oauth1_user_handler.get_authorization_url(signin_with_twitter=True))

PIN = input("Input PIN: ")
access_token, access_secret = oauth1_user_handler.get_access_token(PIN)

twitch_id = input("트위치 아이디 : ")
twitter_id = input("트위터 아이디 : ")
tweet = input("문장 : ")
input_category = input("카테고리를 넣으려면 Y : ")
input_name = input("방제를 넣으려면 Y : ")
input_link = input("링크를 넣으려면 Y : ")
input_image = input("이미지를 넣으려면 Y : ")

if input_category == "Y":
    req_data = "True"
else:
    req_data = "False"
if input_name == "Y":
    req_data += ", True"
else:
    req_data += ", False"
if input_link == "Y":
    req_data += ", True"
else:
    req_data += ", False"

num = str(len(streamer_dict))
streamer_dict[num] = {}
streamer_dict[num]["1_twitch_id"] = twitch_id
streamer_dict[num]["2_twitter_id"] = twitter_id
streamer_dict[num]["3_tweet"] = tweet
streamer_dict[num]["4_signal"] = "False"
streamer_dict[num]["5_access_token"] = access_token
streamer_dict[num]["6_access_secret"] = access_secret
streamer_dict[num]["7_req_data"] = req_data
if input_image == "Y":
    streamer_dict[num]["8_img"] = "data/img/" + twitch_id + ".png"
else:
    streamer_dict[num]["8_img"] = ""

with open(streamer_json_path, 'w', encoding='utf-8') as file:
    json.dump(streamer_dict, file, indent='\t')
