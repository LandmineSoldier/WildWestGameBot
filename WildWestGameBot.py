
import discord, asyncio
import random
import time
from random import *

token = "ODc0OTc0MjM2MjAzMTU5NjYz.YROxQg.9aIt-pEa-8hpDQIZ4P0VpLV-HpM"
client = discord.Client()

JimPattern = ["123456789","789456123","987654321","321654987",   "147258369","369258147","741852963","963852741"]
JimDelay = 7

@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.online, activity=discord.Game("PATCH TESTING"))
    print("I'm Ready!")
    print(client.user.name)
    print(client.user.id)

@client.event
async def on_message(message):
    if message.author.bot:
        return None
    
    if message.content == '!전설의총잡이':

        channel = message.channel

        embed=discord.Embed(title="전설의 총잡이", description="", color=0x69A5C9)
        embed.set_author(name="나오는 숫자들을 반대로 입력하여 적을 쓰러뜨려라", url="https://steamcommunity.com/id/LandmineSoldier/", icon_url="https://cdn.discordapp.com/app-icons/681470208648544279/3194ed1f665a08c5431ff9f009b5dd61.png?size=256")
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/874976109429686283/874976157844537354/logo.png")
        embed.add_field(name="마을이 위험에 처했습니다..", value="마을을 지켜주십시오!", inline=True)
        embed.add_field(name="5~10초 후 종이 울립니다. (Dang)", value="그 때 나오는 숫자들을 반대로 입력하여 총을 쏘십시오.", inline=True)
        embed.add_field(name="적은 4~10초 사이에 쏩니다.", value="적의 강력함에 따라 더 빨라집니다.. (후반으로 갈수록)", inline=True)
        embed.set_footer(text="10초 내에 '예'라고 답하세요")
        await message.channel.send(embed=embed)

        def yesFight(m):
            return m.content == '예' and m.channel == channel
        await client.wait_for('message', check=yesFight, timeout=60.0)
        
        await message.channel.send("https://cdn.discordapp.com/attachments/874976109429686283/874976161741013022/village.png")
        await message.channel.send("평화롭던 마을...")
        time.sleep(2)
        await message.channel.send("https://cdn.discordapp.com/attachments/874976109429686283/874976155831271454/enemy-jim.png")
        await message.channel.send("무친 악당의 등장!")
        time.sleep(2)
        await message.channel.send("https://cdn.discordapp.com/attachments/874976109429686283/874976157844537354/logo.png")
        await message.channel.send("이걸로 쓰러뜨려주셈!")
        time.sleep(2)


        await message.channel.send("https://cdn.discordapp.com/attachments/874976109429686283/874976160692437092/Ready.png")
        await message.channel.send("Jim : 심장을 쏴주마...")

        await message.channel.send("정적이 흐른다...")
        showdown = randint(5,10)

        time.sleep(showdown)
        #time.sleep(2)
        r = randint(1,8)
        alive = True

        await message.channel.send("Dang")

        if r == 1:
            await message.channel.send(JimPattern[r-1])
            def r1(m):
                return m.content == '987654321' and m.channel == channel
            try:
                await client.wait_for('message', check=r1, timeout=JimDelay) #7sec
            except asyncio.TimeoutError:
                await message.channel.send("https://cdn.discordapp.com/attachments/874976109429686283/874976159677435934/Lose.png")
                alive = False
            else:
                await message.channel.send("https://cdn.discordapp.com/attachments/874976109429686283/874976162823176202/win.png")
        elif r == 2:
            await message.channel.send(JimPattern[r-1])
            def r2(m):
                return m.content == '321654987' and m.channel == channel
            try:
                await client.wait_for('message', check=r2, timeout=JimDelay)
            except asyncio.TimeoutError:
                await message.channel.send("https://cdn.discordapp.com/attachments/874976109429686283/874976159677435934/Lose.png")
                alive = False
            else:
                await message.channel.send("https://cdn.discordapp.com/attachments/874976109429686283/874976162823176202/win.png")
        elif r == 3:
            await message.channel.send(JimPattern[r-1])
            def r3(m):
                return m.content == '123456789' and m.channel == channel
            try:
                await client.wait_for('message', check=r3, timeout=JimDelay)
            except asyncio.TimeoutError:
                await message.channel.send("https://cdn.discordapp.com/attachments/874976109429686283/874976159677435934/Lose.png")
                alive = False
            else:
                await message.channel.send("https://cdn.discordapp.com/attachments/874976109429686283/874976162823176202/win.png")
        elif r == 4:
            await message.channel.send(JimPattern[r-1])
            def r4(m):
                return m.content == '789456123' and m.channel == channel
            try:
                await client.wait_for('message', check=r4, timeout=JimDelay)
            except asyncio.TimeoutError:
                await message.channel.send("https://cdn.discordapp.com/attachments/874976109429686283/874976159677435934/Lose.png")
                alive = False
            else:
                await message.channel.send("https://cdn.discordapp.com/attachments/874976109429686283/874976162823176202/win.png")
        elif r == 5:
            await message.channel.send(JimPattern[r-1])
            def r5(m):
                return m.content == '963852741' and m.channel == channel
            try:
                await client.wait_for('message', check=r5, timeout=JimDelay)
            except asyncio.TimeoutError:
                await message.channel.send("https://cdn.discordapp.com/attachments/874976109429686283/874976159677435934/Lose.png")
                alive = False
            else:
                await message.channel.send("https://cdn.discordapp.com/attachments/874976109429686283/874976162823176202/win.png")
        elif r == 6:
            await message.channel.send(JimPattern[r-1])
            def r6(m):
                return m.content == '741852963' and m.channel == channel
            try:
                await client.wait_for('message', check=r6, timeout=JimDelay)
            except asyncio.TimeoutError:
                await message.channel.send("https://cdn.discordapp.com/attachments/874976109429686283/874976159677435934/Lose.png")
                alive = False
            else:
                await message.channel.send("https://cdn.discordapp.com/attachments/874976109429686283/874976162823176202/win.png")
        elif r == 7:
            await message.channel.send(JimPattern[r-1])
            def r7(m):
                return m.content == '369258147' and m.channel == channel
            try:
                await client.wait_for('message', check=r7, timeout=JimDelay)
            except asyncio.TimeoutError:
                await message.channel.send("https://cdn.discordapp.com/attachments/874976109429686283/874976159677435934/Lose.png")
                alive = False
            else:
                await message.channel.send("https://cdn.discordapp.com/attachments/874976109429686283/874976162823176202/win.png")
        elif r == 8:
            await message.channel.send(JimPattern[r-1])
            def r8(m):
                return m.content == '147258369' and m.channel == channel
            try:
                await client.wait_for('message', check=r8, timeout=JimDelay)
            except asyncio.TimeoutError:
                await message.channel.send("https://cdn.discordapp.com/attachments/874976109429686283/874976159677435934/Lose.png")
                alive = False
            else:
                await message.channel.send("https://cdn.discordapp.com/attachments/874976109429686283/874976162823176202/win.png")

        time.sleep(2)
        if alive == True:
            await message.channel.send("https://cdn.discordapp.com/attachments/874976109429686283/874976161741013022/village.png")
            await message.channel.send("당신은 그를 죽였고 마을에 평화가 찾아왔습니다!")
            await message.channel.send("만든이 : https://github.com/LandmineSoldier")
        elif alive == False:
            await message.channel.send("https://cdn.discordapp.com/attachments/874976109429686283/874976153390178314/dead.png")
            await message.channel.send("당신은 죽었고 마을은 쑥대밭이 되었습니다...")

client.run(token)
