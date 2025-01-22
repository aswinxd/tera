from terabox import app
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from datetime import datetime, timedelta
from database import get_user, update_user

@app.on_message(filters.private & filters.text)
async def process_terabox_link(client, message):
    user_id = message.from_user.id
    user_message = message.text.strip()
    user = get_user(user_id)
    has_access = user and (datetime.now().timestamp() < user.get("session_expiry", 0) or user.get("is_premium", False))
    if "teraboxapp.com" in user_message:
        if has_access:
            base_url = "https://teradownloader.com/download?w=0&link="
            direct_link = base_url + user_message
            await message.reply_text(f"Here is your direct download link:\n\n{direct_link}")
        else:
            await message.reply_text(
                "Your free session has expired. Please get a new session to continue using the bot.",
                reply_markup=InlineKeyboardMarkup([
                    [InlineKeyboardButton("Choose Premium (₹50)", callback_data="choose_premium")],
                    [InlineKeyboardButton("Recharge Energy", callback_data="recharge_energy")],
                    [InlineKeyboardButton("What is Energy?", callback_data="what_is_energy")]
                ])
            )
    else:
        await message.reply_text("Please send a valid TeraBox link!")

@app.on_callback_query(filters.regex("choose_premium"))
async def choose_premium(client, callback_query):
    await callback_query.answer("Premium purchase is not yet implemented!", show_alert=True)

@app.on_callback_query(filters.regex("recharge_energy"))
async def recharge_energy(client, callback_query):
    await callback_query.answer("Energy recharge is not yet implemented!", show_alert=True)

@app.on_callback_query(filters.regex("what_is_energy"))
async def what_is_energy(client, callback_query):
    await callback_query.message.edit_text(
        "Energy is the free session quota you use to generate direct download links. "
        "You can recharge energy or buy premium to enjoy unlimited access!"
    )
