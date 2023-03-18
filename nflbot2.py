import os
import sys
import urllib
import discord
import interactions
import asyncio
import deeppyer
from PIL import Image

bot = interactions.Client(token="")

@bot.command(
    name="gamba",
    description="Get it twisted."
)
async def gamba(ctx: interactions.CommandContext):
    await ctx.send("🦍 🗣 GET IT TWISTED 🌪 , GAMBLE ✅ . PLEASE START GAMBLING 👍 . GAMBLING IS AN INVESTMENT 🎰 AND AN INVESTMENT ONLY 👍 . YOU WILL PROFIT 💰 , YOU WILL WIN ❗ ️. YOU WILL DO ALL OF THAT 💯 , YOU UNDERSTAND ⁉ ️ YOU WILL BECOME A BILLIONAIRE 💵 📈 AND REBUILD YOUR FUCKING LIFE 🤯")

@bot.command(
    name="fry",
    description="fry an image",
    options = [
    interactions.Option(
        name="img",
        description="Add an image",
        type=interactions.OptionType.ATTACHMENT,
        required=True,
    ),
],
)
async def fry(ctx: interactions.CommandContext, img):
    files = []
    url = img.url
    name = img.filename
    img = urllib.request.urlretrieve(url, name)
    img = Image.open(img)
    img = await deeppyer.deepfry(img)
    img = discord.File(name)
    files.append(img)
    await ctx.send(files=files)



bot.start()
