# Reponu öz adına çıxardan ve menden xebersiz satan peyserdi t.me/edalet_22

from telethon import events
import asyncio
import random
from telethon import events
from Plugins.komekci.edaletconfig import edalet

@edalet.on(events.NewMessage(pattern="^/id ?(.*)"))
async def id(event):
    if event.reply_to_msg_id:
        previous_message = await event.get_reply_message()
        user_id = previous_message.sender_id
        chat_id = event.chat_id
        if event.is_private:
            return await event.reply(f"**Sizin Telegram id:** `{user_id}`")
        else:
            return await event.reply(f"**İstifadəçi id:** `{user_id}`\n**Qrup id:** `{chat_id}`")

#Edalet_22 
    else:
        user_id = event.sender_id
        chat_id = event.chat_id
        if event.is_private:
            return await event.reply(f"**Sizin Telegram id:** `{user_id}`")
        else:
            return await event.reply(f"**İstifadəçi id:** `{user_id}`\n**Qrup id:** `{chat_id}`")

print("Id qoz kimidi")
