import os
import sys
import discord
import interactions
import asyncio
# import deeppyer
# from PIL import Image

bot = interactions.Client(token="")

@bot.command(
    name="gamba",
    description="Get it twisted."
)
async def gamba(ctx: interactions.CommandContext):
    await ctx.send("🦍 🗣 GET IT TWISTED 🌪 , GAMBLE ✅ . PLEASE START GAMBLING 👍 . GAMBLING IS AN INVESTMENT 🎰 AND AN INVESTMENT ONLY 👍 . YOU WILL PROFIT 💰 , YOU WILL WIN ❗ ️. YOU WILL DO ALL OF THAT 💯 , YOU UNDERSTAND ⁉ ️ YOU WILL BECOME A BILLIONAIRE 💵 📈 AND REBUILD YOUR FUCKING LIFE 🤯")

@bot.command(
    name="tyfys",
    description="Thank the troops."
)
async def tyfys(ctx: interactions.CommandContext):
    emoji = '<:Salute:723745354243375236>'
    response = f"{emoji} Thank You For Your Service"
    await ctx.send(response)

@bot.command(
    name="clap",
    description="Bring out the clapper."
)
async def clap(ctx: interactions.CommandContext):
    emoji = '<a:clapper:755219763017285652>'
    response = emoji*5
    await ctx.send(response)

@bot.command(
    name="bitch",
    description="Kyle vibes.",
    options = [
        interactions.Option(
            name="person",
            description="Add a person.",
            type=interactions.OptionType.STRING,
            required=False,
        ),
    ],
)
async def bitch(ctx: interactions.CommandContext, text: str="kyle"):
    response = f"{text} how you already bitchin"
    await ctx.send(response)

@bot.command(
    name="drunk",
    description="Chado vibes.",
    options = [
        interactions.Option(
            name="person",
            description="Add a person.",
            type=interactions.OptionType.STRING,
            required=False,
        ),
    ],
)
async def drunk(ctx: interactions.CommandContext, text: str="Chado"):
    response = f"{text} how you drunk already"
    await ctx.send(response)
    
@bot.command(
    name="cowboys",
    description="Let us know about the boys."
)
async def cowboys(ctx: interactions.CommandContext):
    response = "Triggered ? Bro I'm excited ! I'm ready for Dak to show the world why he deserves to be paid and for Kellen Moore to show how big his brain is :p"
    await ctx.send(response)

# @bot.event
# async def on_message_create(message):
#     if message.author == bot.get_self_user():
#         return

#     if message.content.startswith('$fry'):
#         if message.referenced_message is not None:
#             message = await message.channel.fetch_message(message.referenced_message.message_id)
#         img = await message.attachments[0].download()
#         img = Image.open(img).convert("RGB")
#         img = await deeppyer.deepfry(img)
#         img.save("fried.png")
#         img = discord.File("fried.png")
#         await message.channel.send(file=img)
#         os.remove("fried.png")

# @bot.command(
#     name="fry",
#     description="fry an image",
    # options = [
    # interactions.Option(
    #     name="img",
    #     description="Add an image",
    #     type=interactions.OptionType.ATTACHMENT,
    #     required=True,
    # ),
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
