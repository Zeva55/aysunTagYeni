# **🐺 EdaletRoBot**  <img title="PP" height="40" src="https://avatars.githubusercontent.com/u/99437747?v=4">

### **🌐 Əsasən özüm ve bəzi kodları aykhan_s köməyi ilə yazmışam**
</br>

- İçində sadə funksiyalar var.

- Özünü multi bot kimi aparır.

</br>

## Botun init və main fayıllarını telethon üçün yazdığım üçün Telethonla daha rahat olur
</br>

## Örnəy Plugin Telethon üçün:

</br>

```python

from Plugins.komekci.edaletconfig import edalet
from telethon import events, Button
import random

@edalet.on(events.NewMessage(pattern="^/test$"))
async def start(event):
  if event.is_private:
     await event.reply(f"Test dəf kimi işləyir", buttons=(
        [Button.url("👤 Sahib", url="https://t.me/Hasbullahh")],
    ), 


```
</br>

## Örnəy Plugin Pyrogram üçün:

</br>

```python
from Config import Config
from pyrogram.handlers import MessageHandler
from aiohttp import ClientSession
from pyrogram import Client, filters, idle
from pyrogram.types import (
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    Message
)

app = Client(
    'EdaletRoBot',
    bot_token = Config.BOT_TOKEN,
    api_id = Config.API_ID,
    api_hash = Config.API_HASH
)

@app.on_message(filters.command(['start']))
def start(client, message):
    edalet = f'👋 **Salam** Bot işləyir**'
    message.reply_text(
        text=edalet, 
        quote=False,
        reply_markup=InlineKeyboardMarkup(
            [[
                    InlineKeyboardButton('Rəsmi Kanal ✅', url='https://t.me/HasbullaBlog'),
                    InlineKeyboardButton('Music Bot 🎵', url=f'https://t.me/KrayzenMusicbot')
                  ],[
                    InlineKeyboardButton('Sahib 👨🏻‍💻', url=f't.me/Hasbullahh')
                ]
            ]
        )
    )
    


app.run()

```



## **🕹 Qurulum:**

</br>

<p><a href="https://heroku.com/deploy?template=https://github.com/Fakebody31/edaletasistan"><img alt="Heroku" width="52px" src="https://www.nicepng.com/png/full/223-2233246_heroku-logo-salesforce-heroku.png"></p>

</br>

### **📨 Əlaqə :**

[![Github](https://img.shields.io/badge/Github-525252?style=for-the-badge&logo=github)](https://github.com/EdaletRoBot) [![Opensource](https://img.shields.io/badge/Telegram-2CA5E0?style=for-the-badge&logo=telegram&logoColor=white)](https://t.me/edalet_22)

</br>
