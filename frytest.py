from PIL import Image
import deeppyer, asyncio

async def main():
    img = Image.open('./foo.jpg')
    img = await deeppyer.deepfry(img)
    img.save('./bar.jpg')

loop = asyncio.get_event_loop()
loop.run_until_complete(main())
