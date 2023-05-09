import asyncio

from twitch_chat_irc import twitch_chat_irc

twitch_bot_path = 'D:/TereBin/coding/TLA/data/twitch_bot_data.txt'


async def send_chat(channel):
    username = '테레빈_봇'
    oauth_data = open(twitch_bot_path, 'r', encoding='utf-8')
    oauth = oauth_data.read()
    oauth_data.close()
    connection = twitch_chat_irc.TwitchChatIRC(username, oauth)

    message = '[TLA_Bot] 방송시작 알림이 자동으로 트윗되었습니다.'
    connection.send(channel, message)
    await asyncio.sleep(5)
    connection.close_connection()
