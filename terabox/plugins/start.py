
from terabox import app
from pyrogram import Client, filters
from datetime import datetime, timedelta
from database import update_user, get_user

@app.on_message(filters.command("start") & filters.private)
async def start_command(client, message):
    user_id = message.from_user.id
    if len(message.command) > 1:
        parameter = message.command[1]

        if parameter == "free_session":
            session_expiry = datetime.now() + timedelta(hours=3)
            update_user(user_id, {"session_expiry": session_expiry.timestamp()})
            await message.reply_text(
                "Welcome! You've been granted 3 hours of unlimited access. "
                "Send me a TeraBox link, and I'll generate a direct download link for you!"
            )
            return
    await message.reply_text(
        "Hi! Send me a TeraBox link, and I'll generate a direct download link for you!"
    )
