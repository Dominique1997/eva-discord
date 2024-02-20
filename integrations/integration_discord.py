import json
import discord
import requests
from secrets import Secrets
from settings import Settings
from discord.ext import commands


bot = commands.Bot(command_prefix=Settings.get_bot_prefix(), intents=discord.Intents.all())


async def send_message(channel, message):
    if str(message).startswith(Settings.get_bot_name()):
        message = str(message).replace(Settings.get_bot_name() + " ", "")
        params = json.dumps({'command': message, "OSType": "discord"})
        answer = json.loads(
            requests.post(f"http://{Settings.get_api_ip()}:{Settings.get_api_port()}/api/ai/check",
                          params).text)
        print(answer)
        if "answer" in answer:
            await channel.typing()
            if len(answer["answer"]) > 4000:
                for answerLine in str(answer["answer"]).split("/n"):
                    await channel.send(answerLine)
            else:
                if str(channel).lower() == "bot-channel":
                    await channel.send("Eva " + answer["answer"])
                else:
                    await channel.send(answer["answer"])
class IntegrationDiscord:
    @classmethod
    def start_bot(cls):
        bot.run(token=Secrets.get_token())

    @bot.event
    async def on_message(ctx):
        channel = ctx.channel
        message = str(ctx.content).lower()
        is_bot = ctx.author.bot
        if is_bot is False:
            await send_message(channel, message)



