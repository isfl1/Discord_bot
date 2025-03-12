import discord
from discord.ext import commands
import random
import os
from dotenv import load_dotenv

# Carregar variáveis do .env
load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")

# Configurar intents do bot
intents = discord.Intents.default()
intents.message_content = True  

bot = commands.Bot(command_prefix="!", intents=intents)  


@bot.event
async def on_ready():
    print(f'✅ Bot conectado com sucesso como: {bot.user}')


@bot.command(name='hello')
async def hello(ctx):
    nome_usuario = ctx.author.name  # Obtém o nome do usuário que digitou o comando
    await ctx.send(f"Olá, {nome_usuario}!")





   


  

bot.run(TOKEN)
