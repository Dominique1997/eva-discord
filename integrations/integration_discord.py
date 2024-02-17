import json
import discord
import requests
from secrets import Secrets
from settings import Settings
from discord.ext import commands


bot = commands.Bot(command_prefix=Settings.get_bot_prefix(), intents=discord.Intents.all())


class IntegrationDiscord:
    @classmethod
    def start_bot(cls):
        bot.run(token=Secrets.get_token())

    @bot.event
    async def on_message(ctx):
        channel = ctx.channel
        message = str(ctx.content).lower()
        author = ctx.author.name
        if Settings.get_bot_name() != author:
            bot_channel = "eva-testing" if Settings.get_dev_status() else "eva-main"
            if str(channel).lower() == bot_channel:
                message = str(message).replace(Settings.get_bot_name() + " ", "")
                params = json.dumps({'command': message, "OSType": "discord"})
                answer = json.loads(requests.post(f"http://{Settings.get_api_ip()}:{Settings.get_api_port()}/api/ai/check", params).text)
                if "answer" in answer:
                    if len(answer["answer"]) > 4000:
                        for answerLine in str(answer["answer"]).split("/n"):
                            await channel.send(answerLine)
                    else:
                        await channel.send(answer["answer"])
