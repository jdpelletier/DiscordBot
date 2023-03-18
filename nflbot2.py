import os
import sys
import interactions
import asyncio
from PIL import Image, ImageOps, ImageEnhance

bot = interactions.Client(token="")

@bot.command(
    name="gamba",
    description="Get it twisted."
)
async def gamba(ctx: interactions.CommandContext):
    await ctx.send("🦍 🗣 GET IT TWISTED 🌪 , GAMBLE ✅ . PLEASE START GAMBLING 👍 . GAMBLING IS AN INVESTMENT 🎰 AND AN INVESTMENT ONLY 👍 . YOU WILL PROFIT 💰 , YOU WILL WIN ❗ ️. YOU WILL DO ALL OF THAT 💯 , YOU UNDERSTAND ⁉ ️ YOU WILL BECOME A BILLIONAIRE 💵 📈 AND REBUILD YOUR FUCKING LIFE 🤯")

@bot.command(
    name="tyfys",
    description="Thank the troops.",
    options = [
        interactions.Option(
            name="person",
            description="Add a person.",
            type=interactions.OptionType.STRING,
            required=False,
        ),
    ],
)
async def tyfys(ctx: interactions.CommandContext, person: str=""):
    emoji = '<:Salute:723745354243375236>'
    response = f"{emoji} Thank You For Your Service {person} {emoji}"
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
async def bitch(ctx: interactions.CommandContext, person: str="kyle"):
    response = f"{person} how you already bitchin"
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
async def drunk(ctx: interactions.CommandContext, person: str="Chado"):
    response = f"{person} how you drunk already"
    await ctx.send(response)
    
@bot.command(
    name="cowboys",
    description="Let us know about the boys."
)
async def cowboys(ctx: interactions.CommandContext):
    response = "Triggered ? Bro I'm excited ! I'm ready for Dak to show the world why he deserves to be paid and for Kellen Moore to show how big his brain is :p"
    await ctx.send(response)

@bot.event
async def on_message_create(message):
    if message.author == bot.get_self_user():
        return

    if message.content.startswith('$fry'):
        files = []
        if message.referenced_message is not None:
            message = await message.channel_id.fetch_message(message.referenced_message.message_id)
        img = await message.attachments[0].download()
        img = Image.open(img).convert("RGB")
        width, height = img.width, img.height
        img = img.resize((int(width ** .75), int(height ** .75)), resample=Image.LANCZOS)
        img = img.resize((int(width ** .88), int(height ** .88)), resample=Image.BILINEAR)
        img = img.resize((int(width ** .9), int(height ** .9)), resample=Image.BICUBIC)
        img = img.resize((width, height), resample=Image.BICUBIC)
        img = ImageOps.posterize(img, 4)
        # Generate colour overlay
        r = img.split()[0]
        r = ImageEnhance.Contrast(r).enhance(2.0)
        r = ImageEnhance.Brightness(r).enhance(1.5)

        r = ImageOps.colorize(r, (254, 0, 2), (255, 255, 15))

        # Overlay red and yellow onto main image and sharpen the hell out of it
        img = Image.blend(img, r, 0.75)
        img = ImageEnhance.Sharpness(img).enhance(100.0)

        img.save("fried.png")
        img = interactions.File("fried.png")
        files.append(img)
        channel = await message.get_channel()
        await channel.send(files=files)
        os.remove("fried.png")

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
    img = await img.download()
    img = Image.open(img).convert("RGB")
    width, height = img.width, img.height
    img = img.resize((int(width ** .75), int(height ** .75)), resample=Image.LANCZOS)
    img = img.resize((int(width ** .88), int(height ** .88)), resample=Image.BILINEAR)
    img = img.resize((int(width ** .9), int(height ** .9)), resample=Image.BICUBIC)
    img = img.resize((width, height), resample=Image.BICUBIC)
    img = ImageOps.posterize(img, 4)
    # Generate colour overlay
    r = img.split()[0]
    r = ImageEnhance.Contrast(r).enhance(2.0)
    r = ImageEnhance.Brightness(r).enhance(1.5)

    r = ImageOps.colorize(r, (254, 0, 2), (255, 255, 15))

    # Overlay red and yellow onto main image and sharpen the hell out of it
    img = Image.blend(img, r, 0.75)
    img = ImageEnhance.Sharpness(img).enhance(100.0)

    img.save("fried.png")
    img = interactions.File("fried.png")
    files.append(img)
    await ctx.send(files=files)



bot.start()
