from pyrogram import Client, filters
import os

Bot = Client(
    "RunBot",
    bot_token="5931770179:AAHoonbw-4iJF6_rCzj02sph_6wNTkUssFs",
    api_id="15681435",
    api_hash="29021e7d8f6fe5338a45470115567f9e"
)

@Bot.on_message(filters.private & filters.command('start'))
async def start(bot, update):
    await update.send_message(
        chat_id=update.chat.id,
        text="Hi Java jaba jabaa.. 💥🔥🎉🎁",
        parse_mode="html")

@Bot.on_message(filters.private & filters.command('hlp'))
async def hlp(bot, update):
    await update.send_message(
        chat_id=update.chat.id,
        text="Hi Java jaba jabaa.. 💥🔥🎉🎁",
        parse_mode="html")
    

