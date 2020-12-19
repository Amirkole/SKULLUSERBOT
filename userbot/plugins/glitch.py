"""
designed By @Krishna_Singhal in userge
ported to telethon by @mayank1rajput
"""

import os

from glitch_this import ImageGlitcher
from PIL import Image
from telethon import functions, types

from .. import CMD_HELP, LOGS
from ..utils import admin_cmd, edit_or_reply, sudo_cmd
from . import runcmd, take_screen_shot


@bot.on(admin_cmd(outgoing=True, pattern="(glitch|glitchs)(?: |$)(.*)"))
@bot.on(sudo_cmd(pattern="(glitch|glitchs)(?: |$)(.*)", allow_sudo=True))
async def glitch(skull):
    if skull.fwd_from:
        return
    cmd = skull.pattern_match.group(1)
    skullinput = skull.pattern_match.group(2)
    reply = await skull.get_reply_message()
    skullid = skull.reply_to_msg_id
    skull = await edit_or_reply(skull, "```Glitching... 😁```")
    if not (reply and (reply.media)):
        await skull.edit("`Media not found...`")
        return
    if not os.path.isdir("./temp/"):
        os.mkdir("./temp/")
    skullsticker = await reply.download_media(file="./temp/")
    if not skullsticker.endswith((".mp4", ".webp", ".tgs", ".png", ".jpg")):
        os.remove(skullsticker)
        await skull.edit("`Media not found...`")
        return
    os.path.join("./temp/", "glitch.png")
    if skullinput:
        if not skullinput.isdigit():
            await skull.edit("`You input is invalid, check help`")
            return
        skullinput = int(skullinput)
        if not 0 < skullinput < 9:
            await skull.edit("`Invalid Range...`")
            return
    else:
        skullinput = 2
    if skullsticker.endswith(".tgs"):
        skullfile = os.path.join("./temp/", "glitch.png")
        skullcmd = (
            f"lottie_convert.py --frame 0 -if lottie -of png {skullsticker} {skullfile}"
        )
        stdout, stderr = (await runcmd(skullcmd))[:2]
        if not os.path.lexists(skullfile):
            await cat.edit("`catsticker not found...`")
            LOGS.info(stdout + stderr)
        glitch_file = catfile
    elif catsticker.endswith(".webp"):
        catfile = os.path.join("./temp/", "glitch.png")
        os.rename(catsticker, catfile)
        if not os.path.lexists(catfile):
            await cat.edit("`catsticker not found... `")
            return
        glitch_file = catfile
    elif catsticker.endswith(".mp4"):
        catfile = os.path.join("./temp/", "glitch.png")
        await take_screen_shot(catsticker, 0, catfile)
        if not os.path.lexists(catfile):
            await cat.edit("```catsticker not found...```")
            return
        glitch_file = catfile
    else:
        glitch_file = catsticker
    glitcher = ImageGlitcher()
    img = Image.open(glitch_file)
    if cmd == "glitchs":
        glitched = "./temp/" + "glitched.webp"
        glitch_img = glitcher.glitch_image(img, catinput, color_offset=True)
        glitch_img.save(glitched)
        await cat.client.send_file(cat.chat_id, glitched, reply_to=catid)
        os.remove(glitched)
        await cat.delete()
    elif cmd == "glitch":
        Glitched = "./temp/" + "glitch.gif"
        glitch_img = glitcher.glitch_image(img, catinput, color_offset=True, gif=True)
        DURATION = 200
        LOOP = 0
        glitch_img[0].save(
            Glitched,
            format="GIF",
            append_images=glitch_img[1:],
            save_all=True,
            duration=DURATION,
            loop=LOOP,
        )
        sandy = await cat.client.send_file(cat.chat_id, Glitched, reply_to=catid)
        await cat.client(
            functions.messages.SaveGifRequest(
                id=types.InputDocument(
                    id=sandy.media.document.id,
                    access_hash=sandy.media.document.access_hash,
                    file_reference=sandy.media.document.file_reference,
                ),
                unsave=True,
            )
        )
        os.remove(Glitched)
        await skull.delete()
    for files in (skullsticker, glitch_file):
        if files and os.path.exists(files):
            os.remove(files)


CMD_HELP.update(
    {
        "glitch": "**Plugin : **`glitch`\
    \n\n**Syntax : **`.glitch` reply to media file\
    \n**Usage :** glitches the given mediafile (gif , stickers , image, videos) to a gif and glitch range is from 1 to 8.\
    If nothing is mentioned then by default it is 2\
    \n\n**Syntax : **`.glitchs` reply to media file\
    \n**Usage :** glitches the given mediafile (gif , stickers , image, videos) to a sticker and glitch range is from 1 to 8.\
    If nothing is mentioned then by default it is 2\
    "
    }
)
