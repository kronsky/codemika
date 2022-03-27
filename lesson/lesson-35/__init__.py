import json
import requests
from dbot import config
import discord
from discord.ext import commands

bot = commands.Bot(command_prefix=config.prefix)


def get_image(title):
    response = requests.get(f'https://some-random-api.ml/img/{title}')
    json_data = json.loads(response.text)

    embed = discord.Embed(color=0xff9900, title=f'Случайная картинка {title}')
    embed.set_image(url=json_data['link'])
    return embed


@bot.command()
async def hello(ctx):
    author = ctx.message.author
    await ctx.send(f'Hello, {author.mention}!')


@bot.command()
async def animal(ctx, title):
    await ctx.send(embed=get_image(title))



bot.run(config.token)
