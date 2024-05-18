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
async def beneficios(ctx):
    listeco = (
        "Producción de oxígeno: Los árboles absorben dióxido de carbono y producen oxígeno durante su proceso de respiracion, ayudando a purificar el aire.",
        "Hábitat para la vida silvestre: Los árboles proporcionan refugio y alimento para diversas especies de animales, ayudando a mantener la biodiversidad.",
        "Reducción de la contaminación: Los árboles absorben contaminantes del aire y del suelo, ayudando a mejorar la calidad del aire y del agua.",
        "Control de la erosión del suelo: Las raíces de los árboles ayudan a prevenir la erosión del suelo, protegiendo así contra deslizamientos de tierra y pérdida de suelo fértil.",
        "Sombra y enfriamiento: Los árboles proporcionan sombra en áreas urbanas, reduciendo la temperatura ambiente.",
        "Embellecimiento del entorno: Los árboles añaden belleza y valor estético a los paisajes urbanos y rurales, mejorando la calidad de vida de las personas."
        )
    await ctx.send(random.choice(listeco))

@bot.command()
async def materiales(ctx):
    await ctx.send("Árbol joven: Puedes adquirir un árbol joven en un vivero - Pala: Para cavar el hoyo donde plantarás el árbol. - Tierra y lugar donde plantar el arbol - Abono orgánico: Ayudará a enriquecer la tierra y a nutrir el árbol (completamente opcional). - Agua: Es esencial para el crecimiento inicial del árbol, especialmente durante los primeros meses. - Guantes de jardinería: Para proteger tus manos durante el proceso de plantación. - Estacas y cordeles: Si es necesario para sostener el árbol mientras se establece.")

@bot.command()
async def arboles(ctx):
    await ctx.send("$cerezo - $lulo - $mango - $mora - $durazno - $tomatedearbol")

@bot.command()
async def cerezo(ctx):
    await ctx.send("Se cultiva en zonas con clima templado, siendo su temperatura optima de entre 18 y 28 °C" " https://cdn.wikifarmer.com/wp-content/uploads/2023/02/Informacion-sobre-el-cerezo.jpg")

@bot.command()
async def mango(ctx):
    await ctx.send("Se cultiva en zonas de clima tropical y subtropical, siendo un cultivo perfecto en las zonas cercanas a la linea del Ecuador"" https://www.ica.gov.co/CMSPages/GetFile.aspx?guid=722f5285-edee-4e07-a525-cf8016fe3c09")

@bot.command()
async def mora(ctx):
    await ctx.send("Se cultiva en zonas de clima tropical y soporta los climas mayores 30°C "" https://www.invesa.com/wp-content/uploads/2020/10/Mora3.jpg")

@bot.command()
async def durazno(ctx):
    await ctx.send("Crecen en un rango limitado de climas secos o templados continentales."" https://infonegocios.info/content/images/2022/10/22/344878/conversions/duraznos-py-medium-size.jpg")

@bot.command()
async def lulo(ctx):
    await ctx.send("Este crece bien en climas fríos moderados, en un rango de temperatura que debe oscilar entre 15 y 24 °" "https://cdn.portalfruticola.com/2022/11/media-works-10.png")

@bot.command()
async def tomatedearbol(ctx):
    await ctx.send("Es una planta de climas templados y fríos. Su temperatura está entre los 14 º y 20 ºC, siendo la óptima entre 16º y 19ºC" "https://i0.wp.com/www.elcondorchicago.com/wp-content/uploads/2022/10/Tomate-de-Arbol-Tamarillo.jpg?fit=612%2C402&ssl=1") 

@bot.command()
async def tutorial(ctx):
    embed = discord.Embed(title="Tutorial", description="Un paso a paso de como plantar un arbol", color=0x00ff00)
    embed.add_field(name="Paso 1", value="Hacer un hueco de 30cm de profundidad y 20cm de ancho (al hacer el hueco, se divide la tierra sacada en dos, la parte mas cercana a la superficie [o mas fertil] se separa de parte mas profunda [o menos fertil]), luego, se coloca la tierra mas fertil en el fondo de agujero - ", inline=False)
    embed.add_field(name="Paso 2", value="Se retira con mucho cuidado la planta o vivero del arbol de la bolsa y se coloca en el centro del agujero dejando un espacio minusculo entre el suelo y la raiz", inline=False)
    embed.add_field(name="Paso 3", value="Se procede a recolocar el resto de la tierra [osease la mas profunda o infertil] hasta rellenar el hueco", inline=False)
    embed.add_field(name="Paso 4", value="Se compacta la tierra con los pies o las manos sin dejarla muy compacta ni muy suelta", inline=False)
    embed.add_field(name="Paso 5", value="Hacer una especie de crater [se le conoce como bordo o cajete] al rededor del arbol para mejorar la captacion de agua", inline=True)
    embed.add_field(name="Paso 6", value="Hacer una estaca para ayudar al arbol a crecer completamente recto y atarlo a al arbol", inline=False) 
    embed.set_footer(text="Y obviamente, regar el arbol cada 3 dias")
    await ctx.send(embed=embed)


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
