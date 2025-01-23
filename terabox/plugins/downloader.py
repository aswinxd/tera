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
            await message.reply_text("Here is your direct download link\nClick below button to get it 👇. \nPurchase premium to download videos directly to telegram.",
                                      reply_markup=InlineKeyboardMarkup(
                                       [
                                          [InlineKeyboardButton("Click here to watch it", url=f"{direct_link}")],
                                          [InlineKeyboardButton("Send it on telegram", callback_data="processing_query")]
                                       ]
                                 )
                           )
        else:
            await message.reply_text(
                """🚨 Token Expired!

Token Timeout: 3 hours 

It looks like your access token has expired. Don't worry—you can easily refresh it to continue using the bot.?

🔑 What is this token?

This token is your access pass to the bot's premium features. By completing a simple ad process, you'll unlock 12 hours of uninterrupted access to all services. No hidden fees, no catches—just seamless functionality! 🌟

👉 Tap the button below to refresh your token and get started instantly. For guidance, check out our step-by-step tutorial.

💡 Why tokens?

Tokens helps to connect your browser on bot to download terabox content""",
                reply_markup=InlineKeyboardMarkup([
                    [InlineKeyboardButton("subscribe Premium ₹50", callback_data="buy_premium")],
                    [InlineKeyboardButton("What is token help", callback_data="get_token")],
                    [InlineKeyboardButton("Refresh token", url="https://modijiurl.com/o4MXhr")]
                ])
            )
    else:
        await message.reply_text("The link is invalid or broken bot cant find a terabox content on that link")


@app.on_callback_query()
async def handle_callback_query(client, callback_query):
    data = callback_query.data
    if data == "processing_query":
        await callback_query.answer(
            "Processing query. Available only for premium users.", show_alert=True
        )
