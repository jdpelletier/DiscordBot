import os
import sys
import interactions
import asyncio
import textwrap
import shutil
from PIL import Image, ImageOps, ImageEnhance, ImageDraw, ImageFont, ImageSequence

intents = interactions.Intents.ALL
bot = interactions.Client(token="", intents=intents)

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
    name="yugioh",
    description="please please please go outside"
)
async def yugioh(ctx: interactions.CommandContext):
    text = "I feel like every time you mention anything yugioh related to me it's always about a blowjob first this week it was that fucking dog that forces your opponent to oral you and now it's this fucking dick sucking goblin rider can you please please please go outside"
    await ctx.send(text)

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
    name="mybad",
    description="What are you looking back on?",
    options = [
        interactions.Option(
            name="topic",
            description="Add a topic that was your bad.",
            type=interactions.OptionType.STRING,
            required=True,
        ),
    ],
)
async def mybad(ctx: interactions.CommandContext, topic):
    response = f"Looking back on it, I was way too much of an asshole about the {topic} thing\n\nMy bad"
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

@bot.command(
    name="eagles",
    description="Let us know about the birds."
)
async def eagles(ctx: interactions.CommandContext):
    response = "Triggered ? Bro I'm excited ! I'm ready for Jalen to show the world why he deserves to be paid and for Kellen Moore to show how big his brain is :p"
    await ctx.send(response)

@bot.event
async def on_message_create(message):
    if message.author == await bot.get_self_user():
        return

    if message.content.startswith('$fry'):
        files = []
        channel = await message.get_channel()
        if message.referenced_message is not None:
            message = await channel.get_message(message.referenced_message.id)
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
    await ctx.send("Frying...", ephemeral=True)
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


@bot.command(
    name="mouse",
    description="Make Mickey say what you want while holding a gun",
    options = [
        interactions.Option(
            name="sentence",
            description="Add some dialog.",
            type=interactions.OptionType.STRING,
            required=True,
        ),
    ],
)
async def mouse(ctx: interactions.CommandContext, sentence):
    img = Image.open("Disney.png").convert("RGB")
    draw = ImageDraw.Draw(img)
    font = ImageFont.truetype("Pillow/Tests/fonts/FreeMonoBold.ttf", 23)
    outputStrs = textwrap.wrap(sentence, width=15, break_long_words=False)
    sentence = '\n'.join(outputStrs)
    draw.text((370, 65), sentence, fill="#000000", font=font)
    img.save("Moused.png")
    img = interactions.File("Moused.png")
    files = []
    files.append(img)
    await ctx.send(files=files)


jenu = interactions.SelectMenu(
    custom_id="jenu",
    options=[
        interactions.SelectOption(label="Joel", value="Joel.gif"),
        interactions.SelectOption(label="Joeler", value="Joeler.gif"),
        interactions.SelectOption(label="JoelNopers", value="JoelNopers.gif"),
        interactions.SelectOption(label="JoelPride", value="JoelPride.gif")
    ],
)

@bot.component("jenu")
async def jenu_response(ctx, value):
    shutil.copy(value[0], "joeling.gif")
    await ctx.send("Select a location", components=menu, ephemeral=True)


menu = interactions.SelectMenu(
    custom_id="menu",
    options=[
        interactions.SelectOption(label="Top Right", value="1"),
        interactions.SelectOption(label="Top Left", value="2"),
        interactions.SelectOption(label="Bottom Right", value="3"),
        interactions.SelectOption(label="Bottom Left", value="4"),
        interactions.SelectOption(label="Middle", value="5"),
    ],
)


@bot.component("menu")
async def menu_response(ctx, value):
    await ctx.send("joeling...", ephemeral=True)
    await ctx.delete()
    background = Image.open("toJoel.png").convert("RGB")
    images = []
    img_w, img_h = background.size
    background.close()
    with Image.open("joeling.gif") as im:
        for frame in ImageSequence.Iterator(im):
            background = Image.open("toJoel.png").convert("RGB")
            frame = frame.convert("RGBA")
            fr_w, fr_h = frame.size
            if value[0] == "1" :
                offset = ((img_w-fr_w), 0) #topright
            elif value[0] == "2":
                offset = (0,0) #topleft
            elif value[0] == "3":
                offset = ((img_w-fr_w), (img_h-fr_h)) #bottomright
            elif value[0] == "4":
                offset = (0, (img_h-fr_h)) #bottomleft
            else :
                offset = ((img_w-fr_w) // 2, (img_h-fr_h) // 2) #middle
            
            background.paste(frame, offset, frame)
            images.append(background)
    
    images[0].save('joeled.gif',
               save_all=True, append_images=images[1:], duration=50, loop=0, quality=50, optimize=True)
    img = interactions.File("joeled.gif")
    files = []
    files.append(img)
    await ctx.send(files=files)


@bot.command(
    name="joel",
    description="Joel up an image",
    options = [
        interactions.Option(
            name="img",
            description="Add an image",
            type=interactions.OptionType.ATTACHMENT,
            required=True,
        ),
    ],
)
async def joel(ctx: interactions.CommandContext, img):
    await ctx.send("Joeling...", ephemeral=True)
    base = await img.download()
    background = Image.open(base)
    background.save("toJoel.png")
    await ctx.send("Select a joel", components=jenu, ephemeral=True)
    



bot.start()
