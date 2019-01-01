from discord.ext.commands import Bot
import requests
import random
import asyncio


BOT_PREFIX = ("!")
TOKEN = "NTI4NjY3NzI2NTAwMDY5Mzc2.DwnNJA.DeuZPwepzAoWieMPMLqyrqw8VtA"
client = Bot(command_prefix=BOT_PREFIX)



@client.event
async def on_ready():
    print('FUN IS ONLINE')


client = Bot(command_prefix=BOT_PREFIX)
@client.command(name='8ball',
                description='Unbiased, unexplainable, and perfectly legitimate answers from a robot.',
                brief='It spooks you with unsettling accuracy.\n',
                aliases = ['eight_ball', '8-ball', 'eightball'],
                pass_context=True)
async def eightball(context):
    responses = [
        'That\'s going to be a ho-ho-no from me, ',
        'Hell yeah, ',
        'There is a ' + str(random.randrange(38,72))+'% chance, ',
        'Not likely, ',
        'Like a 50 percent chance, ',
        'Why do you think asking me will change anything? Is this some kind of sick joke to you? This isn\'t even random, it\'s like pseudo-random. Point is, stop asking about your chances and just go for it, '
    ]
    await client.say(random.choice(responses) + context.message.author.mention)


@client.command(name='bitcoin',
                description='No mining at night.',
                brief='Gives you current discord price.\n',
                aliases = ['bit', 'btc']
                )
async def bitcoin():
    url = 'https://api.coindesk.com/v1/bpi/currentprice.json'
    response = requests.get(url)
    value = response.json()['bpi']['USD']['rate']
    await client.say('Bitcoin price: $' + value)


@client.command(name='ping',
                description='What goes around...',
                brief='Newton\'s Third Law.\n',
                pass_context=True)
async def ping(context):
    await client.say('Pong!')


@client.command(name='wave',
                description='Just try it.',
                brief='Really? Just try it.\n',
                pass_context=True)
async def wave(context):
    await client.say(':wave::wave::wave: ' + context.message.author.mention)


@client.command(name='conebot',
                description='Your benevolent (sometimes) creator.',
                brief='Invoke the wrath of the Conical King of Canada.\n',
                pass_context=True)
async def conebot(context):
    await client.say('How :rage: dare :rage: you :rage: taint :rage: my :rage: name :rage: with :rage: your :rage: filthy :rage: mouth. :rage: Conical :rage: frustrums :rage: wish :rage: their :rage: truncated :rage: areas :rage: were :rage: as :rage: beautifully :rage: grafted :rage: as :rage:  mine!')


@client.command(name='dab',
                description='White House-approved dab.',
                brief='Ages 10 and down ONLY.\n',
                pass_context=True)
async def dab(context):
    dab = ['https://media.giphy.com/media/AHN0PfASlNy3S/giphy.gif',
           'https://media.giphy.com/media/l3q2FOeVbpGSqHj4Q/giphy.gif',
           'https://media.giphy.com/media/3oz8xzgGdsIpE8kPBu/giphy.gif',
           'https://media.giphy.com/media/26FPpIxroCqzJzi7K/giphy.gif',
           'https://media.giphy.com/media/viQI4wVoRl38s/giphy.gif',
           'https://media.giphy.com/media/XoVBuF6pwWnM14YuNu/giphy.gif',
           'https://media.giphy.com/media/3ohfFzTZ8DObi2eO4g/giphy.gif',
           'https://media.giphy.com/media/XzyRSldegQhGM/giphy.gif',
           'https://media.giphy.com/media/UiQGTTjmUeqJy/giphy.gif']
    await client.say(random.choices(dab))


@client.command(name = 'remindme',
                description='Reminds you of a message after a given time in minutes.',
                brief='Input message and time, reminds after given time (minutes).',
                pass_context=True)
async def remindme(ctx, delay: float, message):
    delaysecond: float = delay*60
    await asyncio.sleep(delaysecond)
    await client.say(" :alarm_clock:  " + message + "  :alarm_clock: \n" + ctx.message.author.mention)

client.run(TOKEN)