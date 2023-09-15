import json


class Secrets:
    secrets = json.load(open("json_files/secrets.json"))
    @classmethod
    def get_main_token(cls):
        return cls.secrets["main_token"]

    @classmethod
    def get_dev_token(cls):
        return cls.secrets["dev_token"]