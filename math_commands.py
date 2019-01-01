from discord.ext.commands import Bot
import math

BOT_PREFIX = ("!")
TOKEN = "NTI4NjY3NzI2NTAwMDY5Mzc2.DwnNJA.DeuZPwepzAoWieMPMLqyrqw8VtA"
client = Bot(command_prefix=BOT_PREFIX)


#file running
@client.event
async def on_ready():
    print('Boring math is online...')


@client.command(name='add',
                description='Can add or subtract 2 integers. Negatives can be put on either.',
                brief='Adds/subtracts 2 integers, use negative sign to subtract.\n'
                )
async def add(a: int, b: int):
    c: int = a + b
    await client.say(c)


@client.command(name='multiply',
                description='Can multiply two integers.',
                brief='Multiplies 2 integers.\n'
                )
async def multiply(a: float, b: float):
    c: float = a*b
    await client.say(c)


@client.command(name='divide',
                description='Can divide two integers.',
                brief='Divides 2 integers.\n'
                )
async def divide(a: float, b: float):
    c: float = a/b
    await client.say(c)


@client.command(name='round',
                description='Rounds an integer to a set number of decimal places.',
                brief='Rounds to set number of decimal places.\n'
                )
async def round(a: float, roundNum: int):
    await client.say(round(a, roundNum))


@client.command(name='circlearea',
                description='Gives area of circle, given radius.',
                brief='Input radius, gives area.\n',
                )
async def circleArea(radius: float):
    await client.say((radius**2)*(math.pi))


@client.command(name='circlecircum',
                description='Gives circumference of circle, given radius.',
                brief='Input radius, gives circumference.\n',
                )
async def circleCircum(radius: float):
    await client.say(2 * radius * math.pi)

client.run(TOKEN)