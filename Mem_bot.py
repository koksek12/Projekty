import discord
from discord.ext import commands
import os, random

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)
memes = ['images/mem1.jpg','images/mem2.jpg','images/mem3.jpg','images/mymem.jpg']
dg_memes = ['images/dg_mem1.jpg','images/dg_mem2.jpg','images/dg_mem3.jpg']

@bot.event
async def on_ready():
    print(f'Zalogowaliśmy się jako {bot.user}')

@bot.command()
async def mem(ctx):
    with open(random.choice(memes), 'rb') as f:
        # Zapiszmy przekonwertowany plik biblioteki Discord w tej zmiennej!
        picture = discord.File(f)
# Możemy następnie wysłać ten plik jako parametr!
    await ctx.send(file=picture)

@bot.command()
async def dog_mem(ctx):
    with open(random.choice(dg_memes), 'rb') as f:
        # Zapiszmy przekonwertowany plik biblioteki Discord w tej zmiennej!
        picture = discord.File(f)
# Możemy następnie wysłać ten plik jako parametr!
    await ctx.send(file=picture)

bot.run("Tu wpisz swój token")
