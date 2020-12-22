import sys
import discord
import asyncio
from getScore import allScores, beastScore
from getOdds import getOdds, bigSpreadWatch, dicFileRead

client = discord.Client()



@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$help'):
        text = """nfl-bot is the official NFL bot of this discord. Commands include:

                    -$tyfys: salute your favorite person or thing. (optional name argument)

                    -$cowboys: show how you feel about the boys this year

                    -$clap: summon the clap god

                    -$bitch: call when someone is complaining. (defualts to kyle, can add name)

                    -$odds: pull up the odds for this week (might not work)

                    -$location: see where the bot is currently running

        Please send bot suggestions to JP. This broadcast is copyrighted by NFL Productions for the private use of our audience. Any other use of this telecast, or any pictures, descriptions, or accounts of the game without the consent of NFL Productions is prohibited."""
        await message.channel.send(text)

    if message.content.startswith('$scores'):
        # content = message.content.lower()
        # messagelist = content.split()
        # if len(messagelist) == 1:
        #     await message.channel.send("NFL IS BACK!")
        # else:
            # if 'city' in messagelist:
            #     index = messagelist.index('city')
            #     messagelist[index-1] = messagelist[index-1] + messagelist[index]
            #     del messagelist[index]
        scores = allScores()
        await message.channel.send(scores)

    if message.content.lower().startswith("$tyfys"):
        text = message.content.split()
        emoji = '<:Salute:723745354243375236>'
        response = f"{emoji} Thank You For Your Service"
        if len(text) > 1:
            for name in text:
                if name.lower() != "$tyfys":
                    response = response + " " + name
        response = response + " " + emoji
        await message.channel.send(response)
        await message.delete()

    if message.content.startswith("$clap"):
        emoji = '<a:clapper:755219763017285652>'
        response = emoji*5
        await message.channel.send(response)
        await message.delete()

    if message.content.startswith('$odds'):
        odds = getOdds()
        await message.channel.send(odds)

    if message.content.startswith('$bitch'):
        response = ''
        text = message.content.split()
        if len(text) > 1:
            for name in text:
                if name != "$bitch":
                    response = response + name + " "
        else:
            response = 'kyle '
        response = response + "how you already bitchin"
        await message.channel.send(response)
        await message.delete()

    if message.content.startswith('$couch'):
        text = message.content.split()
        if len(text) == 1:
            response = "Enter a week"
        else:
            response = beastScore(text[1])
        await message.channel.send(response)
        await message.delete()

    if message.content.startswith('$cowboys'):
        text = "Triggered ? Bro I'm excited ! I'm ready for Dak to show the world why he deserves to be paid and for Kellen Moore to show how big his brain is :p"
        await message.channel.send(text)

    if message.content.startswith('$location'):
        operating_sys = sys.platform
        if "win" in operating_sys:
            text = "nfl-bot is currently running on Chado-Server"
        elif "linux" in operating_sys:
            text = "nfl-bot is currently running on JP-Pi"
        else:
            text = "I have no idea where I currently am running"
        await message.channel.send(text)


async def big_spread_tracker():
    await client.wait_until_ready()
    channel = client.get_channel(742460265894903898) # channel ID goes here
    while not client.is_closed():
        dic = dicFileRead()
        text = bigSpreadWatch(dic)
        if text != '':
            await channel.send(text)
        await asyncio.sleep(60) # task runs every 60 seconds

bspread_track = client.loop.create_task(big_spread_tracker())

client.run('')
