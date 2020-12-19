import nekos

from ..utils import admin_cmd, edit_or_reply, sudo_cmd
from . import CMD_HELP


@bot.on(admin_cmd(pattern="tskull$"))
@bot.on(sudo_cmd(pattern="tskull$", allow_sudo=True))
async def hmm(skull):
    if skull.fwd_from:
        return
    reactskull = nekos.textskull()
    await edit_or_reply(skull, reactskull)


@bot.on(admin_cmd(pattern="why$"))
@bot.on(sudo_cmd(pattern="why$", allow_sudo=True))
async def hmm(skull):
    if skull.fwd_from:
        return
    whyskull = nekos.why()
    await edit_or_reply(skull, whyskull)


@bot.on(admin_cmd(pattern="fact$"))
@bot.on(sudo_cmd(pattern="fact$", allow_sudo=True))
async def hmm(skull):
    if skull.fwd_from:
        return
    factskull = nekos.fact()
    await edit_or_reply(skull, factskull)


CMD_HELP.update(
    {
        "funtxts": """**Plugin : **`funtxts`

  •  **Syntax : **`.tskull`
  •  **Function : **__Sens you some random skull facial text art__

  •  **Syntax : **`.why`
  •  **Function : **__Asks some random Funny questions__

  •  **Syntax : **`.fact`
  •  **Function : **__Sends you some random facts__"""
    }
)
