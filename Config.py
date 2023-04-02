import os


class Config():
    # Bu dəyərləri my.telegram.org saytından əldə edin
    #>>> https://my.telegram.org
    API_ID = int(os.environ.get("API_ID","23255992"))
    API_HASH = os.environ.get("API_HASH","da1c7ce7cfe5cd7e5ebb09cfc981b975")
    BOT_TOKEN = "6186814134:AAGEhd-iLFEeMIpLRiucFA3KjsogGzvix2o"


from telethon import TelegramClient
# Config məlumatları

