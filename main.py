# Импортируем настройки бота
# import conf
import discord
from discord.ext import commands
import img_handler as imhl
import os, random

"""
    Настройка бота
"""
# Настраиваем расширенный доступ Intents
intents = discord.Intents.default()
# Даём права для просмотра участников сервера
intents.members = True

# Создаём бота, настравиваем префикс комманд и даём расширенные права
bot = commands.Bot(command_prefix="!", intents=intents)

# Allowed channels
channel = 841210415684780044
servname = "test"


"""
    Комманды бота
"""

@bot.command(name = "hello")
async def command_hello(ctx, *args):
    #Переводим список в строку разделенными пробелами
    message = " ".join(args)
    if ctx.channel.id == channel:
        msg = f'Salam! Dont cry {message}'
        await ctx.channel.send(msg)

@bot.command(name = "about_me")
async def command_hello(ctx, *args):
    #Переводим список в строку разделенными пробелами
    message = " ".join(args)
    if ctx.channel.id == channel:
        msg = f'Salam! {ctx.author.id}'
        if ctx.author.nick:
            msg = f'and your nick is {ctx.author.nick}'
    await ctx.channel.send(msg)

@bot.command(name= "repeat")
async def command_repeat(ctx, *args):
    if ctx.channel.id == channel:
        msg = f'{" ".join(args)}'
    await ctx.channel.send(msg)

@bot.command(name = "get_member")
async def get_member(ctx, member:discord.Member = None):
    msg = None
    global channel
    if ctx.channel.id == channel:

        if member:
            msg = f'Member {member.name}{"({member.nick})" if member.nick else " "} - {member.id}'

        if msg == None:
            msg = "error"


        await ctx.channel.send(msg)

@bot.command(name = "mk")
async def command_mk(ctx, f1:discord.Member=None, f2:discord.Member=None):
    global channel
    msg = None
    if ctx.channel.id == channel:
        if ctx.author.guild.name == servname:
            if f1 and f2:
                msg = f'{f1.name} {f"({f1.nick})" if f1.nick else ""} vs {f2.name} {f"({f2.nick})" if f2.nick else ""}'
                await imhl.vs_create(f1.avatar_url, f2.avatar_url)
            elif f1:
                msg = f'{f1.name} {f"({f1.nick})" if f1.nick else ""} vs {bot.user.name}'
                await imhl.vs_create(f1.avatar_url, bot.user.avatar_url)
        await ctx.channel.send(msg)

        await ctx.channel.send(file=discord.File(os.path.join("./img/result.png")))

@bot.command(name = "mka")
async def mka(ctx, f1:discord.Member = None, f2:discord.Member = bot.user):
    msg = None
    global channel
    if ctx.channel.id == channel:
        if f1 and f2:
            await imhl.vs_create_animated(f1.avatar_url, f2.avatar_url)
            await ctx.channel.send(file =discord.File(os.path.join("./img/result.gif")))

@bot.command(name="join")
async def vc_join(ctx):
    msg = ""
    global channel

    if ctx.channel.id == channel:
        voice_channel = ctx.author.voice.channel
        if voice_channel:
            msg = f'Подключаюсь к {voice_channel.name}'
            await ctx.channel.send(   msg   )
            await voice_channel.connect()

@bot.command(name="leave")
async def vc_leave(ctx):
    msg = ""
    global channel

    if ctx.channel.id == channel:
        voice_channel = ctx.author.voice.channel
        if voice_channel:
            msg = f'Отключаюсь от {voice_channel.name}'
            await ctx.channel.send(   msg   )
            await ctx.voice_client.disconnect()

@bot.command(name="ost")
async def vs_ost(ctx):
    msg = ""
    global channel

    if ctx.channel.id == channel:
        voice_client = discord.utils.get(bot.voice_clients, guild = ctx.guild)
        msg = f'MORTAL COMBAAT'

        await ctx.channel.send(msg)
        # await voice_client.play(discord.FFmpegPCMAudio(executable="./FFmpeg/ffmpeg.exe", source="./mp3/mk.mp3"))
        print(voice_client)
        await voice_client.play(discord.FFmpegPCMAudio(source="./mp3/mk.mp3"))


@bot.command(name="fight")
async def fight(ctx:commands.Context):
    # Первый претендент
    f1 = None
    # Второй претендент
    f2 = bot.user
    # Voice-канал участника
    voice_channel = ctx.author.voice.channel
    
    if voice_channel:
        await vc_join(ctx)
        # Список активных пользователей
        voice_members = voice_channel.members
        # Фильтруем пользователей, оставляя только людей
        voice_members = [m for m in voice_members if m.bot == False]
        
        # Отбираем претендентов
        if len(voice_members) > 1:
            # a,b = [1, 2]   => a = 1    b = 2
            f1, f2 = [voice_members.pop(random.randint(0, len(voice_members))), voice_members.pop(random.randint(0, len(voice_members)))]
        else:
            f1 = ctx.author
        

        # СОЗДАТЬ VS_SCREEN
        # ЗАПУСТИТЬ МУЗЫКУ



        
        
    else: 
        await ctx.channel.send("Durak voidi v voice")





        


"""
    Запуск бота
"""
# bot.run(conf.bot_token)
bot.run(os.environ["BOT_TOKEN"])
