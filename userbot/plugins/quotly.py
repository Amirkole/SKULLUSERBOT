"""
imported from nicegrill
modified by @mayank1rajput
QuotLy: Avaible commands: .qbot
"""
import os

from telethon import events
from telethon.errors.rpcerrorlist import YouBlockedUserError

from .. import CMD_HELP, process
from ..utils import admin_cmd, edit_or_reply, sudo_cmd


@bot.on(admin_cmd(pattern="q(?: |$)(.*)", outgoing=True))
@bot.on(sudo_cmd(pattern="q(?: |$)(.*)", allow_sudo=True))
async def stickerchat(skullquotes):
    if skullquotes.fwd_from:
        return
    reply = await skullquotes.get_reply_message()
    if not reply:
        await edit_or_reply(
            skullquotes, "`I cant quote the message . reply to a message`"
        )
        return
    fetchmsg = reply.message
    repliedreply = await reply.get_reply_message()
    if reply.media and reply.media.document.mime_type in ("mp4"):
        await edit_or_reply(skullquotes, "`this format is not supported now`")
        return
    skullevent = await edit_or_reply(skullquotes, "`Making quote...`")
    user = (
        await event.client.get_entity(reply.forward.sender)
        if reply.fwd_from
        else reply.sender
    )
    res, skullmsg = await process(fetchmsg, user, skullquotes.client, reply, repliedreply)
    if not res:
        return
    skullmsg.save("./temp/sticker.webp")
    await skullquotes.client.send_file(
        skullquotes.chat_id, "./temp/sticker.webp", reply_to=reply
    )
    await skullevent.delete()
    os.remove("./temp/sticker.webp")


@bot.on(admin_cmd(pattern="qbot(?: |$)(.*)", outgoing=True))
@bot.on(sudo_cmd(pattern="qbot(?: |$)(.*)", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    if not event.reply_to_msg_id:
        await edit_or_reply(event, "```Reply to any user message.```")
        return
    reply_message = await event.get_reply_message()
    if not reply_message.text:
        await edit_or_reply(event, "```Reply to text message```")
        return
    chat = "@QuotLyBot"
    skullevent = await edit_or_reply(event, "```Making a Quote```")
    async with event.client.conversation(chat) as conv:
        try:
            response = conv.wait_event(
                events.NewMessage(incoming=True, from_users=1031952739)
            )
            await event.client.forward_messages(chat, reply_message)
            response = await response
        except YouBlockedUserError:
            await skullevent.edit("```Please unblock me (@QuotLyBot) u Nigga```")
            return
        await event.client.send_read_acknowledge(conv.chat_id)
        if response.text.startswith("Hi!"):
            await skullevent.edit(
                "```Can you kindly disable your forward privacy settings for good?```"
            )
        else:
            await skullevent.delete()
            await event.client.send_message(event.chat_id, response.message)


CMD_HELP.update(
    {
        "quotly": "**Plugin :** `quotly`\
        \n\n**  •Syntax : **`.q reply to messge`\
        \n**  •Function : **__Makes your message as sticker quote__\
        \n\n**  •Syntax : **`.qbot reply to messge`\
        \n**  •Function : **__Makes your message as sticker quote by @quotlybot__\
        "
    }
)
