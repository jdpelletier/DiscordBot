import os
import sys
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


bot.start()
