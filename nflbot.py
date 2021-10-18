import os
import sys
import discord
import asyncio
import deeppyer
from PIL import Image
from getScore import beastScore, wentzCount
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

                    -$fry: upload or reply to an image to fry it up

                    -$cowboys: show how you feel about the boys this year

                    -$couch: check to see if the bed is warm this week

                    -$clap: summon the clap god

                    -$bitch: call when someone is complaining. (defaults to "kyle", can add name)

                    -$drunk: call when someone is somehow already drunk. (defaults to "chado", can add name)

                    -$odds: pull up the odds for this week (might not work)

                    -$location: see where the bot is currently running

        Please send bot suggestions to JP. This broadcast is copyrighted by NFL Productions for the private use of our audience. Any other use of this telecast, or any pictures, descriptions, or accounts of the game without the consent of NFL Productions is prohibited."""
        await message.channel.send(text)

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

    if message.content.startswith('$drunk'):
        response = ''
        text = message.content.split()
        if len(text) > 1:
            for name in text:
                if name != "$drunk":
                    response = response + name + " "
        else:
            response = 'chado '
        response = response + "how you already drunk"
        await message.channel.send(response)

    if message.content.startswith('$couch'):
        response = beastScore(message.author)
        await message.channel.send(response)

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

    if message.content.startswith('$fry'):
        if message.reference is not None:
            message = await message.channel.fetch_message(message.reference.message_id)
        img = message.attachments[0]
        name = img.filename
        await img.save(name)
        img = Image.open(name)
        img = await deeppyer.deepfry(img)
        img.save(name)
        img = discord.File(name)
        await message.channel.send(file=img)
        os.remove(name)

    if message.content.startswith('$wentz'):
        # messages = await message.channel.history(limit=10).filter(check_chado).flatten()
        messages = await message.channel.history(limit=10).flatten()
        count = wentzCount(messages)
        text = f"Chado has mentioned Carson Wentz {count} times in this chat.  Talk about living rent free!"



# async def big_spread_tracker():
#     await client.wait_until_ready()
#     channel = client.get_channel(742460265894903898) # channel ID goes here
#     while not client.is_closed():
#         dic = dicFileRead()
#         text = bigSpreadWatch(dic)
#         if text != '':
#             await channel.send(text)
#         await asyncio.sleep(60) # task runs every 60 seconds
#
# bspread_track = client.loop.create_task(big_spread_tracker())

client.run('')
