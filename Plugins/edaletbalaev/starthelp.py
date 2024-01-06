# Reponu öz adına çıxardan ve menden xebersiz satan peyserdi t.me/edalet_22

from Plugins.komekci.edaletconfig import edalet
from telethon import events, Button
from telethon.tl.types import ChannelParticipantsAdmins
import random
#
from requests import get, post
from os import remove
from telethon.tl.functions.users import GetFullUserRequest
from time import time



@edalet.on(events.NewMessage(pattern="^/start$"))
async def start(event):
  if event.is_private:
    async for usr in edalet.iter_participants(event.chat_id):
     ad = f"[{usr.first_name}](tg://user?id={usr.id}) "
     await event.reply(f"Salam 👋🏻 mən çox funksiyalı tağ botuyam\nƏtraflı məlumat üçün '📮 Əmrlər' bölməsinə daxil olun\n\n🎯 Belə bot istəyirsən?\n📥 Yaz: @Thisisgalka\n\n ⚙️ Resmi Kanal: @PalmasBots ", buttons=(
                     [Button.url('➕ Məni Qrupa əlavə et ➕','http://t.me/PalmasTaggerBot?startgroup=a')],
                     [Button.inline(f"Əmrlər", data="help")],
                     [Button.url('Support', 'https://t.me/PalmasBotsSupport')]
                    ),
                    link_preview=False)



  if event.is_group:
    return await galka.send_message(event.chat_id, f"** [Palmas](http://t.me/PalmasTaggerBot)'un Əmrlər üçün?.Bot'a daxil olub.**", buttons=(
                     [Button.url('💡Bota Keç','https://t.me/PalmasTaggerBot?start=start')]
          Button.url('Support', 'https://t.me/KrayzenSupport')],
                    ),
                    link_preview=False)


@edalet.on(events.callbackquery.CallbackQuery(data="start"))
async def handler(event):
    async for usr in edalet.iter_participants(event.chat_id):
     ad = f"[{usr.first_name}](tg://user?id={usr.id}) "
     await event.edit(f"Salam 👋🏻 mən çox funksiyalı tağ botuyam\nƏtraflı məlumat üçün '📮 Əmrlər' bölməsinə daxil olun\n\n🎯 Belə bot istəyirsən?\n📥 Yaz: @Thisisgalka\n\n ⚙ Kanal: @PalmasBots ", buttons=(
                     [Button.url('➕ Məni Qrupa əlavə et ➕','http://t.me/PalmasTaggerBot?startgroup=a')],
                 [Button.inline(f"Əmrlər", data="help")],
                 [Button.url('Support', 'https://t.me/PalmasBotsSupport')]
                    )
                    link_preview=False)


@edalet.on(events.callbackquery.CallbackQuery(data="help"))
async def handler(event):   
    await event.edit(f"📮 Tağ əmirləri bunlardır 📮\n\n\n•━━━━━━━━•••━━━━━━━━•\n🕹 Əmr : /tag \n📜 Açıqlama :<səbəb> - 5-li Tag Atışları.\n🕹 Əmr :  /etag \n📜 Açıqlama :<səbəb> - Emoji ilə etiketlər.\n🕹 Əmr : /stag\n📜 Açıqlama : <səbəb> - Söz'lü Tag etiketlər.\n🕹 Əmr :  /btag\n 📜 Açıqlama : <səbəb> - bayrağlar ilə etiketlər.\n🕹 Əmr :  /mafia\n📜 Açıqlama : <səbəb> - Mafia oyunun rolları ilə etiketlər.\n🕹 Əmr :  /adtag\n📜 Açıqlama : <səbəb> - Marağlı adlar ilə etiket atar.\n🕹 Əmr :  /Bayram \n📜 Açıqlama : <səbəb> - Maraglı sözlər ilə tag eder. \n🕹 Əmr :  /tektag \n📜 Açıqlama : <səbəb> - Üzvləri Tək-Tək etiketlər.\n🕹 Əmr :  /admins \n📜 Açıqlama : <səbəb> -İdarəçilər Tək-Tək etiketlər.\n🕹 Əmr :  /cancel \n📜 Açıqlama :  Tag Ələməyi Dayandır.\n", buttons=(
                 [Button.url('Rəsmi Kanal', 'https://t.me/PalmasBots'),
                 [Button.inline(f"🔙 Geri", data="start")]
                    ),
                    link_preview=False)
