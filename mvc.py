import asyncio
import os
from pyrogram import Client, filters
from pyrogram.types import Message
from pytgcalls import PyTgCalls, StreamType
from pytgcalls.types.input_stream import AudioPiped
from yt_dlp import YoutubeDL


from pyrogram import Client, filters

API_ID = "22710783"
API_HASH = "616ea341acfed51f916506c20b8a0a44"
BOT_TOKEN = "7558230173:AAGVx9CIJGh5QG96sbaSypFhz7e0SsS9jmM"


# Initialize the Pyrogram Client
app = Client("terabox_bot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)

# Start Command
@app.on_message(filters.command("start") & filters.private)
async def start_command(client, message):
    await message.reply_text(
        "Hi! Send me a TeraBox link, and I'll generate a direct download link for you!"
    )

# Process TeraBox Links
@app.on_message(filters.private & filters.text)
async def process_terabox_link(client, message):
    user_message = message.text.strip()

    # Check if it's a TeraBox link
    if "teraboxapp.com" in user_message:
        base_url = "https://teradownloader.com/download?w=0&link="
        direct_link = base_url + user_message
        await message.reply_text(f"Here is your direct download link:\n\n{direct_link}")
    else:
        await message.reply_text("Please send a valid TeraBox link!")

# Run the Bot
if __name__ == "__main__":
    app.run()
