import json

class Settings:
    settings = json.load(open("settings.json"))

    @classmethod
    def get_api_ip(cls):
        return cls.settings["api_ip"]

    @classmethod
    def get_api_port(cls):
        return cls.settings["api_port"]