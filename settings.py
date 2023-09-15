import json

class Settings:
    settings = json.load(open("json_files/settings.json"))

    @classmethod
    def get_api_ip(cls):
        return cls.settings["api_ip"]

    @classmethod
    def get_api_port(cls):
        return cls.settings["api_port"]

    @classmethod
    def get_dev_status(cls):
        return cls.settings["dev_status"]

    @classmethod
    def get_bot_name(cls):
        return str(cls.settings["bot_name"]).lower()

    @classmethod
    def get_bot_prefix(cls):
        return cls.settings["bot_prefix"]
