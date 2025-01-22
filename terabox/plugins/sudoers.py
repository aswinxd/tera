from terabox import app
from pyrogram import filters
from database import update_user
from datetime import datetime, timedelta

SUDOERS = [5815218439, 1137799257] 

@app.on_message(filters.command("premium") & filters.user(SUDOERS))
async def add_premium(client, message):
    if len(message.command) != 2:
        await message.reply_text("Usage: /premium <user_id>")
        return

    try:
        user_id = int(message.command[1])
        expiry_date = datetime.now() + timedelta(days=30)
        update_user(user_id, {"is_premium": True, "premium_expiry": expiry_date.timestamp()})
        await message.reply_text(f"User {user_id} has been granted premium access for 30 days.")
    except ValueError:
        await message.reply_text("Invalid user ID!")
