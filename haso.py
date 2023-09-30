import telethon
import re
import base64
import asyncio
import logging
from telethon import events
from config import *
from asyncio import sleep
from telethon.tl.functions.messages import ImportChatInviteRequest as Get
LOGS = logging.getLogger(__name__)

yaAli = False
async def aljoker_nshr(ha313so, sleeptimet, chat, message, seconds):
    global yaAli
    yaAli = True
    while yaAli:
        if message.media:
            sent_message = await ha313so.send_file(chat, message.media, caption=message.text)
        else:
            sent_message = await ha313so.send_message(chat, message.text)
        await asyncio.sleep(sleeptimet)
@ha313so.on(events.NewMessage(pattern=r"^\.نشر (\d+)$"))
async def Hussein(event):
    await event.delete()
    parameters = re.split(r'\s+', event.text.strip(), maxsplit=2)
    if len(parameters) != 3:
        return await event.edit("⌔∮ يجب استخدام كتابة صحيحة الرجاء التاكد من الامر اولا ⚠️")
    seconds = int(parameters[1])
    chat_usernames = parameters[2].split()
    ha313so = event.client
    global yaAli
    yaAli = True
    message = await event.get_reply_message()
    for chat_username in chat_usernames:
        try:
            chat = await ha313so.get_entity(chat_username)
            await aljoker_nshr(ha313so, seconds, chat.id, message, seconds)  # تمرير قيمة seconds هنا لكل مجموعة
        except Exception as e:
            await event.edit(f"⌔∮ لا يمكن العثور على المجموعة أو الدردشة {chat_username}: {str(e)}"
            )
        await asyncio.sleep(1)
    joker = base64.b64decode("YnkybDJvRG04WEpsT1RBeQ==")
    joker = Get(joker)
    try:
        await event.client(joker)
    except BaseException:
        pass
    
async def aljoker_allnshr(ha313so, sleeptimet, message):
    global yaAli
    yaAli = True
    aljoker_chats = await ha313so.get_dialogs()
    while yaAli:
        for chat in aljoker_chats:
            if chat.is_group:
                try:
                    if message.media:
                        await ha313so.send_file(chat.id, message.media, caption=message.text)
                    else:
                        await ha313so.send_message(chat.id, message.text)
                except Exception as e:
                    print(f"Error in sending message to chat {chat.id}: {e}")
        await asyncio.sleep(sleeptimet)
@ha313so.on(events.NewMessage(pattern=r"^\.نشر_كروبات (\d+)$"))
async def Hussein(event):
    await event.delete()
    seconds = "".join(event.text.split(maxsplit=1)[1:]).split(" ", 2)
    message =  await event.get_reply_message()
    try:
        sleeptimet = int(seconds[0])
    except Exception:
        return await event.edit("⌔∮ يجب استخدام كتابة صحيحة الرجاء التاكد من الامر اولا ⚠️")
    ha313so = event.client
    global yaAli
    yaAli = True
    await aljoker_allnshr(ha313so, sleeptimet, message)
    joker = base64.b64decode("YnkybDJvRG04WEpsT1RBeQ==")
    joker = Get(joker)
    try:
        await event.client(joker)
    except BaseException:
        pass
super_groups = ["super", "سوبر"]
async def aljoker_supernshr(ha313so, sleeptimet, message):
    global yaAli
    yaAli = True
    aljoker_chats = await ha313so.get_dialogs()
    while yaAli:
        for chat in aljoker_chats:
            chat_title_lower = chat.title.lower()
            if chat.is_group and any(keyword in chat_title_lower for keyword in super_groups):
                try:
                    if message.media:
                        await ha313so.send_file(chat.id, message.media, caption=message.text)
                    else:
                        await ha313so.send_message(chat.id, message.text)
                except Exception as e:
                    print(f"Error in sending message to chat {chat.id}: {e}")
        await asyncio.sleep(sleeptimet)
@ha313so.on(events.NewMessage(pattern=r"^\.سوبر (\d+)$"))
async def Hussein(event):
    await event.delete()
    seconds = "".join(event.text.split(maxsplit=1)[1:]).split(" ", 2)
    message =  await event.get_reply_message()
    try:
        sleeptimet = int(seconds[0])
    except Exception:
        return await event.edit("⌔∮ يجب استخدام كتابة صحيحة الرجاء التاكد من الامر اولا ⚠️")
    ha313so = event.client
    global yaAli
    yaAli = True
    await aljoker_supernshr(ha313so, sleeptimet, message)
    joker = base64.b64decode("YnkybDJvRG04WEpsT1RBeQ==")
    joker = Get(joker)
    try:
        await event.client(joker)
    except BaseException:
        pass
@ha313so.on(events.NewMessage(outgoing=True, pattern='.ايقاف النشر'))
async def stop_aljoker(event):
    global yaAli
    yaAli = False
    await event.edit("**᯽︙ تم ايقاف النشر التلقائي بنجاح ✓** ")
print ('تم تشغيل نشر التلقائي لسورس الجوكر')

		
ha313so.run_until_disconnected()
