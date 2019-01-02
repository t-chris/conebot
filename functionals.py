from discord.ext.commands import Bot
import asyncio
import discord


BOT_PREFIX = ("!")
TOKEN = "token here"
client = discord.Client()
client = Bot(command_prefix=BOT_PREFIX)


@client.event
async def on_ready():
    print('Big Brother is online.')


#Might be offensive, but that's a given. Add any more you deem inappropriate.
ban_word = ["fuck","shit"]


@client.event
async def on_message(message):
    contents = message.content.split(" ")
    for word in contents:
        if word in ban_word:
                await client.delete_message(message) #Needs permissions to do this.
                await client.send_message(message.channel, 'Don\'t say that please, {0.author.mention} ! (ban word used)'.format(message))


async def conebotrule():
    await client.wait_until_ready()
    hours = 0
    channel = discord.Object(id='528667607495344135')
    while not client.is_closed:

        await client.send_message(channel, 'Conebot has been ruling for: ' + str(hours) + ' hours.')
        hours += 1
        await asyncio.sleep(3600) #every hour


client.loop.create_task(conebotrule())


client.run(TOKEN)
