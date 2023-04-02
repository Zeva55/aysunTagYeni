from Plugins.komekci.edaletconfig import edalet
import os, logging, asyncio
from telethon import events, Button
from telethon.sessions import StringSession
from telethon.tl.types import ChannelParticipantsAdmins
from asyncio import sleep
import time, random 

# Silmeyiniz. 
anlik_calisan = []
rxyzdev_tagTot = {}
rxyzdev_initT = {}

@edalet.on(events.NewMessage(pattern="^/cancel$"))
async def cancel_spam(event):
  if not event.chat_id in anlik_calisan:
    return
  else:
    try:
      anlik_calisan.remove(event.chat_id)
    except:
      pass
    return await event.respond('✅ Tağ prosesi uğurla dayandırıldı.')


@edalet.on(events.NewMessage(pattern="^/mafia ?(.*)"))
async def mentionall(event):
  rxyzdev_tagTot[event.chat_id] = 0
  if event.is_private:
    return await event.respond("Bu əmri yalnız qruplarda və ya kanallarda istifadə edə bilərsiniz.")
  
  admins = []
  async for admin in edalet.iter_participants(event.chat_id, filter=ChannelParticipantsAdmins):
    admins.append(admin.id)
  if not event.sender_id in admins:
    return await event.respond("**Bu əmrdən yalnız idarəçilər istifadə edə bilər.**")
  
  if event.pattern_match.group(1):
    mode = "text_on_cmd"
    msg = event.pattern_match.group(1)
  elif event.reply_to_msg_id:
    mode = "text_on_reply"
    msg = event.reply_to_msg_id
    if msg == None:
        return await event.respond("__Köhnə yazılar üçün üzvləri qeyd edə bilmərəm! (qrupa əlavə edilməzdən əvvəl göndərilən mesajlar))__")
  elif event.pattern_match.group(1) and event.reply_to_msg_id:
    return await event.respond("Bana bir metin verin.")
  else:
    return await event.respond("**Başlamaq üçün səbəbi etiketləyin... ✋\n\n(Nümunə: /btag Hamıya Salam!)**")
  
  if mode == "text_on_cmd":
    anlik_calisan.append(event.chat_id)
    usrnum = 0
    usrtxt = ""
    await event.respond("**✅ Tağ prosesi başladı.**")
        
    async for x in edalet.iter_participants(event.chat_id, aggressive=False):
      rxyzdev_tagTot[event.chat_id] += 1
      usrnum += 1
      usrtxt += f"[{random.choice(mafia)}](tg://user?id={x.id}),"
      if event.chat_id not in anlik_calisan:
        return
      if usrnum == 6:
        await edalet.send_message(event.chat_id, f"📢 ~ **{msg}**\n{usrtxt}")
        await asyncio.sleep(3)
        usrnum = 0
        usrtxt = ""
        
    sender = await event.get_sender()
    rxyzdev_initT = f"[{sender.first_name}](tg://user?id={sender.id})"      
    if event.chat_id in rxyzdev_tagTot:
           a = await event.respond(f"**✅ Tağ prosesi uğurla dayandırıldı.**\n\n**Etiket edilmiş şəxslərin sayı:** {rxyzdev_tagTot[event.chat_id]}\n\nReklam üçün @EdaletProject")
           await sleep(10)
           await a.delete()

  if mode == "text_on_reply":
    anlik_calisan.append(event.chat_id)
 
    usrnum = 0
    usrtxt = ""
    async for x in edalet.iter_participants(event.chat_id, aggressive=False):
      rxyzdev_tagTot[event.chat_id] += 1
      usrnum += 1
      usrtxt += f"[{random.choice(mafia)}](tg://user?id={x.id})"
      if event.chat_id not in anlik_calisan:
        return
      if usrnum == 6:
        await edalet.send_message(event.chat_id, usrtxt, reply_to=msg)
        await asyncio.sleep(3)
        usrnum = 0
        usrtxt = ""
    sender = await event.get_sender()
    rxyzdev_initT = f"[{sender.first_name}](tg://user?id={sender.id})"      
    if event.chat_id in rxyzdev_tagTot:
           a = await event.respond(f"**✅ Tağ prosesi uğurla dayandırıldı.**\n\n**Etiket edilmiş şəxslərin sayı:** {rxyzdev_tagTot[event.chat_id]}\n\nReklam üçün @EdaletProject")
           await sleep(10)
           await a.delete()

mafia = (
"Sənin oyundakı rolun 👮🏼 Çavuş!",
"Sənin oyundakı rolun 🐺 Oboroten!",
"Sənin oyundakı rolun 🤓 Satqın!",
"Sənin oyundakı rolun 💃 Məşuqə!",
"Sənin oyundakı rolun 🤵🏼 Mafia!",
"Sənin oyundakı rolun 🧙‍ Maq!",
"Sənin oyundakı rolun 🤞🏼 Şanslı Vətəndaş!",
"Sənin oyundakı rolun 💣 Kamikadze!",
"Sənin oyundakı rolun 👩🏼‍💻 Jurnalist!",
"Sənin oyundakı rolun 🤹🏻 Aferist!",
"Sənin oyundakı rolun 👨🏼 Vətəndaş!",
"Sənin oyundakı rolun 🕵🏼 Komissar Kattani!",
"Sənin oyundakı rolun 🎖 Mer!",
"Sənin oyundakı rolun 🔪 Manyak!",
"Sənin oyundakı rolun 👨🏼‍⚕️️Doktor!",
"Sənin oyundakı rolun 🤵🏻 Don!",
"Sənin oyundakı rolun 🧙🏼 Bomj!",
"Sənin oyundakı rolun 👨🏼‍💼 Vəkil!",
"Sənin oyundakı rolun 🧟 Arsonist!",
"Sənin oyundakı rolun 🕴️ Qatil!",
"Sənin oyundakı rolun 🧝🏻‍♀️Şəhzadə!",
"Sənin oyundakı rolun 🧟‍♀️Cadugar!",
"Sənin oyundakı rolun 🧛🏻‍♂️Vampir!",
"Sənin oyundakı rolun 🧚🏻‍♀️Mələk!",
"Sənin oyundakı rolun 🦹🏻‍♂️BOSS!",
"Sənin oyundakı rolun 🦦Köstəbək!",
"Sənin oyundakı rolun 🦎Buqələmun!",
"Sənin oyundakı rolun 🤡Joker!",
"Sənin oyundakı rolun 🙍🏻‍♂️Məhbus!",
"Sənin oyundakı rolun 🙇🏻‍♂️Oğru!",
"Sənin oyundakı rolun 🕵️Suiqəstçi!",
"Sənin oyundakı rolun 🔮Reviver!",
"Sənin oyundakı rolun 👷🏻‍♂️Mədənçi!",
"Sənin oyundakı rolun 💂Killer!",
"Sənin oyundakı rolun 👻Ruh!",
"Sənin oyundakı rolun 👳🏻‍♂️Satıcı!",
"Sənin oyundakı rolun 👨🏻‍🦱Dedektiv!",
"Sənin oyundakı rolun  👨🏻‍🎤Specialist!",
"Sənin oyundakı rolun ⭐️General!",
"Sənin oyundakı rolun 🥷Ninja!"
) 
