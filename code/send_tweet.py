import tweepy

twitter_api_path = "../data/twitter_api_data.txt"


async def send_tweet(streamer_data, category, title):
    with open(twitter_api_path, 'r') as f:
        twitter_data = f.read().splitlines()
        api_key = twitter_data[0]
        api_secret = twitter_data[1]

    tweet = streamer_data["3_tweet"]
    access_token = streamer_data["5_access_token"]
    access_secret = streamer_data["6_access_secret"]
    img_file = streamer_data["8_img"]
    streamer_req_data = list(map(str, streamer_data["7_req_data"].split(", ")))
    i = 0

    while i < len(streamer_req_data):
        if streamer_req_data[i] == "True":
            streamer_req_data[i] = True
        else:
            streamer_req_data[i] = False
        i = i+1
        
    if streamer_req_data[0]:  # category
        tweet = tweet + "\n카테고리 : [ " + category + " ]"
    if streamer_req_data[1]:  # title
        tweet = tweet + "\n방제 : [ " + title + " ]"
    if streamer_req_data[2]:  # link
        tweet = tweet + "\ntwitch.tv/" + streamer_data["1_twitch_id"]

    bot = tweepy.Client(consumer_key=api_key, consumer_secret=api_secret, access_token = access_token, access_token_secret=access_secret)
    if img_file != "":
        img = bot.upload_media(img_file)
        bot.create_tweet(status=tweet, media_ids=[media.media_key])
    else:
        bot.create_tweet(text=tweet)

    print(tweet)

