# collage plugin for skulluserbot by @mayank1rajput

# Copyright (C) 2020 Alfiananda P.A
#
# Licensed under the Raphielscape Public License, Version 1.d (the "License");
# you may not use this file except in compliance with the License.

import os

from ..utils import admin_cmd, edit_or_reply, sudo_cmd
from . import CMD_HELP, make_gif, runcmd


@bot.on(admin_cmd(pattern="collage(?: |$)(.*)", outgoing=True))
@bot.on(sudo_cmd(pattern="collage(?: |$)(.*)", allow_sudo=True))
async def collage(skull):
    if skull.fwd_from:
        return
    skullinput = skull.pattern_match.group(1)
    reply = await skull.get_reply_message()
    skullid = skull.reply_to_msg_id
    skull = await edit_or_reply(
        skull, "```collaging this may take several minutes too..... 馃榿```"
    )
    if not (reply and (reply.media)):
        await skull.edit("`Media not found...`")
        return
    if not os.path.isdir("./temp/"):
        os.mkdir("./temp/")
    skullsticker = await reply.download_media(file="./temp/")
    if not skullsticker.endswith((".mp4", ".mkv", ".tgs")):
        os.remove(skullsticker)
        await skull.edit("`Media format is not supported...`")
        return
    if skullinput:
        if not skullinput.isdigit():
            os.remove(skullsticker)
            await skull.edit("`You input is invalid, check help`")
            return
        skullinput = int(skullinput)
        if not 0 < skullinput < 10:
            os.remove(skullsticker)
            await skull.edit(
                "`Why too big grid you cant see images, use size of grid between 1 to 9`"
            )
            return
    else:
        skullinput = 3
    if skullsticker.endswith(".tgs"):
        hmm = await make_gif(skull, skullsticker)
        if hmm.endswith(("@tgstogifbot")):
            os.remove(skullsticker)
            return await skull.edit(hmm)
        collagefile = hmm
    else:
        collagefile = skullsticker
    endfile = "./temp/collage.png"
    skullcmd = f"vcsi -g {skullinput}x{skullinput} '{collagefile}' -o {endfile}"
    stdout, stderr = (await runcmd(skullcmd))[:2]
    if not os.path.exists(endfile):
        for files in (skullsticker, collagefile):
            if files and os.path.exists(files):
                os.remove(files)
        return await edit_delete(
            skull, f"`media is not supported or try with smaller grid size`", 5
        )
    await skull.client.send_file(
        skull.chat_id,
        endfile,
        reply_to=skullid,
    )
    await skull.delete()
    for files in (skullsticker, collagefile, endfile):
        if files and os.path.exists(files):
            os.remove(files)


CMD_HELP.update(
    {
        "collage": "**Plugin : **`collage`\
        \n\n  鈥�  **Syntax : **`.collage <grid size>`\
        \n  鈥�  **Function : **__Shows you the grid image of images extracted from video \n Grid size must be between 1 to 9 by default it is 3__"
    }
)
