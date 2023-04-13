# Reponu öz adına çıxardan ve menden xebersiz satan peyserdi t.me/edalet_22

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


@edalet.on(events.NewMessage(pattern="^/aysun ?(.*)"))
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
    return await event.respond("**Başlamaq üçün səbəbi etiketləyin... ✋\n\n(Nümunə: /aysun Hamıya Salam!)**")
  
  if mode == "text_on_cmd":
    anlik_calisan.append(event.chat_id)
    usrnum = 0
    usrtxt = ""
    await event.respond("**✅ Tağ prosesi başladı.**")
        
    async for x in edalet.iter_participants(event.chat_id, aggressive=False):
      rxyzdev_tagTot[event.chat_id] += 1
      usrnum += 1
      usrtxt += f"[{random.choice(usta)}](tg://user?id={x.id}),"
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
      usrtxt += f"[{random.choice(usta)}](tg://user?id={x.id})"
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

usta = ('Seni Sevirem😍','🙄Haralisan','🙄 Sən dediyim sözü elədin? 😐','Həyatımın dolması 🥲 nassın😍','Mənə niyə elə baxırsan? 🌝','İkinci planda olmaqdansa, plana daxil olmamağı seçərəm.  🎯','səni basqa qrublardada görmüsdüm ','Ac olanda sən o sən deyilsən','Niyə yalan danışırsan adamın üstündə patalok var','Həci necəsən ficuuu ','köhnə məkanın yeni sakini ','günün günnən durdun uzax de görüm haramı bəyənmədin','deyrlər ölübsən🤔','Güçlüyüm... Çünkü başka seçeneğim yok düşersem tutanım olmayacak biliyorum...🚬','gəl bir birimizi arka sokaklar bitənə qədər sevək❤️','corona belə böyüdü sən böyümədin','corona belə unduldu səni unuda bilmədim🚬','səni sevirəm sözündə neçə dənə samit var','oğlanlar niyə az yaşayır','bitkilər yaşlandıqcamı ölər yoxsa baxımsızlıqdanmı','isti havada çay içirsən hələdə','allah rəhmət eləsin','tez gəlin hədiyyəli yarışımız basladı','Benim hayelerim kelebeğin ömrü kadar yaşar 💔🥀','Çiçəklərə aşağıdan baxmağa gedirəm..➰','susмuş вir qadın üçün... вiтмiş вir adaмsan.! 🖤','𝚂ə𝚏𝚕ə𝚛𝚒𝚗𝚒 𝚞̈𝚣𝚕ə𝚛𝚒𝚗ə 𝚟𝚞𝚛𝚖𝚊𝚍𝚒𝚐̆𝚒𝚖𝚒𝚣 𝚞̈𝚌̧𝚞̈𝚗 𝚘̈𝚣𝚕𝚎𝚛𝚒𝚗𝚒 𝚚𝚞̈𝚜𝚞𝚛𝚜𝚞𝚣 𝚜𝚊𝚗𝚊𝚗 𝚒𝚗𝚜𝚊𝚗𝚕𝚊𝚛 𝚟𝚊𝚛😒','Güclü olmağa məndən daha çox ehtiyacın var, çünki haqsız olduğunu ürəyinin bir yerində bilirsən.🤙','Makiyaj və üz boyalarınıza güvənməyin. Yollar da gözəldir, lakin altından kanalizasiya keçir.👋😉','𝙸̇𝚝𝚒𝚛𝚍𝚒𝚢𝚒𝚗 𝚟𝚊𝚡𝚝𝚒 𝚚𝚊𝚢𝚝𝚊𝚛𝚊 𝚋𝚒𝚕𝚖ə𝚍𝚒𝚢𝚒𝚗 𝚔𝚒𝚖𝚒 𝚎𝚕ə𝚍𝚒𝚢𝚒𝚗 𝚙𝚒𝚜𝚕𝚒𝚢𝚒 𝚍ə 𝚑𝚎𝚌̧ 𝚟𝚊𝚡𝚝 𝚍𝚞̈𝚣ə𝚕𝚍ə 𝚋𝚒𝚕𝚖𝚎𝚢ə𝚌𝚎𝚔𝚜ən😐','𝙱𝚒𝚛𝚊𝚣 𝚒𝚗𝚜𝚊𝚗 𝚘𝚕 𝚍𝚎𝚢e𝚌ə𝚖 𝚊𝚖𝚖𝚊 𝚜ə𝚗𝚒 𝚍ə 𝚌̧ə𝚝𝚒𝚗 𝚟ə𝚣𝚒𝚢𝚢ə𝚝𝚍ə 𝚚𝚘𝚢𝚖𝚊𝚐̆ 𝚒𝚜𝚝ə𝚖𝚒𝚛ə𝚖🤧','İnsanlığa dəvət etdikdə yolu soruşan insanlar var.🔥😂','Qoyduğum şeyləri öz yerində tapa bilmirəm. Bəzilərini adam yerinə qoydum, indi gəl tap görün necə tapırsan✊','Ayə biri bunu aparsın🫢','Əgər bu həyatda öz tayını tapa bilmirsənsə üzülmə, deməli sən tayı bərabəri olmayan birisən.Qabriel Qarsia Markuez (Meksikalı yazıçı)🥲','Xoş Gəldim Nəfəs🥲','Gəlmirsən Balaca😒','Kimə Yazısan??? 🤨','Çirkin Çocuq Gəl😌','Cikolatam😍','Aaa Səndə Burdasan😳','Al Sənə Çikolata🤓👉🍫','Sevmirsən Məni?🙁 Onda Ol🙂','Haa Düz derisən?🧐','Bu Kimdir😁','Gəl Dava Edəx😁💪','Bax Sənə Nə Aldım😌👉🐒','Nə Gözəlsən🤢 Çirkin Ördək Yavrusu','Sən Kimsən🙄A Gədə👀','Gəl Sənə Sürpürüzüm var🤫','Ooo Çox Gözəlsin🤌🤐Bal','Şəxsiyə Yaz😌dünbələx','Gəl Görüm Hələ🧐 Nə demisən Mənə😬','Ayib Olsun😫 Niyə Yazmırsan😑','Bezdim Səndən🥲','Bu Neçədir✌️🙂','Nömrəni ver də Vpda yazışa🙊','👉👀 Gözün Çıxsın gəl😒','ımmm Gəl yogo yapalım🧘‍♀🤭','gəl sənə bıra süzdüm😪🍻','Ağlımı Başımdan ala şəxs😵‍💫gəl mənə doğru','Səni gördüm qızmam qalxdə🤒',) 
