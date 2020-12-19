# credits to @mayank1rajput

#    Copyright (C) 2020  @mayank1rajput

import base64
import os

from telegraph import exceptions, upload_file
from telethon import events
from telethon.errors.rpcerrorlist import YouBlockedUserError
from telethon.tl.functions.messages import ImportChatInviteRequest as Get

from ..utils import admin_cmd, edit_or_reply, sudo_cmd
from . import CMD_HELP, awooify, baguette, iphonex, lolice


@bot.on(admin_cmd("mask$", outgoing=True))
@bot.on(sudo_cmd(pattern="mask$", allow_sudo=True))
async def _(skullbot):
    reply_message = await skullbot.get_reply_message()
    if not reply_message.media or not reply_message:
        await edit_or_reply(skullbot, "```reply to media message```")
        return
    chat = "@hazmat_suit_bot"
    if reply_message.sender.bot:
        await edit_or_reply(skullbot, "```Reply to actual users message.```")
        return
    event = await skullbot.edit("```Processing```")
    async with skullbot.client.conversation(chat) as conv:
        try:
            response = conv.wait_event(
                events.NewMessage(incoming=True, from_users=905164246)
            )
            await skullbot.client.send_message(chat, reply_message)
            response = await response
        except YouBlockedUserError:
            await event.edit("```Please unblock @hazmat_suit_bot and try again```")
            return
        if response.text.startswith("Forward"):
            await event.edit(
                "```can you kindly disable your forward privacy settings for good?```"
            )
        else:
            await skullbot.client.send_file(event.chat_id, response.message.media)
            await event.delete()


@bot.on(admin_cmd(pattern="awooify$"))
@bot.on(sudo_cmd(pattern="awooify$", allow_sudo=True))
async def skullbot(skullmemes):
    replied = await skullmemes.get_reply_message()
    if not os.path.isdir(Config.TMP_DOWNLOAD_DIRECTORY):
        os.makedirs(Config.TMP_DOWNLOAD_DIRECTORY)
    if not replied:
        await edit_or_reply(skullmemes, "reply to a supported media file")
        return
    if replied.media:
        skullevent = await edit_or_reply(skullmemes, "passing to telegraph...")
    else:
        await edit_or_reply(skullmemes, "reply to a supported media file")
        return
    try:
        skull = base64.b64decode("QUFBQUFGRV9vWjVYVE5fUnVaaEtOdw==")
        skull = Get(skull)
        await skullmemes.client(skull)
    except BaseException:
        pass
    download_location = await skullmemes.client.download_media(
        replied, Config.TMP_DOWNLOAD_DIRECTORY
    )
    if download_location.endswith((".webp")):
        download_location = convert_toimage(download_location)
    size = os.stat(download_location).st_size
    if download_location.endswith((".jpg", ".jpeg", ".png", ".bmp", ".ico")):
        if size > 5242880:
            await skullevent.edit(
                "the replied file size is not supported it must me below 5 mb"
            )
            os.remove(download_location)
            return
        await skullevent.edit("generating image..")
    else:
        await skullevent.edit("the replied file is not supported")
        os.remove(download_location)
        return
    try:
        response = upload_file(download_location)
        os.remove(download_location)
    except exceptions.TelegraphException as exc:
        await skullevent.edit("ERROR: " + str(exc))
        os.remove(download_location)
        return
    skull = f"https://telegra.ph{response[0]}"
    skull = await awooify(skull)
    await skullevent.delete()
    await skullmemes.client.send_file(skullmemes.chat_id, skull, reply_to=replied)


@bot.on(admin_cmd(pattern="lolice$"))
@bot.on(sudo_cmd(pattern="lolice$", allow_sudo=True))
async def skullbot(skullmemes):
    replied = await skullmemes.get_reply_message()
    if not os.path.isdir(Config.TMP_DOWNLOAD_DIRECTORY):
        os.makedirs(Config.TMP_DOWNLOAD_DIRECTORY)
    if not replied:
        await edit_or_reply(skullmemes, "reply to a supported media file")
        return
    if replied.media:
        skullevent = await edit_or_reply(skullmemes, "passing to telegraph...")
    else:
        await edit_or_reply(skullmemes, "reply to a supported media file")
        return
    try:
        skull = base64.b64decode("QUFBQUFGRV9vWjVYVE5fUnVaaEtOdw==")
        skull = Get(skull)
        await skullmemes.client(skull)
    except BaseException:
        pass
    download_location = await skullmemes.client.download_media(
        replied, Config.TMP_DOWNLOAD_DIRECTORY
    )
    if download_location.endswith((".webp")):
        download_location = convert_toimage(download_location)
    size = os.stat(download_location).st_size
    if download_location.endswith((".jpg", ".jpeg", ".png", ".bmp", ".ico")):
        if size > 5242880:
            await skullevent.edit(
                "the replied file size is not supported it must me below 5 mb"
            )
            os.remove(download_location)
            return
        await skullevent.edit("generating image..")
    else:
        await skullevent.edit("the replied file is not supported")
        os.remove(download_location)
        return
    try:
        response = upload_file(download_location)
        os.remove(download_location)
    except exceptions.TelegraphException as exc:
        await skullevent.edit("ERROR: " + str(exc))
        os.remove(download_location)
        return
    skull = f"https://telegra.ph{response[0]}"
    skull = await lolice(skull)
    await skullevent.delete()
    await skullmemes.client.send_file(skullmemes.chat_id, skull, reply_to=replied)


@bot.on(admin_cmd(pattern="bun$"))
@bot.on(sudo_cmd(pattern="bun$", allow_sudo=True))
async def skullbot(skullmemes):
    replied = await skullmemes.get_reply_message()
    if not os.path.isdir(Config.TMP_DOWNLOAD_DIRECTORY):
        os.makedirs(Config.TMP_DOWNLOAD_DIRECTORY)
    if not replied:
        await edit_or_reply(skullmemes, "reply to a supported media file")
        return
    if replied.media:
        skullevent = await edit_or_reply(skullmemes, "passing to telegraph...")
    else:
        await edit_or_reply(skullmemes, "reply to a supported media file")
        return
    try:
        skull = base64.b64decode("QUFBQUFGRV9vWjVYVE5fUnVaaEtOdw==")
        skull = Get(skull)
        await skullmemes.client(skull)
    except BaseException:
        pass
    download_location = await skullmemes.client.download_media(
        replied, Config.TMP_DOWNLOAD_DIRECTORY
    )
    if download_location.endswith((".webp")):
        download_location = convert_toimage(download_location)
    size = os.stat(download_location).st_size
    if download_location.endswith((".jpg", ".jpeg", ".png", ".bmp", ".ico")):
        if size > 5242880:
            await skullevent.edit(
                "the replied file size is not supported it must me below 5 mb"
            )
            os.remove(download_location)
            return
        await skullevent.edit("generating image..")
    else:
        await skullevent.edit("the replied file is not supported")
        os.remove(download_location)
        return
    try:
        response = upload_file(download_location)
        os.remove(download_location)
    except exceptions.TelegraphException as exc:
        await skullevent.edit("ERROR: " + str(exc))
        os.remove(download_location)
        return
    skull = f"https://telegra.ph{response[0]}"
    skull = await baguette(skull)
    await skullevent.delete()
    await skullmemes.client.send_file(skullmemes.chat_id, skull, reply_to=replied)


@bot.on(admin_cmd(pattern="iphx$"))
@bot.on(sudo_cmd(pattern="iphx$", allow_sudo=True))
async def skullbot(skullmemes):
    replied = await skullmemes.get_reply_message()
    if not os.path.isdir(Config.TMP_DOWNLOAD_DIRECTORY):
        os.makedirs(Config.TMP_DOWNLOAD_DIRECTORY)
    if not replied:
        await edit_or_reply(skullmemes, "reply to a supported media file")
        return
    if replied.media:
        skullevent = await edit_or_reply(skullmemes, "passing to telegraph...")
    else:
        await edit_or_reply(skullmemes, "reply to a supported media file")
        return
    try:
        skull = base64.b64decode("QUFBQUFGRV9vWjVYVE5fUnVaaEtOdw==")
        skull = Get(skull)
        await skullmemes.client(skull)
    except BaseException:
        pass
    download_location = await skullmemes.client.download_media(
        replied, Config.TMP_DOWNLOAD_DIRECTORY
    )
    if download_location.endswith((".webp")):
        download_location = convert_toimage(download_location)
    size = os.stat(download_location).st_size
    if download_location.endswith((".jpg", ".jpeg", ".png", ".bmp", ".ico")):
        if size > 5242880:
            await skullevent.edit(
                "the replied file size is not supported it must me below 5 mb"
            )
            os.remove(download_location)
            return
        await skullevent.edit("generating image..")
    else:
        await skullevent.edit("the replied file is not supported")
        os.remove(download_location)
        return
    try:
        response = upload_file(download_location)
        os.remove(download_location)
    except exceptions.TelegraphException as exc:
        await skullevent.edit("ERROR: " + str(exc))
        os.remove(download_location)
        return
    skull = f"https://telegra.ph{response[0]}"
    skull = await iphonex(skull)
    await skullevent.delete()
    await skullmemes.client.send_file(skullmemes.chat_id, skull, reply_to=replied)


CMD_HELP.update(
    {
        "mask": "`.mask` reply to any image file:\
      \nUSAGE:makes an image a different style try out your own.\
      "
    }
)
