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


@edalet.on(events.NewMessage(pattern="^/stag ?(.*)"))
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
    return await event.respond("**Başlamaq üçün səbəbi etiketləyin... ✋\n\n(Nümunə: /stag Hamıya Salam!)**")
  
  if mode == "text_on_cmd":
    anlik_calisan.append(event.chat_id)
    usrnum = 0
    usrtxt = ""
    await event.respond("**✅ Tağ prosesi başladı.**")
        
    async for x in edalet.iter_participants(event.chat_id, aggressive=False):
      rxyzdev_tagTot[event.chat_id] += 1
      usrnum += 1
      usrtxt += f"[{random.choice(ad)}](tg://user?id={x.id}),"
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
      usrtxt += f"[{random.choice(ad)}](tg://user?id={x.id})"
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

ad = ( "Qaş qabağın yerlə gedir",
"De görüm neyləmişəm",
"Ürəyim gup-gup edir",
"Bir günahım yoxdur, inan",
"Varsa – de, olum qurban!",
"Dözmərəm bu hala mən",
"Ölürəm az qala mən",

"Bir mənə bax, naz eyləmə",
"Qaş qabaq tökmə belə",
"Gəl mənə dağ çəkmə belə",

"Kim nə deyib, söylə, görüm",
"Səni yoldan eyləyib?",
"Kim sənə nə danışıb",
"Məni xortdan eyləyib?",
"Hardadır o mərdiməzar?",
"Onu qoy tutsun azar!..",

"Dağlarda duman gözəldir",
"Qaşların - kaman gözəldir",
"Sözünə heç bir söz olmaz",
"Gözlərin yaman gözəldir",
"Alıbdır ağlımı başdan",
"Keçmək olmaz bu göz-qaşdan",
"Səni mən yaman sevirəm",
"Ürəkdən, candan sevirəm",
"Mənə gəl eylə vəfa, yar",
"Aşiqə etmə cəfa, yar",
"Söyüdlər başın əyəndə",
"Sənə mən yarım deyəndə",
"Sanıram dünya mənimdir",
"Gözümə gözün deyəndə",
"Alıbdır ağlımı başdan",
"Keçmək olmaz bu göz-qaşdan",
"Səni mən yaman sevirəm",
"Ürəkdən, candan sevirəm",
"Mənə gəl eylə vəfa, yar",
"Aşiqə etmə cəfa, yar",
"O qara göz olmasaydı",
"Əhdimiz düz olmasaydı",
"Sənə heç könül verərdim",
"Sözümüz söz olmasaydı?",

"Gedirəm bu axşam, gedirəm gülüm",
"Bilirəm gül üzün solacaq mənsiz",
"Gedirəm gəlməsəm qalacaq sevgim",
"Bəlkə də gözlərin dolacaq mənsiz",
"Yaşadır sevdalı bir xəyal məni",
"Gedirəm gəlməsəm yada sal məni",
"Bürüyüb göyləri indi çən, duman",
"Torpaq dilə gəlib aman! ay aman!",
"Vətən gözü yaşlı qalsa o zaman",
"Ay Allah, sevgilim qalacaq mənsiz!",

"Axtarıb tapdım səni ",
"Sən dəmi sevdim, yar, məni? ",
"Gör nə haldır görmür gözüm Şadlığımdan dünyanı",
"Gəl gəl, maralım, gəl",
"Gəl, ceyranım, gəl",
"Halal olsun Süleyman",
"Sən nə kələkbazsan, şeytan!",
"Öyrədib məni yola saldın",
 "Mənə rast gəldi yarcan",
"Dünyaya sığdıra bilmədim inan dərdlərimi",
"Bu qədər dərd içində dərman olub neyləmisən?",
"Hər sözünə can deyən insandan əsər qalmadı Bax",
"Nə fayda Can deməyim canan olub neyləmisən?",
"Düşünrsənmi sən hərdən görəsən nə haldadır?",
"Bəlkə mənsiz çətindədir boranda ya Qardadır",
"Bəlkə də məndən uzağ ölümlərdədi dardadı",
"Düşünmədin nə fayda insan olub neyləmisən?",
"Yanımda yad biri ilə xoşbəxtliyi təsvir edir",
"Səni yadlarla görəndə ruh bədəni təslim edir",
"O qədər dərd içində əzab vermə bəsdi dedim",
"Sənə görə yar ürəyim al-qan olub neyləmisən?",
"Hər gecə xəyalınla yuxuya dalır bu gözlərim",
"Mən səni gecəni gözləyən ulduz qədər gözlədim",
"Bir dəfə heç olmasa yanıma qonaq gəl istədim",
"Hər gecə xəyalımda mehman olub neyləmisən?",
"Sənə çox can dedim ey can,can olub neyləmisən?",
"Demə canan özünə, canan olub neyləmisən?",
"Getmisən daima biganəni şad eyləmisən",
"Həsrətinlə ürəyim al-qan olub, neynəmisən?",
"Bax indi min cür əzab var başımın üstün duman",
"Mənsiz xoşbəxtdir uzaqlarda eylə güman",
"Mən sənə xəyanət etməm düşünmə əsla bir an" ,
"Xoşbəxtliyi bəxş etməyə fərman olub neyləmisən?",
"Həyatım səliqəlidir istəsən dağıt yenidən",
"Çox heyif gör kimləri qonağ eylədin yerimə",
"Artıq çox yorulmuşam dönürəm day geri mən",
"Biryerdə yolu yeriməyə imkan olub neyləmisən?",
"Gül olub neyləmisən bağçalarda qar borandı",
"Sevirəm söyləmə məni inandırma yar yalandı",
"Buludlar qan ağlayır hər gecələr bu nə qandı?",
"Ürəyim həsrətinlə viran olub neyləmisən?",
"Nə xəyalım var idi səninlə sən məhv elədin",
"O qədər qırmısan ki ürəyim səni əhv eləmir",
"Deyirsən qurban olum məni bağışla səhv elədim",
"Hər dəfə səhvinə görə qurban olub neyləmisən?",
)