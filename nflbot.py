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

    if message.content.startswith("$TYFYS"):
        text = message.content.split()
        emoji = '<:Salute:723745354243375236>'
        response = f"{emoji} Thank You For Your Service"
        if len(text) > 1:
            for name in text:
                if name != "$TYFYS":
                    response = response + " " + name
        response = response + " " + emoji
        await message.channel.send(response)

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

    if message.content.startswith('$couch'):
        text = message.content.split()
        if len(text) == 1:
            response = "Enter a week"
        else:
            response = beastScore(text[1])
        await message.channel.send(response)

    if message.content.startswith('$cowboys'):
        text = "Triggered ? Bro I'm excited ! I'm ready for Dak to show the world why he deserves to be paid and for Kellen Moore to show how big his brain is :p"
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

client.run('NzU0MDY0NTgwMzc5OTM0NzIw.X1vTXQ.opf24Jt0USUrfataEtKjLwboB1w')
