import discord as d, os
from discord.ext import commands
import botNuevo as bn
from dotenv import load_dotenv
import comandos as c


load_dotenv()
intents = d.Intents.default()
intents.message_content = True

token = os.getenv("dt")

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    await bn.handle_guess(bot,message)
    await bot.process_commands(message)

@bot.command()
async def hello(ctx):
    await ctx.send(f'Hola, soy un bot {bot.user}!')

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)

@bot.command(name = "Contraseña")
async def passwd(ctx, a:int):
    password = bn.gen_pass(a)
    await ctx.send(f'Su contraseña es: {password}')

@bot.command(name = "meme")
async def memeImg(ctx):
    img = c.memes()
    await ctx.send(file = img)

@bot.command(name = "momos")
async def randImg(ctx):
    img = c.momos()
    await ctx.send(file = img)

@bot.command('pato')
async def duck(ctx):
    '''Una vez que llamamos al comando duck, 
    el programa llama a la función get_duck_image_url'''
    image_url = c.get_duck_image_url()
    await ctx.send(image_url)

#Comando para activar API de img de anime por busqueda con palabra clave
@bot.command(name = "anime")
async def anime(ctx, a):
    query = a
    anime_data = c.get_anime_image(query)
    if anime_data:
        for anime in anime_data:
            
            image_url = anime['attributes']['posterImage']['small']
            await ctx.send(f"Image URL: {image_url}")
    else:
        await ctx.send("No se pudieron obtener datos de anime.")

bot.run(token)
