import asyncio

from telethon.errors.rpcerrorlist import YouBlockedUserError

from ..utils import admin_cmd, edit_or_reply, sudo_cmd
from . import CMD_HELP, parse_pre, sanga_seperator


@bot.on(admin_cmd(pattern="(sg|sgu)($| (.*))"))
@bot.on(sudo_cmd(pattern="(sg|sgu)($| (.*))", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    # https://t.me/skulluserbot_support/2
    input_str = "".join(event.text.split(maxsplit=1)[1:])
    reply_message = await event.get_reply_message()
    if not input_str and not reply_message:
        skullevent = await edit_or_reply(
            event,
            "`reply to  user's text message to get name/username history or give userid`",
        )
        await asyncio.sleep(5)
        return await skullevent.delete()
    if input_str:
        try:
            uid = int(input_str)
        except ValueError:
            try:
                u = await event.client.get_entity(input_str)
            except ValueError:
                skullevent = await edit_or_reply(
                    event, "`Give userid or username to find name history`"
                )
                await asyncio.sleep(5)
                return await skullevent.delete()
            uid = u.id
    else:
        uid = reply_message.sender_id
    chat = "@SangMataInfo_bot"
    skullevent = await edit_or_reply(event, "`Processing...`")
    async with event.client.conversation(chat) as conv:
        try:
            await conv.send_message(f"/search_id {uid}")
        except YouBlockedUserError:
            await skullevent.edit("`unblock @Sangmatainfo_bot and then try`")
            await asyncio.sleep(5)
            return await skullevent.delete()
        responses = []
        while True:
            try:
                response = await conv.get_response(timeout=2)
            except asyncio.TimeoutError:
                break
            responses.append(response.text)
        await event.client.send_read_acknowledge(conv.chat_id)
    if not responses:
        await skullevent.edit("`bot can't fetch results`")
        await asyncio.sleep(5)
        return await skullevent.delete()
    if "No records found" in responses:
        await skullevent.edit("`The user doesn't have any record`")
        await asyncio.sleep(5)
        return await skullevent.delete()
    names, usernames = await sanga_seperator(responses)
    cmd = event.pattern_match.group(1)
    if cmd == "sg":
        mayank = None
        for i in names:
            if mayank:
                await event.reply(i, parse_mode=parse_pre)
            else:
                mayank = True
                await skullevent.edit(i, parse_mode=parse_pre)
    elif cmd == "sgu":
        mayank = None
        for i in usernames:
            if mayank:
                await event.reply(i, parse_mode=parse_pre)
            else:
                mayank = True
                await skullevent.edit(i, parse_mode=parse_pre)


CMD_HELP.update(
    {
        "sangmata": "**Plugin : **`sangmata`\
    \n\n**Syntax : **`.sg <username/userid/reply>`\
    \n**Function : **__Shows you the previous name history of user.__\
    \n\n**Syntax : **`.sgu <username/userid/reply>`\
    \n**Function : **__Shows you the previous username history of user.__\
    "
    }
)
