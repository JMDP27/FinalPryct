import discord
import random
import os
import requests
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

def get_duck_image_url():    
    url = 'https://random-d.uk/api/random'
    res = requests.get(url)
    data = res.json()
    return data['url']


@bot.command('duck')
async def pato(ctx):
    '''Una vez que llamamos al comando duck, 
    el programa llama a la función get_duck_image_url'''
    image_url = get_duck_image_url()
    await ctx.send(image_url)

def imagen_zorro():    
    url = 'https://randomfox.ca/floof/'
    res = requests.get(url)
    data = res.json()
    return data["link"]


@bot.command('')
async def zorro(ctx):
    image_url = imagen_zorro()
    await ctx.send(image_url)


@bot.command()
async def mem(ctx):
    listmeme = (os.listdir('Images'))
    img_name = random.choice(listmeme)
    with open(f"Images/{img_name}", "rb") as f:
        picture = discord.File(f)
    await ctx.send(file=picture)

@bot.command()
async def joined(ctx, member: discord.Member):
    """Says when a member joined."""
    await ctx.send(f'{member.name} joined {discord.utils.format_dt(member.joined_at)}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Hola, soy un bot {bot.user}!')

@bot.command()
async def add(ctx, left: int, right: int):
    """Adds two numbers together."""
    await ctx.send(left + right)

@bot.command()
async def dado(ctx):
   await ctx.send(random.choice([1,2,3,4,5,6]))

@bot.command()
async def music(ctx):
    await ctx.send("https://open.spotify.com/playlist/1p4yCXaf3PxZGikZl3ZKKZ?si=b6ae34d120be44f0")

@bot.command()
async def spam(ctx, times: int, content='repeating...'):
    """Repeats a message multiple times."""
    for i in range(times):
        await ctx.send(content)

@bot.command()
async def moneda(ctx):
    await ctx.send(random.choice(["Cara", "Cruz"]))

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)

bot.run()