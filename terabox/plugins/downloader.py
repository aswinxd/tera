from terabox import app
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from datetime import datetime, timedelta
from database import get_user, update_user

@app.on_callback_query(filters.regex("get_alert"))
async def on_callback_query(client, callback_query):
    await callback_query.answer(
        "Buy premium to download video directly to telegram", show_alert=True
    )

@app.on_message(filters.text)
async def process_terabox_link(client, message):
    user_id = message.from_user.id
    user_message = message.text.strip()
    user = get_user(user_id)
    has_access = user and (datetime.now().timestamp() < user.get("session_expiry", 0) or user.get("is_premium", False))
    if ".com" in user_message:
        if has_access:
            base_url = "https://teradownloader.com/download?w=0&link="
            direct_link = base_url + user_message
            await message.reply_text("Here is your direct download link\n Click below button to get it 👇.",
                                      reply_markup=InlineKeyboardMarkup(
                                       [
                                          [InlineKeyboardButton("Watch online / download link", url=f"{direct_link}")],
                                          [InlineKeyboardButton("Get video in telegram", callback_data="get_alert")]
                                       ]
                                 )
                           )
        else:
            await message.reply_text(
                """🚨 Token Expired!

Token Timeout: 24hours 

It looks like your access token has expired. Don't worry—you can easily refresh it to continue using the bot.?

🔑 What is this token?

This token is your access pass to the bot's premium features. By completing a simple ad process, you'll unlock 24hours of uninterrupted access to all services. No hidden fees, no catches—just seamless functionality! 🌟

👉 Tap the button below to refresh your token and get started instantly. For guidance, check out our step-by-step tutorial.

💡 Why tokens?

Tokens helps to connect your browser on bot to download terabox content""",
                reply_markup=InlineKeyboardMarkup(
                    [
                    [InlineKeyboardButton("Refresh token", url="https://modijiurl.com/o4MXhr")],
                    [InlineKeyboardButton("Tutorial video", url="https://t.me/TeraboxHelpChannel/3")]
                ])
            )
    else:
        await message.reply_text("The link is invalid or broken bot cant find a terabox content on that link")


