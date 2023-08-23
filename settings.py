import json

class Settings:
    settings = json.load(open("settings.json"))

    @classmethod
    def get_api_ip(cls):
        return cls.settings["api_ip"]

    @classmethod
    def get_api_port(cls):
        return cls.settings["api_port"]

    @classmethod
    def get_dev_status(cls):
        if cls.settings["dev_status"] == "False":
            return True
        return False

    @classmethod
    def get_bot_name(cls):
        return str(cls.settings["bot_name"]).lower()

    @classmethod
    def get_bot_prefix(cls):
        return cls.settings["bot_prefix"]
