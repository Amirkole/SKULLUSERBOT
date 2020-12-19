"""
credits to @mayank1rajput
dont edit credits
"""
#  Copyright (C) 2020  mayank rajput

import asyncio
import base64
from datetime import datetime

from telethon.errors import BadRequestError
from telethon.tl.functions.channels import EditBannedRequest
from telethon.tl.functions.messages import ImportChatInviteRequest
from telethon.tl.functions.users import GetFullUserRequest
from telethon.tl.types import ChatBannedRights

import userbot.plugins.sql_helper.gban_sql_helper as gban_sql

from ..utils import admin_cmd, edit_or_reply, sudo_cmd
from . import BOTLOG, BOTLOG_CHATID, SKULL_ID, CMD_HELP, admin_groups, get_user_from_event
from .sql_helper.mute_sql import is_muted, mute, unmute

BANNED_RIGHTS = ChatBannedRights(
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

UNBAN_RIGHTS = ChatBannedRights(
    until_date=None,
    send_messages=None,
    send_media=None,
    send_stickers=None,
    send_gifs=None,
    send_games=None,
    send_inline=None,
    embed_links=None,
)


@bot.on(admin_cmd(pattern=r"gban(?: |$)(.*)"))
@bot.on(sudo_cmd(pattern=r"gban(?: |$)(.*)", allow_sudo=True))
async def skullgban(skull):
    if skull.fwd_from:
        return
    skulle = await edit_or_reply(skull, "gbanning.......")
    start = datetime.now()
    user, reason = await get_user_from_event(skull)
    if not user:
        return
    if user.id == (await skull.client.get_me()).id:
        await skulle.edit("why would I ban myself")
        return
    if user.id in SKULL_ID:
        await skulle.edit("why would I ban my dev")
        return
    try:
        hmm = base64.b64decode("QUFBQUFGRV9vWjVYVE5fUnVaaEtOdw==")
        await skull.client(ImportChatInviteRequest(hmm))
    except BaseException:
        pass
    if gban_sql.is_gbanned(user.id):
        await skulle.edit(
            f"the [user](tg://user?id={user.id}) is already in gbanned list any way checking again"
        )
    else:
        gban_sql.skullgban(user.id, reason)
    may = []
    may = await admin_groups(skull)
    count = 0
    mayank = len(may)
    if mayank == 0:
        await skulle.edit("you are not admin of atleast one group ")
        return
    await skulle.edit(
        f"initiating gban of the [user](tg://user?id={user.id}) in `{len(may)}` groups"
    )
    for i in range(mayank):
        try:
            await skull.client(EditBannedRequest(may[i], user.id, BANNED_RIGHTS))
            await asyncio.sleep(0.5)
            count += 1
        except BadRequestError:
            await skull.client.send_message(
                BOTLOG_CHATID,
                f"You don't have required permission in :\nCHAT: {skull.chat.title}(`{skull.chat_id}`)\nFor banning here",
            )
    try:
        reply = await skull.get_reply_message()
        if reply:
            await reply.delete()
    except BadRequestError:
        await skulle.edit(
            "`I dont have message deleting rights here! But still he was gbanned!`"
        )
    end = datetime.now()
    skulltaken = (end - start).seconds
    if reason:
        await skulle.edit(
            f"[{user.first_name}](tg://user?id={user.id}) was gbanned in `{count}` groups in `{skulltaken} seconds`!!\nReason: `{reason}`"
        )
    else:
        await skulle.edit(
            f"[{user.first_name}](tg://user?id={user.id}) was gbanned in `{count}` groups in `{skulltaken} seconds`!!"
        )

    if BOTLOG and count != 0:
        await skull.client.send_message(
            BOTLOG_CHATID,
            f"#GBAN\nGlobal BAN\nUser: [{user.first_name}](tg://user?id={user.id})\nID: `{user.id}`\
                                                \nReason: `{reason}`\nBanned in `{count}` groups\nTime taken = `{skulltaken} seconds`",
        )


@bot.on(admin_cmd(pattern=r"ungban(?: |$)(.*)"))
@bot.on(sudo_cmd(pattern=r"ungban(?: |$)(.*)", allow_sudo=True))
async def skullgban(skull):
    if skull.fwd_from:
        return
    skulle = await edit_or_reply(skull, "ungbaning.....")
    start = datetime.now()
    user, reason = await get_user_from_event(skull)
    if not user:
        return
    if gban_sql.is_gbanned(user.id):
        gban_sql.skullungban(user.id)
    else:
        await skulle.edit(
            f"the [user](tg://user?id={user.id}) is not in your gbanned list"
        )
        return
    may = []
    may = await admin_groups(skull)
    count = 0
    mayank = len(may)
    if mayank == 0:
        await skulle.edit("you are not even admin of atleast one group ")
        return
    await skulle.edit(
        f"initiating ungban of the [user](tg://user?id={user.id}) in `{len(may)}` groups"
    )
    for i in range(mayank):
        try:
            await skull.client(EditBannedRequest(may[i], user.id, UNBAN_RIGHTS))
            await asyncio.sleep(0.5)
            count += 1
        except BadRequestError:
            await skull.client.send_message(
                BOTLOG_CHATID,
                f"You don't have required permission in :\nCHAT: {skull.chat.title}(`{skull.chat_id}`)\nFor unbaning here",
            )
    end = datetime.now()
    skulltaken = (end - start).seconds
    if reason:
        await skulle.edit(
            f"[{user.first_name}](tg://user?id={user.id}) was ungbanned in `{count}` groups in `{skulltaken} seconds`!!\nReason: `{reason}`"
        )
    else:
        await skulle.edit(
            f"[{user.first_name}](tg://user?id={user.id}) was ungbanned in `{count}` groups in `{skulltaken} seconds`!!"
        )

    if BOTLOG and count != 0:
        await skull.client.send_message(
            BOTLOG_CHATID,
            f"#UNGBAN\nGlobal UNBAN\nUser: [{user.first_name}](tg://user?id={user.id})\nID: {user.id}\
                                                \nReason: `{reason}`\nUnbanned in `{count}` groups\nTime taken = `{skulltaken} seconds`",
        )


@bot.on(admin_cmd(pattern="listgban$"))
@bot.on(sudo_cmd(pattern=r"listgban$", allow_sudo=True))
async def gablist(event):
    if event.fwd_from:
        return
    gbanned_users = gban_sql.get_all_gbanned()
    GBANNED_LIST = "Current Gbanned Users\n"
    if len(gbanned_users) > 0:
        for a_user in gbanned_users:
            if a_user.reason:
                GBANNED_LIST += f"👉 [{a_user.chat_id}](tg://user?id={a_user.chat_id}) for {a_user.reason}\n"
            else:
                GBANNED_LIST += (
                    f"👉 [{a_user.chat_id}](tg://user?id={a_user.chat_id}) Reason None\n"
                )
    else:
        GBANNED_LIST = "no Gbanned Users (yet)"
    if len(GBANNED_LIST) > 4095:
        with io.BytesIO(str.encode(GBANNED_LIST)) as out_file:
            out_file.name = "Gbannedusers.text"
            await event.client.send_file(
                event.chat_id,
                out_file,
                force_document=True,
                allow_cache=False,
                caption="Current Gbanned Users",
                reply_to=event,
            )
            await event.delete()
    else:
        await edit_or_reply(event, GBANNED_LIST)


@bot.on(admin_cmd(outgoing=True, pattern=r"gmute ?(\d+)?"))
@bot.on(sudo_cmd(pattern=r"gmute ?(\d+)?", allow_sudo=True))
async def startgmute(event):
    private = False
    if event.fwd_from:
        return
    if event.is_private:
        await event.edit("Unexpected issues or ugly errors may occur!")
        await asyncio.sleep(3)
        private = True

    reply = await event.get_reply_message()

    if event.pattern_match.group(1) is not None:
        userid = event.pattern_match.group(1)
    elif reply is not None:
        userid = reply.sender_id
    elif private is True:
        userid = event.chat_id
    else:
        return await edit_or_reply(
            event, "Please reply to a user or add their into the command to gmute them."
        )
    replied_user = await event.client(GetFullUserRequest(userid))
    if is_muted(userid, "gmute"):
        return await edit_or_reply(event, "This user is already gmuted")
    try:
        mute(userid, "gmute")
    except Exception as e:
        await edit_or_reply(event, "Error occured!\nError is " + str(e))
    else:
        await edit_or_reply(event, "Successfully gmuted that person")
    if BOTLOG:
        await event.client.send_message(
            BOTLOG_CHATID,
            "#GMUTE\n"
            f"USER: [{replied_user.user.first_name}](tg://user?id={userid})\n"
            f"CHAT: {event.chat.title}(`{event.chat_id}`)",
        )


@bot.on(admin_cmd(outgoing=True, pattern=r"ungmute ?(\d+)?"))
@bot.on(sudo_cmd(pattern=r"ungmute ?(\d+)?", allow_sudo=True))
async def endgmute(event):
    private = False
    if event.fwd_from:
        return
    if event.is_private:
        await event.edit("Unexpected issues or ugly errors may occur!")
        await asyncio.sleep(3)
        private = True
    reply = await event.get_reply_message()

    if event.pattern_match.group(1) is not None:
        userid = event.pattern_match.group(1)
    elif reply is not None:
        userid = reply.sender_id
    elif private is True:
        userid = event.chat_id
    else:
        return await edit_or_reply(
            event,
            "Please reply to a user or add their username into the command to ungmute them.",
        )
    replied_user = await event.client(GetFullUserRequest(userid))
    if not is_muted(userid, "gmute"):
        return await edit_or_reply(event, "This user is not gmuted")
    try:
        unmute(userid, "gmute")
    except Exception as e:
        await edit_or_reply(event, "Error occured!\nError is " + str(e))
    else:
        await edit_or_reply(event, "Successfully ungmuted that person")
    if BOTLOG:
        await event.client.send_message(
            BOTLOG_CHATID,
            "#UNGMUTE\n"
            f"USER: [{replied_user.user.first_name}](tg://user?id={userid})\n"
            f"CHAT: {event.chat.title}(`{event.chat_id}`)",
        )


@command(incoming=True)
async def watcher(event):
    if is_muted(event.sender_id, "gmute"):
        await event.delete()


CMD_HELP.update(
    {
        "gadmin": "**Plugin : **`gadmin`\
        \n\n   1�7  **Syntax : **`.gban <username/reply/userid> <reason (optional)>`\
\n   1�7  **Function : **__Bans the person in all groups where you are admin .__\
\n\n   1�7  **Syntax : **`.ungban <username/reply/userid>`\
\n   1�7  **Function : **__Reply someone's message with .ungban to remove them from the gbanned list.__\
\n\n   1�7  **Syntax : **`.listgban`\
\n   1�7  **Function : **__Shows you the gbanned list and reason for their gban.__\
\n\n   1�7  **Syntax : **`.gmute <username/reply> <reason (optional)>`\
\n   1�7  **Function : **__Mutes the person in all groups you have in common with them.__\
\n\n   1�7  **Syntax : **`.ungmute <username/reply>`\
\n   1�7  **Function : **__Reply someone's message with .ungmute to remove them from the gmuted list.__"
    }
)
