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

@bot.event
async def on_message_create(message):
    if message.author == bot.get_self_user():
        return

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

# @bot.command(
#     name="fry",
#     description="fry an image",
#     options = [
#     interactions.Option(
#         name="img",
#         description="Add an image",
#         type=interactions.OptionType.ATTACHMENT,
#         required=True,
#     ),
# ],
# )
# async def fry(ctx: interactions.CommandContext, img):
#     files = []
#     img = await img.download()
#     name = img.filename
#     img = Image.open(name)
#     img = await deeppyer.deepfry(img)
#     img = discord.File(name)
#     files.append(img)
#     await ctx.send(files=files)



bot.start()
