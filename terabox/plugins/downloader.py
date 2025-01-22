from terabox import app
from pyrogram import Client, filters
from datetime import datetime
from database import get_user

@app.on_message(filters.private & filters.text)
async def process_terabox_link(client, message):
    user_id = message.from_user.id
    user_message = message.text.strip()


    user = get_user(user_id)
    has_access = user and datetime.now().timestamp() < user.get("session_expiry", 0)

    if "teraboxapp.com" in user_message:
        if has_access:
            base_url = "https://teradownloader.com/download?w=0&link="
            direct_link = base_url + user_message
            await message.reply_text(f"Here is your direct download link:\n\n{direct_link}")
        else:
            await message.reply_text(
                "Your free session has expired. Please get a new session to continue using the bot."
            )
    else:
        await message.reply_text("Please send a valid TeraBox link!")
