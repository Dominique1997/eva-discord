import json
import discord
import pyttsx3
import requests
from urllib import parse
from discord import utils
from secrets import Secrets
from settings import Settings
from discord.ext import commands
from discord import FFmpegPCMAudio


bot = commands.Bot(command_prefix=Settings.get_bot_prefix(), intents=discord.Intents.all())
engine = pyttsx3.init()


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
        await bot.get_channel(1118164745871179926).connect()

    @bot.event
    async def on_message(ctx):
        channel = ctx.channel
        channelType = str(ctx.channel.type)
        message = str(ctx.content).lower()
        author = ctx.author.name
        if Settings.get_bot_name() != author:
            if str(message).startswith(Settings.get_bot_name()):
                message = str(message).replace(Settings.get_bot_name() + " ", "")
                params = {'sentence': message}
                answer = json.loads(requests.get(f"http://{Settings.get_api_ip()}:{Settings.get_api_port()}/api/discord/check_command?{parse.urlencode(params)}").text)
                if "answer" in answer:
                    if channelType != "voice":
                        channel.typing()
                        await channel.send(answer["answer"])
                    else:
                        engine.save_to_file(answer["answer"], "answer.wav")
                        engine.runAndWait()
                        voice = utils.get(bot.voice_clients, guild=bot.get_guild(1085854249147187220))
                        source = FFmpegPCMAudio("answer.wav")
                        audio = voice.play(source)
                else:
                    if str(answer["answer"]).startswith("Wolfram Alpha"):
                        if channelType != "voice":
                            await channel.send(str(answer["error"]).replace("Wolfram Alpha", "I am sorry. I"))
                    else:
                        if channelType != "voice":
                            await channel.send(answer["error"])
