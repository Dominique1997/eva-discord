import json
import discord
from urllib import parse
from requests import get, post
from discord.ext import commands
from secrets import Secrets
from settings import Settings

bot = commands.Bot(command_prefix=Settings.get_bot_prefix(), intents=discord.Intents.all())

class IntegrationDiscord:
    @classmethod
    def start_bot(cls):
        if Settings.get_dev_status():
            bot.run(token=Secrets.get_dev_token())
        else:
            bot.run(token=Secrets.get_main_token())

    @bot.event
    async def on_ready():
        print("ready for use")

    @bot.event
    async def on_message(ctx):
        channel = ctx.channel
        message = str(ctx.content).lower()
        author = ctx.author.name
        if Settings.get_bot_name() != author:
            if str(message).startswith(Settings.get_bot_name()):
                message = str(message).replace(Settings.get_bot_name() + " ", "")
                params = {'sentence': message}
                answer = json.loads(get(f"http://{Settings.get_api_ip()}:{Settings.get_api_port()}/api/general/check_command?{parse.urlencode(params)}").text)
                print(answer)
                if "answer" in answer:
                    channel.typing()
                    await channel.send(answer["answer"])
                else:
                    channel.typing()
                    print(str(answer["answer"]).startswith("Wolfram Alpha"))
                    if str(answer["answer"]).startswith("Wolfram Alpha"):
                        await channel.send(str(answer["error"]).replace("Wolfram Alpha", "I am sorry. I"))
                    else:
                        await channel.send(answer["error"])
