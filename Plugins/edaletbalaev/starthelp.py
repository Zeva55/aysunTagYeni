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
     await event.reply(f"Salam 👋🏻 mən çox funksiyalı tağ botuyam\nƏtraflı məlumat üçün '📮 Əmrlər' bölməsinə daxil olun\n\n🎯 Belə bot istəyirsən?\n📥 Yaz: @Nehmedov\n\n ⚙️ Qrupumuz: @PopularGrup ", buttons=(
                     [Button.url('➕ Məni Qrupa əlavə et ➕','http://t.me/AysunTagBot?startgroup=a')],
                     [Button.inline(f"Əmrlər 📮", data="help")],
                     [Button.url('Support 🎴', 'https://t.me/ilkinsupport'),
                      Button.url('Sahib 👨‍💻', 'https://t.me/Nehmedov')],
                    ),
                    link_preview=False)



  if event.is_group:
    return await edalet.send_message(event.chat_id, f"** [𝐀𝐲𝐬𝐮𝐧 💕](http://t.me/AysunTagBot)'un Əmrlər üçün?.Bot'a daxil olub.**", buttons=(
                     [Button.url('💡Bota Keç','https://t.me/AysunTagBot?start=start')],
               [Button.url('Sahib 👨‍💻', 'https://t.me/Nehmedov'),
          Button.url('Support 🎴', 'https://t.me/ilkinsupport')],
                    ),
                    link_preview=False)


@edalet.on(events.callbackquery.CallbackQuery(data="start"))
async def handler(event):
    async for usr in edalet.iter_participants(event.chat_id):
     ad = f"[{usr.first_name}](tg://user?id={usr.id}) "
     await event.edit(f"Salam 👋🏻 mən çox funksiyalı tağ botuyam\nƏtraflı məlumat üçün '📮 Əmrlər' bölməsinə daxil olun\n\n🎯 Belə bot istəyirsən?\n📥 Yaz: @Nehmedov\n\n ⚙️ Qrupumuz: @PopularGrup ", buttons=(
                     [Button.url('➕ Məni Qrupa əlavə et ➕','http://t.me/AysunTagBot?startgroup=a')],
                 [Button.inline(f"Əmrlər 📮", data="help")],
                 [Button.url('Support 🎴', 'https://t.me/ilkinsupport'),
                      Button.url('Sahib 👨‍💻', 'https://t.me/Nehmedov')],
                    ),
                    link_preview=False)


@edalet.on(events.callbackquery.CallbackQuery(data="help"))
async def handler(event):   
    await event.edit(f"📮 Tağ əmirləri bunlardır 📮\n\n\n•━━━━━━━━•••━━━━━━━━•\n🕹 Əmr : /tag \n📜 Açıqlama :<səbəb> - 5-li Tag Atışları.\n🕹 Əmr :  /etag \n📜 Açıqlama :<səbəb> - Emoji ilə etiketlər.\n🕹 Əmr : /stag\n📜 Açıqlama : <səbəb> - Söz'lü Tag etiketlər.\n🕹 Əmr :  /btag\n 📜 Açıqlama : <səbəb> - bayrağlar ilə etiketlər.\n🕹 Əmr :  /mafia\n📜 Açıqlama : <səbəb> - Mafia oyunun rolları ilə etiketlər.\n🕹 Əmr :  /adtag\n📜 Açıqlama : <səbəb> - Marağlı adlar ilə etiket atar.\n🕹 Əmr :  /aysun \n📜 Açıqlama : <səbəb> - Maraglı sözlər ilə tag eder. \n🕹 Əmr :  /tektag \n📜 Açıqlama : <səbəb> - Üzvləri Tək-Tək etiketlər.\n🕹 Əmr :  /admins \n📜 Açıqlama : <səbəb> -İdarəçilər Tək-Tək etiketlər.\n🕹 Əmr :  /cancel \n📜 Açıqlama :  Tag Ələməyi Dayandır.\n", buttons=(
                 [Button.url('Qrup💬', 'https://t.me/ilkinsupport'),
                      Button.url('Sahib 👨‍💻', 'https://t.me/Nehmedov')],
                 [Button.inline(f"🔙 Geri", data="start")]
                    ),
                    link_preview=False)
