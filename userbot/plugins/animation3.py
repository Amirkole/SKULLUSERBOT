import asyncio
from collections import deque

from ..utils import admin_cmd, edit_or_reply, sudo_cmd
from . import ALIVE_NAME, CMD_HELP

DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "SKULL"


@bot.on(admin_cmd(pattern=r"star$", outgoing=True))
@bot.on(sudo_cmd(pattern=r"star$", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    event = await edit_or_reply(event, "`stars.....`")
    deq = deque(list("馃鉁煢嬧湪馃鉁煢嬧湪"))
    for _ in range(48):
        await asyncio.sleep(0.3)
        await event.edit("".join(deq))
        deq.rotate(1)


@bot.on(admin_cmd(pattern=r"boxs$", outgoing=True))
@bot.on(sudo_cmd(pattern=r"boxs$", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    event = await edit_or_reply(event, "`boxs...`")
    deq = deque(list("馃煡馃煣馃煥馃煩馃煢馃煪馃煫猬涒瑴"))
    for _ in range(999):
        await asyncio.sleep(0.3)
        await event.edit("".join(deq))
        deq.rotate(1)


@bot.on(admin_cmd(pattern=r"rain$", outgoing=True))
@bot.on(sudo_cmd(pattern=r"rain$", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    event = await edit_or_reply(event, "`Raining.......`")
    deq = deque(list("馃尙鈽侊笍馃尒馃尐馃導馃對馃尌鉀咅煂�"))
    for _ in range(48):
        await asyncio.sleep(0.3)
        await event.edit("".join(deq))
        deq.rotate(1)


@bot.on(admin_cmd(pattern=r"deploy$", outgoing=True))
@bot.on(sudo_cmd(pattern=r"deploy$", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    animation_interval = 3
    animation_ttl = range(12)
    event = await edit_or_reply(event, "`Deploying...`")
    animation_chars = [
        "**Heroku Connecting To Latest Github Build **",
        f"**Build started by user** {DEFAULTUSER}",
        f"**Deploy** `535a74f0` **by user** {DEFAULTUSER}",
        "**Restarting Heroku Server...**",
        "**State changed from up to starting**",
        "**Stopping all processes with SIGTERM**",
        "**Process exited with** `status 143`",
        "**Starting process with command** `python3 -m userbot`",
        "**State changed from starting to up**",
        "__INFO:Userbot:Logged in as 557667062__",
        "__INFO:Userbot:Successfully loaded all plugins__",
        "**Build Succeeded**",
    ]
    for i in animation_ttl:
        await asyncio.sleep(animation_interval)
        await event.edit(animation_chars[i % 12])


@bot.on(admin_cmd(pattern=r"dump$", outgoing=True))
@bot.on(sudo_cmd(pattern=r"dump$", allow_sudo=True))
async def _(message):
    if event.fwd_from:
        return
    try:
        obj = message.pattern_match.group(1)
        if len(obj) != 3:
            raise IndexError
        inp = " ".join(obj)
    except IndexError:
        inp = "馃 馃巶 馃崼"
    event = await edit_or_reply(message, "`droping....`")
    u, t, g, o, s, n = inp.split(), "馃棏", "<(^_^ <)", "(> ^_^)>", "鉅� ", "\n"
    h = [(u[0], u[1], u[2]), (u[0], u[1], ""), (u[0], "", "")]
    for something in reversed(
        [
            y
            for y in (
                [
                    "".join(x)
                    for x in (
                        f + (s, g, s + s * f.count(""), t),
                        f + (g, s * 2 + s * f.count(""), t),
                        f[:i] + (o, f[i], s * 2 + s * f.count(""), t),
                        f[:i] + (s + s * f.count(""), o, f[i], s, t),
                        f[:i] + (s * 2 + s * f.count(""), o, f[i], t),
                        f[:i] + (s * 3 + s * f.count(""), o, t),
                        f[:i] + (s * 3 + s * f.count(""), g, t),
                    )
                ]
                for i, f in enumerate(reversed(h))
            )
        ]
    ):
        for something_else in something:
            await asyncio.sleep(0.3)
            try:
                await event.edit(something_else)
            except errors.MessageIdInvalidError:
                return


@bot.on(admin_cmd(pattern=r"fleaveme$", outgoing=True))
@bot.on(sudo_cmd(pattern=r"fleaveme$", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    animation_interval = 1
    animation_ttl = range(10)
    animation_chars = [
        "猬涒瑳猬沑n猬涒瑳猬沑n猬涒瑳猬�",
        "猬涒瑳猬沑n猬涴煍勨瑳\n猬涒瑳猬�",
        "猬涒瑔锔忊瑳\n猬涴煍勨瑳\n猬涒瑳猬�",
        "猬涒瑔锔忊啑锔廫n猬涴煍勨瑳\n猬涒瑳猬�",
        "猬涒瑔锔忊啑锔廫n猬涴煍勨灐锔廫n猬涒瑳猬�",
        "猬涒瑔锔忊啑锔廫n猬涴煍勨灐锔廫n猬涒瑳鈫橈笍",
        "猬涒瑔锔忊啑锔廫n猬涴煍勨灐锔廫n猬涒瑖锔忊啒锔�",
        "猬涒瑔锔忊啑锔廫n猬涴煍勨灐锔廫n鈫欙笍猬囷笍鈫橈笍",
        "猬涒瑔锔忊啑锔廫n猬咃笍馃攧鉃★笍\n鈫欙笍猬囷笍鈫橈笍",
        "鈫栵笍猬嗭笍鈫楋笍\n猬咃笍馃攧鉃★笍\n鈫欙笍猬囷笍鈫橈笍",
    ]
    event = await edit_or_reply(event, "fleaveme....")
    await asyncio.sleep(2)
    for i in animation_ttl:
        await asyncio.sleep(animation_interval)
        await event.edit(animation_chars[i % 10])


@bot.on(admin_cmd(pattern=r"loveu$", outgoing=True))
@bot.on(sudo_cmd(pattern=r"loveu$", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    animation_interval = 0.5
    animation_ttl = range(70)
    event = await edit_or_reply(event, "loveu")
    animation_chars = [
        "馃榾",
        "馃懇鈥嶐煄�",
        "馃榿",
        "馃槀",
        "馃ぃ",
        "馃槂",
        "馃槃",
        "馃槄",
        "馃槉",
        "鈽�",
        "馃檪",
        "馃",
        "馃え",
        "馃槓",
        "馃槕",
        "馃樁",
        "馃槪",
        "馃槬",
        "馃槷",
        "馃",
        "馃槸",
        "馃槾",
        "馃様",
        "馃槙",
        "鈽�",
        "馃檨",
        "馃槚",
        "馃槥",
        "馃槦",
        "馃槩",
        "馃槶",
        "馃く",
        "馃挃",
        "鉂�",
        "I Love You鉂�",
    ]
    for i in animation_ttl:
        await asyncio.sleep(animation_interval)
        await event.edit(animation_chars[i % 35])


@bot.on(admin_cmd(pattern=r"plane$", outgoing=True))
@bot.on(sudo_cmd(pattern=r"plane$", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    event = await edit_or_reply(event, "Wait for plane...")
    await event.edit("鉁�-------------")
    await event.edit("-鉁�------------")
    await event.edit("--鉁�-----------")
    await event.edit("---鉁�----------")
    await event.edit("----鉁�---------")
    await event.edit("-----鉁�--------")
    await event.edit("------鉁�-------")
    await event.edit("-------鉁�------")
    await event.edit("--------鉁�-----")
    await event.edit("---------鉁�----")
    await event.edit("----------鉁�---")
    await event.edit("-----------鉁�--")
    await event.edit("------------鉁�-")
    await event.edit("-------------鉁�")
    await asyncio.sleep(3)


@bot.on(admin_cmd(pattern=r"police$", outgoing=True))
@bot.on(sudo_cmd(pattern=r"police$", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    animation_interval = 0.3
    animation_ttl = range(12)
    event = await edit_or_reply(event, "Police")
    animation_chars = [
        "馃敶馃敶馃敶猬溾瑴猬滒煍叼煍叼煍礬n馃敶馃敶馃敶猬溾瑴猬滒煍叼煍叼煍礬n馃敶馃敶馃敶猬溾瑴猬滒煍叼煍叼煍�",
        "馃數馃數馃數猬溾瑴猬滒煍答煍答煍碶n馃數馃數馃數猬溾瑴猬滒煍答煍答煍碶n馃數馃數馃數猬溾瑴猬滒煍答煍答煍�",
        "馃敶馃敶馃敶猬溾瑴猬滒煍叼煍叼煍礬n馃敶馃敶馃敶猬溾瑴猬滒煍叼煍叼煍礬n馃敶馃敶馃敶猬溾瑴猬滒煍叼煍叼煍�",
        "馃數馃數馃數猬溾瑴猬滒煍答煍答煍碶n馃數馃數馃數猬溾瑴猬滒煍答煍答煍碶n馃數馃數馃數猬溾瑴猬滒煍答煍答煍�",
        "馃敶馃敶馃敶猬溾瑴猬滒煍叼煍叼煍礬n馃敶馃敶馃敶猬溾瑴猬滒煍叼煍叼煍礬n馃敶馃敶馃敶猬溾瑴猬滒煍叼煍叼煍�",
        "馃數馃數馃數猬溾瑴猬滒煍答煍答煍碶n馃數馃數馃數猬溾瑴猬滒煍答煍答煍碶n馃數馃數馃數猬溾瑴猬滒煍答煍答煍�",
        "馃敶馃敶馃敶猬溾瑴猬滒煍叼煍叼煍礬n馃敶馃敶馃敶猬溾瑴猬滒煍叼煍叼煍礬n馃敶馃敶馃敶猬溾瑴猬滒煍叼煍叼煍�",
        "馃數馃數馃數猬溾瑴猬滒煍答煍答煍碶n馃數馃數馃數猬溾瑴猬滒煍答煍答煍碶n馃數馃數馃數猬溾瑴猬滒煍答煍答煍�",
        "馃敶馃敶馃敶猬溾瑴猬滒煍叼煍叼煍礬n馃敶馃敶馃敶猬溾瑴猬滒煍叼煍叼煍礬n馃敶馃敶馃敶猬溾瑴猬滒煍叼煍叼煍�",
        "馃數馃數馃數猬溾瑴猬滒煍答煍答煍碶n馃數馃數馃數猬溾瑴猬滒煍答煍答煍碶n馃數馃數馃數猬溾瑴猬滒煍答煍答煍�",
        "馃敶馃敶馃敶猬溾瑴猬滒煍叼煍叼煍礬n馃敶馃敶馃敶猬溾瑴猬滒煍叼煍叼煍礬n馃敶馃敶馃敶猬溾瑴猬滒煍叼煍叼煍�",
        f"[{DEFAULTUSER}]({USERNAME}) **Police iz Here**",
    ]
    for i in animation_ttl:
        await asyncio.sleep(animation_interval)
        await event.edit(animation_chars[i % 12])


@bot.on(admin_cmd(pattern=r"jio$", outgoing=True))
@bot.on(sudo_cmd(pattern=r"jio$", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    animation_interval = 1
    animation_ttl = range(19)
    event = await edit_or_reply(event, "jio network boosting...")
    animation_chars = [
        "`Connecting To JIO NETWORK ....`",
        "`鈻� 鈻� 鈻� 鈻� 鈻� 鈻� 鈻乣",
        "`鈻� 鈻� 鈻� 鈻� 鈻� 鈻� 鈻乣",
        "`鈻� 鈻� 鈻� 鈻� 鈻� 鈻� 鈻乣",
        "`鈻� 鈻� 鈻� 鈻� 鈻� 鈻� 鈻乣",
        "`鈻� 鈻� 鈻� 鈻� 鈻� 鈻� 鈻乣",
        "`鈻� 鈻� 鈻� 鈻� 鈻� 鈻� 鈻乣",
        "`鈻� 鈻� 鈻� 鈻� 鈻� 鈻� 鈻乣",
        "`鈻� 鈻� 鈻� 鈻� 鈻� 鈻� 鈻抈",
        "*Optimising JIO NETWORK...*",
        "`鈻� 鈻� 鈻� 鈻� 鈻� 鈻� 鈻抈",
        "`鈻� 鈻� 鈻� 鈻� 鈻� 鈻� 鈻抈",
        "`鈻� 鈻� 鈻� 鈻� 鈻� 鈻� 鈻抈",
        "`鈻� 鈻� 鈻� 鈻� 鈻� 鈻� 鈻抈",
        "`鈻� 鈻� 鈻� 鈻� 鈻� 鈻� 鈻抈",
        "`鈻� 鈻� 鈻� 鈻� 鈻� 鈻� 鈻抈",
        "`鈻� 鈻� 鈻� 鈻� 鈻� 鈻� 鈻抈",
        "`鈻� 鈻� 鈻� 鈻� 鈻� 鈻� 鈻坄",
        "**JIO NETWORK Boosted....**",
    ]
    for i in animation_ttl:
        await asyncio.sleep(animation_interval)
        await event.edit(animation_chars[i % 19])


@bot.on(admin_cmd(pattern=r"solarsystem$", outgoing=True))
@bot.on(sudo_cmd(pattern=r"solarsystem$", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    animation_interval = 0.1
    animation_ttl = range(80)
    event = await edit_or_reply(event, "solarsystem")
    animation_chars = [
        "`鈼硷笍鈼硷笍鈼硷笍鈼硷笍鈼硷笍\n鈼硷笍鈼硷笍鈼硷笍鈼硷笍鈽�\n鈼硷笍鈼硷笍馃寧鈼硷笍鈼硷笍\n馃寱鈼硷笍鈼硷笍鈼硷笍鈼硷笍\n鈼硷笍鈼硷笍鈼硷笍鈼硷笍鈼硷笍`",
        "`鈼硷笍鈼硷笍鈼硷笍鈼硷笍鈼硷笍\n馃寱鈼硷笍鈼硷笍鈼硷笍鈼硷笍\n鈼硷笍鈼硷笍馃寧鈼硷笍鈼硷笍\n鈼硷笍鈼硷笍鈼硷笍鈼硷笍鈽�\n鈼硷笍鈼硷笍鈼硷笍鈼硷笍鈼硷笍`",
        "`鈼硷笍馃寱鈼硷笍鈼硷笍鈼硷笍\n鈼硷笍鈼硷笍鈼硷笍鈼硷笍鈼硷笍\n鈼硷笍鈼硷笍馃寧鈼硷笍鈼硷笍\n鈼硷笍鈼硷笍鈼硷笍鈼硷笍鈼硷笍\n鈼硷笍鈼硷笍鈼硷笍鈽�鈼硷笍`",
        "`鈼硷笍鈼硷笍鈼硷笍馃寱鈼硷笍\n鈼硷笍鈼硷笍鈼硷笍鈼硷笍鈼硷笍\n鈼硷笍鈼硷笍馃寧鈼硷笍鈼硷笍\n鈼硷笍鈼硷笍鈼硷笍鈼硷笍鈼硷笍\n鈼硷笍鈽�鈼硷笍鈼硷笍鈼硷笍`",
        "`鈼硷笍鈼硷笍鈼硷笍鈼硷笍鈼硷笍\n鈼硷笍鈼硷笍鈼硷笍鈼硷笍馃寱\n鈼硷笍鈼硷笍馃寧鈼硷笍鈼硷笍\n鈽�鈼硷笍鈼硷笍鈼硷笍鈼硷笍\n鈼硷笍鈼硷笍鈼硷笍鈼硷笍鈼硷笍`",
        "`鈼硷笍鈼硷笍鈼硷笍鈼硷笍鈼硷笍\n鈽�鈼硷笍鈼硷笍鈼硷笍鈼硷笍\n鈼硷笍鈼硷笍馃寧鈼硷笍鈼硷笍\n鈼硷笍鈼硷笍鈼硷笍鈼硷笍馃寱\n鈼硷笍鈼硷笍鈼硷笍鈼硷笍鈼硷笍`",
        "`鈼硷笍鈽�鈼硷笍鈼硷笍鈼硷笍\n鈼硷笍鈼硷笍鈼硷笍鈼硷笍鈼硷笍\n鈼硷笍鈼硷笍馃寧鈼硷笍鈼硷笍\n鈼硷笍鈼硷笍鈼硷笍鈼硷笍鈼硷笍\n鈼硷笍鈼硷笍鈼硷笍馃寱鈼硷笍`",
        "`鈼硷笍鈼硷笍鈼硷笍鈽�鈼硷笍\n鈼硷笍鈼硷笍鈼硷笍鈼硷笍鈼硷笍\n鈼硷笍鈼硷笍馃寧鈼硷笍鈼硷笍\n鈼硷笍鈼硷笍鈼硷笍鈼硷笍鈼硷笍\n鈼硷笍馃寱鈼硷笍鈼硷笍鈼硷笍`",
    ]
    for i in animation_ttl:
        await asyncio.sleep(animation_interval)
        await event.edit(animation_chars[i % 8])


CMD_HELP.update(
    {
        "animation3": """**Plugin : **`animation3`
        
**Commands in animation3 are **
  鈥�  `.star`
  鈥�  `.boxs`
  鈥�  `.rain`
  鈥�  `.deploy`
  鈥�  `.dump`
  鈥�  `.fleaveme`
  鈥�  `.loveu`
  鈥�  `.plane`
  鈥�  `.police`
  鈥�  `.jio`
  鈥�  `.solarsystem`
  
**Function : **__Different kinds of animation commands check yourself for their animation .__"""
    }
)
