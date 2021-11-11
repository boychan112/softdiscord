import discord
import datetime
import os
import time
import pytz
import asyncio
from discord.ext import tasks
from itertools import cycle

client = discord.Client()

@client.event
async def on_ready():
    print("디스코드 봇 로그인이 완료되었습니다.")
    print("디스코드 봇 이름 : " +client.user.name)
    print("디스코드 봇 ID" +str(client.user.id))
    print("디스코드봇 버전 : " + str(discord.__version__))
    print('------')
    
    change_status.start()
    
status = cycle(["Visual Studio Code", "Dev C++", "League of Legend", "!도움말", "ZOOM","전략적 팀 전투","Starcraft","Overwatch","즐거운 추석 보내세요"])
@tasks.loop(seconds=10)
async def change_status():
    await client.change_presence(activity=discord.Game(next(status)))

@client.event
async def on_message(message):
    content = message.content
    
    if content.startswith("!준민이 뺨따구 때리기"):
        await message.channel.send("짝짝짝짝짝짝짝짝짝짝짝짝짝짝")
        
    if content.startswith("!씨발오류"):
        await message.channel.send("ㅈ같네")

    if content.startswith("!자기소개"):
        embed=discord.Embed(description="응애 나는야 IT소프트웨어과 1-9 반디코 도우미 봇", color=0x00ff56)
        embed.set_author(name="응애 나 아기 디코봇")
        await message.channel.send(embed=embed)

    if content.startswith("!인백이의 드립은"):
        await message.channel.send("개씹노잼입니다")
        
    if content.startswith("!민혁이의 봇은"):
        await message.channel.send("작동 안되죠? 작동 안되죠? 작동 안되죠? 작동 안되죠? 작동 안되죠? 작동 안되죠? 작동 안되죠? 작동 안되죠?`")

    if content.startswith("!시간표"):
        embed=discord.Embed(title=" ", description=" ", color=0x00ff56)
        embed.set_author(name="```수원정보과학고등학교 1학년 9반 시간표```", url="https://cdn.discordapp.com/attachments/873384182997479457/879342240839905360/unknown.png")
        embed.set_image(url="https://cdn.discordapp.com/attachments/873384182997479457/879342240839905360/unknown.png")
        await message.channel.send(embed=embed)

    if content.startswith("!월시간표"):
        embed=discord.Embed(description="<1교시>\n프로\n임미경선생님\nhttps://zoom.us/j/3477694372?pwd=NlIvbDlGRHVKQlQ4WVphSVg3RkJOQT09#success\n\n<2교시>\n프로\n임미경선생님\nhttps://zoom.us/j/3477694372?pwd=NlIvbDlGRHVKQlQ4WVphSVg3RkJOQT09#success\n\n<3교시>\n프로\n임미경선생님\nhttps://zoom.us/j/3477694372?pwd=NlIvbDlGRHVKQlQ4WVphSVg3RkJOQT09#success\n\n<4교시>\n프로\n임미경선생님\nhttps://zoom.us/j/3477694372?pwd=NlIvbDlGRHVKQlQ4WVphSVg3RkJOQT09#success\n\n<5교시>\n수학\nhttps://us02web.zoom.us/j/7076631677?pwd=RkVPYzRXcDVrdXM3VEUyTlBHMXN2Zz09\n\n<6교시>\n사회\n이용각선생님\nhttps://us02web.zoom.us/j/9546996730\n암호 : 810052", color=0x00ff56)
        embed.set_author(name="IT 소프트웨어과 1-9 월요일 시간표", url="https://cdn.discordapp.com/attachments/873384182997479457/879342240839905360/unknown.png")
        embed.set_image(url="https://cdn.discordapp.com/attachments/873384182997479457/879342240839905360/unknown.png")
        await message.channel.send(embed=embed)
    
    if content.startswith("!화시간표"):
        embed=discord.Embed(description="<1교시>\n체육\nhttps://us02web.zoom.us/j/5523718127?pwd=TEhQeFJaanJ0dVVuOUVIdzFJUTRIUT09\n암호 : 2246\n\n<2교시>\n컴일\n임미경선생님\nhttps://zoom.us/j/3477694372?pwd=NlIvbDlGRHVKQlQ4WVphSVg3RkJOQT09#success\n박진영선생님\nhttps://zoom.us/j/8064557267?pwd=VjUrbUxJZkI2bDJPNklIZHA1YkpBZz09\n\n<3교시>\n컴일\n임미경선생님\nhttps://zoom.us/j/3477694372?pwd=NlIvbDlGRHVKQlQ4WVphSVg3RkJOQT09#success\n박진영선생님\nhttps://zoom.us/j/8064557267?pwd=VjUrbUxJZkI2bDJPNklIZHA1YkpBZz09\n\n<4교시>\n영어\nhttps://zoom.us/j/7334811715?pwd=TnAwc2dMeWFHYlRWdkFocTlQVWVlQT09\n\n<5교시>\n수학\nhttps://us02web.zoom.us/j/7076631677?pwd=RkVPYzRXcDVrdXM3VEUyTlBHMXN2Zz09\n\n<6교시>\n음악\nhttps://zoom.us/j/3079582246?pwd=clh3Ym82NGNDZXZlTC9yUzR2RUhnZz09\n암호 : 2246\n\n<7교시>\n사회\n이진경선생님\nhttps://zoom.us/j/9785974688\n암호 : 4688", color=0x00ff56)
        embed.set_author(name="IT 소프트웨어과 1-9 화요일 시간표", url="https://cdn.discordapp.com/attachments/873384182997479457/879342240839905360/unknown.png")
        embed.set_image(url="https://cdn.discordapp.com/attachments/873384182997479457/879342240839905360/unknown.png")
        await message.channel.send(embed=embed)

    if content.startswith("!수시간표"):
        embed=discord.Embed(description="<1교시>\n국어\nhttps://us02web.zoom.us/j/8980834250\n암호 : 4250\n\n<2교시>\n음악\nhttps://zoom.us/j/3079582246?pwd=clh3Ym82NGNDZXZlTC9yUzR2RUhnZz09\n암호 : 2246\n\n<3교시>\n수학\nhttps://us02web.zoom.us/j/7076631677?pwd=RkVPYzRXcDVrdXM3VEUyTlBHMXN2Zz09\n\n<4교시>\n영어\nhttps://zoom.us/j/7334811715?pwd=TnAwc2dMeWFHYlRWdkFocTlQVWVlQT09\n\n<5교시>\n사회\n이용각선생님\n\nhttps://us02web.zoom.us/j/9546996730\n암호 : 810052\n\n<6교시>\n과학\nhttps://zoom.us/j/8212455526?pwd=SnRkaFBZU05ETHFWOExRMXJlc243Zz09\n암호 : 5526\n\n<7교시>\n진로\nhttps://us02web.zoom.us/j/7414780713?pwd=aDdiYldHVTRScVk3WjFQMG9SQkxUQT09\n암호 : 1234", color=0x00ff56)
        embed.set_author(name="IT 소프트웨어과 1-9 수요일 시간표", url="https://cdn.discordapp.com/attachments/873384182997479457/879342240839905360/unknown.png")
        embed.set_image(url="https://cdn.discordapp.com/attachments/873384182997479457/879342240839905360/unknown.png")
        await message.channel.send(embed=embed)

    if content.startswith("!목시간표"):
        embed=discord.Embed(description="<1교시>\n과학\nhttps://zoom.us/j/8212455526?pwd=SnRkaFBZU05ETHFWOExRMXJlc243Zz09\n암호 : 5526\n\n<2교시>\n프로\n박진영선생님\nhttps://zoom.us/j/8064557267?pwd=VjUrbUxJZkI2bDJPNklIZHA1YkpBZz09\n\n<3교시>\n프로\n박진영선생님\nhttps://zoom.us/j/8064557267?pwd=VjUrbUxJZkI2bDJPNklIZHA1YkpBZz09\n\n<4교시>\n체육\nhttps://us02web.zoom.us/j/5523718127?pwd=TEhQeFJaanJ0dVVuOUVIdzFJUTRIUT09\n암호 : 2246\n\n<5교시>\n국어\nhttps://us02web.zoom.us/j/8980834250\n암호 : 4250\n\n<6교시>\n영어\nhttps://zoom.us/j/7334811715?pwd=TnAwc2dMeWFHYlRWdkFocTlQVWVlQT09\n\n<7교시>\n사회\n이진경선생님\nhttps://zoom.us/j/9785974688\n암호 : 4688", color=0x00ff56)
        embed.set_author(name="IT 소프트웨어과 1-9 목요일 시간표", url="https://cdn.discordapp.com/attachments/873384182997479457/879342240839905360/unknown.png")
        embed.set_image(url="https://cdn.discordapp.com/attachments/873384182997479457/879342240839905360/unknown.png")
        await message.channel.send(embed=embed)

    if content.startswith("!금시간표"):
        embed=discord.Embed(description="<1교시>\n미술\nhttps://us02web.zoom.us/j/88329393006?pwd=bks5STl3RHRQYU9SZDJjNEVzNUp5UT09\n\n<2교시>\n미술\nhttps://us02web.zoom.us/j/88329393006?pwd=bks5STl3RHRQYU9SZDJjNEVzNUp5UT09\n\n<3교시>\n처리\n임미경선생님\nhttps://zoom.us/j/3477694372?pwd=NlIvbDlGRHVKQlQ4WVphSVg3RkJOQT09#success\n박진영선생님\nhttps://zoom.us/j/8064557267?pwd=VjUrbUxJZkI2bDJPNklIZHA1YkpBZz09\n\n<4교시>\n처리\n임미경선생님\nhttps://zoom.us/j/3477694372?pwd=NlIvbDlGRHVKQlQ4WVphSVg3RkJOQT09#success\n박진영선생님\nhttps://zoom.us/j/8064557267?pwd=VjUrbUxJZkI2bDJPNklIZHA1YkpBZz09\n\n<5교시>\n융합\nhttps://us02web.zoom.us/j/7076631677?pwd=RkVPYzRXcDVrdXM3VEUyTlBHMXN2Zz09\n\n<6교시>\n창체\nhttps://us02web.zoom.us/j/7076631677?pwd=RkVPYzRXcDVrdXM3VEUyTlBHMXN2Zz09\n", color=0x00ff56)
        embed.set_author(name="IT 소프트웨어과 1-9 금요일 시간표", url="https://cdn.discordapp.com/attachments/873384182997479457/879342240839905360/unknown.png")
        embed.set_image(url="https://cdn.discordapp.com/attachments/873384182997479457/879342240839905360/unknown.png")
        await message.channel.send(embed=embed)

    if content.startswith("!시정표"):
        embed=discord.Embed(description="<1교시>\n09:10 ~ 10:00\n\n<2교시>\n10:10 ~ 11:00\n\n<3교시>\n11:10 ~ 12:00\n\n<4교시>\n12:10 ~ 1:00\n\n<5교시>\n02:00 ~ 2:50\n\n<6교시>\n03:00 ~ 3:50\n\n<7교시>\n04:00 ~ 4:50", color=0x00ff56)
        embed.set_author(name="수원정보과학고등학교 시정표", url=" ")
        await message.channel.send(embed=embed)

    if content.startswith("!40분 단축"):
        embed=discord.Embed(description="<1교시>\n09:10 ~ 09:50\n\n<2교시>\n10:00 ~ 10:40\n\n<3교시>\n10:50 ~ 11:30\n\n<4교시>\n11:40 ~ 12:20\n\n<5교시>\n1:20 ~ 2:00\n\n<6교시>\n02:10 ~ 2:50\n\n<7교시>\n03:00 ~ 3:40", color=0x00ff56)
        embed.set_author(name="수원정보과학고등학교 시정표", url=" ")
        await message.channel.send(embed=embed)

    if content.startswith("!30분 단축"):
        embed=discord.Embed(description="<1교시>\n09:10 ~ 09:40\n\n<2교시>\n09:50 ~ 10:20\n\n<3교시>\n10:30 ~ 11:00\n\n<4교시>\n11:10 ~ 11:40\n\n<5교시>\n12:40 ~ 1:10\n<6교시>\n1:20 ~ 1:50\n\n<7교시>\n02:00 ~ 2:30", color=0x00ff56)
        embed.set_author(name="수원정보과학고등학교 시정표", url=" ")
        await message.channel.send(embed=embed)

    if content.startswith("!도움말"):
        embed=discord.Embed(description="```diff\n-------반디코-------\n!준민이 뺨따꾸 때리기\n!인백이의 드립은\n!자기소개\n!시간\n!깃헙 (아이디)\n!청소 (청소할 메시지 개수)\n!투표/(투표항목)/(투표항목)...\n!시간표\n!월시간표\n!화시간표\n!수시간표\n!목시간표\n!금시간표\n!공지 (공지내용)\n!오피지지\n!옵지 (닉네임)\n\n-------롤체-------\n!롤체지지\n!롤체 (닉네임)\n!(레벨)확률\n-------이터널 리턴-------\n!닥지 (닉네임)\n!음식지도\n!로드맵\n!지도\n!레시피```", color=0x00ff55)
        embed.set_author(name="<<명령어>>", url="")
        await message.channel.send(embed=embed)

    if content.startswith("!코드업"):
        nick = message.content[5:]
        embed=discord.Embed(description="코드업 {} 바로가기\nhttps://www.codeup.kr/problem.php?id={}".format(nick,nick), color=0x00ff56)
        embed.set_author(name="<<{}번 문제>>".format(nick))
        await message.channel.send(embed=embed)
    
    if message.content.startswith ("!청소"):
        i = (message.author.guild_permissions.administrator)

        if i is True:
            amount = message.content[4:]
            await message.channel.purge(limit=1)
            await message.channel.purge(limit=int(amount))

            embed = discord.Embed(title="메시지 삭제 알림", description="최근 디스코드 채팅 {}개가\n관리자 {}님에 의해 삭제 되었습니다".format(amount, message.author), color=0x00ff56)
            await message.channel.send(embed=embed)
        
        if i is False:
            await message.channel.purge(limit=1)
            await message.channel.send("{}, 당신은 명령어를 사용할 수 있는 권한이 없습니다".format(message.author.mention))
                
    if message.content.startswith ("!공지"):
        await message.channel.purge(limit=1)
        i = (message.author.guild_permissions.administrator)
        if i is True:
            notice = message.content[4:]
            channel = client.get_channel('')
            embed = discord.Embed(title="**공지사항 제목*", description="\n――――――――――――――――――――――――――――\n\n{}\n\n――――――――――――――――――――――――――――".format(notice),timestamp=datetime.datetime.now(pytz.timezone('UTC')), color=0x00ff00)
            embed.set_footer(text="공지 작성자 : {}".format(message.author))
            await message.channel.send ("@everyone", embed=embed)
            await message.author.send("```*[ BOT 자동 알림 ]* | 정상적으로 공지가 채널에 작성이 완료되었습니다 : )\n\n[ 기본 작성 설정 채널 ] : {}\n[ 공지 발신자 ] : {}\n\n[ 내용 ]\n{}```".format(channel, message.author, notice))
       
        if i is False:
            await message.channel.send("{}, 당신은 관리자가 아닙니다".format(message.author.mention))
    
    if content.startswith("!2확률"):
        embed=discord.Embed(description="100/0/0/0/0", color=0x00ff56)
        embed.set_author(name="<<2렙 확률>>" , url=" ")
        await message.channel.send(embed=embed)

    if content.startswith("!3확률"):
        embed=discord.Embed(description="75/25/0/0/0", color=0x00ff56)
        embed.set_author(name="<<3렙 확률>>" , url=" ")
        await message.channel.send(embed=embed)

    if content.startswith("!4확률"):
        embed=discord.Embed(description="55/30/15/0/0", color=0x00ff56)
        embed.set_author(name="<<4렙 확률>>" , url=" ")
        await message.channel.send(embed=embed)

    if content.startswith("!5확률"):
        embed=discord.Embed(description="45/33/20/2/0", color=0x00ff56)
        embed.set_author(name="<<5렙 확률>>" , url=" ")
        await message.channel.send(embed=embed)

    if content.startswith("!6확률"):
        embed=discord.Embed(description="25/40/30/5/0", color=0x00ff56)
        embed.set_author(name="<<6렙 확률>>" , url=" ")
        await message.channel.send(embed=embed)
    
    if content.startswith("!7확률"):
        embed=discord.Embed(description="19/30/35/15/1", color=0x00ff56)
        embed.set_author(name="<<7렙 확률>>" , url=" ")
        await message.channel.send(embed=embed)

    if content.startswith("!8확률"):
        embed=discord.Embed(description="15/20/35/25/5", color=0x00ff56)
        embed.set_author(name="<<8렙 확률>>" , url=" ")
        await message.channel.send(embed=embed)

    if content.startswith("!9확률"):
        embed=discord.Embed(description="10/15/30/30/15", color=0x00ff56)
        embed.set_author(name="<<9렙 확률>>" , url=" ")
        await message.channel.send(embed=embed)

    if content.startswith("!1코확률"):
        embed=discord.Embed(description="100/100/75/55/45/25/19/15/10", color=0x9c9684)
        embed.set_author(name="<<1코스트 확률>>" , url=" ")
        await message.channel.send(embed=embed)

    if content.startswith("!2코확률"):
        embed=discord.Embed(description="0/0/25/30/33/40/30/20/15", color=0x39b65a)
        embed.set_author(name="<<2코스트 확률>>" , url=" ")
        await message.channel.send(embed=embed)

    if content.startswith("!3코확률"):
        embed=discord.Embed(description="0/0/0/15/20/30/35/35/30", color=0x42c3ff)
        embed.set_author(name="<<3코스트 확률>>" , url=" ")
        await message.channel.send(embed=embed)

    if content.startswith("!4코확률"):
        embed=discord.Embed(description="0/0/0/0/2/5/15/25/30", color=0xa708a5)
        embed.set_author(name="<<4코스트 확률>>" , url=" ")
        await message.channel.send(embed=embed)

    if content.startswith("!5코확률"):
        embed=discord.Embed(description="0/0/0/0/0/0/1/5/15", color=0xff8e00)
        embed.set_author(name="<<5코스트 확률>>" , url=" ")
        await message.channel.send(embed=embed)

    if content.startswith("!롤체지지"):
        embed=discord.Embed(description="https://lolchess.gg/meta", color=0x00ff56)
        embed.set_author(name="<<롤체지지>>", url="https://lolchess.gg/meta")
        await message.channel.send(embed=embed)

    if content.startswith("!CBT"):
        embed=discord.Embed(description="https://www.comcbt.com/xe/c2/4400733", color=0x00ff56)
        embed.set_author(name="<<CBT>>", url="https://www.comcbt.com/xe/c2/4400733")
        await message.channel.send(embed=embed)
    
    if content.startswith("!오피지지"):
        embed=discord.Embed(description="https://op.gg", color=0x00ff56)
        embed.set_author(name="<<오피지지>>",url="https://op.gg")
        await message.channel.send(embed=embed)

    if content.startswith("!파이썬"):
        embed=discord.Embed(description="https://replit.com/", color=0xffffff)
        embed.set_author(name="<<REPLIT>>",url="https://replit.com/")
        await message.channel.send(embed=embed)
   
    if content.startswith("!9월 학사일정"):
        embed=discord.Embed(description="14일 : 영어듣기평가(1학년)\n15일 : 영어듣기평가(2학년)\n17일 : 교내체육대회\n21일 : 추석 & 킹갓제네럴엠페러 서버장 이원찬 탄신일\n30일 : 수정제", color=0x00ff56)
        embed.set_author(name="<<수원정보과학고등학교 9월 학사일정>>",url=" ")
        await message.channel.send(embed=embed)

    
    if content.startswith("!10월 학사일정"):
        embed=discord.Embed(description="1일 : 체험학습\n8일 : 동아리\n12~14일 : 1차 지필평가 & 졸업고사", color=0x00ff56)
        embed.set_author(name="<<수원정보과학고등학교 10월 학사일정>>",url=" ")
        await message.channel.send(embed=embed)

    if content.startswith("!11월 학사일정"):
        embed=discord.Embed(description="5일 : 동아리\n18일 : 수능\n19일 : 동아리", color=0x00ff56)
        embed.set_author(name="<<수원정보과학고등학교 11월 학사일정>>",url=" ")
        await message.channel.send(embed=embed)

    if content.startswith("!12월 학사일정"):
        embed=discord.Embed(description="10일 : 동아리\n20~23일\n25일 : 성탄절", color=0x00ff56)
        embed.set_author(name="<<수원정보과학고등학교 12월 학사일정>>",url=" ")
        await message.channel.send(embed=embed)

    if content.startswith("!1월 학사일정"):
        embed=discord.Embed(description="1일 : 신정\n6일 : 교내합창대회\n7일 : 동아리\n11일 : 졸업식", color=0x00ff56)
        embed.set_author(name="<<수원정보과학고등학교 1월 학사일정>>",url=" ")
        await message.channel.send(embed=embed)
        
    if(message.content == "!시간"):
        await message.channel.send(embed=discord.Embed(title="Time", timestamp=datetime.datetime.utcnow()))
        
    if content.startswith("!옵지"):
        nick = message.content[4:]
        embed=discord.Embed(description="오피지지 {} 바로가기\nhttps://www.op.gg/summoner/userName={}".format(nick,nick), color=0x00ff56)
        embed.set_author(name="<<{}>>".format(nick))
        await message.channel.send(embed=embed)
        
    if content.startswith("!롤체"):
        nick = message.content[4:]
        embed=discord.Embed(description="롤체지지 {} 바로가기\nhttps://lolchess.gg/profile/kr/{}".format(nick,nick), color=0x00ff56)
        embed.set_author(name="<<{}>>".format(nick))
        await message.channel.send(embed=embed)
        
    if content.startswith("!닥지"):
        nick = message.content[4:]
        embed=discord.Embed(description="닥지지 {} 바로가기\nhttps://dak.gg/bser/players/{}".format(nick,nick), color=0x00ff56)
        embed.set_author(name="<<{}>>".format(nick))
        await message.channel.send(embed=embed)
    
    if content.startswith("!깃헙"):
        nick = message.content[4:]
        embed=discord.Embed(description="깃허브 {} 바로가기\nhttps://github.com/{}".format(nick,nick), color=0x00ff56)
        embed.set_author(name="<<{}>>".format(nick))
        await message.channel.send(embed=embed)
        
    if content.startswith("!음식지도"):
        embed=discord.Embed(title=" ", description=" ", color=0x00ff56)
        embed.set_author(name="```음식 지도```")
        embed.set_image(url="https://cdn.discordapp.com/attachments/873384182997479457/873384193722298398/common.png")
        await message.channel.send(embed=embed)

    if content.startswith("!지도"):
        embed=discord.Embed(title=" ", description=" ", color=0x00ff56)
        embed.set_author(name="```지도```")
        embed.set_image(url="https://cdn.discordapp.com/attachments/873384182997479457/873384713216225341/common.png")
        await message.channel.send(embed=embed)

    if content.startswith("!레시피"):
        embed=discord.Embed(description="```fix\n힐링포션```\n난초 + 유리병\n난초 = 약초 + 꽃\n========================\n```fix\n구급상자```\n지혈제 + 붕대\n지혈제 = 알코올 + 붕대\n========================\n```fix\n생선튀김```\n붕어 + 뜨거운 오일\n뜨거운 오일 = 오일 + 라이터\n========================\n```fix\n감자튀김```\n감자 + 뜨거운 오일\n뜨거운 오일 = 오일 + 라이터\n========================\n```fix\n피쉬앤칩스```\n감자튀김 + 생선튀김\n========================\n```fix\n햄버거```\n고기 + 빵\n========================\n```fix\n감자튀김```\n감자 + 뜨거운 오일\n뜨거운오일 = 라이터 + 오일\n========================\n```fix\n일레븐세트```\n햄버거 + 감자튀김\n========================", color=0x00ff56)
        await message.channel.send(embed=embed)
        
    if content.startswith("!로드맵"):
        embed=discord.Embed(title=" ", description=" ", color=0x00ff56)
        embed.set_author(name="이터널 리턴 로드맵 바로가기", url="https://trello.com/b/EjEt8ZPk/%EC%9D%B4%ED%84%B0%EB%84%90-%EB%A6%AC%ED%84%B4-%EB%A1%9C%EB%93%9C%EB%A7%B5")
        await message.channel.send(embed=embed)

    if message.content.startswith ("!도배"):
        i = (message.author.guild_permissions.administrator)

        if i is True:
            dob = message.content[4:]
            dobae=int(dob)
            for x in range(dobae):
                await message.channel.send("도배메시지")
        
        if i is False:
            await message.channel.purge(limit=1)
            await message.channel.send("{}, 당신은 명령어를 사용할 수 있는 권한이 없습니다".format(message.author.mention))
        
access_token = os.environ["BOT_TOKEN"]
client.run(access_token)
