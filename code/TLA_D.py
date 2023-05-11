import json
import requests
import asyncio
import discord
from discord.ext import commands, tasks
from check_twitch import check_twitch
from read_list import read_list
from err_logging import err_logging

discord_data_path = "../data/discord_data.json"
streamer_json_path = "../data/discord_list.json"
twitch_api_path = "../data/twitch_api_data.txt"

discord_dict = asyncio.run(read_list(discord_data_path))
token = discord_dict["token"]
bot = commands.Bot(command_prefix='!', intents=discord.Intents.all())

with open(twitch_api_path, 'r') as f:
    twitch_api_data = f.read().splitlines()
    twitch_key = twitch_api_data[0]
    twitch_secret = twitch_api_data[1]

auth_req = requests.post(
    'https://id.twitch.tv/oauth2/token?client_id=' + twitch_key + '&client_secret=' + twitch_secret + '&grant_type=client_credentials')
auth_req_json = auth_req.json()
access_token = auth_req_json["access_token"]
token_type = auth_req_json["token_type"]
token_type = token_type[0].upper() + token_type[1:]
auth_token = token_type + " " + access_token

async def edit_channel(server_id, channel_id):
    discord_json = json.load(open(discord_data_path, 'r'))
    discord_json["server"][server_id]["channel"] = channel_id
    with open(discord_data_path, 'w') as file:
        json.dump(discord_json, file, indent="\t")
    discord_dict = await read_list(discord_data_path)
    return discord_dict

async def edit_sent(num, bool):
    streamer_json = json.load(open(streamer_json_path, 'r'))
    sent = streamer_json[num]["sent"]
    if bool:
        streamer_json[num]["sent"] = "True"
    else:
        streamer_json[num]["sent"] = "False"
    with open(streamer_json_path, 'w') as file:
        json.dump(streamer_json, file, indent="\t")
    result = await read_list(discord_data_path)
    return result


@bot.event
async def on_ready():
    print(f'{bot.user.name} on-line')
    print("-"*30)
    auto_alarm.start()
    await bot.change_presence(status=discord.Status.online, activity=discord.CustomActivity("방송 여부 확인중"))


@bot.command()
async def setchannel(ctx):
    server_id = str(ctx.guild.id)
    discord_dict = await read_list(discord_data_path)
    discord_server = discord_dict["server"]
    if str(ctx.author.id) == discord_server[server_id]["manager"] or discord_dict["dev"]:  # 서버장이 명령어 사용
        c_channel_id = ctx.channel.id
        if discord_server[server_id]["channel"] == str(c_channel_id):  # 이미 지정되어있는 채널인 경우
            await ctx.send("이 채널로 알림이 설정되어 있습니다.")
        else:  # 새로운 채널 지정
            await edit_channel(server_id, str(c_channel_id))
            c_channel_name = bot.get_channel(c_channel_id)
            await ctx.send(f"{c_channel_name} 채널에서 알림이 갑니다")
            print(f"[{ctx.guild}] channel set to : {c_channel_name}\n" + '-'*30)
    else:  # 서버장이 아닌 유저가 명령어 사용
        await ctx.send("서버장만 사용 가능한 명령어입니다.")


@bot.command()
async def alarm(ctx, streamer_id):
    discord_dict = await read_list(discord_data_path)
    discord_server = discord_dict["server"]
    channel = int(discord_server[str(ctx.guild.id)]["channel"])
    channel = bot.get_channel(channel)
    await channel.send(f"https://twitch.tv/{streamer_id}")
    print(f"[{ctx.guild}] alarm sent : https://twitch.tv/{streamer_id}\n" + '-'*30)

@tasks.loop(minutes=1)
async def auto_alarm():
    streamer_dict = await read_list(streamer_json_path)
    for list_num, list_data in streamer_dict.items():  # check each streamer
        try:
            if list_num != "0":
                twitch_id = list_data["id"]
                is_live, category, title = await check_twitch(twitch_id, twitch_key, auth_token)  # check twitch
                if is_live and list_data["sent"] == "False":            
                    message = list_data["message"]
                    req = []
                    for i in list(list_data["req"]):
                        req.append(bool(int(i)))
                    for data_num, server_id in list_data["server"].items():
                        discord_dict = await read_list(discord_data_path)
                        server_data = discord_dict["server"].get(server_id)
                        guild = bot.get_guild(int(server_id))
                        channel = bot.get_channel(int(server_data["channel"]))
                        if req[0]:
                            message = message + "\n방송제목 : " + title
                        if req[1]:
                            message = message + "\nzkxprhfl : " + category
                        print(f"[{guild}] alarm sent : https://twitch.tv/{twitch_id}\n")
                        if req[2]:
                            await channel.send(f"{message}\nhttps://twitch.tv/{twitch_id}")
                        else:
                            await channel.send(f"https://twitch.tv/{twitch_id}")
                        await edit_sent(list_num, True)
                elif (not is_live) and list_data["sent"] == "True":
                    await edit_sent(list_num, False)
        except Exception as err_data:
            print("error under TLA_D.py")
            await err_logging(err_data)
    print("-" * 30)

bot.run(token)

