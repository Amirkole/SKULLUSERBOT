import asyncio
import random

from ..utils import admin_cmd, edit_or_reply, sudo_cmd
from . import CMD_HELP, skullmemes


@bot.on(admin_cmd(outgoing=True, pattern="abuse$"))
@bot.on(sudo_cmd(pattern="abuse$", allow_sudo=True))
async def abusing(abused):
    reply_text = random.choice(skullmemes.ABUSE_STRINGS)
    await edit_or_reply(abused, reply_text)


@bot.on(admin_cmd(outgoing=True, pattern="abusehard$"))
@bot.on(sudo_cmd(pattern="abusehard$", allow_sudo=True))
async def fuckedd(abusehard):
    reply_text = random.choice(skullmemes.ABUSEHARD_STRING)
    await edit_or_reply(abusehard, reply_text)


@bot.on(admin_cmd(outgoing=True, pattern="rendi$"))
@bot.on(sudo_cmd(pattern="rendi$", allow_sudo=True))
async def metoo(e):
    txt = random.choice(skullmemes.RENDISTR)
    await edit_or_reply(e, txt)


@bot.on(admin_cmd(outgoing=True, pattern="rape$"))
@bot.on(sudo_cmd(pattern="rape$", allow_sudo=True))
async def raping(raped):
    reply_text = random.choice(skullmemes.RAPE_STRINGS)
    await edit_or_reply(raped, reply_text)


@bot.on(admin_cmd(outgoing=True, pattern="fuck$"))
@bot.on(sudo_cmd(pattern="fuck$", allow_sudo=True))
async def chutiya(fuks):
    reply_text = random.choice(skullmemes.CHU_STRINGS)
    await edit_or_reply(fuks, reply_text)


@bot.on(admin_cmd(outgoing=True, pattern="thanos$"))
@bot.on(sudo_cmd(pattern="thanos$", allow_sudo=True))
async def thanos(thanos):
    reply_text = random.choice(skullmemes.THANOS_STRINGS)
    await edit_or_reply(thanos, reply_text)


@bot.on(admin_cmd(outgoing=True, pattern="kiss$"))
@bot.on(sudo_cmd(pattern="kiss$", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    skullevent = await edit_or_reply(event, "`kiss`")
    animation_interval = 0.2
    animation_ttl = range(100)
    animation_chars = ["馃さ       馃懓", "馃さ     馃懓", "馃さ  馃懓", "馃さ馃拫馃懓"]
    for i in animation_ttl:
        await asyncio.sleep(animation_interval)
        await skullevent.edit(animation_chars[i % 4])


@bot.on(admin_cmd(outgoing=True, pattern="fuk$"))
@bot.on(sudo_cmd(pattern="fuk$", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    skullevent = await edit_or_reply(event, "`fuking....`")
    animation_interval = 0.2
    animation_ttl = range(100)
    animation_chars = ["馃憠       鉁婏笍", "馃憠     鉁婏笍", "馃憠  鉁婏笍", "馃憠鉁婏笍馃挦"]
    for i in animation_ttl:
        await asyncio.sleep(animation_interval)
        await skullevent.edit(animation_chars[i % 4])


@bot.on(admin_cmd(outgoing=True, pattern="sex$"))
@bot.on(sudo_cmd(pattern="sex$", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    skullevent = await edit_or_reply(event, "`sex`")
    animation_interval = 0.2
    animation_ttl = range(100)
    animation_chars = ["馃さ       馃懓", "馃さ     馃懓", "馃さ  馃懓", "馃さ馃懠馃懓"]
    for i in animation_ttl:
        await asyncio.sleep(animation_interval)
        await skullevent.edit(animation_chars[i % 4])


CMD_HELP.update(
    {
        "gali": "**plugin : **`gali`\
        \n\n**Commands :**\
        \n  鈥�  `.abuse`\
        \n  鈥�  `.abusehard`\
        \n  鈥�  `.rendi`\
        \n  鈥�  `.rape`\
        \n  鈥�  `.fuck`\
        \n  鈥�  `.thanos`\
        \n  鈥�  `.kiss`\
        \n  鈥�  `.fuk`\
        \n  鈥�  `.sex`\
        \n\n**Function :**\
        \n__First 5 are random gali string generaters__\
        \n__Last 3 are animations__\
        "
    }
)
