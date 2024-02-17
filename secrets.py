import json
from settings import Settings

class Secrets:
    secrets = json.load(open("json_files/secrets.json"))
    @classmethod
    def get_token(cls):
        if Settings.get_dev_status():
            return cls.secrets["dev_token"]
        return cls.secrets["main_token"]
