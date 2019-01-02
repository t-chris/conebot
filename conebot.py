import discord
import random
from discord import Game


client = discord.Client()


#file is running
@client.event
async def on_ready():
    print('Logged in as ' + (client.user.name))
    print(client.user.id)
    print('---------')
    await client.change_presence(game=Game(name="with human subjects."))



# basic commands!
@client.event
async def on_message(message):
    #don't reply to yourself
    if message.author == client.user:
        return
    if message.content.startswith('!hello'):
        msg = 'Hello {0.author.mention}'.format(message)
        await client.send_message(message.channel, msg)
    elif message.content.startswith('!christmas') or message.content.startswith('!merry'):
        msg = 'MERRY CHRISTMAS, {0.author.mention}!'.format(message)
        await client.send_message(message.channel, msg)
    elif message.content.startswith('!flip'):
        msg=random.choice(['Heads, you win, {0.author.mention}'.format(message), 'Tails, you lose, {0.author.mention}'.format(message)])
        await client.send_message(message.channel, msg)




client.run('token here')
