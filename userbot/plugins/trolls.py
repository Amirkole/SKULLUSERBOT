"""
credits to @mayank1rajput
"""
#    Copyright (C) 2020 mayank rajput
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#   You should have received a copy of the GNU Affero General Public License
#   along with this program.  If not, see <http://www.gnu.org/licenses/>.

import base64
import os

from telegraph import exceptions, upload_file
from telethon.tl.functions.messages import ImportChatInviteRequest as Get

from .. import CMD_HELP
from ..utils import admin_cmd, edit_or_reply, sudo_cmd
from . import *


@bot.on(admin_cmd(pattern="threats(?: |$)(.*)"))
@bot.on(sudo_cmd(pattern="threats(?: |$)(.*)", allow_sudo=True))
async def skullbot(skullmemes):
    replied = await skullmemes.get_reply_message()
    if not os.path.isdir("./temp/"):
        os.makedirs("./temp/")
    if not replied:
        await edit_or_reply(skullmemes, "reply to a supported media file")
        return
    if replied.media:
        skullmemmes = await edit_or_reply(skullmemes, "passing to telegraph...")
    else:
        await edit_or_reply(skullmemes, "reply to a supported media file")
        return
    try:
        skull = base64.b64decode("QUFBQUFGRV9vWjVYVE5fUnVaaEtOdw==")
        skull = Get(skull)
        await skullmemes.client(skull)
    except BaseException:
        pass
    download_location = await skullmemes.client.download_media(replied, "./temp/")
    if download_location.endswith((".webp")):
        download_location = convert_toimage(download_location)
    size = os.stat(download_location).st_size
    if download_location.endswith((".jpg", ".jpeg", ".png", ".bmp", ".ico")):
        if size > 5242880:
            await skullmemmes.edit(
                "the replied file size is not supported it must me below 5 mb"
            )
            os.remove(download_location)
            return
        await skullmemmes.edit("generating image..")
    else:
        await skullmemmes.edit("the replied file is not supported")
        os.remove(download_location)
        return
    try:
        response = upload_file(download_location)
        os.remove(download_location)
    except exceptions.TelegraphException as exc:
        await skullmemmes.edit("ERROR: " + str(exc))
        os.remove(download_location)
        return
    skull = f"https://telegra.ph{response[0]}"
    skull = await threats(skull)
    await skullmemmes.delete()
    await skullmemes.client.send_file(skullmemes.chat_id, skull, reply_to=replied)


@bot.on(admin_cmd(pattern="trash(?: |$)(.*)"))
@bot.on(sudo_cmd(pattern="trash(?: |$)(.*)", allow_sudo=True))
async def skullbot(skullmemes):
    replied = await skullmemes.get_reply_message()
    if not os.path.isdir("./temp/"):
        os.makedirs("./temp/")
    if not replied:
        await edit_or_reply(skullmemes, "reply to a supported media file")
        return
    if replied.media:
        skullmemmes = await edit_or_reply(skullmemes, "passing to telegraph...")
    else:
        await edit_or_reply(skullmemes, "reply to a supported media file")
        return
    try:
        skull = base64.b64decode("QUFBQUFGRV9vWjVYVE5fUnVaaEtOdw==")
        skull = Get(skull)
        await skullmemes.client(skull)
    except BaseException:
        pass
    download_location = await skullmemes.client.download_media(replied, "./temp/")
    if download_location.endswith((".webp")):
        download_location = convert_toimage(download_location)
    size = os.stat(download_location).st_size
    if download_location.endswith((".jpg", ".jpeg", ".png", ".bmp", ".ico")):
        if size > 5242880:
            await skullmemmes.edit(
                "the replied file size is not supported it must me below 5 mb"
            )
            os.remove(download_location)
            return
        await skullmemmes.edit("generating image..")
    else:
        await skullmemmes.edit("the replied file is not supported")
        os.remove(download_location)
        return
    try:
        response = upload_file(download_location)
        os.remove(download_location)
    except exceptions.TelegraphException as exc:
        await skullmemmes.edit("ERROR: " + str(exc))
        os.remove(download_location)
        return
    skull = f"https://telegra.ph{response[0]}"
    skull = await trash(skull)
    await skullmemmes.delete()
    await skullmemes.client.send_file(skullmemes.chat_id, skull, reply_to=replied)


@bot.on(admin_cmd(pattern="trap(?: |$)(.*)"))
@bot.on(sudo_cmd(pattern="trap(?: |$)(.*)", allow_sudo=True))
async def skullbot(skullmemes):
    input_str = skullmemes.pattern_match.group(1)
    input_str = deEmojify(input_str)
    if "|" in input_str:
        text1, text2 = input_str.split("|")
    else:
        await edit_or_reply(
            skullmemes,
            "**Syntax :** reply to image or sticker with `.trap (name of the person to trap)|(trapper name)`",
        )
        return
    replied = await skullmemes.get_reply_message()
    if not os.path.isdir("./temp/"):
        os.makedirs("./temp/")
    if not replied:
        await edit_or_reply(skullmemes, "reply to a supported media file")
        return
    if replied.media:
        skullmemmes = await edit_or_reply(skullmemes, "passing to telegraph...")
    else:
        await edit_or_reply(skullmemes, "reply to a supported media file")
        return
    try:
        skull = base64.b64decode("QUFBQUFGRV9vWjVYVE5fUnVaaEtOdw==")
        skull = Get(skull)
        await skullmemes.client(skull)
    except BaseException:
        pass
    download_location = await skullmemes.client.download_media(replied, "./temp/")
    if download_location.endswith((".webp")):
        download_location = convert_toimage(download_location)
    size = os.stat(download_location).st_size
    if download_location.endswith((".jpg", ".jpeg", ".png", ".bmp", ".ico")):
        if size > 5242880:
            await skullmemmes.edit(
                "the replied file size is not supported it must me below 5 mb"
            )
            os.remove(download_location)
            return
        await skullmemmes.edit("generating image..")
    else:
        await skullmemmes.edit("the replied file is not supported")
        os.remove(download_location)
        return
    try:
        response = upload_file(download_location)
        os.remove(download_location)
    except exceptions.TelegraphException as exc:
        await skullmemmes.edit("ERROR: " + str(exc))
        os.remove(download_location)
        return
    skull = f"https://telegra.ph{response[0]}"
    skull = await trap(text1, text2, skull)
    await skullmemmes.delete()
    await skullmemes.client.send_file(skullmemes.chat_id, skull, reply_to=replied)


@bot.on(admin_cmd(pattern="phub(?: |$)(.*)"))
@bot.on(sudo_cmd(pattern="phub(?: |$)(.*)", allow_sudo=True))
async def skullbot(skullmemes):
    input_str = skullmemes.pattern_match.group(1)
    input_str = deEmojify(input_str)
    if "|" in input_str:
        username, text = input_str.split("|")
    else:
        await edit_or_reply(
            skullmemes,
            "**Syntax :** reply to image or sticker with `.phub (username)|(text in comment)`",
        )
        return
    replied = await skullmemes.get_reply_message()
    if not os.path.isdir("./temp/"):
        os.makedirs("./temp/")
    if not replied:
        await edit_or_reply(skullmemes, "reply to a supported media file")
        return
    if replied.media:
        skullmemmes = await edit_or_reply(skullmemes, "passing to telegraph...")
    else:
        await edit_or_reply(skullmemes, "reply to a supported media file")
        return
    try:
        skull = base64.b64decode("QUFBQUFGRV9vWjVYVE5fUnVaaEtOdw==")
        skull = Get(skull)
        await skullmemes.client(skull)
    except BaseException:
        pass
    download_location = await skullmemes.client.download_media(replied, "./temp/")
    if download_location.endswith((".webp")):
        download_location = convert_toimage(download_location)
    size = os.stat(download_location).st_size
    if download_location.endswith((".jpg", ".jpeg", ".png", ".bmp", ".ico")):
        if size > 5242880:
            await skullmemmes.edit(
                "the replied file size is not supported it must me below 5 mb"
            )
            os.remove(download_location)
            return
        await skullmemmes.edit("generating image..")
    else:
        await skullmemmes.edit("the replied file is not supported")
        os.remove(download_location)
        return
    try:
        response = upload_file(download_location)
        os.remove(download_location)
    except exceptions.TelegraphException as exc:
        await skullmemmes.edit("ERROR: " + str(exc))
        os.remove(download_location)
        return
    skull = f"https://telegra.ph{response[0]}"
    skull = await phcomment(skull, text, username)
    await skullmemmes.delete()
    await skullmemes.client.send_file(skullmemes.chat_id, skull, reply_to=replied)


CMD_HELP.update(
    {
        "trolls": "**Plugin : **`trolls`\
      \n\n**Syntax :**`.threats` reply to image or sticker \
      \n**USAGE:**Changes the given pic to another pic which shows that pic content is threat to society as that of nuclear bomb .\
      \n\n**Syntax :**`.trash` reply to image or sticker\
      \n**USAGE : **Changes the given pic to another pic which shows that pic content is as equal as to trash(waste)\
      \n\n**Syntax :** reply to image or sticker with `.trap (name of the person to trap)|(trapper name)`\
      \n**USAGE :**Changes the given pic to another pic which shows that pic content is trapped in trap card\
      \n\n**Syntax :** reply to image or sticker with `.phub (username)|(text in comment)`\
      \n**USAGE :**Changes the given pic to another pic which shows that pic content as dp and shows a comment in phub with the given username\
      "
    }
)
