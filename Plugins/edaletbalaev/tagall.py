from Plugins.komekci.edaletconfig import edalet
import os, logging, asyncio
from telethon import events, Button
from telethon.sessions import StringSession
from telethon.tl.types import ChannelParticipantsAdmins
from asyncio import sleep 
import time, random 

 
anlik_calisan = []
rxyzdev_tagTot = {}
rxyzdev_initT = {}
# ---------------------------- Komutlar ---------------------------
@edalet.on(events.NewMessage(pattern="^/cancel$"))
async def cancel_spam(event):
  if not event.chat_id in anlik_calisan:
    return
  else:
    try:
      anlik_calisan.remove(event.chat_id)
    except:
      pass
    return await event.respond('✅ Tağ prosesi uğurla dayandırıldı')

# -------------------Tagger-------------------------------
@edalet.on(events.NewMessage(pattern="^/tag ?(.*)"))
async def mentionall(event):
  global anlik_calisan 
  rxyzdev_tagTot[event.chat_id] = 0
  if event.is_private:
    return await event.respond("Bu əmri yalnız qruplarda və ya kanallarda istifadə edə bilərsiniz.")
  
  admins = []
  async for admin in edalet.iter_participants(event.chat_id, filter=ChannelParticipantsAdmins):
    admins.append(admin.id)
  if not event.sender_id in admins:
    return await event.respond("**Bu əmrdən yalnız idarəçilər istifadə edə bilər. ✋**")
  
  if event.pattern_match.group(1):
    mode = "text_on_cmd"
    msg = event.pattern_match.group(1)
  elif event.reply_to_msg_id:
    mode = "text_on_reply"
    msg = event.reply_to_msg_id
    if msg == None:
        return await event.respond("__Köhnə yazılar üçün üzvləri qeyd edə bilmərəm! (qrupa əlavə edilməzdən əvvəl göndərilən mesajlar)__")
  elif event.pattern_match.group(1) and event.reply_to_msg_id:
    return await event.respond("Mənə mətn ver.")
  else:
    return await event.respond("**Tağı başlamaq üçün səbəb yazın.\n\n(Məsələn: /tag Hamıya Salam!)**")
  
  if mode == "text_on_cmd":
    anlik_calisan.append(event.chat_id)
    usrnum = 0
    usrtxt = ""
    await event.respond("**✅ Etiketləmə prosesi başladı.**")
        
    async for usr in edalet.iter_participants(event.chat_id, aggressive=False):
      rxyzdev_tagTot[event.chat_id] += 1
      usrnum += 1
      usrtxt += f"[{usr.first_name}](tg://user?id={usr.id}),"
      if event.chat_id not in anlik_calisan:
        return
      if usrnum == 6:
        await edalet.send_message(event.chat_id, f"📢 ~ **{msg}**\n\n{usrtxt}")
        await asyncio.sleep(3)
        usrnum = 0
        usrtxt = ""
        
    sender = await event.get_sender()
    rxyzdev_initT = f"[{sender.first_name}](tg://user?id={sender.id})"      
    if event.chat_id in rxyzdev_tagTot:
           a = await event.respond(f"**✅ Teqləmə prosesi uğurla dayandırıldı.**\n\n**Etiklənən İnsanların Sayı:** {rxyzdev_tagTot[event.chat_id]}")
           await sleep(10)
           await a.delete()

  if mode == "text_on_reply":
    anlik_calisan.append(event.chat_id)
    usrnum = 0
    usrtxt = ""
    async for usr in edalet.iter_participants(event.chat_id, aggressive=False):
      rxyzdev_tagTot[event.chat_id] += 1
      usrnum += 1
      usrtxt += f"[{usr.first_name}](tg://user?id={usr.id}),"
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
           a = await event.respond(f"**✅ Teqləmə prosesi uğurla dayandırıldı.**\n\n**Etiklənən İnsanların Sayı:** {rxyzdev_tagTot[event.chat_id]}")
           await sleep(10)
           await a.delete()
