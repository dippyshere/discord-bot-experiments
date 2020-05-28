import datetime

import asyncio
import discord
from discord.ext import commands
import time

client = commands.AutoShardedBot(command_prefix='hey ', shard_count=1, case_insensetive=True)
client.remove_command('help')

weekDays = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
datetime.datetime.today()

Human = {
    "Monday": {
        "BS": "_ _",
        "P1": "Class",
        "P2": "Class",
        "P3": "Class",
        "P4": "Class",
        "P5": "Class",
        "AS": "_ _"
    },
    "Tuesday": {
        "BS": "_ _",
        "P1": "Class",
        "P2": "Class",
        "P3": "Class",
        "P4": "Class",
        "P5": "Class",
        "AS": "_ _"
    },
    "Wednesday": {
        "BS": "_ _",
        "P1": "Class",
        "P2": "Class",
        "P3": "Class",
        "P4": "Class",
        "P5": "Class",
        "AS": "_ _"
    },
    "Thursday": {
        "BS": "_ _",
        "P1": "Class",
        "P2": "Class",
        "P3": "Class",
        "AS": "Sport"
    },
    "Friday": {
        "BS": "_ _",
        "P1": "Class",
        "P2": "Class",
        "P3": "Class",
        "P4": "Class",
        "P5": "Class",
        "AS": "_ _"
    }
}

AlexA = {
    "Monday": {
        "BS": "_ _",
        "P1": "Science",
        "P2": "Science",
        "P3": "IST",
        "P4": "IST",
        "P5": "Commerce",
        "AS": "_ _"
    },
    "Tuesday": {
        "BS": "_ _",
        "P1": "D&T",
        "P2": "Science",
        "P3": "Maths",
        "P4": "History",
        "P5": "Commerce",
        "AS": "_ _"
    },
    "Wednesday": {
        "BS": "_ _",
        "P1": "Commerce",
        "P2": "D&T",
        "P3": "Science",
        "P4": "English",
        "P5": "IST",
        "AS": "_ _"
    },
    "Thursday": {
        "BS": "_ _",
        "P1": "Geography",
        "P2": "English",
        "P3": "PDHPE",
        "AS": "Sport"
    },
    "Friday": {
        "BS": "_ _",
        "P1": "Maths",
        "P2": "Geography",
        "P3": "PDHPE",
        "P4": "History",
        "P5": "English",
        "AS": "_ _"
    }
}

AlexB = {
    "Monday": {
        "BS": "_ _",
        "P1": "Commerce",
        "P2": "English",
        "P3": "D&T",
        "P4": "Maths",
        "P5": "PDHPE",
        "AS": "_ _"
    },
    "Tuesday": {
        "BS": "_ _",
        "P1": "Science",
        "P2": "Maths",
        "P3": "IST",
        "P4": "History",
        "P5": "D&T",
        "AS": "_ _"
    },
    "Wednesday": {
        "BS": "_ _",
        "P1": "Commerce",
        "P2": "IST",
        "P3": "Careers",
        "P4": "PDHPE",
        "P5": "Geography",
        "AS": "_ _"
    },
    "Thursday": {
        "BS": "_ _",
        "P1": "Maths",
        "P2": "English",
        "P3": "Geography",
        "AS": "Sport"
    },
    "Friday": {
        "BS": "_ _",
        "P1": "Maths",
        "P2": "Science",
        "P3": "History",
        "P4": "D&T",
        "P5": "English",
        "AS": "_ _"
    }
}

AhouraA = {
    "Monday": {
        "BS": "_ _",
        "P1": "Science",
        "P2": "Science",
        "P3": "Commerce",
        "P4": "Commerce",
        "P5": "Japanese",
        "AS": "_ _"
    },
    "Tuesday": {
        "BS": "_ _",
        "P1": "IST",
        "P2": "Science",
        "P3": "Maths",
        "P4": "History",
        "P5": "Japanese",
        "AS": "_ _"
    },
    "Wednesday": {
        "BS": "_ _",
        "P1": "Japanese",
        "P2": "IST",
        "P3": "Science",
        "P4": "English",
        "P5": "Commerce",
        "AS": "_ _"
    },
    "Thursday": {
        "BS": "_ _",
        "P1": "PDHPE",
        "P2": "English",
        "P3": "History",
        "AS": "Sport"
    },
    "Friday": {
        "BS": "_ _",
        "P1": "Maths",
        "P2": "Geography",
        "P3": "PDHPE",
        "P4": "History",
        "P5": "English",
        "AS": "_ _"
    }
}

AhouraB = {
    "Monday": {
        "BS": "_ _",
        "P1": "Japanese",
        "P2": "English",
        "P3": "IST",
        "P4": "Maths",
        "P5": "Science",
        "AS": "_ _"
    },
    "Tuesday": {
        "BS": "_ _",
        "P1": "Geography",
        "P2": "Maths",
        "P3": "Commerce",
        "P4": "History",
        "P5": "IST",
        "AS": "_ _"
    },
    "Wednesday": {
        "BS": "_ _",
        "P1": "Japanese",
        "P2": "Commerce",
        "P3": "Geography",
        "P4": "Science",
        "P5": "Careers",
        "AS": "_ _"
    },
    "Thursday": {
        "BS": "_ _",
        "P1": "Maths",
        "P2": "English",
        "P3": "PDHPE",
        "AS": "Sport"
    },
    "Friday": {
        "BS": "_ _",
        "P1": "Maths",
        "P2": "PDHPE",
        "P3": "Geography",
        "P4": "IST",
        "P5": "English",
        "AS": "_ _"
    }
}

JeanA = {
    "Monday": {
        "BS": "_ _",
        "P1": "Science",
        "P2": "Science",
        "P3": "IST",
        "P4": "IST",
        "P5": "Commerce",
        "AS": "_ _"
    },
    "Tuesday": {
        "BS": "_ _",
        "P1": "INTE",
        "P2": "Science",
        "P3": "Maths",
        "P4": "History",
        "P5": "Commerce",
        "AS": "_ _"
    },
    "Wednesday": {
        "BS": "_ _",
        "P1": "Commerce",
        "P2": "INTE",
        "P3": "Science",
        "P4": "English",
        "P5": "IST",
        "AS": "_ _"
    },
    "Thursday": {
        "BS": "_ _",
        "P1": "Geography",
        "P2": "English",
        "P3": "PDHPE",
        "AS": "Sport"
    },
    "Friday": {
        "BS": "_ _",
        "P1": "Maths",
        "P2": "Geography",
        "P3": "PDHPE",
        "P4": "History",
        "P5": "English",
        "AS": "_ _"
    }
}

JeanB = {
    "Monday": {
        "BS": "_ _",
        "P1": "Commerce",
        "P2": "English",
        "P3": "D&T",
        "P4": "Maths",
        "P5": "PDHPE",
        "AS": "_ _"
    },
    "Tuesday": {
        "BS": "_ _",
        "P1": "Science",
        "P2": "Maths",
        "P3": "IST",
        "P4": "History",
        "P5": "INTE",
        "AS": "_ _"
    },
    "Wednesday": {
        "BS": "_ _",
        "P1": "Commerce",
        "P2": "IST",
        "P3": "Careers",
        "P4": "PDHPE",
        "P5": "Geography",
        "AS": "_ _"
    },
    "Thursday": {
        "BS": "_ _",
        "P1": "Maths",
        "P2": "English",
        "P3": "Geography",
        "AS": "Sport"
    },
    "Friday": {
        "BS": "_ _",
        "P1": "Maths",
        "P2": "Science",
        "P3": "History",
        "P4": "INTE",
        "P5": "English",
        "AS": "_ _"
    }
}

periods = {
    "Monday": ["BS", "P1", "P2", "P3", "P4", "P5", "AS"],
    "Tuesday": ["BS", "P1", "P2", "P3", "P4", "P5", "AS"],
    "Wednesday": ["BS", "P1", "P2", "P3", "P4", "P5", "AS"],
    "Thursday": ["BS", "P1", "P2", "P3", "AS"],
    "Friday": ["BS", "P1", "P2", "P3", "P4", "P5", "AS"]
}

# strings and values
week_current = 'B'
week_number = '4'
bs_time = 'Before School (7:50-8:50)'
p1_time = 'Period 1 (9:00-10:05)'
p2_time = 'Period 2 (10:05-11:05)'
p3_time = 'Period 3 (11:25-12:25)'
p4_time = 'Period 4 (12:30-1:30)'
p5_time = 'Period 5 (2:10-3:10)'
as_time = 'After School (3:10-4:10)'
p1mon_time = 'Period 1 (9:00-9:55)'
p2mon_time = 'Period 2 (9:55-10:50)'
p3mon_time = 'Period 3 (11:30-12:30)'
p1thur_time = 'Period 1 (9:00-9:50)'
p2thur_time = 'Period 2 (9:50-10:45)'
p3thur_time = 'Period 3 (11:00-11:50)'
asthur_time = 'Sport (12:30-2:30)'
bs_check = False
rc_check = False
rlc_check = False
p1_check = False
p2_check = False
p3_check = False
p4_check = False
p5_check = False
as_check = False
lunch_check = False


def dayofweek(plus='0'):
    if plus == '0':
        value = datetime.datetime.today().weekday()
        day = weekDays[value]
        return day
    else:
        return plus


def is_time_between(begin_time, end_time, check_time=None):
    # If check time is not given, default to current UTC time
    check_time = check_time or datetime.datetime.now().time()
    if begin_time < end_time:
        return begin_time <= check_time <= end_time
    else:  # crosses midnight
        return check_time >= begin_time or check_time <= end_time


def current_period():
    if dayofweek() == 'Monday':
        if is_time_between(datetime.time(15, 10), datetime.time(16, 10)):
            return 'AS'
        if is_time_between(datetime.time(14, 10), datetime.time(15, 10)):
            return 'P5'
        if is_time_between(datetime.time(13, 30), datetime.time(14, 10)):
            return 'Lunch'
        if is_time_between(datetime.time(12, 30), datetime.time(13, 30)):
            return 'P4'
        if is_time_between(datetime.time(11, 30), datetime.time(12, 30)):
            return 'P3'
        if is_time_between(datetime.time(10, 50), datetime.time(11, 30)):
            return 'Assembly'
        if is_time_between(datetime.time(9, 55), datetime.time(10, 50)):
            return 'P2'
        if is_time_between(datetime.time(9, 0), datetime.time(9, 55)):
            return 'P1'
        if is_time_between(datetime.time(8, 50), datetime.time(9, 0)):
            return 'Roll Call'
        if is_time_between(datetime.time(7, 50), datetime.time(8, 50)):
            return 'BS'
        else:
            return 'Nothing'
    elif dayofweek() == 'Thursday':
        if is_time_between(datetime.time(12, 30), datetime.time(14, 30)):
            return 'AS'
        if is_time_between(datetime.time(11, 50), datetime.time(12, 30)):
            return 'Lunch'
        if is_time_between(datetime.time(11, 0), datetime.time(11, 50)):
            return 'P3'
        if is_time_between(datetime.time(10, 45), datetime.time(11, 0)):
            return 'Recess'
        if is_time_between(datetime.time(9, 50), datetime.time(10, 45)):
            return 'P2'
        if is_time_between(datetime.time(9, 0), datetime.time(9, 50)):
            return 'P1'
        if is_time_between(datetime.time(8, 50), datetime.time(9, 0)):
            return 'Roll Call'
        if is_time_between(datetime.time(7, 50), datetime.time(8, 50)):
            return 'BS'
        else:
            return 'Nothing'
    elif dayofweek() == 'Tuesday' or dayofweek() == 'Wednesday' or dayofweek() == 'Friday':
        if is_time_between(datetime.time(15, 10), datetime.time(16, 10)):
            return 'AS'
        if is_time_between(datetime.time(14, 10), datetime.time(15, 10)):
            return 'P5'
        if is_time_between(datetime.time(13, 30), datetime.time(14, 10)):
            return 'Lunch'
        if is_time_between(datetime.time(12, 30), datetime.time(13, 30)):
            return 'P4'
        if is_time_between(datetime.time(11, 25), datetime.time(12, 30)):
            return 'P3'
        if is_time_between(datetime.time(11, 5), datetime.time(11, 25)):
            return 'Recess'
        if is_time_between(datetime.time(10, 5), datetime.time(11, 5)):
            return 'P2'
        if is_time_between(datetime.time(9, 0), datetime.time(10, 5)):
            return 'P1'
        if is_time_between(datetime.time(8, 50), datetime.time(9, 0)):
            return 'Roll Call'
        if is_time_between(datetime.time(7, 50), datetime.time(8, 50)):
            return 'BS'
        else:
            return 'Nothing'
    else:
        return 'Nothing'


@client.event
async def on_ready():
    print('Client open')
    await client.change_presence(activity=discord.Game("I'm not bloody done yet."), status=discord.Status.idle, afk=False)

@client.command()
async def help(message):
    embed = discord.Embed(
        title='Help',
        description='Commands:',
        colour=discord.Colour.red()

    )
    embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/448073494660644884/710796488929837086/help2.png')
    embed.set_author(name=message.author.name, icon_url=message.author.avatar_url)
    embed.add_field(name='timetable', value="Sends you your timetable if configured.", inline=False)
    embed.add_field(name='timetable [day, week a / b, person] OR [person, day, week a / b]', value="Add arguments to "
                                                                                                   "your message to "
                                                                                                   "request other "
                                                                                                   "info.\ne.g. ``hey "
                                                                                                   "timetable monday "
                                                                                                   "a alex`` "
                                                                                                   "will fetch you "
                                                                                                   "Alex's timetable "
                                                                                                   "for Monday on "
                                                                                                   "week A.\n**case "
                                                                                                   "insensitive**",
                    inline=False)
    embed.add_field(name='week', value="Sends the current week (a or b).", inline=False)
    embed.add_field(name='next', value="Sends you what your next period is, then the period after that.", inline=False)
    embed.add_field(name='emoji', value="Sends an animated emoji (Looser lounge only).", inline=False)
    embed.add_field(name='rn', value="Sends which period we are currently in.", inline=False)
    embed.add_field(name='what do i have', value="If you have not been migrated to the new command, you can give this "
                                                 "one a go.\nIf you have no idea what **The looser lounge** is, "
                                                 "you wont be on this.", inline=False)

    await message.channel.send(embed=embed)


@client.command()
async def timetable(message, arg_day=dayofweek(), arg_week=week_current, arg_person='none'):
    classes = ''
    tt_week = arg_week.capitalize()
    alex_args = ['alex', 'alexander', '349076896266452994', '<@!349076896266452994>', 'areks']
    ahoura_args = ['298042908513271818', '<@!298042908513271818>', 'ahoura', 'ahouts', 'shaft', 'shafahi', 'ahor',
                   'ahour', 'im_skinny']
    jean_args = ['jean', 'jean du', 'jane', 'jen', '<@!237465974545055744>', '237465974545055744', 'gene', '368682763093671936', '<@!368682763093671936>']
    jayden_args = ['jayden', 'god', 'jay', 'user id', '<@!user id>', 'jaydon']
    if arg_person == 'none':
        arg_person = str(message.author.id)
    if arg_day.capitalize() == 'Saturday' or arg_day.capitalize() == 'Sunday':
        if arg_week == 'A':
            tt_week = 'B'
        elif arg_week == 'B':
            tt_week = 'A'
    embed = discord.Embed(
        title='Here is your timetable',
        url='https://www.reddit.com/r/YouFellForItFool/comments/cjlngm/you_fell_for_it_fool/',
        description="_ _",
        colour=discord.Colour.green()
    )
    embed.set_footer(text=f"This is "
                          f"{dayofweek(arg_day.lower().capitalize())}'s timetable for week {tt_week.capitalize()}."
                          f"\nRequested by: {message.author.name} • "
                          f"{time.strftime('%H:%M')} {datetime.date.today().strftime('%d/%m/%Y')}"
                     , icon_url=message.author.avatar_url)
    if arg_person.lower() in alex_args:
        embed.set_author(name="Alex", icon_url='https://cdn.discordapp.com/avatars/349076896266452994'
                                               '/c627d15be04a30880314240305bb2202.png')
        if arg_day.capitalize() == 'Thursday':
            embed.add_field(name='Period (Time)',
                            value=f"{bs_time}\n{p1thur_time}\n{p2thur_time}\n{p3thur_time}\n{asthur_time}",
                            inline=True)
        elif arg_day.capitalize() == 'Monday':
            embed.add_field(name='Period (Time)',
                            value=f"{bs_time}\n{p1mon_time}\n{p2mon_time}\n{p3mon_time}\n{p4_time}\n{p5_time}\n{as_time}",
                            inline=True)
        else:
            embed.add_field(name='Period (Time)',
                            value=f"{bs_time}\n{p1_time}\n{p2_time}\n{p3_time}\n{p4_time}\n{p5_time}\n{as_time}",
                            inline=True)
        if arg_week.capitalize() == 'A':
            if arg_day.capitalize() == 'Saturday' or arg_day.capitalize() == 'Sunday':
                for prd in periods.get("Monday"):
                    classes = classes + f'{AlexB.get("Monday").get(prd)}\n'
            else:
                for prd in periods.get(arg_day.capitalize()):
                    classes = classes + f'{AlexA.get(arg_day.capitalize()).get(prd)}\n'
        elif arg_week.capitalize() == 'B':
            if arg_day.capitalize() == 'Saturday' or arg_day.capitalize() == 'Sunday':
                for prd in periods.get("Monday"):
                    classes = classes + f'{AlexA.get("Monday").get(prd)}\n'
            else:
                for prd in periods.get(arg_day.capitalize()):
                    classes = classes + f'{AlexB.get(arg_day.capitalize()).get(prd)}\n'
    elif arg_person.lower() in ahoura_args:
        embed.set_author(name="Ahoura",
                         icon_url='https://cdn.discordapp.com/avatars/298042908513271818/4253d4af1535177c8991498a5fb81828.png')
        if arg_day.capitalize() == 'Thursday':
            embed.add_field(name='Period (Time)',
                            value=f"{bs_time}\n{p1thur_time}\n{p2thur_time}\n{p3thur_time}\n{asthur_time}",
                            inline=True)
        elif arg_day.capitalize() == 'Monday':
            embed.add_field(name='Period (Time)',
                            value=f"{bs_time}\n{p1mon_time}\n{p2mon_time}\n{p3mon_time}\n{p4_time}\n{p5_time}\n{as_time}",
                            inline=True)
        else:
            embed.add_field(name='Period (Time)',
                            value=f"{bs_time}\n{p1_time}\n{p2_time}\n{p3_time}\n{p4_time}\n{p5_time}\n{as_time}",
                            inline=True)
        if arg_week.capitalize() == 'A':
            if arg_day.capitalize() == 'Saturday' or arg_day.capitalize() == 'Sunday':
                for prd in periods.get("Monday"):
                    classes = classes + f'{AhouraB.get("Monday").get(prd)}\n'
            else:
                for prd in periods.get(arg_day.capitalize()):
                    classes = classes + f'{AhouraA.get(arg_day.capitalize()).get(prd)}\n'
        elif arg_week.capitalize() == 'B':
            if arg_day.capitalize() == 'Saturday' or arg_day.capitalize() == 'Sunday':
                for prd in periods.get("Monday"):
                    classes = classes + f'{AhouraA.get("Monday").get(prd)}\n'
            else:
                for prd in periods.get(arg_day.capitalize()):
                    classes = classes + f'{AhouraB.get(arg_day.capitalize()).get(prd)}\n'
    elif arg_person.lower() in jean_args:
        embed.set_author(name="Jean", icon_url='https://cdn.discordapp.com/avatars/237465974545055744/097d92443bcf0a40b85795c2b783238c.png')
        if arg_day.capitalize() == 'Thursday':
            embed.add_field(name='Period (Time)',
                            value=f"{bs_time}\n{p1thur_time}\n{p2thur_time}\n{p3thur_time}\n{asthur_time}",
                            inline=True)
        elif arg_day.capitalize() == 'Monday':
            embed.add_field(name='Period (Time)',
                            value=f"{bs_time}\n{p1mon_time}\n{p2mon_time}\n{p3mon_time}\n{p4_time}\n{p5_time}\n{as_time}",
                            inline=True)
        else:
            embed.add_field(name='Period (Time)',
                            value=f"{bs_time}\n{p1_time}\n{p2_time}\n{p3_time}\n{p4_time}\n{p5_time}\n{as_time}",
                            inline=True)
        if arg_week.capitalize() == 'A':
            if arg_day.capitalize() == 'Saturday' or arg_day.capitalize() == 'Sunday':
                for prd in periods.get("Monday"):
                    classes = classes + f'{JeanB.get("Monday").get(prd)}\n'
            else:
                for prd in periods.get(arg_day.capitalize()):
                    classes = classes + f'{JeanA.get(arg_day.capitalize()).get(prd)}\n'
        elif arg_week.capitalize() == 'B':
            if arg_day.capitalize() == 'Saturday' or arg_day.capitalize() == 'Sunday':
                for prd in periods.get("Monday"):
                    classes = classes + f'{JeanA.get("Monday").get(prd)}\n'
            else:
                for prd in periods.get(arg_day.capitalize()):
                    classes = classes + f'{JeanB.get(arg_day.capitalize()).get(prd)}\n'
    elif arg_person.lower() in jayden_args:
        embed.set_author(name="Jean", icon_url='')
        if arg_day.capitalize() == 'Thursday':
            embed.add_field(name='Period (Time)',
                            value=f"{bs_time}\n{p1thur_time}\n{p2thur_time}\n{p3thur_time}\n{asthur_time}",
                            inline=True)
        elif arg_day.capitalize() == 'Monday':
            embed.add_field(name='Period (Time)',
                            value=f"{bs_time}\n{p1mon_time}\n{p2mon_time}\n{p3mon_time}\n{p4_time}\n{p5_time}\n{as_time}",
                            inline=True)
        else:
            embed.add_field(name='Period (Time)',
                            value=f"{bs_time}\n{p1_time}\n{p2_time}\n{p3_time}\n{p4_time}\n{p5_time}\n{as_time}",
                            inline=True)
        if arg_week.capitalize() == 'A':
            if arg_day.capitalize() == 'Saturday' or arg_day.capitalize() == 'Sunday':
                for prd in periods.get("Monday"):
                    classes = classes + f'{JeanB.get("Monday").get(prd)}\n'
            else:
                for prd in periods.get(arg_day.capitalize()):
                    classes = classes + f'{JeanA.get(arg_day.capitalize()).get(prd)}\n'
        elif arg_week.capitalize() == 'B':
            if arg_day.capitalize() == 'Saturday' or arg_day.capitalize() == 'Sunday':
                for prd in periods.get("Monday"):
                    classes = classes + f'{JeanA.get("Monday").get(prd)}\n'
            else:
                for prd in periods.get(arg_day.capitalize()):
                    classes = classes + f'{JeanB.get(arg_day.capitalize()).get(prd)}\n'
    if classes != '':
        embed.add_field(name='Class', value=classes)
    await message.channel.send(embed=embed)


@client.command()
async def week(message):
    embed = discord.Embed(
        title='What week is it?',
        description=f'It is currently week {week_current}.\nIt is also week {week_number}.',
        colour=discord.Colour.blue()

    )
    embed.set_footer(text=f"Requested by: {message.author.name} • "
                          f"{time.strftime('%H:%M')} {datetime.date.today().strftime('%d/%m/%Y')}"
                     , icon_url=message.author.avatar_url)

    await message.channel.send(embed=embed)


@client.command()
async def emoji(message):
    await message.channel.send(f'<a:god:424520269315440650>')
    await message.channel.send(f'<a:hyperblob:424526491699904522 to save your eyes')
    await message.channel.send(f'<a:toung:424526490512785408>')
    await message.channel.send(f'<a:crying:603902355540541440>')


@client.command()
async def rn(message):
    user_class = ''
    if week_current == 'A':
        if message.author.id == 349076896266452994:
            if current_period() == "Lunch" or current_period() == "Assembly" or current_period() == "Roll Call" or current_period() == "Recess" or current_period() == "Nothing":
                user_class = current_period()
            else:
                user_class = AlexA.get(week_current.capitalize()).get(current_period())
        if message.author.id == 298042908513271818:
            if current_period() == "Lunch" or current_period() == "Assembly" or current_period() == "Roll Call" or current_period() == "Recess" or current_period() == "Nothing":
                user_class = current_period()
            else:
                user_class = AhouraA.get(week_current.capitalize()).get(current_period())
    elif week_current == 'B':
        if message.author.id == 349076896266452994:
            if current_period() == "Lunch" or current_period() == "Assembly" or current_period() == "Roll Call" or current_period() == "Recess" or current_period() == "Nothing":
                user_class = current_period()
            else:
                user_class = AlexB.get(dayofweek().capitalize()).get(current_period())
        if message.author.id == 298042908513271818:
            if current_period() == "Lunch" or current_period() == "Assembly" or current_period() == "Roll Call" or current_period() == "Recess" or current_period() == "Nothing":
                user_class = current_period()
            else:
                user_class = AhouraB.get(dayofweek().capitalize()).get(current_period())
    embed = discord.Embed(
        title='What period is it right now?',
        description=f'The current period is: {user_class}',
        colour=discord.Colour.blue()

    )
    embed.set_footer(text=f"Requested by: {message.author.name} • "
                          f"{time.strftime('%H:%M')} {datetime.date.today().strftime('%d/%m/%Y')}"
                     , icon_url=message.author.avatar_url)
    await message.channel.send(embed=embed)


@client.command()
async def next(message):
    next_subject = []
    if dayofweek() != 'Saturday' or dayofweek() != 'Sunday':
        for prd in periods.get(dayofweek().capitalize()):
            print(next_subject)
            print(AlexA.get(dayofweek().capitalize()).get(prd))
            next_subject.append(AlexA.get(dayofweek().capitalize()).get(prd))
        print(next_subject)
    if next_subject[0] == '_ _':
        next_subject.pop(0)
    if next_subject[-1] == '_ _':
        next_subject.pop(-1)
    print(next_subject)
    embed = discord.Embed(
        title='What is my next subject?',
        description=f'Your next subject is: {next_subject[0]}',
        colour=discord.Colour.blue()

    )
    embed.set_footer(text=f"Requested by: {message.author.name} • "
                          f"{time.strftime('%H:%M')} {datetime.date.today().strftime('%d/%m/%Y')}"
                     , icon_url=message.author.avatar_url)
    embed.add_field(name='Then you have', value=str(next_subject[1]))
    await message.channel.send(embed=embed)


async def next_period():
    global bs_check
    global rc_check
    global rlc_check
    global p1_check
    global p2_check
    global p3_check
    global p4_check
    global p5_check
    global as_check
    global rc_check
    global lunch_check
    await client.wait_until_ready()
    channel = client.get_channel(448073494660644884)
    while True:
        if time.strftime('%H:%M') == '7:50' and bs_check is False:
            await channel.send('Hey guys, Before School classes have started now.')
            bs_check = True
        if time.strftime('%H:%M') == '8:50' and rlc_check is False:
            await channel.send('Hey guys, Roll call starts now.')
            rlc_check = True
        if time.strftime('%H:%M') == '9:00' and p1_check is False:
            await channel.send('Hey guys, Period 1 has started.')
            p1_check = True
        if time.strftime('%H:%M') == '10:05' and p2_check is False:
            await channel.send('Hey guys, Period 2 has started.')
            p2_check = True
        if time.strftime('%H:%M') == '11:05' and rc_check is False:
            await channel.send("Hey guys, it's recess now.")
            rc_check = True
        if time.strftime('%H:%M') == '11:25' and p3_check is False:
            await channel.send('Hey guys, Period 3 has started.')
            p3_check = True
        if time.strftime('%H:%M') == '12:34' and p4_check is False:
            await channel.send('Hey guys, Period 4 has started.')
            p4_check = True
        if time.strftime('%H:%M') == '13:30' and lunch_check is False:
            await channel.send("Hey guys, it's lunch now.")
            lunch_check = True
        if time.strftime('%H:%M') == '14:10' and p5_check is False:
            await channel.send('Hey guys, Period 5 has started.')
            p5_check = True
        if time.strftime('%H:%M') == '15:10' and as_check is False:
            await channel.send('Schools over.')
            as_check = True
        await asyncio.sleep(30)


async def next_period2():
    global bs_check, rc_check, rlc_check, p1_check, p2_check, p3_check, p4_check, p5_check, as_check, rc_check, lunch_check
    await client.wait_until_ready()
    channel = client.get_channel(448073494660644884)
    while True:
        if current_period() == 'Nothing':
            pass
        if current_period() == 'BS' and not bs_check:
            bs_check = True
            await channel.send('Before school started.')
        if current_period() == 'Roll Call' and not rlc_check:
            rlc_check = True
            await channel.send('Roll Call has started.')
        if current_period() == 'P1' and not p1_check:
            p1_check = True
            await channel.send('Period 1 has started.')
        if current_period() == 'P2' and not p2_check:
            p2_check = True
            await channel.send('Period 2 has started.')
        if current_period() == 'Recess' and not rc_check:
            rc_check = True
            await channel.send('Recess has started.')
        if current_period() == 'P3' and not p3_check:
            p3_check = True
            await channel.send('Period 3 has started.')
        if current_period() == 'P4' and not p4_check:
            p4_check = True
            await channel.send('Period 4 has started.')
        if current_period() == 'Lunch' and not lunch_check:
            lunch_check = True
            await channel.send('Lunch has started.')
        if current_period() == 'P5' and not p5_check:
            p5_check = True
            await channel.send('Period 5 has started.')
        if current_period() == 'AS' and not as_check and dayofweek() == 'Thursday':
            as_check = True
            await channel.send('Sport has started.')
        if current_period() == 'AS' and not as_check and not dayofweek() == 'Thursday':
            as_check = True
            await channel.send('School is out. After school classes begin if you have any.')
        await asyncio.sleep(5)


@client.event
async def on_message(message):
    await client.process_commands(message)
    if message.content.find("what do i have") != -1 or message.content.find("what dont i have") != -1:
        if message.author.id == 349076896266452994 or message.content.find("alex") != -1:
            pass
        elif message.author.id == 237465974545055744 or message.author.id == 368682763093671936 or message.content.find(
                "what do i have jean") != -1:
            if datetime.datetime.today().weekday() == 0 or message.content.find(
                    "0") != -1 or datetime.datetime.today().weekday() == 5 or datetime.datetime.today().weekday() == 6:
                embed = discord.Embed(
                    title='Here are your classes:',
                    description='You have:',
                    colour=discord.Colour.green()
                )
                embed.set_footer(text='Monday :(')

                embed.set_author(name=message.author.name, icon_url=message.author.avatar_url)
                embed.add_field(name='Week A', value="Double Science, Double IST, Commerce", inline=False)
                embed.add_field(name='Week B', value="Commerce, English, INTE, Maths, PDHPE", inline=False)
                await message.channel.send(embed=embed)
            if datetime.datetime.today().weekday() == 1 or message.content.find("1") != -1:
                embed = discord.Embed(
                    title='Here are your classes:',
                    description='You have:',
                    colour=discord.Colour.green()
                )
                embed.set_footer(text='Tuesday :(')

                embed.set_author(name=message.author.name, icon_url=message.author.avatar_url)
                embed.add_field(name='Week A', value="INTE, Science, Maths, History, Commerce", inline=False)
                embed.add_field(name='Week B', value="Science, Maths, IST, History, INTE", inline=False)
                await message.channel.send(embed=embed)
            if datetime.datetime.today().weekday() == 2 or message.content.find("2") != -1:
                embed = discord.Embed(
                    title='Here are your classes:',
                    description='You have:',
                    colour=discord.Colour.green()
                )
                embed.set_footer(text='Wednesday')

                embed.set_author(name=message.author.name, icon_url=message.author.avatar_url)
                embed.add_field(name='Week A', value="Commerce, INTE, Science, English, IST", inline=False)
                embed.add_field(name='Week B', value="Commerce, IST, Careers, PDHPE, Geography", inline=False)
                await message.channel.send(embed=embed)
            if datetime.datetime.today().weekday() == 3 or message.content.find("3") != -1:
                embed = discord.Embed(
                    title='Here are your classes:',
                    description='You have:',
                    colour=discord.Colour.green()
                )
                embed.set_footer(text='Urgh thursday')

                embed.set_author(name=message.author.name, icon_url=message.author.avatar_url)
                embed.add_field(name='Week A', value="Geography, English, PDHPE", inline=False)
                embed.add_field(name='Week B', value="Maths, English, Geography", inline=False)
                await message.channel.send(embed=embed)
            if datetime.datetime.today().weekday() == 4 or message.content.find("4") != -1:
                embed = discord.Embed(
                    title='Here are your classes:',
                    description='You have:',
                    colour=discord.Colour.green()
                )
                embed.set_footer(text='Whew last day of the week!')

                embed.set_author(name=message.author.name, icon_url=message.author.avatar_url)
                embed.add_field(name='Week A', value="Maths, Geography, PDHPE, History, English", inline=False)
                embed.add_field(name='Week B', value="Maths, Science, History, INTE, English", inline=False)
                await message.channel.send(embed=embed)
        elif message.author.id == 563988053962653696 or message.content.find("what do i have brennan") != -1:
            if datetime.datetime.today().weekday() == 0 or message.content.find(
                    "0") != -1 or datetime.datetime.today().weekday() == 5 or datetime.datetime.today().weekday() == 6:
                embed = discord.Embed(
                    title='Here are your classes:',
                    description='You have:',
                    colour=discord.Colour.green()
                )
                embed.set_footer(text='Monday :(')

                embed.set_author(name=message.author.name, icon_url=message.author.avatar_url)
                embed.add_field(name='Week A', value="Double Science, Double Food, Japanese", inline=False)
                embed.add_field(name='Week B', value="Japanese, English, Commerce, Maths, PDHPE", inline=False)
                await message.channel.send(embed=embed)
            if datetime.datetime.today().weekday() == 1 or message.content.find("1") != -1:
                embed = discord.Embed(
                    title='Here are your classes:',
                    description='You have:',
                    colour=discord.Colour.green()
                )
                embed.set_footer(text='Tuesday :(')

                embed.set_author(name=message.author.name, icon_url=message.author.avatar_url)
                embed.add_field(name='Week A', value="Commerce, Science, Maths, History, Japanese", inline=False)
                embed.add_field(name='Week B', value="Science, Maths, Food, History, Commerce", inline=False)
                await message.channel.send(embed=embed)
            if datetime.datetime.today().weekday() == 2 or message.content.find("2") != -1:
                embed = discord.Embed(
                    title='Here are your classes:',
                    description='You have:',
                    colour=discord.Colour.green()
                )
                embed.set_footer(text='Wednesday')

                embed.set_author(name=message.author.name, icon_url=message.author.avatar_url)
                embed.add_field(name='Week A', value="Japanese, Commerce, Science, English, Food", inline=False)
                embed.add_field(name='Week B', value="Japanese, Food, Careers, PDHPE, Geography", inline=False)
                await message.channel.send(embed=embed)
            if datetime.datetime.today().weekday() == 3 or message.content.find("3") != -1:
                embed = discord.Embed(
                    title='Here are your classes:',
                    description='You have:',
                    colour=discord.Colour.green()
                )
                embed.set_footer(text='Urgh thursday')

                embed.set_author(name=message.author.name, icon_url=message.author.avatar_url)
                embed.add_field(name='Week A', value="Geography, English, PDHPE", inline=False)
                embed.add_field(name='Week B', value="Maths, English, Geography", inline=False)
                await message.channel.send(embed=embed)
            if datetime.datetime.today().weekday() == 4 or message.content.find("4") != -1:
                embed = discord.Embed(
                    title='Here are your classes:',
                    description='You have:',
                    colour=discord.Colour.green()
                )
                embed.set_footer(text='Whew last day of the week!')

                embed.set_author(name=message.author.name, icon_url=message.author.avatar_url)
                embed.add_field(name='Week A', value="Maths, Geography, PDHPE, History, English", inline=False)
                embed.add_field(name='Week B', value="Maths, Science, History, Commerce, English", inline=False)
                await message.channel.send(embed=embed)
        elif message.author.id == 341488528674521091 or message.content.find("what do i have jayden") != -1:
            if datetime.datetime.today().weekday() == 0 or message.content.find(
                    "0") != -1 or datetime.datetime.today().weekday() == 5 or datetime.datetime.today().weekday() == 6:
                embed = discord.Embed(
                    title='Here are your classes:',
                    description='You have:',
                    colour=discord.Colour.green()
                )
                embed.set_footer(text='Monday :(')

                embed.set_author(name=message.author.name, icon_url=message.author.avatar_url)
                embed.add_field(name='Week A', value="History, Careers, Double Commerce, SoR", inline=False)
                embed.add_field(name='Week B', value="SoR, English, Design and Technology, Maths, History",
                                inline=False)
                await message.channel.send(embed=embed)
            if datetime.datetime.today().weekday() == 1 or message.content.find("1") != -1:
                embed = discord.Embed(
                    title='Here are your classes:',
                    description='You have:',
                    colour=discord.Colour.green()
                )
                embed.set_footer(text='Tuesday :(')

                embed.set_author(name=message.author.name, icon_url=message.author.avatar_url)
                embed.add_field(name='Week A', value="Design and Technology, Geography, Maths, PDHPE, SoR",
                                inline=False)
                embed.add_field(name='Week B', value="Science, Maths, Commerce, PDHPE, Design and Technology",
                                inline=False)
                await message.channel.send(embed=embed)
            if datetime.datetime.today().weekday() == 2 or message.content.find("2") != -1:
                embed = discord.Embed(
                    title='Here are your classes:',
                    description='You have:',
                    colour=discord.Colour.green()
                )
                embed.set_footer(text='Wednesday')

                embed.set_author(name=message.author.name, icon_url=message.author.avatar_url)
                embed.add_field(name='Week A', value="SoR, SoR, Design and Technology, Science, English, Commerce",
                                inline=False)
                embed.add_field(name='Week B', value="SoR, SoR, Commerce, History, Geography, Science", inline=False)
                await message.channel.send(embed=embed)
            if datetime.datetime.today().weekday() == 3 or message.content.find("3") != -1:
                embed = discord.Embed(
                    title='Here are your classes:',
                    description='You have:',
                    colour=discord.Colour.green()
                )
                embed.set_footer(text='Urgh thursday')

                embed.set_author(name=message.author.name, icon_url=message.author.avatar_url)
                embed.add_field(name='Week A', value="Geography, English, History", inline=False)
                embed.add_field(name='Week B', value="SoR, Maths, English, Geography", inline=False)
                await message.channel.send(embed=embed)
            if datetime.datetime.today().weekday() == 4 or message.content.find("4") != -1:
                embed = discord.Embed(
                    title='Here are your classes:',
                    description='You have:',
                    colour=discord.Colour.green()
                )
                embed.set_footer(text='Whew last day of the week!')

                embed.set_author(name=message.author.name, icon_url=message.author.avatar_url)
                embed.add_field(name='Week A', value="Maths, PDHPE, Double Science, English", inline=False)
                embed.add_field(name='Week B', value="Maths, Science, Geography, Design and Technology, English",
                                inline=False)
                await message.channel.send(embed=embed)
        elif message.author.id == 298042908513271818 or message.content.find("what do i have ahoura") != -1:
            if datetime.datetime.today().weekday() == 0 or message.content.find(
                    "0") != -1 or datetime.datetime.today().weekday() == 5 or datetime.datetime.today().weekday() == 6:
                embed = discord.Embed(
                    title='Here are your classes:',
                    description='You have:',
                    colour=discord.Colour.green()
                )
                embed.set_footer(text='Monday :(')

                embed.set_author(name=message.author.name, icon_url=message.author.avatar_url)
                embed.add_field(name='Week A', value="Double Science, Double Commerce, Japanese", inline=False)
                embed.add_field(name='Week B', value="Japanese, English, IST, Maths, Science", inline=False)
                await message.channel.send(embed=embed)
            if datetime.datetime.today().weekday() == 1 or message.content.find("1") != -1:
                embed = discord.Embed(
                    title='Here are your classes:',
                    description='You have:',
                    colour=discord.Colour.green()
                )
                embed.set_footer(text='Tuesday :(')

                embed.set_author(name=message.author.name, icon_url=message.author.avatar_url)
                embed.add_field(name='Week A', value="IST, Science, Maths, History, Japanese", inline=False)
                embed.add_field(name='Week B', value="Geography, Maths, Commerce, History, IST", inline=False)
                await message.channel.send(embed=embed)
            if datetime.datetime.today().weekday() == 2 or message.content.find("2") != -1:
                embed = discord.Embed(
                    title='Here are your classes:',
                    description='You have:',
                    colour=discord.Colour.green()
                )
                embed.set_footer(text='Wednesday')

                embed.set_author(name=message.author.name, icon_url=message.author.avatar_url)
                embed.add_field(name='Week A', value="Japanese, IST, Science, English, Commerce",
                                inline=False)
                embed.add_field(name='Week B', value="Japanese, Commerce, Geography, Science, Careers", inline=False)
                await message.channel.send(embed=embed)
            if datetime.datetime.today().weekday() == 3 or message.content.find("3") != -1:
                embed = discord.Embed(
                    title='Here are your classes:',
                    description='You have:',
                    colour=discord.Colour.green()
                )
                embed.set_footer(text='Urgh thursday')

                embed.set_author(name=message.author.name, icon_url=message.author.avatar_url)
                embed.add_field(name='Week A', value="PDHPE, English, History", inline=False)
                embed.add_field(name='Week B', value="Maths, English, PDHPE", inline=False)
                await message.channel.send(embed=embed)
            if datetime.datetime.today().weekday() == 4 or message.content.find("4") != -1:
                embed = discord.Embed(
                    title='Here are your classes:',
                    description='You have:',
                    colour=discord.Colour.green()
                )
                embed.set_footer(text='Whew last day of the week!')

                embed.set_author(name=message.author.name, icon_url=message.author.avatar_url)
                embed.add_field(name='Week A', value="Maths, Geography, PDHPE, History, English", inline=False)
                embed.add_field(name='Week B', value="Maths, PDHPE, Geography, IST, English",
                                inline=False)
                await message.channel.send(embed=embed)
        else:
            await message.channel.send('your user id is: ' + str(message.author.id))
            embed = discord.Embed(
                title='Oh no!',
                description='It looks like an error has occurred.',
                colour=discord.Colour.red()

            )
            embed.set_footer(text='Error four hundred and four')
            embed.set_thumbnail(url='https://cdn2.iconfinder.com/data/icons/mix-color-5/100/Mix_color_5__info-512.png')
            embed.set_author(name=message.author.name, icon_url=message.author.avatar_url)
            embed.add_field(name='Heres some debug info:',
                            value="I'm not ready yet! Sorry about that :/ . I'm being re-written right now. If you "
                                  "would like your timetable added to me, please DM it to Alex H.",
                            inline=False)

            await message.channel.send(embed=embed)


current_period()

client.loop.create_task(next_period2())
client.run('token')
