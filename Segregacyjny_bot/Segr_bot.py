import discord
from discord.ext import commands
import random

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'Zalogowaliśmy się jako {bot.user}')

sposoby = ['Idź na zakupy z własną torbą',
            'Ponownie wykorzystuj opakowania',
            'Kupuj produkty na wagę',
            'Wybieraj długie daty przydatności',
            'Segreguj odpady',
            'Kupuj odzież używaną',
            'Ogranicz ilość zużywanego papieru',
            'Dokładnie planuj zakupy',
            'Zmniejsz ilość plastiku',
            'Regularnie pozbywaj się niepotrzebnych rzeczy']

seg = ['czarny kosz – należy wrzucać odpady zmieszane',
        'brązowy kosz – bio odpady',
        'zielony kosz – szkło',
        'niebieskich kosz – papier',
        'żółty kosz – metal i tworzywa sztuczne']

memy = ["images/mem_sg1.jpg","images/mem_sg2.jpg","images/mem_sg3.jpg"]

@bot.command()
async def komendy(ctx):
    await ctx.send("jak_ograniczyc_ilosc_odpadow_w_domu, segregacja_mem")

@bot.command()
async def jak_ograniczyc_ilosc_odpadow_w_domu(ctx):
    await ctx.send(random.choice(sposoby))

@bot.command()
async def segregacja_mem(ctx):
    with open(random.choice(memy), 'rb') as f:
        # Zapiszmy przekonwertowany plik biblioteki Discord w tej zmiennej!
        picture = discord.File(f)
# Możemy następnie wysłać ten plik jako parametr!
    await ctx.send(file=picture)

@bot.command()
async def segregacja(ctx):
    await ctx.send(seg)

bot.run("Wpisz tu swój token")
