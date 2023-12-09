import discord
from discord.ext import commands
from discord import Member
from detect import detect_trash
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='$', intents=intents)
@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Привет! Я бот {bot.user}!')
    await ctx.send(f'Hi! I am a bot {bot.user}!')

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)
@bot.command()
async def kickm(ctx, member_id):
    member_id = int(member_id)
    member: Member = ctx.guild.get_member(member_id)

    await member.kick(reason=f'{ctx.author} Выгнал {member}')
@bot.command()
async def info(ctx):
    await ctx.send ("Префикс: $ Команды: detect - определение мусора по картинке/kickm - кикнуть участника с сервера/about - получить информация о глобальном потеплении")
@bot.command()
async def about(ctx):
    await ctx.send ("Глобальное Потепление - повышение средней температуры климатической системы Земли, происходящее уже больше ста лет, основной причиной чего,по мнению большинства учёных, является антропогенное воздействие.")
@bot.command()
async def detect(ctx):
    if len(ctx.message.attachments) > 0:
        for attachment in ctx.message.attachments:
            file_name = attachment.filename
            file_url = attachment.url
            await attachment.save(f"./images/{file_name}")
            await ctx.send ("Картинка сохранена")
            class_name = detect_trash(f"./images/{file_name}")
            await ctx.send (class_name)
    else:
        await ctx.send("Вы забыли отправить картинку.")
bot.run("MTEwOTM4NjMyMzIyNTIxOTE3Mg.GFq-rr.7oPlWKd9mG7s7majJZSDidn65DlYJns49_2lmI")