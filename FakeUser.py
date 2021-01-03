"""
The following code is used to replace every text by a user with a bot.
The warrant for this was when someone changed his username to match that of another user.
The bot was nicknamed to the user's actual name, such that when the bot replaced his texts,
    the texts matched his name instead of his username (i.e. the second user's name).
"""


import discord
import random
from discord.ext import commands

intents = discord.Intents(messages = True, guilds = True, reactions = True, members = True, presences = True)
client = commands.Bot(command_prefix = '.', intents = intents)

@client.event
async def on_ready():
    print('Bot is ready.')

@client.command()
async def ping(ctx):
    await ctx.send(f'Pong! {round(client.latency * 1000)} ms')

@client.event
async def on_message(message):
    ctx = await client.get_context(message)

    #replace user discriminator below as a string
    discriminator = 'USER DISCRIMINATOR'
    message_author = message.author
    #The programonly works for small discord servers in which everyone has a distinct discriminator

    #end the function if the users do not match
    if message_author.discriminator != discriminator:
        return

    #replace the user's message with a message from the bot
    text = message.content
    await ctx.channel.purge(limit = 1)
    await ctx.send(text)

#replace bot discriminator below as a string
client.run('BOT TOKEN')
