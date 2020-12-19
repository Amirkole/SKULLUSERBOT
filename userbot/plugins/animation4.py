import asyncio

from ..utils import admin_cmd, edit_or_reply, sudo_cmd
from . import ALIVE_NAME, CMD_HELP

DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "SKULL"


@bot.on(admin_cmd(outgoing=True, pattern="kilr( (.*)|$)"))
@bot.on(sudo_cmd(pattern="kilr( (.*)|$)", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    name = event.pattern_match.group(1)
    if not name:
        name = "die"
    animation_interval = 0.7
    animation_ttl = range(8)
    event = await edit_or_reply(event, f"**Ready Commando **__{DEFAULTUSER}....")
    animation_chars = [
        "锛︼綁锝夛綁锝夛綁锝掞絽",
        f"__**Commando **__{DEFAULTUSER}          \n\n_/锕媆_\n (覀`_麓)\n <,锔烩暒鈺も攢 覊 - \n _/锕媆_\n",
        f"__**Commando **__{DEFAULTUSER}          \n\n_/锕媆_\n (覀`_麓)\n  <,锔烩暒鈺も攢 覊 - -\n _/锕媆_\n",
        f"__**Commando **__{DEFAULTUSER}          \n\n_/锕媆_\n (覀`_麓)\n <,锔烩暒鈺も攢 覊 - - -\n _/锕媆_\n",
        f"__**Commando **__{DEFAULTUSER}          \n\n_/锕媆_\n (覀`_麓)\n<,锔烩暒鈺も攢 覊 - -\n _/锕媆_\n",
        f"__**Commando **__{DEFAULTUSER}          \n\n_/锕媆_\n (覀`_麓)\n <,锔烩暒鈺も攢 覊 - \n _/锕媆_\n",
        f"__**Commando **__{DEFAULTUSER}         \n\n_/锕媆_\n (覀`_麓)\n  <,锔烩暒鈺も攢 覊 - -\n _/锕媆_\n",
        f"__**Commando **__{DEFAULTUSER}          \n\n_/锕媆_\n (覀`_麓)\n <,锔烩暒鈺も攢 覊 - - - {name}\n _/锕媆_\n",
    ]
    for i in animation_ttl:
        await asyncio.sleep(animation_interval)
        await event.edit(animation_chars[i % 8])


@bot.on(admin_cmd(pattern="eye$"))
@bot.on(sudo_cmd(pattern="eye$", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    animation_interval = 3
    animation_ttl = range(10)
    event = await edit_or_reply(event, "馃憗馃憗")
    animation_chars = [
        "馃憗馃憗\n  馃憚  =====> Hey, How are you?",
        "馃憗馃憗\n  馃憛  =====> Everything okay?",
        "馃憗馃憗\n  馃拫  =====> Why are you staring at this?",
        "馃憗馃憗\n  馃憚  =====> You idiot",
        "馃憗馃憗\n  馃憛  =====> Go away",
        "馃憗馃憗\n  馃拫  =====> Stop laughing",
        "馃憗馃憗\n  馃憚  =====> It's not funny",
        "馃憗馃憗\n  馃憛  =====> I guess ur still looking",
        "馃憗馃憗\n  馃拫  =====> Ok man 馃槕",
        "馃憗馃憗\n  馃憚  =====> I go away then",
    ]
    for i in animation_ttl:
        await asyncio.sleep(animation_interval)
        await event.edit(animation_chars[i % 10])
    await asyncio.sleep(animation_interval)
    await event.delete()


@bot.on(admin_cmd(pattern="thinking$"))
@bot.on(sudo_cmd(pattern="thinking$", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    animation_interval = 0.01
    animation_ttl = range(288)
    event = await edit_or_reply(event, "thinking..")
    animation_chars = [
        "THINKING",
        "THI&K#N鈧�",
        "T+IN@I?G",
        "驴H$NK鈭哊G",
        "露H脳NK&N*",
        "NGITHKIN",
        "T+I#K@鈧笹",
        "THINKING",
        "THI&K#N鈧�",
        "T+IN@I?G",
        "驴H$NK鈭哊G",
        "露H脳NK&N*",
        "NGITHKIN",
        "T+I#K@鈧笹",
        "THINKING",
        "THI&K#N鈧�",
        "T+IN@I?G",
        "驴H$NK鈭哊G",
        "露H脳NK&N*",
        "NGITHKIN",
        "T+I#K@鈧笹",
        "THINKING",
        "THI&K#N鈧�",
        "T+IN@I?G",
        "驴H$NK鈭哊G",
        "露H脳NK&N*",
        "NGITHKIN",
        "T+I#K@鈧笹",
        "THINKING",
        "THI&K#N鈧�",
        "T+IN@I?G",
        "驴H$NK鈭哊G",
        "露H脳NK&N*",
        "NGITHKIN",
        "T+I#K@鈧笹",
        "THINKING... 馃",
    ]
    for i in animation_ttl:
        await asyncio.sleep(animation_interval)
        await event.edit(animation_chars[i % 36])


@bot.on(admin_cmd(pattern=f"snake$", outgoing=True))
@bot.on(sudo_cmd(pattern="snake$", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    animation_interval = 0.3
    animation_ttl = range(27)
    event = await edit_or_reply(event, "snake..")
    animation_chars = [
        "鈼硷笍鈼硷笍鈼硷笍鈼硷笍鈼硷笍\n鈼硷笍鈼硷笍鈼硷笍鈼硷笍鈼硷笍\n鈼硷笍鈼硷笍鈼硷笍鈼硷笍鈼硷笍\n鈼硷笍鈼硷笍鈼硷笍鈼硷笍鈼硷笍\n鈼硷笍鈼硷笍鈼硷笍鈼硷笍鈼硷笍",
        "鈼伙笍鈼硷笍鈼硷笍鈼硷笍鈼硷笍\n鈼硷笍鈼硷笍鈼硷笍鈼硷笍鈼硷笍\n鈼硷笍鈼硷笍鈼硷笍鈼硷笍鈼硷笍\n鈼硷笍鈼硷笍鈼硷笍鈼硷笍鈼硷笍\n鈼硷笍鈼硷笍鈼硷笍鈼硷笍鈼硷笍",
        "鈼伙笍鈼伙笍鈼硷笍鈼硷笍鈼硷笍\n鈼硷笍鈼硷笍鈼硷笍鈼硷笍鈼硷笍\n鈼硷笍鈼硷笍鈼硷笍鈼硷笍鈼硷笍\n鈼硷笍鈼硷笍鈼硷笍鈼硷笍鈼硷笍\n鈼硷笍鈼硷笍鈼硷笍鈼硷笍鈼硷笍",
        "鈼伙笍鈼伙笍鈼伙笍锔忊椉锔忊椉锔廫n鈼硷笍鈼硷笍鈼硷笍鈼硷笍鈼硷笍\n鈼硷笍鈼硷笍鈼硷笍鈼硷笍鈼硷笍\n鈼硷笍鈼硷笍鈼硷笍鈼硷笍鈼硷笍\n鈼硷笍鈼硷笍鈼硷笍鈼硷笍鈼硷笍",
        "鈼伙笍鈼伙笍鈼伙笍鈼伙笍鈼硷笍\n鈼硷笍鈼硷笍鈼硷笍鈼硷笍鈼硷笍\n鈼硷笍鈼硷笍鈼硷笍鈼硷笍鈼硷笍\n鈼硷笍鈼硷笍鈼硷笍鈼硷笍鈼硷笍\n鈼硷笍鈼硷笍鈼硷笍鈼硷笍鈼硷笍",
        "鈥庘椈锔忊椈锔忊椈锔忊椈锔忊椈锔廫n鈼硷笍鈼硷笍鈼硷笍鈼硷笍鈼硷笍\n鈼硷笍鈼硷笍鈼硷笍鈼硷笍鈼硷笍\n鈼硷笍鈼硷笍鈼硷笍鈼硷笍鈼硷笍\n鈼硷笍鈼硷笍鈼硷笍鈼硷笍鈼硷笍",
        "鈼伙笍鈼伙笍鈼伙笍鈼伙笍鈼伙笍\n鈼硷笍鈼硷笍鈼硷笍鈼硷笍鈼伙笍\n鈼硷笍鈼硷笍鈼硷笍鈼硷笍鈼硷笍\n鈼硷笍鈼硷笍鈼硷笍鈼硷笍鈼硷笍\n鈼硷笍鈼硷笍鈼硷笍鈼硷笍鈼硷笍",
        "鈼伙笍鈼伙笍鈼伙笍鈼伙笍鈼伙笍\n鈼硷笍鈼硷笍鈼硷笍鈼硷笍鈼伙笍\n鈼硷笍鈼硷笍鈼硷笍鈼硷笍鈼伙笍\n鈼硷笍鈼硷笍鈼硷笍鈼硷笍鈼硷笍\n鈼硷笍鈼硷笍鈼硷笍鈼硷笍鈼硷笍",
        "鈼伙笍鈼伙笍鈼伙笍鈼伙笍鈼伙笍\n鈼硷笍鈼硷笍鈼硷笍鈼硷笍鈼伙笍\n鈼硷笍鈼硷笍鈼硷笍鈼硷笍鈼伙笍\n鈼硷笍鈼硷笍鈼硷笍鈼硷笍鈼伙笍\n鈼硷笍鈼硷笍鈼硷笍鈼硷笍鈼硷笍",
        "鈼伙笍鈼伙笍鈼伙笍鈼伙笍鈼伙笍\n鈼硷笍鈼硷笍鈼硷笍鈼硷笍鈼伙笍\n鈼硷笍鈼硷笍鈼硷笍鈼硷笍鈼伙笍\n鈼硷笍鈼硷笍鈼硷笍鈼硷笍鈼伙笍\n鈼硷笍鈼硷笍鈼硷笍鈼硷笍鈼伙笍",
        "鈼伙笍鈼伙笍鈼伙笍鈼伙笍鈼伙笍\n鈼硷笍鈼硷笍鈼硷笍鈼硷笍鈼伙笍\n鈼硷笍鈼硷笍鈼硷笍鈼硷笍鈼伙笍\n鈼硷笍鈼硷笍鈼硷笍鈼硷笍鈼伙笍\n鈼硷笍鈼硷笍鈼硷笍鈼伙笍鈼伙笍",
        "鈼伙笍鈼伙笍鈼伙笍鈼伙笍鈼伙笍\n鈼硷笍鈼硷笍鈼硷笍鈼硷笍鈼伙笍\n鈼硷笍鈼硷笍鈼硷笍鈼硷笍鈼伙笍\n鈼硷笍鈼硷笍鈼硷笍鈼硷笍鈼伙笍\n鈼硷笍鈼硷笍鈼伙笍鈼伙笍鈼伙笍",
        "鈼伙笍鈼伙笍鈼伙笍鈼伙笍鈼伙笍\n鈼硷笍鈼硷笍鈼硷笍鈼硷笍鈼伙笍\n鈼硷笍鈼硷笍鈼硷笍鈼硷笍鈼伙笍\n鈼硷笍鈼硷笍鈼硷笍鈼硷笍鈼伙笍\n鈼硷笍鈼伙笍鈼伙笍鈼伙笍鈼伙笍",
        "鈼伙笍鈼伙笍鈼伙笍鈼伙笍鈼伙笍\n鈼硷笍鈼硷笍鈼硷笍鈼硷笍鈼伙笍\n鈼硷笍鈼硷笍鈼硷笍鈼硷笍鈼伙笍\n鈼硷笍鈼硷笍鈼硷笍鈼硷笍鈼伙笍\n鈼伙笍鈼伙笍鈼伙笍鈼伙笍鈼伙笍",
        "鈼伙笍鈼伙笍鈼伙笍鈼伙笍鈼伙笍\n鈼硷笍鈼硷笍鈼硷笍鈼硷笍鈼伙笍\n鈼硷笍鈼硷笍鈼硷笍鈼硷笍鈼伙笍\n鈼伙笍鈼硷笍鈼硷笍鈼硷笍鈼伙笍\n鈼伙笍鈼伙笍鈼伙笍鈼伙笍鈼伙笍",
        "鈼伙笍鈼伙笍鈼伙笍鈼伙笍鈼伙笍\n鈼硷笍鈼硷笍鈼硷笍鈼硷笍鈼伙笍\n鈼伙笍鈼硷笍鈼硷笍鈼硷笍鈼伙笍\n鈼伙笍鈼硷笍鈼硷笍鈼硷笍鈼伙笍\n鈼伙笍鈼伙笍鈼伙笍鈼伙笍鈼伙笍",
        "鈼伙笍鈼伙笍鈼伙笍鈼伙笍鈼伙笍\n鈼伙笍鈼硷笍鈼硷笍鈼硷笍鈼伙笍\n鈼伙笍鈼硷笍鈼硷笍鈼硷笍鈼伙笍\n鈼伙笍鈼硷笍鈼硷笍鈼硷笍鈼伙笍\n鈼伙笍鈼伙笍鈼伙笍鈼伙笍鈼伙笍",
        "鈼伙笍鈼伙笍鈼伙笍鈼伙笍鈼伙笍\n鈼伙笍鈼伙笍鈼硷笍鈼硷笍鈼伙笍\n鈼伙笍鈼硷笍鈼硷笍鈼硷笍鈼伙笍\n鈼伙笍鈼硷笍鈼硷笍鈼硷笍鈼伙笍\n鈼伙笍鈼伙笍鈼伙笍鈼伙笍鈼伙笍",
        "鈼伙笍鈼伙笍鈼伙笍鈼伙笍鈼伙笍\n鈼伙笍鈼伙笍鈼伙笍鈼硷笍鈼伙笍\n鈼伙笍鈼硷笍鈼硷笍鈼硷笍鈼伙笍\n鈼伙笍鈼硷笍鈼硷笍鈼硷笍鈼伙笍\n鈼伙笍鈼伙笍鈼伙笍鈼伙笍鈼伙笍",
        "鈼伙笍鈼伙笍鈼伙笍鈼伙笍鈼伙笍\n鈼伙笍鈼伙笍鈼伙笍鈼伙笍鈼伙笍\n鈼伙笍鈼硷笍鈼硷笍鈼硷笍鈼伙笍\n鈼伙笍鈼硷笍鈼硷笍鈼硷笍鈼伙笍\n鈼伙笍鈼伙笍鈼伙笍鈼伙笍鈼伙笍",
        "鈼伙笍鈼伙笍鈼伙笍鈼伙笍鈼伙笍\n鈼伙笍鈼伙笍鈼伙笍鈼伙笍鈼伙笍\n鈼伙笍鈼硷笍鈼硷笍鈼伙笍鈼伙笍\n鈼伙笍鈼硷笍鈼硷笍鈼硷笍鈼伙笍\n鈼伙笍鈼伙笍鈼伙笍鈼伙笍鈼伙笍",
        "鈼伙笍鈼伙笍鈼伙笍鈼伙笍鈼伙笍\n鈼伙笍鈼伙笍鈼伙笍鈼伙笍鈼伙笍\n鈼伙笍鈼硷笍鈼硷笍鈼伙笍鈼伙笍\n鈼伙笍鈼硷笍鈼硷笍鈼伙笍鈼伙笍\n鈼伙笍鈼伙笍鈼伙笍鈼伙笍鈼伙笍",
        "鈼伙笍鈼伙笍鈼伙笍鈼伙笍鈼伙笍\n鈼伙笍鈼伙笍鈼伙笍鈼伙笍鈼伙笍\n鈼伙笍鈼硷笍鈼硷笍鈼伙笍鈼伙笍\n鈼伙笍鈼硷笍鈼伙笍鈼伙笍鈼伙笍\n鈼伙笍鈼伙笍鈼伙笍鈼伙笍鈼伙笍",
        "鈼伙笍鈼伙笍鈼伙笍鈼伙笍鈼伙笍\n鈼伙笍鈼伙笍鈼伙笍鈼伙笍鈼伙笍\n鈼伙笍鈼硷笍鈼硷笍鈼伙笍鈼伙笍\n鈼伙笍鈼伙笍鈼伙笍鈼伙笍鈼伙笍\n鈼伙笍鈼伙笍鈼伙笍鈼伙笍鈼伙笍",
        "鈼伙笍鈼伙笍鈼伙笍鈼伙笍鈼伙笍\n鈼伙笍鈼伙笍鈼伙笍鈼伙笍鈼伙笍\n鈼伙笍鈼伙笍鈼硷笍鈼伙笍鈼伙笍\n鈼伙笍鈼伙笍鈼伙笍鈼伙笍鈼伙笍\n鈼伙笍鈼伙笍鈼伙笍鈼伙笍鈼伙笍",
        "鈼伙笍鈼伙笍鈼伙笍鈼伙笍鈼伙笍\n鈼伙笍鈼伙笍鈼伙笍鈼伙笍鈼伙笍\n鈼伙笍鈼伙笍鈼伙笍鈼伙笍鈼伙笍\n鈼伙笍鈼伙笍鈼伙笍鈼伙笍鈼伙笍\n鈼伙笍鈼伙笍鈼伙笍鈼伙笍鈼伙笍",
        "鈼伙笍鈼伙笍鈼伙笍鈼伙笍鈼伙笍\n鈼伙笍鈼硷笍鈼伙笍鈼硷笍鈼伙笍\n鈼伙笍鈼伙笍鈼伙笍鈼伙笍鈼伙笍\n鈼伙笍鈼硷笍鈼硷笍鈼硷笍鈼伙笍\n鈼伙笍鈼伙笍鈼伙笍鈼伙笍鈼伙笍",
    ]
    for i in animation_ttl:
        await asyncio.sleep(animation_interval)
        await event.edit(animation_chars[i % 27])


@bot.on(admin_cmd(pattern=f"human$", outgoing=True))
@bot.on(sudo_cmd(pattern="human$", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    animation_interval = 0.5
    animation_ttl = range(16)
    event = await edit_or_reply(event, "human...")
    animation_chars = [
        "猬涒瑳猬涒瑳猬涒瑳猬沑n猬涒瑳猬涒瑳猬涒瑳猬沑n猬涒瑳猬涒瑳猬涒瑳猬沑n猬涒瑳猬涒瑳猬涒瑳猬沑n猬涒瑳猬涒瑳猬涒瑳猬沑n猬溾瑴猬溾瑴猬溾瑴猬淺n猬溾瑴猬溾瑴猬溾瑴猬淺n馃敳馃敳馃敳馃敳馃敳馃敳馃敳",
        "猬涒瑳猬涒瑳猬涒瑳猬沑n猬涒瑳猬涒瑳猬涒瑳猬沑n猬涒瑳猬涒瑳猬涒瑳猬沑n猬涒瑳猬涒瑳猬涒瑳猬沑n猬涒瑳猬涒瑳猬涒瑳馃殫\n猬溾瑴猬溾瑴猬溾瑴猬淺n猬溾瑴猬溾瑴猬溾瑴猬淺n馃敳馃敳馃敳馃敳馃敳馃敳馃敳",
        "猬涒瑳猬涒瑳猬涒瑳猬沑n猬涒瑳猬涒瑳猬涒瑳猬沑n猬涒瑳猬涒瑳猬涒瑳猬沑n猬涒瑳猬涒瑳猬涒瑳猬沑n猬涒瑳猬涒瑳猬涴煔椻瑳\n猬溾瑴猬溾瑴猬溾瑴猬淺n猬溾瑴猬溾瑴猬溾瑴猬淺n馃敳馃敳馃敳馃敳馃敳馃敳馃敳",
        "猬涒瑳猬涒瑳猬涒瑳猬沑n猬涒瑳猬涒瑳猬涒瑳猬沑n猬涒瑳猬涒瑳猬涒瑳猬沑n猬涒瑳猬涒瑳猬涒瑳猬沑n猬涒瑳猬涒瑳馃殫猬涒瑳\n猬溾瑴猬溾瑴猬溾瑴猬淺n猬溾瑴猬溾瑴猬溾瑴猬淺n馃敳馃敳馃敳馃敳馃敳馃敳馃敳",
        "猬涒瑳猬涒瑳猬涒瑳猬沑n猬涒瑳猬涒瑳猬涒瑳猬沑n猬涒瑳猬涒瑳猬涒瑳猬沑n猬涒瑳猬涒瑳猬涒瑳猬沑n猬涒瑳猬涴煔椻瑳猬涒瑳\n猬溾瑴猬溾瑴猬溾瑴猬淺n猬溾瑴猬溾瑴猬溾瑴猬淺n馃敳馃敳馃敳馃敳馃敳馃敳馃敳",
        "猬涒瑳猬涒瑳猬涒瑳猬沑n猬涒瑳猬涒瑳猬涒瑳猬沑n猬涒瑳猬涒瑳猬涒瑳猬沑n猬涒瑳猬涒瑳猬涒瑳猬沑n猬涒瑳馃殫猬涒瑳猬涒瑳\n猬溾瑴猬溾瑴猬溾瑴猬淺n猬溾瑴猬溾瑴猬溾瑴猬淺n馃敳馃敳馃敳馃敳馃敳馃敳馃敳",
        "猬涒瑳猬涒瑳猬涒瑳猬沑n猬涒瑳猬涒瑳猬涒瑳猬沑n猬涒瑳猬涒瑳猬涒瑳猬沑n猬涒瑳猬涒瑳猬涒瑳猬沑n猬涴煔椻瑳猬涒瑳猬涒瑳\n猬溾瑴猬溾瑴猬溾瑴猬淺n猬溾瑴猬溾瑴猬溾瑴猬淺n馃敳馃敳馃敳馃敳馃敳馃敳馃敳",
        "猬涒瑳猬涒瑳猬涒瑳猬沑n猬涒瑳猬涒瑳猬涒瑳猬沑n猬涒瑳猬涒瑳猬涒瑳猬沑n猬涒瑳猬涒瑳猬涒瑳猬沑n馃殫猬涒瑳猬涒瑳猬涒瑳\n猬溾瑴猬溾瑴猬溾瑴猬淺n猬溾瑴猬溾瑴猬溾瑴猬淺n馃敳馃敳馃敳馃敳馃敳馃敳馃敳",
        "猬涒瑳猬涒瑳猬涒瑳猬沑n猬涒瑳猬涒瑳猬涒瑳猬沑n猬涒瑳猬涒瑳猬涒瑳猬沑n猬涒瑳猬涒瑳猬涒瑳猬沑n猬涒瑳猬涒瑳猬涒瑳猬沑n猬溾瑴猬溾瑴猬溾瑴猬淺n猬溾瑴猬溾瑴猬溾瑴猬淺n馃敳馃敳馃敳馃敳馃敳馃敳馃敳",
        "猬涒瑳猬涒瑳猬涒瑳猬沑n猬涒瑳猬涒瑳猬涒瑳猬沑n猬涒瑳猬涒瑳猬涒瑳猬沑n猬涒瑳猬涒瑳猬涒瑳猬沑n猬涒瑳猬涒瑳猬涒瑳猬沑n猬溾瑴猬滒煒娾瑴猬溾瑴\n猬溾瑴猬溾瑴猬溾瑴猬淺n馃敳馃敳馃敳馃敳馃敳馃敳馃敳",
        "猬涒瑳猬涒瑳猬涒瑳猬沑n猬涒瑳猬涴煒娾瑳猬涒瑳\n猬涒瑴猬溾瑴猬溾瑴猬沑n猬涒瑳猬涒瑴猬涒瑳猬沑n猬涒瑳猬溾瑳猬溾瑳猬沑n猬涒瑳猬溾瑳猬溾瑳猬沑n猬涒瑳猬溾瑳猬溾瑳猬沑n馃敳馃敳馃敳馃敳馃敳馃敳馃敳",
        "猬涒瑳猬涒瑳猬涒瑳猬沑n猬涒瑳猬涴煒娾瑳猬涒瑳\n猬涒瑴猬溾瑴猬溾瑴猬沑n猬涒瑳猬涒瑴猬涒瑳猬沑n猬涒瑳猬溾瑳猬溾瑳猬沑n猬涒瑳猬溾瑳猬涒瑴猬沑n猬涒瑳猬溾瑳猬涒瑳猬沑n馃敳馃敳馃敳馃敳馃敳馃敳馃敳",
        "猬涒瑳猬涒瑳猬涒瑳猬沑n猬涒瑳猬涴煒娾瑳猬涒瑳\n猬涒瑴猬溾瑴猬溾瑴猬沑n猬涒瑳猬涒瑴猬涒瑳猬沑n猬涒瑳猬溾瑳猬溾瑳猬沑n猬涒瑴猬涒瑳猬涒瑴猬沑n猬涒瑳猬涒瑳猬涒瑳猬沑n馃敳馃敳馃敳馃敳馃敳馃敳馃敳",
        "猬涒瑳猬涒瑳猬涒瑳猬沑n猬涒瑴猬涴煒娾瑳猬溾瑳\n猬涒瑳猬溾瑴猬溾瑳猬沑n猬涒瑳猬涒瑴猬涒瑳猬沑n猬涒瑳猬溾瑳猬溾瑳猬沑n猬涒瑴猬涒瑳猬涒瑴猬沑n猬涒瑳猬涒瑳猬涒瑳猬沑n馃敳馃敳馃敳馃敳馃敳馃敳馃敳",
        "猬涒瑳猬涒瑳猬涒瑳猬沑n猬涒瑳猬涴煒娾瑳猬涒瑳\n猬涒瑳猬溾瑴猬溾瑳猬沑n猬涒瑴猬涒瑴猬涒瑴猬沑n猬涒瑳猬溾瑳猬溾瑳猬沑n猬涒瑳猬溾瑳猬溾瑳猬沑n猬涒瑳猬溾瑳猬溾瑳猬沑n馃敳馃敳馃敳馃敳馃敳馃敳馃敳",
        "猬涒瑳猬涒瑳猬涒瑳猬沑n猬涒瑳猬涒瑳猬涒瑳猬沑n猬涒瑳猬涒瑳猬涒瑳猬沑n猬涒瑳猬涒瑳猬涒瑳猬沑n猬涒瑳猬涒瑳猬涒瑳猬沑n猬溾瑴猬滒煒娾瑴猬溾瑴\n猬溾瑴猬溾瑴猬溾瑴猬淺n馃敳馃敳馃敳馃敳馃敳馃敳馃敳",
    ]
    for i in animation_ttl:
        await asyncio.sleep(animation_interval)
        await event.edit(animation_chars[i % 16])


@bot.on(admin_cmd(pattern=f"mc$", outgoing=True))
@bot.on(sudo_cmd(pattern="mc$", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    animation_interval = 0.3
    animation_ttl = range(28)
    event = await edit_or_reply(event, "mc..")
    animation_chars = [
        "鈼硷笍鈼硷笍鈼硷笍鈼硷笍鈼硷笍\n鈼硷笍鈼硷笍鈼硷笍鈼硷笍鈼硷笍\n鈼硷笍鈼硷笍鈼硷笍鈼硷笍鈼硷笍\n鈼硷笍鈼硷笍鈼硷笍鈼硷笍鈼硷笍\n鈼硷笍鈼硷笍鈼硷笍鈼硷笍鈼硷笍",
        "鈼伙笍鈼硷笍鈼硷笍鈼硷笍鈼硷笍\n鈼硷笍鈼硷笍鈼硷笍鈼硷笍鈼硷笍\n鈼硷笍鈼硷笍鈼硷笍鈼硷笍鈼硷笍\n鈼硷笍鈼硷笍鈼硷笍鈼硷笍鈼硷笍\n鈼硷笍鈼硷笍鈼硷笍鈼硷笍鈼硷笍",
        "鈼硷笍鈼伙笍鈼硷笍鈼硷笍鈼硷笍\n鈼硷笍鈼硷笍鈼硷笍鈼硷笍鈼硷笍\n鈼硷笍鈼硷笍鈼硷笍鈼硷笍鈼硷笍\n鈼硷笍鈼硷笍鈼硷笍鈼硷笍鈼硷笍\n鈼硷笍鈼硷笍鈼硷笍鈼硷笍鈼硷笍",
        "鈼硷笍鈼硷笍鈼伙笍鈼硷笍鈼硷笍\n鈼硷笍鈼硷笍鈼硷笍鈼硷笍鈼硷笍\n鈼硷笍鈼硷笍鈼硷笍鈼硷笍鈼硷笍\n鈼硷笍鈼硷笍鈼硷笍鈼硷笍鈼硷笍\n鈼硷笍鈼硷笍鈼硷笍鈼硷笍鈼硷笍",
        "鈼硷笍鈼硷笍鈼硷笍鈼伙笍鈼硷笍\n鈼硷笍鈼硷笍鈼硷笍鈼硷笍鈼硷笍\n鈼硷笍鈼硷笍鈼硷笍鈼硷笍鈼硷笍\n鈼硷笍鈼硷笍鈼硷笍鈼硷笍鈼硷笍\n鈼硷笍鈼硷笍鈼硷笍鈼硷笍鈼硷笍",
        "鈼硷笍鈼硷笍鈼硷笍鈼硷笍鈼伙笍\n鈼硷笍鈼硷笍鈼硷笍鈼硷笍鈼硷笍\n鈼硷笍鈼硷笍鈼硷笍鈼硷笍鈼硷笍\n鈼硷笍鈼硷笍鈼硷笍鈼硷笍鈼硷笍\n鈼硷笍鈼硷笍鈼硷笍鈼硷笍鈼硷笍",
        "鈼硷笍鈼硷笍鈼硷笍鈼硷笍鈼硷笍\n鈼硷笍鈼硷笍鈼硷笍鈼硷笍鈼伙笍\n鈼硷笍鈼硷笍鈼硷笍鈼硷笍鈼硷笍\n鈼硷笍鈼硷笍鈼硷笍鈼硷笍鈼硷笍\n鈼硷笍鈼硷笍鈼硷笍鈼硷笍鈼硷笍",
        "鈼硷笍鈼硷笍鈼硷笍鈼硷笍鈼硷笍\n鈼硷笍鈼硷笍鈼硷笍鈼伙笍鈼硷笍\n鈼硷笍鈼硷笍鈼硷笍鈼硷笍鈼硷笍\n鈼硷笍鈼硷笍鈼硷笍鈼硷笍鈼硷笍\n鈼硷笍鈼硷笍鈼硷笍鈼硷笍鈼硷笍",
        "鈼硷笍鈼硷笍鈼硷笍鈼硷笍鈼硷笍\n鈼硷笍鈼硷笍鈼伙笍鈼硷笍鈼硷笍\n鈼硷笍鈼硷笍鈼硷笍鈼硷笍鈼硷笍\n鈼硷笍鈼硷笍鈼硷笍鈼硷笍鈼硷笍\n鈼硷笍鈼硷笍鈼硷笍鈼硷笍鈼硷笍",
        "鈼硷笍鈼硷笍鈼硷笍鈼硷笍鈼硷笍\n鈼硷笍鈼伙笍鈼硷笍鈼硷笍鈼硷笍\n鈼硷笍鈼硷笍鈼硷笍鈼硷笍鈼硷笍\n鈼硷笍鈼硷笍鈼硷笍鈼硷笍鈼硷笍\n鈼硷笍鈼硷笍鈼硷笍鈼硷笍鈼硷笍",
        "鈼硷笍鈼硷笍鈼硷笍鈼硷笍鈼硷笍\n鈼伙笍鈼硷笍鈼硷笍鈼硷笍鈼硷笍\n鈼硷笍鈼硷笍鈼硷笍鈼硷笍鈼硷笍\n鈼硷笍鈼硷笍鈼硷笍鈼硷笍鈼硷笍\n鈼硷笍鈼硷笍鈼硷笍鈼硷笍鈼硷笍",
        "鈼硷笍鈼硷笍鈼硷笍鈼硷笍鈼硷笍\n鈼硷笍鈼硷笍鈼硷笍鈼硷笍鈼硷笍\n鈼伙笍鈼硷笍鈼硷笍鈼硷笍鈼硷笍\n鈼硷笍鈼硷笍鈼硷笍鈼硷笍鈼硷笍\n鈼硷笍鈼硷笍鈼硷笍鈼硷笍鈼硷笍",
        "鈼硷笍鈼硷笍鈼硷笍鈼硷笍鈼硷笍\n鈼硷笍鈼硷笍鈼硷笍鈼硷笍鈼硷笍\n鈼硷笍鈼伙笍鈼硷笍鈼硷笍鈼硷笍\n鈼硷笍鈼硷笍鈼硷笍鈼硷笍鈼硷笍\n鈼硷笍鈼硷笍鈼硷笍鈼硷笍鈼硷笍",
        "鈼硷笍鈼硷笍鈼硷笍鈼硷笍鈼硷笍\n鈼硷笍鈼硷笍鈼硷笍鈼硷笍鈼硷笍\n鈼硷笍鈼硷笍鈼伙笍鈼硷笍鈼硷笍\n鈼硷笍鈼硷笍鈼硷笍鈼硷笍鈼硷笍\n鈼硷笍鈼硷笍鈼硷笍鈼硷笍鈼硷笍",
        "鈼硷笍鈼硷笍鈼硷笍鈼硷笍鈼硷笍\n鈼硷笍鈼硷笍鈼硷笍鈼硷笍鈼硷笍\n鈼硷笍鈼硷笍鈼硷笍鈼伙笍鈼硷笍\n鈼硷笍鈼硷笍鈼硷笍鈼硷笍鈼硷笍\n鈼硷笍鈼硷笍鈼硷笍鈼硷笍鈼硷笍",
        "鈼硷笍鈼硷笍鈼硷笍鈼硷笍鈼硷笍\n鈼硷笍鈼硷笍鈼硷笍鈼硷笍鈼硷笍\n鈼硷笍鈼硷笍鈼硷笍鈼硷笍鈼伙笍\n鈼硷笍鈼硷笍鈼硷笍鈼硷笍鈼硷笍\n鈼硷笍鈼硷笍鈼硷笍鈼硷笍鈼硷笍",
        "鈼硷笍鈼硷笍鈼硷笍鈼硷笍鈼硷笍\n鈼硷笍鈼硷笍鈼硷笍鈼硷笍鈼硷笍\n鈼硷笍鈼硷笍鈼硷笍鈼硷笍鈼硷笍\n鈼硷笍鈼硷笍鈼硷笍鈼硷笍鈼伙笍\n鈼硷笍鈼硷笍鈼硷笍鈼硷笍鈼硷笍",
        "鈼硷笍鈼硷笍鈼硷笍鈼硷笍鈼硷笍\n鈼硷笍鈼硷笍鈼硷笍鈼硷笍鈼硷笍\n鈼硷笍鈼硷笍鈼硷笍鈼硷笍鈼硷笍\n鈼硷笍鈼硷笍鈼硷笍鈼伙笍鈼硷笍\n鈼硷笍鈼硷笍鈼硷笍鈼硷笍鈼硷笍",
        "鈼硷笍鈼硷笍鈼硷笍鈼硷笍鈼硷笍\n鈼硷笍鈼硷笍鈼硷笍鈼硷笍鈼硷笍\n鈼硷笍鈼硷笍鈼硷笍鈼硷笍鈼硷笍\n鈼硷笍鈼硷笍鈼伙笍鈼硷笍鈼硷笍\n鈼硷笍鈼硷笍鈼硷笍鈼硷笍鈼硷笍",
        "鈼硷笍鈼硷笍鈼硷笍鈼硷笍鈼硷笍\n鈼硷笍鈼硷笍鈼硷笍鈼硷笍鈼硷笍\n鈼硷笍鈼硷笍鈼硷笍鈼硷笍鈼硷笍\n鈼硷笍鈼伙笍鈼硷笍鈼硷笍鈼硷笍\n鈼硷笍鈼硷笍鈼硷笍鈼硷笍鈼硷笍",
        "鈼硷笍鈼硷笍鈼硷笍鈼硷笍鈼硷笍\n鈼硷笍鈼硷笍鈼硷笍鈼硷笍鈼硷笍\n鈼硷笍鈼硷笍鈼硷笍鈼硷笍鈼硷笍\n鈼伙笍鈼硷笍鈼硷笍鈼硷笍鈼硷笍\n鈼硷笍鈼硷笍鈼硷笍鈼硷笍鈼硷笍",
        "鈼硷笍鈼硷笍鈼硷笍鈼硷笍鈼硷笍\n鈼硷笍鈼硷笍鈼硷笍鈼硷笍鈼硷笍\n鈼硷笍鈼硷笍鈼硷笍鈼硷笍鈼硷笍\n鈼硷笍鈼硷笍鈼硷笍鈼硷笍鈼硷笍\n鈼伙笍鈼硷笍鈼硷笍鈼硷笍鈼硷笍",
        "鈼硷笍鈼硷笍鈼硷笍鈼硷笍鈼硷笍\n鈼硷笍鈼硷笍鈼硷笍鈼硷笍鈼硷笍\n鈼硷笍鈼硷笍鈼硷笍鈼硷笍鈼硷笍\n鈼硷笍鈼硷笍鈼硷笍鈼硷笍鈼硷笍\n鈼硷笍鈼伙笍鈼硷笍鈼硷笍鈼硷笍",
        "鈼硷笍鈼硷笍鈼硷笍鈼硷笍鈼硷笍\n鈼硷笍鈼硷笍鈼硷笍鈼硷笍鈼硷笍\n鈼硷笍鈼硷笍鈼硷笍鈼硷笍鈼硷笍\n鈼硷笍鈼硷笍鈼硷笍鈼硷笍鈼硷笍\n鈼硷笍鈼硷笍鈼伙笍鈼硷笍鈼硷笍",
        "鈼硷笍鈼硷笍鈼硷笍鈼硷笍鈼硷笍\n鈼硷笍鈼硷笍鈼硷笍鈼硷笍鈼硷笍\n鈼硷笍鈼硷笍鈼硷笍鈼硷笍鈼硷笍\n鈼硷笍鈼硷笍鈼硷笍鈼硷笍鈼硷笍\n鈼硷笍鈼硷笍鈼硷笍鈼伙笍鈼硷笍",
        "鈼硷笍鈼硷笍鈼硷笍鈼硷笍鈼硷笍\n鈼硷笍鈼硷笍鈼硷笍鈼硷笍鈼硷笍\n鈼硷笍鈼硷笍鈼硷笍鈼硷笍鈼硷笍\n鈼硷笍鈼硷笍鈼硷笍鈼硷笍鈼硷笍\n鈼硷笍鈼硷笍鈼硷笍鈼硷笍鈼伙笍",
        "鈼硷笍鈼硷笍鈼硷笍鈼硷笍鈼硷笍\n鈼硷笍鈼硷笍鈼硷笍鈼硷笍鈼硷笍\n鈼硷笍鈼硷笍鈼硷笍鈼硷笍鈼硷笍\n鈼硷笍鈼硷笍鈼硷笍鈼硷笍鈼硷笍\n鈼硷笍鈼硷笍鈼硷笍鈼硷笍鈼硷笍",
        "鈼硷笍鈼硷笍鈼硷笍鈼硷笍鈼硷笍\n鈼硷笍鈼伙笍鈼硷笍鈼伙笍鈼硷笍\n鈼硷笍鈼硷笍鈼硷笍鈼硷笍鈼硷笍\n鈼硷笍鈼伙笍鈼伙笍鈼伙笍鈼硷笍\n鈼硷笍鈼硷笍鈼硷笍鈼硷笍鈼硷笍",
    ]
    for i in animation_ttl:
        await asyncio.sleep(animation_interval)
        await event.edit(animation_chars[i % 28])


@bot.on(admin_cmd(pattern="virus$"))
@bot.on(sudo_cmd(pattern="virus$", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    animation_interval = 1
    animation_ttl = range(30)
    event = await edit_or_reply(event, "Injecting virus....")
    animation_chars = [
        "馃敶馃數馃寱鈾撯檸鉀庰煍答煍叼煂曗檽鈾庘泿馃敶馃數馃寱鈾撯檸鉀庰煍答煍叼煂曗檽鈾庘泿馃敶馃數馃寱鈾撯檸鉀嶾n馃敶馃數馃寱鈾撯檸鉀庰煍答煍叼煂曗檽鈾庘泿馃敶馃數馃寱鈾撯檸鉀庰煍答煍叼煂曗檽鈾庘泿馃敶馃數馃寱鈾撯檸鉀嶾n馃敶馃數馃寱鈾撯檸鉀庰煍答煍叼煂曗檽鈾庘泿馃敶馃數馃寱鈾撯檸鉀庰煍答煍叼煂曗檽鈾庘泿馃敶馃數馃寱鈾撯檸鉀嶾n馃敶馃數馃寱鈾撯檸鉀庰煍答煍叼煂曗檽鈾庘泿馃敶馃數馃寱鈾撯檸鉀庰煍答煍叼煂曗檽鈾庘泿馃敶馃數馃寱鈾撯檸鉀嶾n馃敶馃數馃寱鈾撯檸鉀庰煍答煍叼煂曗檽鈾庘泿馃敶馃數馃寱鈾撯檸鉀庰煍答煍叼煂曗檽鈾庘泿馃敶馃數馃寱鈾撯檸鉀�",
        "鈼硷笍馃敶馃數馃寱鈾撯檸鉀庰煍答煍叼煂曗檽鈾庘泿馃敶馃數馃寱鈾撯檸鉀庰煍答煍叼煂曗檽鈾庘泿\n馃敶馃數馃寱鈾撯檸鉀庰煍答煍叼煂曗檽鈾庘泿馃敶馃數馃寱鈾撯檸鉀庰煍答煍叼煂曗檽鈾庘泿馃敶馃數馃寱鈾撯檸鉀嶾n馃敶馃數馃寱鈾撯檸鉀庰煍答煍叼煂曗檽鈾庘泿馃敶馃數馃寱鈾撯檸鉀庰煍答煍叼煂曗檽鈾庘泿馃敶馃數馃寱鈾撯檸鉀嶾n馃敶馃數馃寱鈾撯檸鉀庰煍答煍叼煂曗檽鈾庘泿馃敶馃數馃寱鈾撯檸鉀庰煍答煍叼煂曗檽鈾庘泿馃敶馃數馃寱鈾撯檸鉀嶾n馃敶馃數馃寱鈾撯檸鉀庰煍答煍叼煂曗檽鈾庘泿馃敶馃數馃寱鈾撯檸鉀庰煍答煍叼煂曗檽鈾庘泿馃敶馃數馃寱鈾撯檸鉀�",
        "鈼硷笍鈼硷笍馃敶馃數馃寱鈾撯檸鉀庰煍答煍叼煂曗檽鈾庘泿馃敶馃數馃寱鈾撯檸鉀嶾n馃敶馃數馃寱鈾撯檸鉀庰煍答煍叼煂曗檽鈾庘泿馃敶馃數馃寱鈾撯檸鉀庰煍答煍叼煂曗檽鈾庘泿馃敶馃數馃寱鈾撯檸鉀嶾n馃敶馃數馃寱鈾撯檸鉀庰煍答煍叼煂曗檽鈾庘泿馃敶馃數馃寱鈾撯檸鉀庰煍答煍叼煂曗檽鈾庘泿馃敶馃數馃寱鈾撯檸鉀嶾n馃敶馃數馃寱鈾撯檸鉀庰煍答煍叼煂曗檽鈾庘泿馃敶馃數馃寱鈾撯檸鉀庰煍答煍叼煂曗檽鈾庘泿馃敶馃數馃寱鈾撯檸鉀嶾n馃敶馃數馃寱鈾撯檸鉀庰煍答煍叼煂曗檽鈾庘泿馃敶馃數馃寱鈾撯檸鉀庰煍答煍叼煂曗檽鈾庘泿馃敶馃數馃寱鈾撯檸鉀�",
        "鈼硷笍鈼硷笍鈼硷笍锔忦煍答煍叼煂曗檽鈾庘泿馃敶馃數馃寱鈾撯檸鉀嶾n馃敶馃數馃寱鈾撯檸鉀庰煍答煍叼煂曗檽鈾庘泿馃敶馃數馃寱鈾撯檸鉀庰煍答煍叼煂曗檽鈾庘泿馃敶馃數馃寱鈾撯檸鉀嶾n馃敶馃數馃寱鈾撯檸鉀庰煍答煍叼煂曗檽鈾庘泿馃敶馃數馃寱鈾撯檸鉀庰煍答煍叼煂曗檽鈾庘泿馃敶馃數馃寱鈾撯檸鉀嶾n馃敶馃數馃寱鈾撯檸鉀庰煍答煍叼煂曗檽鈾庘泿馃敶馃數馃寱鈾撯檸鉀庰煍答煍叼煂曗檽鈾庘泿馃敶馃數馃寱鈾撯檸鉀嶾n馃敶馃數馃寱鈾撯檸鉀庰煍答煍叼煂曗檽鈾庘泿馃敶馃數馃寱鈾撯檸鉀庰煍答煍叼煂曗檽鈾庘泿馃敶馃數馃寱鈾撯檸鉀�",
        "鈼硷笍鈼硷笍鈼硷笍鈼硷笍馃敶馃數馃寱鈾撯檸鉀嶾n馃敶馃數馃寱鈾撯檸鉀庰煍答煍叼煂曗檽鈾庘泿馃敶馃數馃寱鈾撯檸鉀庰煍答煍叼煂曗檽鈾庘泿馃敶馃數馃寱鈾撯檸鉀嶾n馃敶馃數馃寱鈾撯檸鉀庰煍答煍叼煂曗檽鈾庘泿馃敶馃數馃寱鈾撯檸鉀庰煍答煍叼煂曗檽鈾庘泿馃敶馃數馃寱鈾撯檸鉀嶾n馃敶馃數馃寱鈾撯檸鉀庰煍答煍叼煂曗檽鈾庘泿馃敶馃數馃寱鈾撯檸鉀庰煍答煍叼煂曗檽鈾庘泿馃敶馃數馃寱鈾撯檸鉀嶾n馃敶馃數馃寱鈾撯檸鉀庰煍答煍叼煂曗檽鈾庘泿馃敶馃數馃寱鈾撯檸鉀庰煍答煍叼煂曗檽鈾庘泿馃敶馃數馃寱鈾撯檸鉀�",
        "鈥庘椉锔忊椉锔忊椉锔忊椉锔忊椉锔廫n馃敶馃數馃寱鈾撯檸鉀庰煍答煍叼煂曗檽鈾庘泿馃敶馃數馃寱鈾撯檸鉀庰煍答煍叼煂曗檽鈾庘泿馃敶馃數馃寱鈾撯檸鉀嶾n馃敶馃數馃寱鈾撯檸鉀庰煍答煍叼煂曗檽鈾庘泿馃敶馃數馃寱鈾撯檸鉀庰煍答煍叼煂曗檽鈾庘泿馃敶馃數馃寱鈾撯檸鉀嶾n馃敶馃數馃寱鈾撯檸鉀庰煍答煍叼煂曗檽鈾庘泿馃敶馃數馃寱鈾撯檸鉀庰煍答煍叼煂曗檽鈾庘泿馃敶馃數馃寱鈾撯檸鉀嶾n馃敶馃數馃寱鈾撯檸鉀庰煍答煍叼煂曗檽鈾庘泿馃敶馃數馃寱鈾撯檸鉀庰煍答煍叼煂曗檽鈾庘泿馃敶馃數馃寱鈾撯檸鉀�",
        "鈼硷笍鈼硷笍鈼硷笍鈼硷笍鈼硷笍\n馃敶馃數馃寱鈾撯檸鉀庰煍答煍叼煂曗檽鈾庘泿馃敶馃數馃寱鈾撯檸鉀庰煍答煍叼煂曗檽鈾庘泿鈼硷笍\n馃敶馃數馃寱鈾撯檸鉀庰煍答煍叼煂曗檽鈾庘泿馃敶馃數馃寱鈾撯檸鉀庰煍答煍叼煂曗檽鈾庘泿馃敶馃數馃寱鈾撯檸鉀嶾n馃敶馃數馃寱鈾撯檸鉀庰煍答煍叼煂曗檽鈾庘泿馃敶馃數馃寱鈾撯檸鉀庰煍答煍叼煂曗檽鈾庘泿馃敶馃數馃寱鈾撯檸鉀嶾n馃敶馃數馃寱鈾撯檸鉀庰煍答煍叼煂曗檽鈾庘泿馃敶馃數馃寱鈾撯檸鉀庰煍答煍叼煂曗檽鈾庘泿馃敶馃數馃寱鈾撯檸鉀�",
        "鈼硷笍鈼硷笍鈼硷笍鈼硷笍鈼硷笍\n馃敶馃數馃寱鈾撯檸鉀庰煍答煍叼煂曗檽鈾庘泿馃敶馃數馃寱鈾撯檸鉀庰煍答煍叼煂曗檽鈾庘泿鈼硷笍\n馃敶馃數馃寱鈾撯檸鉀庰煍答煍叼煂曗檽鈾庘泿馃敶馃數馃寱鈾撯檸鉀庰煍答煍叼煂曗檽鈾庘泿鈼硷笍\n馃敶馃數馃寱鈾撯檸鉀庰煍答煍叼煂曗檽鈾庘泿馃敶馃數馃寱鈾撯檸鉀庰煍答煍叼煂曗檽鈾庘泿馃敶馃數馃寱鈾撯檸鉀嶾n馃敶馃數馃寱鈾撯檸鉀庰煍答煍叼煂曗檽鈾庘泿馃敶馃數馃寱鈾撯檸鉀庰煍答煍叼煂曗檽鈾庘泿馃敶馃數馃寱鈾撯檸鉀�",
        "鈼硷笍鈼硷笍鈼硷笍鈼硷笍鈼硷笍\n馃敶馃數馃寱鈾撯檸鉀庰煍答煍叼煂曗檽鈾庘泿馃敶馃數馃寱鈾撯檸鉀庰煍答煍叼煂曗檽鈾庘泿鈼硷笍\n馃敶馃數馃寱鈾撯檸鉀庰煍答煍叼煂曗檽鈾庘泿馃敶馃數馃寱鈾撯檸鉀庰煍答煍叼煂曗檽鈾庘泿鈼硷笍\n馃敶馃數馃寱鈾撯檸鉀庰煍答煍叼煂曗檽鈾庘泿馃敶馃數馃寱鈾撯檸鉀庰煍答煍叼煂曗檽鈾庘泿鈼硷笍\n馃敶馃數馃寱鈾撯檸鉀庰煍答煍叼煂曗檽鈾庘泿馃敶馃數馃寱鈾撯檸鉀庰煍答煍叼煂曗檽鈾庘泿馃敶馃數馃寱鈾撯檸鉀�",
        "鈼硷笍鈼硷笍鈼硷笍鈼硷笍鈼硷笍\n馃敶馃數馃寱鈾撯檸鉀庰煍答煍叼煂曗檽鈾庘泿馃敶馃數馃寱鈾撯檸鉀庰煍答煍叼煂曗檽鈾庘泿鈼硷笍\n馃敶馃數馃寱鈾撯檸鉀庰煍答煍叼煂曗檽鈾庘泿馃敶馃數馃寱鈾撯檸鉀庰煍答煍叼煂曗檽鈾庘泿鈼硷笍\n馃敶馃數馃寱鈾撯檸鉀庰煍答煍叼煂曗檽鈾庘泿馃敶馃數馃寱鈾撯檸鉀庰煍答煍叼煂曗檽鈾庘泿鈼硷笍\n馃敶馃數馃寱鈾撯檸鉀庰煍答煍叼煂曗檽鈾庘泿馃敶馃數馃寱鈾撯檸鉀庰煍答煍叼煂曗檽鈾庘泿鈼硷笍",
        "鈼硷笍鈼硷笍鈼硷笍鈼硷笍鈼硷笍\n馃敶馃數馃寱鈾撯檸鉀庰煍答煍叼煂曗檽鈾庘泿馃敶馃數馃寱鈾撯檸鉀庰煍答煍叼煂曗檽鈾庘泿鈼硷笍\n馃敶馃數馃寱鈾撯檸鉀庰煍答煍叼煂曗檽鈾庘泿馃敶馃數馃寱鈾撯檸鉀庰煍答煍叼煂曗檽鈾庘泿鈼硷笍\n馃敶馃數馃寱鈾撯檸鉀庰煍答煍叼煂曗檽鈾庘泿馃敶馃數馃寱鈾撯檸鉀庰煍答煍叼煂曗檽鈾庘泿鈼硷笍\n馃敶馃數馃寱鈾撯檸鉀庰煍答煍叼煂曗檽鈾庘泿馃敶馃數馃寱鈾撯檸鉀庘椉锔忊椉锔�",
        "鈼硷笍鈼硷笍鈼硷笍鈼硷笍鈼硷笍\n馃敶馃數馃寱鈾撯檸鉀庰煍答煍叼煂曗檽鈾庘泿馃敶馃數馃寱鈾撯檸鉀庰煍答煍叼煂曗檽鈾庘泿鈼硷笍\n馃敶馃數馃寱鈾撯檸鉀庰煍答煍叼煂曗檽鈾庘泿馃敶馃數馃寱鈾撯檸鉀庰煍答煍叼煂曗檽鈾庘泿鈼硷笍\n馃敶馃數馃寱鈾撯檸鉀庰煍答煍叼煂曗檽鈾庘泿馃敶馃數馃寱鈾撯檸鉀庰煍答煍叼煂曗檽鈾庘泿鈼硷笍\n馃敶馃數馃寱鈾撯檸鉀庰煍答煍叼煂曗檽鈾庘泿鈼硷笍鈼硷笍鈼硷笍",
        "鈼硷笍鈼硷笍鈼硷笍鈼硷笍鈼硷笍\n馃敶馃數馃寱鈾撯檸鉀庰煍答煍叼煂曗檽鈾庘泿馃敶馃數馃寱鈾撯檸鉀庰煍答煍叼煂曗檽鈾庘泿鈼硷笍\n馃敶馃數馃寱鈾撯檸鉀庰煍答煍叼煂曗檽鈾庘泿馃敶馃數馃寱鈾撯檸鉀庰煍答煍叼煂曗檽鈾庘泿鈼硷笍\n馃敶馃數馃寱鈾撯檸鉀庰煍答煍叼煂曗檽鈾庘泿馃敶馃數馃寱鈾撯檸鉀庰煍答煍叼煂曗檽鈾庘泿鈼硷笍\n馃敶馃數馃寱鈾撯檸鉀庘椉锔忊椉锔忊椉锔忊椉锔�",
        "鈼硷笍鈼硷笍鈼硷笍鈼硷笍鈼硷笍\n馃敶馃數馃寱鈾撯檸鉀庰煍答煍叼煂曗檽鈾庘泿馃敶馃數馃寱鈾撯檸鉀庰煍答煍叼煂曗檽鈾庘泿鈼硷笍\n馃敶馃數馃寱鈾撯檸鉀庰煍答煍叼煂曗檽鈾庘泿馃敶馃數馃寱鈾撯檸鉀庰煍答煍叼煂曗檽鈾庘泿鈼硷笍\n馃敶馃數馃寱鈾撯檸鉀庰煍答煍叼煂曗檽鈾庘泿馃敶馃數馃寱鈾撯檸鉀庰煍答煍叼煂曗檽鈾庘泿鈼硷笍\n鈼硷笍鈼硷笍鈼硷笍鈼硷笍鈼硷笍",
        "鈼硷笍鈼硷笍鈼硷笍鈼硷笍鈼硷笍\n馃敶馃數馃寱鈾撯檸鉀庰煍答煍叼煂曗檽鈾庘泿馃敶馃數馃寱鈾撯檸鉀庰煍答煍叼煂曗檽鈾庘泿鈼硷笍\n馃敶馃數馃寱鈾撯檸鉀庰煍答煍叼煂曗檽鈾庘泿馃敶馃數馃寱鈾撯檸鉀庰煍答煍叼煂曗檽鈾庘泿鈼硷笍\n鈼硷笍馃敶馃數馃寱鈾撯檸鉀庰煍答煍叼煂曗檽鈾庘泿馃敶馃數馃寱鈾撯檸鉀庘椉锔廫n鈼硷笍鈼硷笍鈼硷笍鈼硷笍鈼硷笍",
        "鈼硷笍鈼硷笍鈼硷笍鈼硷笍鈼硷笍\n馃敶馃數馃寱鈾撯檸鉀庰煍答煍叼煂曗檽鈾庘泿馃敶馃數馃寱鈾撯檸鉀庰煍答煍叼煂曗檽鈾庘泿鈼硷笍\n鈼硷笍馃敶馃數馃寱鈾撯檸鉀庰煍答煍叼煂曗檽鈾庘泿馃敶馃數馃寱鈾撯檸鉀庘椉锔廫n鈼硷笍馃敶馃數馃寱鈾撯檸鉀庰煍答煍叼煂曗檽鈾庘泿馃敶馃數馃寱鈾撯檸鉀庘椉锔廫n鈼硷笍鈼硷笍鈼硷笍鈼硷笍鈼硷笍",
        "鈼硷笍鈼硷笍鈼硷笍鈼硷笍鈼硷笍\n鈼硷笍馃敶馃數馃寱鈾撯檸鉀庰煍答煍叼煂曗檽鈾庘泿馃敶馃數馃寱鈾撯檸鉀庘椉锔廫n鈼硷笍馃敶馃數馃寱鈾撯檸鉀庰煍答煍叼煂曗檽鈾庘泿馃敶馃數馃寱鈾撯檸鉀庘椉锔廫n鈼硷笍馃敶馃數馃寱鈾撯檸鉀庰煍答煍叼煂曗檽鈾庘泿馃敶馃數馃寱鈾撯檸鉀庘椉锔廫n鈼硷笍鈼硷笍鈼硷笍鈼硷笍鈼硷笍",
        "鈼硷笍鈼硷笍鈼硷笍鈼硷笍鈼硷笍\n鈼硷笍鈼硷笍馃敶馃數馃寱鈾撯檸鉀庰煍答煍叼煂曗檽鈾庘泿鈼硷笍\n鈼硷笍馃敶馃數馃寱鈾撯檸鉀庰煍答煍叼煂曗檽鈾庘泿馃敶馃數馃寱鈾撯檸鉀庘椉锔廫n鈼硷笍馃敶馃數馃寱鈾撯檸鉀庰煍答煍叼煂曗檽鈾庘泿馃敶馃數馃寱鈾撯檸鉀庘椉锔廫n鈼硷笍鈼硷笍鈼硷笍鈼硷笍鈼硷笍",
        "鈼硷笍鈼硷笍鈼硷笍鈼硷笍鈼硷笍\n鈼硷笍鈼硷笍鈼硷笍馃敶馃數馃寱鈾撯檸鉀庘椉锔廫n鈼硷笍馃敶馃數馃寱鈾撯檸鉀庰煍答煍叼煂曗檽鈾庘泿馃敶馃數馃寱鈾撯檸鉀庘椉锔廫n鈼硷笍馃敶馃數馃寱鈾撯檸鉀庰煍答煍叼煂曗檽鈾庘泿馃敶馃數馃寱鈾撯檸鉀庘椉锔廫n鈼硷笍鈼硷笍鈼硷笍鈼硷笍鈼硷笍",
        "鈼硷笍鈼硷笍鈼硷笍鈼硷笍鈼硷笍\n鈼硷笍鈼硷笍鈼硷笍鈼硷笍鈼硷笍\n鈼硷笍馃敶馃數馃寱鈾撯檸鉀庰煍答煍叼煂曗檽鈾庘泿馃敶馃數馃寱鈾撯檸鉀庘椉锔廫n鈼硷笍馃敶馃數馃寱鈾撯檸鉀庰煍答煍叼煂曗檽鈾庘泿馃敶馃數馃寱鈾撯檸鉀庘椉锔廫n鈼硷笍鈼硷笍鈼硷笍鈼硷笍鈼硷笍",
        "鈼硷笍鈼硷笍鈼硷笍鈼硷笍鈼硷笍\n鈼硷笍鈼硷笍鈼硷笍鈼硷笍鈼硷笍\n鈼硷笍馃敶馃數馃寱鈾撯檸鉀庰煍答煍叼煂曗檽鈾庘泿鈼硷笍鈼硷笍\n鈼硷笍馃敶馃數馃寱鈾撯檸鉀庰煍答煍叼煂曗檽鈾庘泿馃敶馃數馃寱鈾撯檸鉀庘椉锔廫n鈼硷笍鈼硷笍鈼硷笍鈼硷笍鈼硷笍",
        "鈼硷笍鈼硷笍鈼硷笍鈼硷笍鈼硷笍\n鈼硷笍鈼硷笍鈼硷笍鈼硷笍鈼硷笍\n鈼硷笍馃敶馃數馃寱鈾撯檸鉀庰煍答煍叼煂曗檽鈾庘泿鈼硷笍鈼硷笍\n鈼硷笍馃敶馃數馃寱鈾撯檸鉀庰煍答煍叼煂曗檽鈾庘泿鈼硷笍鈼硷笍\n鈼硷笍鈼硷笍鈼硷笍鈼硷笍鈼硷笍",
        "鈼硷笍鈼硷笍鈼硷笍鈼硷笍鈼硷笍\n鈼硷笍鈼硷笍鈼硷笍鈼硷笍鈼硷笍\n鈼硷笍馃敶馃數馃寱鈾撯檸鉀庰煍答煍叼煂曗檽鈾庘泿鈼硷笍鈼硷笍\n鈼硷笍馃敶馃數馃寱鈾撯檸鉀庘椉锔忊椉锔忊椉锔廫n鈼硷笍鈼硷笍鈼硷笍鈼硷笍鈼硷笍",
        "鈼硷笍鈼硷笍鈼硷笍鈼硷笍鈼硷笍\n鈼硷笍鈼硷笍鈼硷笍鈼硷笍鈼硷笍\n鈼硷笍馃敶馃數馃寱鈾撯檸鉀庰煍答煍叼煂曗檽鈾庘泿鈼硷笍鈼硷笍\n鈼硷笍鈼硷笍鈼硷笍鈼硷笍鈼硷笍\n鈼硷笍鈼硷笍鈼硷笍鈼硷笍鈼硷笍",
        "鈼硷笍鈼硷笍鈼硷笍鈼硷笍鈼硷笍\n鈼硷笍鈼硷笍鈼硷笍鈼硷笍鈼硷笍\n鈼硷笍鈼硷笍馃敶馃數馃寱鈾撯檸鉀庘椉锔忊椉锔廫n鈼硷笍鈼硷笍鈼硷笍鈼硷笍鈼硷笍\n鈼硷笍鈼硷笍鈼硷笍鈼硷笍鈼硷笍",
        "鈼硷笍鈼硷笍鈼硷笍鈼硷笍鈼硷笍\n鈼硷笍鈼硷笍鈼硷笍鈼硷笍鈼硷笍\n鈼硷笍鈼硷笍鈼硷笍鈼硷笍鈼硷笍\n鈼硷笍鈼硷笍鈼硷笍鈼硷笍鈼硷笍\n鈼硷笍鈼硷笍鈼硷笍鈼硷笍鈼硷笍",
        "鈼硷笍鈼硷笍鈼硷笍鈼硷笍\n鈼硷笍鈼硷笍鈼硷笍鈼硷笍\n鈼硷笍鈼硷笍鈼硷笍鈼硷笍\n鈼硷笍鈼硷笍鈼硷笍鈼硷笍",
        "鈼硷笍鈼硷笍鈼硷笍\n鈼硷笍鈼硷笍鈼硷笍\n鈼硷笍鈼硷笍鈼硷笍",
        "鈼硷笍鈼硷笍\n鈼硷笍鈼硷笍",
        "鈼硷笍",
    ]
    for i in animation_ttl:
        await asyncio.sleep(animation_interval)
        await event.edit(animation_chars[i % 30])


@bot.on(admin_cmd(pattern=r"repe$", outgoing=True))
@bot.on(sudo_cmd(pattern="repe$", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    animation_interval = 0.2
    animation_ttl = range(30)
    event = await edit_or_reply(event, "repe")
    animation_chars = [
        "**r**",
        "**ra**",
        "**rap**",
        "**rape**",
        "**rape_**",
        "**rape_t**",
        "**rape_tr**",
        "**rape_tra**",
        "**rape_trai**",
        "**rape_train**",
        "**ape_train馃殔**",
        "**pe_train馃殔馃殐馃殐**",
        "**e_train馃殔馃殐馃殐馃殐**",
        "**_train馃殔馃殐馃殐馃殐馃殐**",
        "**train馃殔馃殐馃殐馃殐馃殐馃殐**",
        "**rain馃殔馃殐馃殐馃殐馃殐馃殐馃殐**",
        "**ain馃殔馃殐馃殐馃殐馃殐馃殐馃殐馃殐**",
        "**in馃殔馃殐馃殐馃殐馃殐馃殐馃殐馃殐馃殐**",
        "**n馃殔馃殐馃殐馃殐馃殐馃殐馃殐馃殐馃殐馃殐**",
        "馃殔馃殐馃殐馃殐馃殐馃殐馃殐馃殐馃殐馃殐",
        "馃殐馃殐馃殐馃殐馃殐馃殐馃殐馃殐馃殐",
        "馃殐馃殐馃殐馃殐馃殐馃殐馃殐馃殐",
        "馃殐馃殐馃殐馃殐馃殐馃殐馃殐",
        "馃殐馃殐馃殐馃殐馃殐馃殐",
        "馃殐馃殐馃殐馃殐馃殐",
        "馃殐馃殐馃殐馃殐",
        "馃殐馃殐馃殐",
        "馃殐馃殐",
        "馃殐",
        "**rApEd**",
    ]
    for i in animation_ttl:
        await asyncio.sleep(animation_interval)
        await event.edit(animation_chars[i % 30])


@bot.on(admin_cmd(pattern=f"nikal$", outgoing=True))
@bot.on(sudo_cmd(pattern="nikal$", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    animation_interval = 0.5
    animation_ttl = range(6)
    event = await edit_or_reply(event, "nakal")
    animation_chars = [
        "`鉅�鉅�鉅�猓犫６狻锯爮鉅夆牂鉅斥ⅵ狻�鉅�鉅�鉅�猗犫牉鉅夆牂鉅测鉅�\n 鉅�猓粹牽鉅忊爛鉅�鉅�鉅�鉅�   猗斥鉅�狻忊爛鉅�鉅�   鉅�猗穃n猗犫猓嬧猗�猓�猓�狻�鉅�猓�狻�猓р爛猗糕爛鉅�鉅�  鉅�   狻嘰n猗糕／狻爜鉅糕猓熲爢狻粹；狻测？  猓� Nikal   狻嘰n 猓熲？狻爛鉅�鉅�鉅�鉅�猗扁爛鉅�  猓�  猗光爛        狻嘰n  鉅欌⒖猓爠鉅�鉅�鉅�__鉅�鉅�狻� 鉅�狻団爛鉅�鉅�鉅�    狻糪n鉅�鉅�鉅�鉅光６鉅嗏爛鉅�鉅�鉅�鉅�狻粹爟鉅�   鉅樷牑猓勨鉅炩爛\n鉅�鉅�鉅�鉅�猗糕７狻︹ⅳ狻もⅳ猓炩鉅�鉅�鉅�鉅�鉅�鉅�鉅�鉅�鉅�鉅�\n鉅�猗�猓も４猓库鉅佲爛鉅�鉅糕猗７猓栤＆狻�鉅�鉅�鉅�鉅�鉅�鉅�\n猗�猓锯＝猓库？猓库？鉅涒⒉猓垛＞猗夆》猓库？鉅碘？鉅�鉅�鉅�鉅�鉅�鉅�\n猓尖？鉅嶁爥猓库…鉅夆牂猗衡猓尖鉅�鉅� 鉅�猓勨⒏鉅�鉅�鉅�鉅�鉅�鉅�`",
        "`鉅�鉅�鉅�猓犫６狻锯爮鉅夆牂鉅斥ⅵ狻�鉅�鉅�鉅�猗犫牉鉅夆牂鉅测鉅�\n 鉅�猓粹牽鉅忊爛鉅�鉅�鉅�鉅�  鉅�猗斥鉅�狻忊爛鉅�鉅�   鉅�猗穃n猗犫猓嬧猗�猓�猓�狻�鉅�猓�狻�猓р爛猗糕爛鉅�鉅�      狻嘰n猗糕／狻爜鉅糕猓熲爢狻粹；狻测？  猓� Lavde   狻嘰n 猓熲？狻爛鉅�鉅�鉅�鉅�猗扁爛鉅�  猓�  猗光爛        狻嘰n  鉅欌⒖猓爠鉅�鉅�|__|鉅�鉅�狻� 鉅�狻団爛鉅�鉅�鉅�    狻糪n鉅�鉅�鉅�鉅光６鉅嗏爛鉅�鉅�鉅�鉅�狻粹爟鉅�   鉅樷牑猓勨鉅炩爛\n鉅�鉅�鉅�鉅�猗糕７狻︹ⅳ狻もⅳ猓炩鉅�鉅�鉅�鉅�鉅�鉅�鉅�鉅�鉅�鉅�\n鉅�猗�猓も４猓库鉅佲爛鉅�鉅糕猗７猓栤＆狻�鉅�鉅�鉅�鉅�鉅�鉅�\n猗�猓锯＝猓库？猓库？鉅涒⒉猓垛＞猗夆》猓库？鉅碘？鉅�鉅�鉅�鉅�鉅�鉅�\n猓尖？鉅嶁爥猓库…鉅夆牂猗衡猓尖鉅�鉅� 鉅�猓勨⒏鉅�鉅�鉅�鉅�鉅�鉅�`",
        "`鉅�鉅�鉅�猓犫６狻锯爮鉅夆牂鉅斥ⅵ狻�鉅�鉅�鉅�猗犫牉鉅夆牂鉅测鉅�\n 鉅�猓粹牽鉅忊爛鉅�     鉅�猗斥鉅�狻忊爛鉅�    鉅�猗穃n猗犫猓嬧猗�猓�猓�狻�鉅�猓�狻�猓р爛猗糕爛鉅�鉅�鉅�     狻嘰n猗糕／狻爜鉅糕猓熲爢狻粹；狻测？  猓� Pehli   狻嘰n 猓熲？狻爛鉅�鉅�鉅�鉅�猗扁爛鉅�  猓�  猗光爛         狻嘰n  鉅欌⒖猓爠鉅�鉅�(P)鉅�鉅�狻� 鉅�狻団爛鉅�鉅�鉅�    狻糪n鉅�鉅�鉅�鉅光６鉅嗏爛鉅�鉅�鉅�鉅�狻粹爟鉅�   鉅樷牑猓勨鉅炩爛\n鉅�鉅�鉅�鉅�猗糕７狻︹ⅳ狻もⅳ猓炩鉅�鉅�鉅�鉅�鉅�鉅�鉅�鉅�鉅�鉅�\n鉅�猗�猓も４猓库鉅佲爛鉅�鉅糕猗７猓栤＆狻�鉅�鉅�鉅�鉅�鉅�鉅�\n猗�猓锯＝猓库？猓库？鉅涒⒉猓垛＞猗夆》猓库？鉅碘？鉅�鉅�鉅�鉅�鉅�鉅�\n猓尖？鉅嶁爥猓库…鉅夆牂猗衡猓尖鉅�鉅� 鉅�猓勨⒏鉅�鉅�鉅�鉅�鉅�鉅�`",
        "`鉅�鉅�鉅�猓犫６狻锯爮鉅夆牂鉅斥ⅵ狻�鉅�鉅�鉅�猗犫牉鉅夆牂鉅测鉅�\n 鉅�猓粹牽鉅忊爛鉅�     鉅�猗斥鉅�狻忊爛鉅�    鉅�猗穃n猗犫猓嬧猗�猓�猓�狻�鉅�猓�狻�猓р爛猗糕爛   鉅�     狻嘰n猗糕／狻爜鉅糕猓熲爢狻粹；狻测？  猓� Fursat  狻嘰n 猓熲？狻爛鉅�鉅�鉅�鉅�猗扁爛   猓�  猗光爛        狻嘰n  鉅欌⒖猓爠鉅�鉅�鉅�__ 鉅�鉅�狻� 鉅�狻団爛鉅�鉅�鉅�    狻糪n鉅�鉅�鉅�鉅光６鉅嗏爛鉅�鉅�鉅�鉅�狻粹爟鉅�   鉅樷牑猓勨鉅炩爛\n鉅�鉅�鉅�鉅�猗糕７狻︹ⅳ狻もⅳ猓炩鉅�鉅�鉅�鉅�鉅�鉅�鉅�鉅�鉅�鉅�\n鉅�猗�猓も４猓库鉅佲爛鉅�鉅糕猗７猓栤＆狻�鉅�鉅�鉅�鉅�鉅�鉅�\n猗�猓锯＝猓库？猓库？鉅涒⒉猓垛＞猗夆》猓库？鉅碘？鉅�鉅�鉅�鉅�鉅�鉅�\n猓尖？鉅嶁爥猓库…鉅夆牂猗衡猓尖鉅�鉅� 鉅�猓勨⒏鉅�鉅�鉅�鉅�鉅�鉅�`",
        "`鉅�鉅�鉅�猓犫６狻锯爮鉅夆牂鉅斥ⅵ狻�鉅�鉅�鉅�猗犫牉鉅夆牂鉅测鉅�\n 鉅�猓粹牽鉅忊爛鉅�鉅�鉅�鉅�   猗斥鉅�狻忊爛鉅�    鉅�猗穃n猗犫猓嬧猗�猓�猓�狻�鉅�猓�狻�猓р爛猗糕爛鉅� 鉅�     狻嘰n猗糕／狻爜鉅糕猓熲爢狻粹；狻测？  猓� Meeee   狻嘰n 猓熲？狻爛鉅�鉅�鉅�鉅�猗扁爛鉅�  猓�  猗光爛        狻嘰n  鉅欌⒖猓爠鉅�鉅�|__| 鉅�狻� 鉅�狻団爛鉅�鉅�鉅�    狻糪n鉅�鉅�鉅�鉅光６鉅嗏爛鉅�鉅�鉅�鉅�狻粹爟鉅�   鉅樷牑猓勨鉅炩爛\n鉅�鉅�鉅�鉅�猗糕７狻︹ⅳ狻もⅳ猓炩鉅�鉅�鉅�鉅�鉅�鉅�鉅�鉅�鉅�鉅�\n鉅�猗�猓も４猓库鉅佲爛鉅�鉅糕猗７猓栤＆狻�鉅�鉅�鉅�鉅�鉅�鉅�\n猗�猓锯＝猓库？猓库？鉅涒⒉猓垛＞猗夆》猓库？鉅碘？鉅�鉅�鉅�鉅�鉅�鉅�\n猓尖？鉅嶁爥猓库…鉅夆牂猗衡猓尖鉅�鉅� 鉅�猓勨⒏鉅�鉅�鉅�鉅�鉅�鉅�`",
        "`鉅�鉅�鉅�猓犫６狻锯爮鉅夆牂鉅斥ⅵ狻�鉅�鉅�鉅�猗犫牉鉅夆牂鉅测鉅�\n 鉅�猓粹牽鉅忊爛鉅�鉅�鉅�鉅�  鉅�猗斥鉅�狻忊爛鉅�    鉅�猗穃n猗犫猓嬧猗�猓�猓�狻�鉅�猓�狻�猓р爛猗糕爛  鉅�     狻嘰n猗糕／狻爜鉅糕猓熲爢狻粹；狻测？  猓� Nikal   狻嘰n 猓熲？狻爛鉅�鉅�鉅�鉅�猗扁爛   猓�  猗光爛        狻嘰n  鉅欌⒖猓爠鉅�鉅�lodu鉅�鉅�狻� 鉅�狻団爛鉅�鉅�鉅�    狻糪n鉅�鉅�鉅�鉅光６鉅嗏爛鉅�鉅�鉅�鉅�狻粹爟鉅�   鉅樷牑猓勨鉅炩爛\n鉅�鉅�鉅�鉅�猗糕７狻︹ⅳ狻もⅳ猓炩鉅�鉅�鉅�鉅�鉅�鉅�鉅�鉅�鉅�鉅�\n鉅�猗�猓も４猓库鉅佲爛鉅�鉅糕猗７猓栤＆狻�鉅�鉅�鉅�鉅�鉅�鉅�\n猗�猓锯＝猓库？猓库？鉅涒⒉猓垛＞猗夆》猓库？鉅碘？鉅�鉅�鉅�鉅�鉅�鉅�\n猓尖？鉅嶁爥猓库…鉅夆牂猗衡猓尖鉅�鉅� 鉅�猓勨⒏鉅�鉅�鉅�鉅�鉅�鉅�`",
    ]
    for i in animation_ttl:
        await asyncio.sleep(animation_interval)
        await event.edit(animation_chars[i % 6])


@bot.on(admin_cmd(pattern=f"music$", outgoing=True))
@bot.on(sudo_cmd(pattern="music$", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    animation_interval = 1.5
    animation_ttl = range(11)
    event = await edit_or_reply(event, "starting player...")
    animation_chars = [
        "猬も猬� 81% 鉅�鉅�鉅�鉅�鉅�鉅�鉅�鉅�鉅�鉅�鉅�鉅�鉅�鉅�鉅�鉅�鉅�鉅�鉅�`鉁栵笍`\n\n鉅�鉅�鉅�鉅�鉅�[cee jay Music Player](tg://user?id=916234223)\n\n鉅�鉅�鉅�鉅�**Now Playing:shape of u**\n\n**00:00** 鈻扁柋鈻扁柋鈻扁柋鈻扁柋鈻扁柋 **00:10**\n\n鉅�鉅�鉅�鉅�鉅�`馃攤` `鈴笍` `鈴笍` `鈻讹笍` `鈴╋笍` `鈴笍`\n\n**鉅�Next Song:** __Alan Walker - Alone.__\n\n鉅�鉅�鉅�鉅�**鉅�Device: Nokia 1100**",
        "猬も猬� 81% 鉅�鉅�鉅�鉅�鉅�鉅�鉅�鉅�鉅�鉅�鉅�鉅�鉅�鉅�鉅�鉅�鉅�鉅�鉅�`鉁栵笍`\n\n鉅�鉅�鉅�鉅�鉅�[cee jay Music Player](tg://user?id=916234223)\n\n鉅�鉅�鉅�鉅�**Now Playing:shape of u**\n\n**00:01** 鈻扳柋鈻扁柋鈻扁柋鈻扁柋鈻扁柋 **00:10**\n\n鉅�鉅�鉅�鉅�鉅�`馃攤` `鈴笍` `鈴笍` `鈴革笍` `鈴╋笍` `鈴笍`\n\n**鉅�Next Song:** __Alan Walker - Alone.__\n\n鉅�鉅�鉅�鉅�**鉅�Device: Nokia 1100**",
        "猬も猬� 81% 鉅�鉅�鉅�鉅�鉅�鉅�鉅�鉅�鉅�鉅�鉅�鉅�鉅�鉅�鉅�鉅�鉅�鉅�鉅�`鉁栵笍`\n\n鉅�鉅�鉅�鉅�鉅�[cee jay  Music Player](tg://user?id=916234223)\n\n鉅�鉅�鉅�鉅�**Now Playing:shape of u**\n\n**00:02** 鈻扳柊鈻扁柋鈻扁柋鈻扁柋鈻扁柋 **00:10**\n\n鉅�鉅�鉅�鉅�鉅�`馃攤` `鈴笍` `鈴笍` `鈴革笍` `鈴╋笍` `鈴笍`\n\n**鉅�Next Song:** __Alan Walker - Alone.__\n\n鉅�鉅�鉅�鉅�**鉅�Device: Nokia 1100**",
        "猬も猬� 81% 鉅�鉅�鉅�鉅�鉅�鉅�鉅�鉅�鉅�鉅�鉅�鉅�鉅�鉅�鉅�鉅�鉅�鉅�鉅�`鉁栵笍`\n\n鉅�鉅�鉅�鉅�鉅�[cee jay Music Player](tg://user?id=916234223)\n\n鉅�鉅�鉅�鉅�**Now Playing:shape of u**\n\n**00:03** 鈻扳柊鈻扳柋鈻扁柋鈻扁柋鈻扁柋 **00:10**\n\n鉅�鉅�鉅�鉅�鉅�`馃攤` `鈴笍` `鈴笍` `鈴革笍` `鈴╋笍` `鈴笍`\n\n**鉅�Next Song:** __Alan Walker - Alone.__\n\n鉅�鉅�鉅�鉅�**鉅�Device: Nokia 1100**",
        "猬も鈼� 80% 鉅�鉅�鉅�鉅�鉅�鉅�鉅�鉅�鉅�鉅�鉅�鉅�鉅�鉅�鉅�鉅�鉅�鉅�鉅�`鉁栵笍`\n\n鉅�鉅�鉅�鉅�鉅�[cee jay Music Player](tg://user?id=916234223)\n\n鉅�鉅�鉅�鉅�**Now Playing:shape of u**\n\n**00:04** 鈻扳柊鈻扳柊鈻扁柋鈻扁柋鈻扁柋 **00:10**\n\n鉅�鉅�鉅�鉅�鉅�`馃攤` `鈴笍` `鈴笍` `鈴革笍` `鈴╋笍` `鈴笍`\n\n**鉅�Next Song:** __Alan Walker - Alone.__\n\n鉅�鉅�鉅�鉅�**鉅�Device: Nokia 1100**",
        "猬も鈼� 80% 鉅�鉅�鉅�鉅�鉅�鉅�鉅�鉅�鉅�鉅�鉅�鉅�鉅�鉅�鉅�鉅�鉅�鉅�鉅�`鉁栵笍`\n\n鉅�鉅�鉅�鉅�鉅�[cee jay Music Player](tg://user?id=916234223)\n\n鉅�鉅�鉅�鉅�**Now Playing:shape of u**\n\n**00:05** 鈻扳柊鈻扳柊鈻扁柋鈻扁柋鈻扁柋 **00:10**\n\n鉅�鉅�鉅�鉅�鉅�`馃攤` `鈴笍` `鈴笍` `鈴革笍` `鈴╋笍` `鈴笍`\n\n**鉅�Next Song:** __Alan Walker - Alone.__\n\n鉅�鉅�鉅�鉅�**鉅�Device: Nokia 1100**",
        "猬も鈼� 80% 鉅�鉅�鉅�鉅�鉅�鉅�鉅�鉅�鉅�鉅�鉅�鉅�鉅�鉅�鉅�鉅�鉅�鉅�鉅�`鉁栵笍`\n\n鉅�鉅�鉅�鉅�鉅�[cee jay Music Player](tg://user?id=916234223)\n\n鉅�鉅�鉅�鉅�**Now Playing:shape of u**\n\n**00:06** 鈻扳柊鈻扳柊鈻扳柊鈻扁柋鈻扁柋 **00:10**\n\n鉅�鉅�鉅�鉅�鉅�`馃攤` `鈴笍` `鈴笍` `鈴革笍` `鈴╋笍` `鈴笍`\n\n**鉅�Next Song:** __Alan Walker - Alone.__\n\n鉅�鉅�鉅�鉅�**鉅�Device: Nokia 1100**",
        "猬も鈼� 80% 鉅�鉅�鉅�鉅�鉅�鉅�鉅�鉅�鉅�鉅�鉅�鉅�鉅�鉅�鉅�鉅�鉅�鉅�鉅�`鉁栵笍`\n\n鉅�鉅�鉅�鉅�鉅�[cee jay Music Player](tg://user?id=916234223)\n\n鉅�鉅�鉅�鉅�**Now Playing:shape of u**\n\n**00:07** 鈻扳柊鈻扳柊鈻扳柊鈻扳柋鈻扁柋 **00:10**\n\n鉅�鉅�鉅�鉅�鉅�`馃攤` `鈴笍` `鈴笍` `鈴革笍` `鈴╋笍` `鈴笍`\n\n**鉅�Next Song:** __Alan Walker - Alone.__\n\n鉅�鉅�鉅�鉅�**鉅�Device: Nokia 1100**",
        "猬も鈼� 80% 鉅�鉅�鉅�鉅�鉅�鉅�鉅�鉅�鉅�鉅�鉅�鉅�鉅�鉅�鉅�鉅�鉅�鉅�鉅�`鉁栵笍`\n\n鉅�鉅�鉅�鉅�鉅�[cee jay Music Player](tg://user?id=916234223)\n\n鉅�鉅�鉅�鉅�**Now Playing:shape of u**\n\n**00:08** 鈻扳柊鈻扳柊鈻扳柊鈻扳柊鈻扁柋 **00:10**\n\n鉅�鉅�鉅�鉅�鉅�`馃攤` `鈴笍` `鈴笍` `鈴革笍` `鈴╋笍` `鈴笍`\n\n**鉅�Next Song:** __Alan Walker - Alone.__\n\n鉅�鉅�鉅�鉅�**鉅�Device: Nokia 1100**",
        "猬も鈼� 80% 鉅�鉅�鉅�鉅�鉅�鉅�鉅�鉅�鉅�鉅�鉅�鉅�鉅�鉅�鉅�鉅�鉅�鉅�鉅�`鉁栵笍`\n\n鉅�鉅�鉅�鉅�鉅�[cee jay Music Player](tg://user?id=916234223)\n\n鉅�鉅�鉅�鉅�**Now Playing:shape of u**\n\n**00:09** 鈻扳柊鈻扳柊鈻扳柊鈻扳柊鈻扳柋 **00:10**\n\n鉅�鉅�鉅�鉅�鉅�`馃攤` `鈴笍` `鈴笍` `鈴革笍` `鈴╋笍` `鈴笍`\n\n**鉅�Next Song:** __Alan Walker - Alone.__\n\n鉅�鉅�鉅�鉅�**鉅�Device: Nokia 1100**",
        "猬も鈼� 80% 鉅�鉅�鉅�鉅�鉅�鉅�鉅�鉅�鉅�鉅�鉅�鉅�鉅�鉅�鉅�鉅�鉅�鉅�鉅�`鉁栵笍`\n\n鉅�鉅�鉅�鉅�鉅�[cee jay Music Player](tg://user?id=916234223)\n\n鉅�鉅�鉅�鉅�**Now Playing:shape of u**\n\n**00:10** 鈻扳柊鈻扳柊鈻扳柊鈻扳柊鈻扳柊 **00:10**\n\n鉅�鉅�鉅�鉅�鉅�`馃攤` `鈴笍` `鈴笍` `鈴猴笍` `鈴╋笍` `鈴笍`\n\n**鉅�Next Song:** __Alan Walker - Alone.__\n\n鉅�鉅�鉅�鉅�**鉅�Device: Nokia 1100**",
    ]
    for i in animation_ttl:
        await asyncio.sleep(animation_interval)
        await event.edit(animation_chars[i % 11])


@bot.on(admin_cmd(pattern=f"squ$", outgoing=True))
@bot.on(sudo_cmd(pattern="squ$", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    event = await edit_or_reply(
        event, "鈺斺晲鈺愨晲鈺愨晲鈺愨晲鈺愨晲鈺愨晲鈺愨晲鈺愨晲鈺愨晲鈺愨晲鈺� \n  \n鈺氣晲鈺愨晲鈺愨晲鈺愨晲鈺愨晲鈺愨晲鈺愨晲鈺愨晲鈺愨晲鈺愨晲鈺�"
    )
    await asyncio.sleep(1)
    await event.edit("鈺斺晲鈺愨晲鈺愨晲鈺愨晲鈺愨晲鈺愨晲鈺愨晲鈺愨晲鈺愨晲鈺愨晲鈺� \n \t鈻� \n鈺氣晲鈺愨晲鈺愨晲鈺愨晲鈺愨晲鈺愨晲鈺愨晲鈺愨晲鈺愨晲鈺愨晲鈺�")
    await asyncio.sleep(1)
    await event.edit("鈺斺晲鈺愨晲鈺愨晲鈺愨晲鈺愨晲鈺愨晲鈺愨晲鈺愨晲鈺愨晲鈺愨晲鈺� \n 鈻� \t鈻� \n鈺氣晲鈺愨晲鈺愨晲鈺愨晲鈺愨晲鈺愨晲鈺愨晲鈺愨晲鈺愨晲鈺愨晲鈺�")
    await asyncio.sleep(1)
    await event.edit("鈺斺晲鈺愨晲鈺愨晲鈺愨晲鈺愨晲鈺愨晲鈺愨晲鈺愨晲鈺愨晲鈺愨晲鈺� \n 鈻� 鈻� 鈻� \n鈺氣晲鈺愨晲鈺愨晲鈺愨晲鈺愨晲鈺愨晲鈺愨晲鈺愨晲鈺愨晲鈺愨晲鈺�")
    await asyncio.sleep(1)
    await event.edit("鈺斺晲鈺愨晲鈺愨晲鈺愨晲鈺愨晲鈺愨晲鈺愨晲鈺愨晲鈺愨晲鈺愨晲鈺� \n 鈻� 鈻� 鈻� 鈻� \n鈺氣晲鈺愨晲鈺愨晲鈺愨晲鈺愨晲鈺愨晲鈺愨晲鈺愨晲鈺愨晲鈺愨晲鈺�")
    await asyncio.sleep(1)
    await event.edit("鈺斺晲鈺愨晲鈺愨晲鈺愨晲鈺愨晲鈺愨晲鈺愨晲鈺愨晲鈺愨晲鈺愨晲鈺� \n 鈻� 鈻� 鈻� 鈻� 鈻� \n鈺氣晲鈺愨晲鈺愨晲鈺愨晲鈺愨晲鈺愨晲鈺愨晲鈺愨晲鈺愨晲鈺愨晲鈺�")
    await asyncio.sleep(1)
    await event.edit("鈺斺晲鈺愨晲鈺愨晲鈺愨晲鈺愨晲鈺愨晲鈺愨晲鈺愨晲鈺愨晲鈺愨晲鈺� \n 鈻� 鈻� 鈻� 鈻� 鈻� 鈻� \n鈺氣晲鈺愨晲鈺愨晲鈺愨晲鈺愨晲鈺愨晲鈺愨晲鈺愨晲鈺愨晲鈺愨晲鈺�")
    await asyncio.sleep(1)
    await event.edit("鈺斺晲鈺愨晲鈺愨晲鈺愨晲鈺愨晲鈺愨晲鈺愨晲鈺愨晲鈺愨晲鈺愨晲鈺� \n 鈻� 鈻� 鈻� 鈻� 鈻� 鈻� 鈻� \n鈺氣晲鈺愨晲鈺愨晲鈺愨晲鈺愨晲鈺愨晲鈺愨晲鈺愨晲鈺愨晲鈺愨晲鈺�")
    await asyncio.sleep(1)
    await event.edit("鈺斺晲鈺愨晲鈺愨晲鈺愨晲鈺愨晲鈺愨晲鈺愨晲鈺愨晲鈺愨晲鈺愨晲鈺� \n 鈻� 鈻� 鈻� 鈻� 鈻� 鈻� 鈻� 鈻� \n鈺氣晲鈺愨晲鈺愨晲鈺愨晲鈺愨晲鈺愨晲鈺愨晲鈺愨晲鈺愨晲鈺愨晲鈺�")
    await asyncio.sleep(1)
    await event.edit(
        "鈺斺晲鈺愨晲鈺愨晲鈺愨晲鈺愨晲鈺愨晲鈺愨晲鈺愨晲鈺愨晲鈺愨晲鈺� \n 鈻� 鈻� 鈻� 鈻� 鈻� 鈻� 鈻� 鈻� 鈻� \n鈺氣晲鈺愨晲鈺愨晲鈺愨晲鈺愨晲鈺愨晲鈺愨晲鈺愨晲鈺愨晲鈺愨晲鈺�"
    )
    await asyncio.sleep(1)
    await event.edit(
        "鈺斺晲鈺愨晲鈺愨晲鈺愨晲鈺愨晲鈺愨晲鈺愨晲鈺愨晲鈺愨晲鈺愨晲鈺� \n 鈻� 鈻� 鈻� 鈻� 鈻� 鈻� 鈻� 鈻� 鈻� 鈻� \n鈺氣晲鈺愨晲鈺愨晲鈺愨晲鈺愨晲鈺愨晲鈺愨晲鈺愨晲鈺愨晲鈺愨晲鈺�"
    )
    await asyncio.sleep(1)
    await event.edit(
        "鈺斺晲鈺愨晲鈺愨晲鈺愨晲鈺愨晲鈺愨晲鈺愨晲鈺愨晲鈺愨晲鈺愨晲鈺� \n 鈻� 鈻� 鈻� 鈻� 鈻� 鈻� 鈻� 鈻� 鈻� 鈻� 鈻� \n鈺氣晲鈺愨晲鈺愨晲鈺愨晲鈺愨晲鈺愨晲鈺愨晲鈺愨晲鈺愨晲鈺愨晲鈺�"
    )
    await asyncio.sleep(1)
    await event.edit(
        "鈺斺晲鈺愨晲鈺愨晲鈺愨晲鈺愨晲鈺愨晲鈺愨晲鈺愨晲鈺愨晲鈺愨晲鈺� \n 鈻� 鈻� 鈻� 鈻� 鈻� 鈻� 鈻� 鈻� 鈻� 鈻� 鈻� 鈻� \n鈺氣晲鈺愨晲鈺愨晲鈺愨晲鈺愨晲鈺愨晲鈺愨晲鈺愨晲鈺愨晲鈺愨晲鈺�"
    )
    await asyncio.sleep(1)
    await event.edit(
        "鈺斺晲鈺愨晲鈺愨晲鈺愨晲鈺愨晲鈺愨晲鈺愨晲鈺愨晲鈺愨晲鈺愨晲鈺� \n 鈻� 鈻� 鈻� 鈻� 鈻� 鈻� 鈻� 鈻� 鈻� 鈻� 鈻� 鈻� 鈻� \n鈺氣晲鈺愨晲鈺愨晲鈺愨晲鈺愨晲鈺愨晲鈺愨晲鈺愨晲鈺愨晲鈺愨晲鈺�"
    )
    await asyncio.sleep(1)
    await event.edit(
        "鈺斺晲鈺愨晲鈺愨晲鈺愨晲鈺愨晲鈺愨晲鈺愨晲鈺愨晲鈺愨晲鈺愨晲鈺� \n 鈻� 鈻� 鈻� 鈻� 鈻� 鈻� 鈻� 鈻� 鈻� 鈻� 鈻� 鈻� 鈻� 鈻� \n鈺氣晲鈺愨晲鈺愨晲鈺愨晲鈺愨晲鈺愨晲鈺愨晲鈺愨晲鈺愨晲鈺愨晲鈺�"
    )
    await asyncio.sleep(6)


CMD_HELP.update(
    {
        "animation4": """**Plugin : **`animation4`
        
**Commands in animation4 are **
  鈥�  `.kilr <text>`
  鈥�  `.eye`
  鈥�  `.thinking`
  鈥�  `.snake`
  鈥�  `.human`
  鈥�  `.mc`
  鈥�  `.virus`
  鈥�  `.repe`
  鈥�  `.nikal`
  鈥�  `.music`
  鈥�  `.squ`
  
**Function : **__Different kinds of animation commands check yourself for their animation .__"""
    }
)
