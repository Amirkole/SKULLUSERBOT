# credits to @mayank1rajput

#  Copyright (C) 2020  mayank rajput
import asyncio
import base64
import os
import re

from telethon.tl.functions.messages import ImportChatInviteRequest as Get

from ..utils import admin_cmd, edit_or_reply, sudo_cmd
from . import (
    CMD_HELP,
    changemymind,
    deEmojify,
    fakegs,
    kannagen,
    moditweet,
    reply_id,
    trumptweet,
    tweets,
)


@bot.on(admin_cmd(outgoing=True, pattern="fakegs(?: |$)(.*)", command="fakegs"))
@bot.on(sudo_cmd(allow_sudo=True, pattern="fakegs(?: |$)(.*)", command="fakegs"))
async def nekobot(skull):
    if skull.fwd_from:
        return
    text = skull.pattern_match.group(1)
    reply_to_id = await reply_id(skull)
    if not text:
        if skull.is_reply and not reply_to_id.media:
            text = reply_to_id.message
        else:
            await edit_delete(skull, "`What should i search in google.`", 5)
            return
    skulle = await edit_or_reply(skull, "`Connecting to https://www.google.com/ ...`")
    text = deEmojify(text)
    if ";" in text:
        search, result = text.split(";")
    else:
        await edit_delete(
            skull,
            "__How should i create meme follow the syntax as show__ `.fakegs top text ; bottom text`",
            5,
        )
        return
    skullfile = await fakegs(search, result)
    await asyncio.sleep(2)
    await skull.client.send_file(skull.chat_id, skullfile, reply_to=reply_to_id)
    await skulle.delete()
    if os.path.exists(skullfile):
        os.remove(skullfile)


@bot.on(admin_cmd(outgoing=True, pattern="trump(?: |$)(.*)", command="trump"))
@bot.on(sudo_cmd(allow_sudo=True, pattern="trump(?: |$)(.*)", command="trump"))
async def nekobot(skull):
    if skull.fwd_from:
        return
    text = skull.pattern_match.group(1)
    text = re.sub("&", "", text)
    reply_to_id = await reply_id(skull)
    hmm = base64.b64decode("QUFBQUFGRV9vWjVYVE5fUnVaaEtOdw==")
    reply = await skull.get_reply_message()
    if not text:
        if skull.is_reply and not reply.media:
            text = reply.message
        else:
            await edit_delete(skull, "**Trump : **`What should I tweet`", 5)
            return
    skulle = await edit_or_reply(skull, "`Requesting trump to tweet...`")
    try:
        hmm = Get(hmm)
        await skull.client(hmm)
    except BaseException:
        pass
    text = deEmojify(text)
    await asyncio.sleep(2)
    skullfile = await trumptweet(text)
    await skull.client.send_file(skull.chat_id, skullfile, reply_to=reply_to_id)
    await skulle.delete()
    if os.path.exists(skullfile):
        os.remove(skullfile)


@bot.on(admin_cmd(outgoing=True, pattern="modi(?: |$)(.*)", command="modi"))
@bot.on(sudo_cmd(allow_sudo=True, pattern="modi(?: |$)(.*)", command="modi"))
async def nekobot(skull):
    if skull.fwd_from:
        return
    text = skull.pattern_match.group(1)
    text = re.sub("&", "", text)
    reply_to_id = await reply_id(skull)
    hmm = base64.b64decode("QUFBQUFGRV9vWjVYVE5fUnVaaEtOdw==")
    reply = await skull.get_reply_message()
    if not text:
        if skull.is_reply and not reply.media:
            text = reply.message
        else:
            await edit_delete(skull, "**Modi : **`What should I tweet`", 5)
            return
    skulle = await edit_or_reply(skull, "Requesting modi to tweet...")
    try:
        hmm = Get(hmm)
        await skull.client(hmm)
    except BaseException:
        pass
    text = deEmojify(text)
    await asyncio.sleep(2)
    skullfile = await moditweet(text)
    await skull.client.send_file(skull.chat_id, skullfile, reply_to=reply_to_id)
    await skulle.delete()
    if os.path.exists(skullfile):
        os.remove(skullfile)


@bot.on(admin_cmd(outgoing=True, pattern="cmm(?: |$)(.*)", command="cmm"))
@bot.on(sudo_cmd(allow_sudo=True, pattern="cmm(?: |$)(.*)", command="cmm"))
async def nekobot(skull):
    if skull.fwd_from:
        return
    text = skull.pattern_match.group(1)
    text = re.sub("&", "", text)
    reply_to_id = await reply_id(skull)
    hmm = base64.b64decode("QUFBQUFGRV9vWjVYVE5fUnVaaEtOdw==")
    reply = await skull.get_reply_message()
    if not text:
        if skull.is_reply and not reply.media:
            text = reply.message
        else:
            await edit_delete(skull, "`Give text to write on banner, man`", 5)
            return
    skulle = await edit_or_reply(skull, "`Your banner is under creation wait a sec...`")
    try:
        hmm = Get(hmm)
        await skull.client(hmm)
    except BaseException:
        pass
    text = deEmojify(text)
    await asyncio.sleep(2)
    skullfile = await changemymind(text)
    await skull.client.send_file(skull.chat_id, skullfile, reply_to=reply_to_id)
    await skulle.delete()
    if os.path.exists(skullfile):
        os.remove(skullfile)


@bot.on(admin_cmd(outgoing=True, pattern="kanna(?: |$)(.*)", command="kanna"))
@bot.on(sudo_cmd(allow_sudo=True, pattern="kanna(?: |$)(.*)", command="kanna"))
async def nekobot(skull):
    if skull.fwd_from:
        return
    text = skull.pattern_match.group(1)
    text = re.sub("&", "", text)
    reply_to_id = await reply_id(skull)
    hmm = base64.b64decode("QUFBQUFGRV9vWjVYVE5fUnVaaEtOdw==")
    reply = await skull.get_reply_message()
    if not text:
        if skull.is_reply and not reply.media:
            text = reply.message
        else:
            await edit_delete(skull, "**Kanna : **`What should i show you`", 5)
            return
    skulle = await edit_or_reply(skull, "`Kanna is writing your text...`")
    try:
        hmm = Get(hmm)
        await e.client(hmm)
    except BaseException:
        pass
    text = deEmojify(text)
    await asyncio.sleep(2)
    skullfile = await kannagen(text)
    await skull.client.send_file(skull.chat_id, skullfile, reply_to=reply_to_id)
    await skulle.delete()
    if os.path.exists(skullfile):
        os.remove(skullfile)


@bot.on(admin_cmd(outgoing=True, pattern="tweet(?: |$)(.*)", command="tweet"))
@bot.on(sudo_cmd(allow_sudo=True, pattern="tweet(?: |$)(.*)", command="tweet"))
async def nekobot(skull):
    if skull.fwd_from:
        return
    text = skull.pattern_match.group(1)
    text = re.sub("&", "", text)
    reply_to_id = await reply_id(skull)
    hmm = base64.b64decode("QUFBQUFGRV9vWjVYVE5fUnVaaEtOdw==")
    reply = await skull.get_reply_message()
    if not text:
        if skull.is_reply and not reply.media:
            text = reply.message
        else:
            await edit_delete(
                skull,
                "what should I tweet? Give some text and format must be like `.tweet username ; your text` ",
                5,
            )
            return
    try:
        hmm = Get(hmm)
        await skull.client(hmm)
    except BaseException:
        pass
    if ";" in text:
        username, text = text.split(";")
    else:
        await edit_delete(
            skull,
            "__what should I tweet? Give some text and format must be like__ `.tweet username ; your text`",
            5,
        )
        return
    skulle = await edit_or_reply(skull, f"`Requesting {username} to tweet...`")
    text = deEmojify(text)
    await asyncio.sleep(2)
    skullfile = await tweets(text, username)
    await skull.client.send_file(skull.chat_id, skullfile, reply_to=reply_to_id)
    await skulle.delete()
    if os.path.exists(skullfile):
        os.remove(skullfile)


CMD_HELP.update(
    {
        "imgmemes": """**Plugin : **`imgmemes`

  •  **Syntax : **`.fakegs search query ; what you mean text`
  •  **Function : **__Shows you image meme for your google search query__  

  •  **Syntax : **`.trump reply/text`
  •  **Function : **__sends you the trump tweet sticker with given custom text__

  •  **Syntax : **`.modi reply/text`
  •  **Function : **__sends you the modi tweet sticker with given custom text__ 

  •  **Syntax : **`.cmm reply/text`
  •  **Function : **__sends you the  Change my mind banner with given custom text__ 

  •  **Syntax : **`.kanna reply/text`
  •  **Function : **__sends you the kanna chan sticker with given custom text__  

  •  **Syntax : **`.tweet reply/<username> ; <text>`
  •  **Function : **__sends you the desired person tweet sticker with given custom text__ 
  """
    }
)
