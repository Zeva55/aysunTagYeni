# Reponu öz adına çıxardan ve menden xebersiz satan peyserdi t.me/edalet_22
#edalet_22
from Plugins.komekci.edaletconfig import edalet
from telethon import events
from os import remove
from telethon.tl.functions.users import GetFullUserRequest
from telethon.tl.types import ChannelParticipantsBots
from telethon.tl.types import ChannelParticipantsAdmins


@edalet.on(events.NewMessage(pattern="^/bots ?(.*)"))
async def bots(event):
    if not event.is_group:
        return await event.reply("Bu əmr qruplar üçün etibarlıdır!")
    info = await event.client.get_entity(event.chat_id)
    title = info.title if info.title else "This chat"
    mentions = f'**{title}** qrupunda olan botlar:\n'
    async for user in event.client.iter_participants(event.chat_id, filter=ChannelParticipantsBots):
        if not user.deleted:
            mentions += f"\n➪ [{user.first_name}](tg://user?id={user.id})"
        else:
            mentions += f"\n➪ Silinmiş Bot `{user.id}`"
    await event.reply(mentions)

    
    
@edalet.on(events.NewMessage(pattern="^/admins ?(.*)"))
async def tag_admin(event):
    if not event.is_group:
        return await event.reply("Bu əmr qruplar üçün etibarlıdır!")
    chat = await event.get_input_chat()
    text = "꧁Adminlər Siyahısı꧂\n"
    async for x in event.client.iter_participants(chat, 100, filter=ChannelParticipantsAdmins):
        text += f" \n ➪ [{x.first_name}](tg://user?id={x.id})"
    if event.reply_to_msg_id:
        await event.client.send_message(event.chat_id, text, reply_to=event.reply_to_msg_id)
    else:
        await event.reply(text)
    raise StopPropagation

print("Bost ve Admins listide isleyir")
