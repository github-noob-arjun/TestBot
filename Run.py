TOK="5931770179:AAHoonbw-4iJF6_rCzj02sph_6wNTkUssFs"
ID="15681435"
HAS="29021e7d8f6fe5338a45470115567f9e"


from pyrogram import Client, filters

Bot = Client(
    "RunBot",
    bot_token=TOK,
    api_id=ID,
    api_hash=HAS
)

@Bot.on_message(filters.private & filters.command(["start"]))
async def start(bot, update):
    
    await update.reply_text(
        text="Hi Java jaba jabaa.. 💥🔥🎉🎁",
        disable_web_page_preview=True,
        quote=True
    )

bot = Bot()
bot.run()
