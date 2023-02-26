from dotenv import load_dotenv
import os
load_dotenv()
BOT_TOKEN = os.getenv('DISCORD_BOT_TOKEN')
SERVER_ID = os.getenv('DISCORD_SERVER_ID')
import random
import googletrans
import discord
from discord import app_commands
intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)
tree = app_commands.CommandTree(client)
import src.pokemon as pokemon, src.beauty as beauty, src.pixiv as pixiv, src.mongo as mongo

def rps(choice):
    c = random.randint(1, 3)
    if choice.lower() == 'paper':
        if c == 1: return 'Draw'
        elif c == 2: return 'You lose!'
        else: return 'You win!'
    elif choice.lower() == 'scissors':
        if c == 1: return 'You win!'
        elif c == 2: return 'Draw'
        else: return 'You lose!'
    elif choice.lower() == 'stone':
        if c == 1: return 'You win!'
        elif c == 2: return 'Draw'
        else: return 'You lose!'
    else: return '輸入錯誤'
def arithmetic_function(expression):
    try:
        return eval(expression)
    except: return 'error'
def translate(text, language = 'zh-tw'):
    try:
        translator = googletrans.Translator()
        return translator.translate(text, dest = language).text
    except: return 'error'

@client.event
async def on_ready():
    await tree.sync(guild=discord.Object(id=SERVER_ID))
    game = discord.Game('ぺこみこ大戦争！！')
    await client.change_presence(status=discord.Status.idle, activity=game)
    print('Bot: ', client.user)

@client.event
async def on_message(msg):
    if msg.author == client.user:
        return
        
    if 'みこ' in msg.content or 'miko' in msg.content.lower():
        if random.randint(0, 1):
            await msg.reply('にゃっはろ～！')
        else:
            await msg.reply('さくらみこだよ～！🌸')

    if 'ぺこら' in msg.content or 'pekora' in msg.content.lower():
        if random.randint(0, 1):
            await msg.reply('Peko Peko Peko Peko Peko Peko～！🥕')
        else:
            await msg.reply('Ha↗️Ha↘️Ha↗️Ha↘️Ha↗️Ha↘️Ha↗️Ha↘️')

    if '35' in msg.content:
        await msg.channel.send(file=discord.File(f'src/image/miko/{random.randint(1, 15)}.png'))

    if 'peko' in msg.content and 'pekora' not in msg.content:
        await msg.channel.send(file=discord.File(f'src/image/peko/{random.randint(1, 5)}.png'))

    if '窩不知道' in msg.content:
        await msg.channel.send(file=discord.File(f'src/image/idk/{random.randint(1, 2)}.png'))

    if 'fxxk' in msg.content.lower() or 'fuck' in msg.content.lower() or 'faq' in msg.content.lower():
        await msg.channel.send(file=discord.File('src/image/faq.png'))

    if msg.content.startswith('!好玩的遊戲'):
        await msg.reply('https://holodive.onrender.com/')

@tree.command(name="t",description="英翻中", guild=discord.Object(id=SERVER_ID))
async def slash_command1(interaction: discord.Interaction, text: str):
    await interaction.response.send_message(translate(text))

@tree.command(name="tadv",description="進階翻譯", guild=discord.Object(id=SERVER_ID))
async def slash_command2(interaction: discord.Interaction, text: str, language: str):
    await interaction.response.send_message(translate(text, language))

@tree.command(name="c",description="簡單計算", guild=discord.Object(id=SERVER_ID))
async def slash_command3(interaction: discord.Interaction, text: str):
    await interaction.response.send_message(arithmetic_function(text))

@tree.command(name="beauty",description="隨機爬取表特版圖片", guild=discord.Object(id=SERVER_ID))
async def slash_command4(interaction: discord.Interaction):
    await interaction.response.send_message(beauty.main())

@tree.command(name="pixiv",description="隨機爬取pixiv排行", guild=discord.Object(id=SERVER_ID))
async def slash_command5(interaction: discord.Interaction):
    await interaction.response.send_message(pixiv.main())

@tree.command(name="pixivadv",description="進階爬取pixiv排行", guild=discord.Object(id=SERVER_ID))
async def slash_command6(interaction: discord.Interaction, mode: str, rank: int, date: int):
    await interaction.response.send_message(pixiv.main(mode, rank, date))

@tree.command(name="pmtype",description="屬性相剋表", guild=discord.Object(id=SERVER_ID))
async def slash_command7(interaction: discord.Interaction):
    await interaction.response.send_message(file=discord.File('src/image/typechart.png'))

@tree.command(name="pm",description="寶可夢查詢", guild=discord.Object(id=SERVER_ID))
async def slash_command8(interaction: discord.Interaction, name: str):
    try:
        t = pokemon.type(name)
        s = pokemon.stat(name)
        pm_str = '```屬性: ' + '、'.join(t)
        if len(s) == 14:
            pm_str += '\n血量: {: >3}|{: >3}\n攻擊: {: >3}|{: >3}\n防禦: {: >3}|{: >3}\n特攻: {: >3}|{: >3}\n特防: {: >3}|{: >3}\n速度: {: >3}|{: >3}\n總和: {: >3}|{: >3}```'.format(s[0],s[7],s[1],s[8],s[2],s[9],s[3],s[10],s[4],s[11],s[5],s[12],s[6],s[13])
        else:
            pm_str += '\n血量: {: >3}\n攻擊: {: >3}\n防禦: {: >3}\n特攻: {: >3}\n特防: {: >3}\n速度: {: >3}\n總和: {: >3}```'.format(s[0],s[1],s[2],s[3],s[4],s[5],s[6])
        await interaction.response.send_message(pm_str)
    except:
        await interaction.response.send_message('no such name')

@tree.command(name="pmskill",description="查詢技能表", guild=discord.Object(id=SERVER_ID))
async def slash_command9(interaction: discord.Interaction, name: str):
    try:
        skills = pokemon.skill(name)
        skill_str = '```'
        for s in skills:
            skill_str += '{: >3}|{:　<7}|{:　>2}|{:　>2}|{: >3}|{: >3}\n'.format(s[0],s[2],s[3],s[4],s[5],s[6])
        skill_str += '```'
        await interaction.response.send_message(skill_str)
    except:
        await interaction.response.send_message('no such name')

@tree.command(name="roll",description="擲骰子", guild=discord.Object(id=SERVER_ID))
async def slash_command10(interaction: discord.Interaction, amount: int, point: int):
    try:
        if amount > 0 and point > 0:
            dices = [random.randint(1, point) for i in range(amount)]
            roll_str = f'`{dices[0]}`'
            for dice in dices[1:]:
                roll_str += f',`{dice}`'
            await interaction.response.send_message(roll_str)
    except:
        await interaction.response.send_message('error')

@tree.command(name="rps",description="猜拳", guild=discord.Object(id=SERVER_ID))
async def slash_command11(interaction: discord.Interaction, choice: str):
    await interaction.response.send_message(rps(choice))

@tree.command(name="holodive",description="獲取HoloDive個人資訊", guild=discord.Object(id=SERVER_ID))
async def slash_command12(interaction: discord.Interaction, account: str):
    try:
        profile = mongo.holodive(account)
        if len(profile) != 5:
            await interaction.response.send_message('查無此用戶')
        else:
            userEmbed=discord.Embed(title=profile[0], description="", color=0x5edeec)
            userEmbed.set_author(name="HoloDive", url="https://holodive.onrender.com/", icon_url="https://yesaouo.github.io/HoloDive/img/others/logo.png")
            userEmbed.set_thumbnail(url=profile[1])
            userEmbed.add_field(name="Coin", value=profile[2], inline=True)
            userEmbed.add_field(name="Diamond", value=profile[3], inline=True)
            for i in profile[4]:
                userEmbed.add_field(name=i, value=f"Lv: {profile[4][i]}", inline=False)
            await interaction.response.send_message(embed=userEmbed)
    except:
        await interaction.response.send_message('error')

client.run(BOT_TOKEN)