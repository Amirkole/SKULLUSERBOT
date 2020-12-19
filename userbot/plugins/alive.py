import time
from platform import python_version

from telethon import version

from ..utils import admin_cmd, edit_or_reply, sudo_cmd
from . import ALIVE_NAME, CMD_HELP, StartTime, skulldef, Skullversion, mention, reply_id

DEFAULTUSER = ALIVE_NAME or "SKULL"
SKULL_IMG = Config.ALIVE_PIC
CUSTOM_ALIVE_TEXT = Config.CUSTOM_ALIVE_TEXT or "👻 MY BOT IS RUNNING SUCCESFULLY 👻"
EMOJI = Config.CUSTOM_ALIVE_EMOJI or "  ✄1�7 "


@bot.on(admin_cmd(outgoing=True, pattern="alive$"))
@bot.on(sudo_cmd(pattern="alive$", allow_sudo=True))
async def amireallyalive(alive):
    if alive.fwd_from:
        return
    reply_to_id = await reply_id(alive)
    uptime = await skulldef.get_readable_time((time.time() - StartTime))
    _, check_sgnirts = check_data_base_heal_th()
    if _IMG:
        skull_caption = f"**{CUSTOM_ALIVE_TEXT}**\n\n"
        skull_caption += f"**{EMOJI} Database :** `{check_sgnirts}`\n"
        skull_caption += f"**{EMOJI} Telethon version :** `{version.__version__}\n`"
        skull_caption += f"**{EMOJI} Skulluserbot Version :** `{skullversion}`\n"
        skull_caption += f"**{EMOJI} Python Version :** `{python_version()}\n`"
        skull_caption += f"**{EMOJI} Uptime :** `{uptime}\n`"
        skull_caption += f"**{EMOJI} Master:** {mention}\n"
        await alive.client.send_file(
            alive.chat_id, SKULL_IMG, caption=skull_caption, reply_to=reply_to_id
        )
        await alive.delete()
    else:
        await edit_or_reply(
            alive,
            f"**{CUSTOM_ALIVE_TEXT}**\n\n"
            f"**{EMOJI} Database :** `{check_sgnirts}`\n"
            f"**{EMOJI} Telethon Version :** `{version.__version__}\n`"
            f"**{EMOJI} Skulluserbot Version :** `{skullversion}`\n"
            f"**{EMOJI} Python Version :** `{python_version()}\n`"
            f"**{EMOJI} Uptime :** `{uptime}\n`"
            f"**{EMOJI} Master:** {mention}\n",
        )


@bot.on(admin_cmd(outgoing=True, pattern="ialive$"))
@bot.on(sudo_cmd(pattern="ialive$", allow_sudo=True))
async def amireallyalive(alive):
    if alive.fwd_from:
        return
    tgbotusername = Config.TG_BOT_USER_NAME_BF_HER
    reply_to_id = await reply_id(alive)
    skull_caption = f"**Skulluserbot is Up and Running**\n"
    skull_caption += f"**  -Telethon version :** `{version.__version__}\n`"
    skull_caption += f"**  -Skulluserbot Version :** `{skullversion}`\n"
    skull_caption += f"**  -Python Version :** `{python_version()}\n`"
    skull_caption += f"**  -Master:** {mention}\n"
    results = await bot.inline_query(tgbotusername, skull_caption)  # pylint:disable=E0602
    await results[0].click(alive.chat_id, reply_to=reply_to_id, hide_via=True)
    await alive.delete()


# UniBorg Telegram UseRBot
# Copyright (C) 2020 @UniBorg
# This code is licensed under
# the "you can't use this for anything - public or private,
# unless you know the two prime factors to the number below" license
# 543935563961418342898620676239017231876605452284544942043082635399903451854594062955
# വിവരണം അടിച്ചുമാറ്റിക്കൊണ്ടൄ1�7 പോകുന്നവൄ1�7
# ക്രെഡിറ്റ് വെച്ചാൄ1�7 സന്തോഷമേ ഉള്ളൄ1�7..!
# uniborg


def check_data_base_heal_th():
    # https://stackoverflow.com/a/41961968
    is_database_working = False
    output = "No Database is set"
    if not Config.DB_URI:
        return is_database_working, output
    from userbot.plugins.sql_helper import SESSION

    try:
        # to check database we will execute raw query
        SESSION.execute("SELECT 1")
    except Exception as e:
        output = f"❄1�7 {str(e)}"
        is_database_working = False
    else:
        output = "Functioning Normally"
        is_database_working = True
    return is_database_working, output


CMD_HELP.update(
    {
        "alive": "**Plugin :** `alive`\
      \n\n   1�7  **Syntax : **`.alive` \
      \n   1�7  **Function : **__status of bot will be showed__\
      \n\n   1�7  **Syntax : **`.ialive` \
      \n   1�7  **Function : **__inline status of bot will be shown.__\
      \nSet `ALIVE_PIC` var for media in alive message"
    }
)
