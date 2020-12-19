""" plugin is modified by @mayank1rajput """
import random
import re

from ..utils import admin_cmd, edit_or_reply, sudo_cmd
from . import CMD_HELP, fonts


@bot.on(admin_cmd(pattern="str(?: |$)(.*)"))
@bot.on(sudo_cmd(pattern="str(?: |$)(.*)", allow_sudo=True))
async def stretch(stret):
    textx = await stret.get_reply_message()
    message = stret.text
    message = stret.pattern_match.group(1)
    if message:
        pass
    elif textx:
        message = textx.text
    else:
        await edit_or_reply(stret, "`GiiiiiiiB sooooooomeeeeeee teeeeeeext!`")
        return

    count = random.randint(3, 10)
    reply_text = re.sub(r"([aeiouAEIOU锝侊絽锝夛綇锝曪肌锛ワ缉锛嫉邪械懈芯褍褞褟褘褝褢])", (r"\1" * count), message)
    await edit_or_reply(stret, reply_text)


@bot.on(admin_cmd(pattern="zal(?: |$)(.*)"))
@bot.on(sudo_cmd(pattern="zal(?: |$)(.*)", allow_sudo=True))
async def zal(zgfy):
    reply_text = list()
    textx = await zgfy.get_reply_message()
    message = zgfy.pattern_match.group(1)
    if message:
        pass
    elif textx:
        message = textx.text
    else:
        await edit_or_reply(
            zgfy, "`g瞳 虇 i虥 毯 v蛧虇 e虖蛥   a挞挺   s檀酞 c挞谈 a谈虉 r桐停 y蜄蜑   t台蜌 e虪虂 x挞蜄  t蜎蛿`"
        )
        return

    for charac in message:
        if not charac.isalpha():
            reply_text.append(charac)
            continue

        for _ in range(0, 3):
            randint = random.randint(0, 2)

            if randint == 0:
                charac = charac.strip() + random.choice(fonts.ZALG_LIST[0]).strip()
            elif randint == 1:
                charac = charac.strip() + random.choice(fonts.ZALG_LIST[1]).strip()
            else:
                charac = charac.strip() + random.choice(fonts.ZALG_LIST[2]).strip()

        reply_text.append(charac)

    await edit_or_reply(zgfy, "".join(reply_text))


@bot.on(admin_cmd(pattern="cp(?: |$)(.*)"))
@bot.on(sudo_cmd(pattern="cp(?: |$)(.*)", allow_sudo=True))
async def copypasta(cp_e):
    textx = await cp_e.get_reply_message()
    message = cp_e.pattern_match.group(1)

    if message:
        pass
    elif textx:
        message = textx.text
    else:
        await edit_or_reply(cp_e, "`馃槀馃叡锔廔vE馃憪sOME馃憛text馃憛for鉁岋笍Me馃憣tO馃憪MAkE馃憖iT馃挒funNy!馃挦`")
        return

    reply_text = random.choice(fonts.EMOJIS)
    # choose a random character in the message to be substituted with 馃叡锔�
    b_char = random.choice(message).lower()
    for owo in message:
        if owo == " ":
            reply_text += random.choice(fonts.EMOJIS)
        elif owo in fonts.EMOJIS:
            reply_text += owo
            reply_text += random.choice(fonts.EMOJIS)
        elif owo.lower() == b_char:
            reply_text += "馃叡锔�"
        else:
            if bool(random.getrandbits(1)):
                reply_text += owo.upper()
            else:
                reply_text += owo.lower()
    reply_text += random.choice(fonts.EMOJIS)
    await edit_or_reply(cp_e, reply_text)


@bot.on(admin_cmd(pattern="weeb(?: |$)(.*)"))
@bot.on(sudo_cmd(pattern="weeb(?: |$)(.*)", allow_sudo=True))
async def weebify(event):
    args = event.pattern_match.group(1)
    if not args:
        get = await event.get_reply_message()
        args = get.text
    if not args:
        await edit_or_reply(event, "`What I am Supposed to Weebify `")
        return
    string = "  ".join(args).lower()
    for normiecharacter in string:
        if normiecharacter in fonts.normiefont:
            weebycharacter = fonts.weebyfont[fonts.normiefont.index(normiecharacter)]
            string = string.replace(normiecharacter, weebycharacter)
    await edit_or_reply(event, string)


@bot.on(admin_cmd(pattern="downside(?: |$)(.*)"))
@bot.on(sudo_cmd(pattern="downside(?: |$)(.*)", allow_sudo=True))
async def stylish_generator(event):
    args = event.pattern_match.group(1)
    if not args:
        get = await event.get_reply_message()
        args = get.text
    if not args:
        await edit_or_reply(event, "What I am Supposed to change give text")
        return
    string = "  ".join(args).lower()
    for upsidecharacter in string:
        if upsidecharacter in fonts.upsidefont:
            downsidecharacter = fonts.downsidefont[
                fonts.upsidefont.index(upsidecharacter)
            ]
            string = string.replace(upsidecharacter, downsidecharacter)
    await edit_or_reply(event, string)


@bot.on(admin_cmd(pattern="subscript(?: |$)(.*)"))
@bot.on(sudo_cmd(pattern="subscript(?: |$)(.*)", allow_sudo=True))
async def stylish_generator(event):
    args = event.pattern_match.group(1)
    if not args:
        get = await event.get_reply_message()
        args = get.text
    if not args:
        await edit_or_reply(event, "What I am Supposed to change give text")
        return
    string = "  ".join(args).lower()
    for normaltextcharacter in string:
        if normaltextcharacter in fonts.normaltext:
            subscriptcharacter = fonts.subscriptfont[
                fonts.normaltext.index(normaltextcharacter)
            ]
            string = string.replace(normaltextcharacter, subscriptcharacter)
    await edit_or_reply(event, string)


@bot.on(admin_cmd(pattern="superscript(?: |$)(.*)"))
@bot.on(sudo_cmd(pattern="superscript(?: |$)(.*)", allow_sudo=True))
async def stylish_generator(event):
    args = event.pattern_match.group(1)
    if not args:
        get = await event.get_reply_message()
        args = get.text
    if not args:
        await edit_or_reply(event, "What I am Supposed to change give text")
        return
    string = "  ".join(args).lower()
    for normaltextcharacter in string:
        if normaltextcharacter in fonts.normaltext:
            superscriptcharacter = fonts.superscriptfont[
                fonts.normaltext.index(normaltextcharacter)
            ]
            string = string.replace(normaltextcharacter, superscriptcharacter)
    await edit_or_reply(event, string)


CMD_HELP.update(
    {
        "funnyfonts": """**Plugin : **`funnyfonts`
        
**Commands found in funnyfonts are**
  鈥�  `.str`
  鈥�  `.zal`
  鈥�  `.cp`
  鈥�  `.weeb`
  鈥�  `.downside`
  鈥�  `.subscript`
  鈥�  `.superscript`
  
**Function : **__Reply the command to the text message or give input along with command to convert that text to given font style__"""
    }
)
