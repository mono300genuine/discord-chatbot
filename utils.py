from replit_detector import is_replit
from dotenv import load_dotenv
import json
import logging
import os

logging.basicConfig(level=logging.INFO,
                    format="[%(levelname)s] %(message)s")

if is_replit:
    bot_token: str = os.environ["BOT_TOKEN"]
    api_key: str = os.environ["API_KEY"]
    poe_key: str = os.environ["POE_TOKEN"]
else:
    # Load .env file
    load_dotenv(".env")
    bot_token: str = os.getenv("BOT_TOKEN")
    api_key: str = os.getenv("API_KEY")
    poe_key: str = os.getenv("POE_TOKEN")

if api_key == "0000000000":
    logging.warning("Default API key selected. Generating images will be slower. "
                    "Generated images will be sent to LAION to improve Stable Diffusion.")

# Load config
with open("config.json") as f:
    config = json.load(f)

# Line junk is some stuff that makes Discord hide links.
# See https://www.youtube.com/watch?v=9OgpQHSP5qE (by Ntts)
with open("line_junk.txt") as f:
    line_junk = f.read()


class FakeCtx:
    def __init__(self, message):
        self.author = message.author
        self.message = message

    async def send(self, content, file=None):
        return await self.message.channel.send(content, file=file)
