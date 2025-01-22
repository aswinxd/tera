from terabox import app
from pyrogram import Client, filters

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
