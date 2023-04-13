import os


class Config():
    # Bu dəyərləri my.telegram.org saytından əldə edin
    #>>> https://my.telegram.org
    API_ID = int(os.environ.get("API_ID","26041892"))
    API_HASH = os.environ.get("API_HASH","b25edf599fd7a94f8d84ce3e4422f409")
    BOT_TOKEN = "6041859157:AAHNOk1endHo7m_U48vNdNaASYyL0Y3HcDw"


from telethon import TelegramClient
# Config məlumatları

