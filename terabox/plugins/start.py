from terabox import app
from pyrogram import Client, filters

@app.on_message(filters.command("start") & filters.private)
async def start_command(client, message):
    await message.reply_text(
        "Hi! Send me a TeraBox link, and I'll generate a direct download link for you!"
    )
