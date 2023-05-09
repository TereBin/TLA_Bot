# TLA_Bot

## Twitch Live Alert Bot
트위치 방송의 시작을 트위터, 디스코드 등 여러 매체를 이용해 자동으로 알려주는 봇입니다.

0.1 버전 : [TtMP (Twitch to Multi Platform)](https://github.com/TereBin/Twitch_to_Multi_Platform)

Bot to alert Twitch stream using Twitter, Discord etc

### Contact
Twitch : [테레빈](https://www.twitch.tv/terebin_420)  
Twitter : [@terebin_420](https://twitter.com/TereBin_420)  
Discord : [TereBin#9929](https://www.discord.com/users/537256771501424640)

---
### Program

#### API
twitch API : Twitch API  
twitter API : Twitter API v2  
twitter Authentication : OAuth 1.0a  
dicord API : discord.py

---

#### [code](https://github.com/TereBin/TLA_Bot/tree/main/code)  
실행에 필요한 코드 파일

- [TLA_T.py](https://github.com/TereBin/TLA_Bot/blob/main/code/TLA_T.py)  
자동 트위터 봇의 main  
- [TLA_D.py](https://github.com/TereBin/TLA_Bot/blob/main/code/TLA_D.py)  
자동 디스코드 봇의 main  
- [read_list.py](https://github.com/TereBin/TLA_Bot/blob/main/code/read_list.py)  
json 파일을 python의 dictionary 객체로 변환하는 모듈  
- [check_twitch.py](https://github.com/TereBin/TLA_Bot/blob/main/code/check_twitch.py)  
twitch api를 이용, 스트리머의 아이디를 이용해 방송 정보를 읽어오는 모듈  
- [send_tweet.py](https://github.com/TereBin/TLA_Bot/blob/main/code/send_tweet.py)  
twitter api를 이용, 스트리머의 트위터에 방송 알림을 트윗해주는 모듈  
- [send_chat.py](https://github.com/TereBin/TLA_Bot/blob/main/code/send_chat.py)
twitch 채팅에 방송알림 트윗을 안내하는 모듈  
- [edit_list.py](https://github.com/TereBin/TLA_Bot/blob/main/code/edit_list.py)  
TLA_T에서 방송이 켜지면서 json 데이터의 변경이 필요할 때 json 파일을 수정해주는 모듈  
- [err_logging.py](https://github.com/TereBin/TLA_Bot/blob/main/code/err_logging.py)  
실행 중 생기는 에러로그를 저장해주는 모듈  

- [new_auth.py](https://github.com/TereBin/TLA_Bot/blob/main/code/new_auth.py)  
새로운 등록을 위해 사용되는 함수  

---

#### [data](https://github.com/TereBin/TLA_Bot/tree/main/data)  
실행에 필요한 데이터 파일. *유출을 막기 위해 sensitive한 내용은 \*로 처리되어있음*

- [streamer_list.json](https://github.com/TereBin/TLA_Bot/blob/main/data/streamer_list.json)  
스트리머들의 정보(twitch 아이디, twitter 아이디 등)를 담고 있는 json 파일  
- [twitch_api_data.txt](https://github.com/TereBin/TLA_Bot/blob/main/data/twitch_api_data.txt)  
twitch api를 이용하기 위한 api key를 담고 있는 txt 파일  
- [twitter_api_data.txt](https://github.com/TereBin/TLA_Bot/blob/main/data/twitter_api_data.txt)  
twitter api를 이용하기 위한 api key를 담고 있는 txt 파일
- [twitch_bot_data.txt](https://github.com/TereBin/TLA_Bot/blob/main/data/twitch_bot_data.txt)  
twitch에 채팅을 보내기 위한 auth token을 담고 있는 txt 파일  
- [discord_data.json](https://github.com/TereBin/TLA_Bot/blob/main/data/discord_data.json)  
discord의 각 서버에 대한 관리자, 알림 채널 등의 정보를 담고 있는 json 파일  
- [discord_list.json](https://github.com/TereBin/TLA_Bot/blob/main/data/discord_list.json)  
알림을 받을 사용자에 대한 전송 서버, 전송 여부 등을 담고 있는 json 파일  
