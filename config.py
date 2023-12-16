import os


class Config(object):
    TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "")

    APP_ID = int(os.environ.get("APP_ID", 23091810))

    API_HASH = os.environ.get("API_HASH", "c2e7293196031e36a4e4a1b1287c9f30")
