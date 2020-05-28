import math
import random

import discord
from discord.ext import commands
import sympy

client = commands.AutoShardedBot(command_prefix='hey ', shard_count=1, case_insensetive=True)
client.remove_command('help')

colour_list = [discord.Colour.red(), discord.Colour.green(), discord.Colour.blue()]


@client.event
async def on_ready():
    print('Client open')
    await client.change_presence(status=discord.Status.online,
                                 activity=discord.Game('"hey help me" for help with your maths questions!'))


@client.command()
async def help(message):
    if message.message.content.find("hey help me with your syntax for maths") != -1:
        embed = discord.Embed(
            title='Help',
            description='Commands:',
            colour=0x00C700

        )
        embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/448073494660644884/696272287023890533'
                                '/maths_help_icon-01.png')
        embed.set_author(name=message.author.name, icon_url=message.author.avatar_url)
        embed.add_field(name='For Square root:', value="Format your message as follows: hey maths **sqrt ["
                                                       "number]**.", inline=False)
        embed.add_field(name='For Exponents:', value="Make sure to include a space between your base and your exponent: hey maths **69 ^ 420**", inline=False)

        await message.channel.send(embed=embed)
    else:
        embed = discord.Embed(
            title='Help',
            description='Commands:',
            colour=0x00C700

        )
        embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/448073494660644884/696272287023890533'
                                '/maths_help_icon-01.png')
        embed.set_author(name=message.author.name, icon_url=message.author.avatar_url)
        embed.add_field(name='**hey maths [input]**',
                        value="Attempts to perform mathematical calculations. **Will not do algebra yet.**",
                        inline=False)
        embed.add_field(name='**hey test [input]**', value="Deprecated calculation function. Do not use.", inline=False)
        embed.add_field(name='**hey simplify [input]**', value="SymPy Simplifier for algebra. Variables: X and Y.", inline=False)
        embed.add_field(name='**hey algebra [input]**', value="Currently in testing. Attempts to perform simple "
                                                              "algebra. "
                                                              "Note: all equations by default are equal to 0.",
                        inline=False)
        embed.add_field(name='For more help with **hey maths**:', value="Run the command: **hey help me with your "
                                                                        "syntax for maths**.", inline=False)

        await message.channel.send(embed=embed)


@client.command()
async def test(message):
    await message.channel.send("test")
    vals = message.message.content.split(" ")
    await message.channel.send(vals)
    NumberX = 0
    NumberY = 0
    try:
        NumberX = int(vals[2])
        NumberY = int(vals[4])
    except Exception as e:
        embed = discord.Embed(
            title='Oh no!',
            description='It looks like an error has occured.',
            colour=discord.Colour.red()

        )
        embed.set_thumbnail(url='https://cdn2.iconfinder.com/data/icons/mix-color-5/100/Mix_color_5__info-512.png')
        embed.set_author(name=message.author.name, icon_url=message.author.avatar_url)
        embed.add_field(name='Heres some debug info:', value=e, inline=False)
        await message.channel.send(embed=embed)
    operation = vals[3]
    msg = "Testing 123. Your numbers were: " + str(NumberX) + ' and ' + str(NumberY)
    await message.channel.send(msg)
    await message.channel.send('now lets do some maths')
    if operation == '+':
        answer = NumberX + NumberY
    elif operation == '*':
        answer = NumberX * NumberY
    elif operation == '-':
        answer = NumberX - NumberY
    elif operation == '/':
        answer = NumberX / NumberY
    elif operation == '^':
        answer = pow(NumberX, NumberY)
    elif operation == 'sqrt':
        answer = math.sqrt(NumberX)
    else:
        embed = discord.Embed(
            title='Oh no!',
            description='It looks like an error has occured.',
            colour=discord.Colour.red()

        )
        embed.set_footer(text='Handball Footer')
        embed.set_thumbnail(url='https://cdn2.iconfinder.com/data/icons/mix-color-5/100/Mix_color_5__info-512.png')
        embed.set_author(name=message.author.name, icon_url=message.author.avatar_url)
        embed.add_field(name='Heres some debug info:', value=".", inline=False)
        embed.add_field(name='Input invalid',
                        value="You may have used the incorrect format, or tried to perform an operation that is "
                              "currently unsupported",
                        inline=False)

        await message.channel.send(embed=embed)
    await message.channel.send(answer)


@client.command()
async def maths(message):
    try:
        if message.message.content.find("sqrt") != -1:
            # test
            vals = message.message.content.split(" ")
            NumberX = 0
            try:
                NumberX = int(vals[3])
            except Exception as e:
                embed = discord.Embed(
                    title='Oh no!',
                    description='It looks like an error has occured.',
                    colour=discord.Colour.red()

                )
                embed.set_thumbnail(
                    url='https://cdn2.iconfinder.com/data/icons/mix-color-5/100/Mix_color_5__info-512.png')
                embed.set_author(name=message.author.name, icon_url=message.author.avatar_url)
                embed.add_field(name='Heres some debug info:', value=e, inline=False)
                await message.channel.send(embed=embed)
            operation = vals[2]
            if operation == 'sqrt':
                answer = math.sqrt(NumberX)
            else:
                embed = discord.Embed(
                    title='Oh no!',
                    description='It looks like an error has occured.',
                    colour=discord.Colour.red()

                )
                embed.set_thumbnail(
                    url='https://cdn2.iconfinder.com/data/icons/mix-color-5/100/Mix_color_5__info-512.png')
                embed.set_author(name=message.author.name, icon_url=message.author.avatar_url)
                embed.add_field(name='Heres some debug info:',
                                value="not sqare root, even though you said square root. :/ maybe your trying to "
                                      "square root with the incorrect format",
                                inline=False)
                await message.channel.send(embed=embed)
            # test
            embed = discord.Embed(
                title='Output',
                description=str(answer),
                colour=random.choice(colour_list)

            )
            embed.set_author(name=message.author.name, icon_url=message.author.avatar_url)
            embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/448073494660644884/696278817798357002'
                                    '/square_root_icon-01.png')
            await message.channel.send(embed=embed)
        elif message.message.content.find("^") != -1:
            # test
            vals = message.message.content.split(" ")
            NumberX = 0
            NumberY = 0
            try:
                NumberX = int(vals[2])
                NumberY = int(vals[4])
            except Exception as e:
                embed = discord.Embed(
                    title='Oh no!',
                    description='It looks like an error has occured.',
                    colour=discord.Colour.red()

                )
                embed.set_thumbnail(
                    url='https://cdn2.iconfinder.com/data/icons/mix-color-5/100/Mix_color_5__info-512.png')
                embed.set_author(name=message.author.name, icon_url=message.author.avatar_url)
                embed.add_field(name='Heres some debug info:', value=e, inline=False)
                await message.channel.send(embed=embed)
            operation = vals[3]
            if operation == '^':
                # answer = pow(NumberX, NumberY)
                answer = NumberX ** NumberY
            else:
                embed = discord.Embed(
                    title='Oh no!',
                    description='It looks like an error has occured.',
                    colour=discord.Colour.red()

                )
                embed.set_thumbnail(
                    url='https://cdn2.iconfinder.com/data/icons/mix-color-5/100/Mix_color_5__info-512.png')
                embed.set_author(name=message.author.name, icon_url=message.author.avatar_url)
                embed.add_field(name='Heres some debug info:',
                                value="whoops. :/ looks like your using more than 2 terms.", inline=False)
                await message.channel.send(embed=embed)
            # test
            embed = discord.Embed(
                title='Output',
                description=str(answer),
                colour=random.choice(colour_list)

            )
            embed.set_author(name=message.author.name, icon_url=message.author.avatar_url)
            await message.channel.send(embed=embed)
        else:
            embed = discord.Embed(
                title='Output',
                description='The answer is: ' + str(eval(message.message.content[9:])),
                colour=random.choice(colour_list)

            )
            embed.set_author(name=message.author.name, icon_url=message.author.avatar_url)
            await message.channel.send(embed=embed)
    except NameError as e:
        embed = discord.Embed(
            title='Oh no!',
            description='It looks like an error has occured.',
            colour=discord.Colour.red()

        )
        embed.set_author(name=message.author.name, icon_url=message.author.avatar_url)
        embed.set_thumbnail(url='https://cdn2.iconfinder.com/data/icons/mix-color-5/100/Mix_color_5__info-512.png')
        embed.add_field(name='Heres some debug info:',
                        value="NameError. Can not do maths with pronumerals, variables or words yet. :/", inline=False)
        embed.add_field(name='Further info:', value=e, inline=False)

        await message.channel.send(embed=embed)
    except SyntaxError as e:
        embed = discord.Embed(
            title='Oh no!',
            description='It looks like an error has occured.',
            colour=discord.Colour.red()

        )
        embed.set_author(name=message.author.name, icon_url=message.author.avatar_url)
        embed.set_thumbnail(url='https://cdn2.iconfinder.com/data/icons/mix-color-5/100/Mix_color_5__info-512.png')
        embed.add_field(name='Heres some debug info:',
                        value="NameError. Can not do maths with pronumerals, variables or words yet. :/", inline=False)
        embed.add_field(name='Further info:', value=e, inline=False)

        await message.channel.send(embed=embed)
    except Exception as e:
        embed = discord.Embed(
            title='Oh no!',
            description='It looks like an error has occured.',
            colour=discord.Colour.red()

        )
        embed.set_author(name=message.author.name, icon_url=message.author.avatar_url)
        embed.set_thumbnail(url='https://cdn2.iconfinder.com/data/icons/mix-color-5/100/Mix_color_5__info-512.png')
        embed.add_field(name='Heres some debug info:', value=e, inline=False)

        await message.channel.send(embed=embed)


@client.command()
async def simplify(message):
    try:
        embed = discord.Embed(
            title='Output',
            description='The answer is: ' + str(sympy.simplify(message.message.content[13:])),
            colour=random.choice(colour_list)

        )
        embed.set_author(name=message.author.name, icon_url=message.author.avatar_url)
        await message.channel.send(embed=embed)
    except Exception as e:
        embed = discord.Embed(
            title='Oh no!',
            description='It looks like an error has occured.',
            colour=discord.Colour.red()

        )
        embed.set_author(name=message.author.name, icon_url=message.author.avatar_url)
        embed.set_thumbnail(url='https://cdn2.iconfinder.com/data/icons/mix-color-5/100/Mix_color_5__info-512.png')
        embed.add_field(name='Heres some debug info:', value=e, inline=False)

        await message.channel.send(embed=embed)

client.run('token')
