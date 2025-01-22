import asyncio
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery
from pyrogram import Client, filters, enums
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram.enums import ParseMode
import html
from terabox import app
@app.on_callback_query()
async def handle_callback_query(client, callback_query):
    data = callback_query.data

    if data == "buy_premium":
        buttons = [
            [InlineKeyboardButton("Step-by-Step Guide", callback_data="premium_steps")],
            [InlineKeyboardButton("🔙", callback_data="menu")],
        ]
        await callback_query.message.edit_text(
            premium_text,
            reply_markup=InlineKeyboardMarkup(buttons)
        )
    elif data == "premium_steps":
        await callback_query.message.edit_text(
"""Terabox premium helps you to download without limits.

**Features**

1. Bot sends media directly on telegram.
2. 200+ request per hour
3. Unlimited media downloads
4. No balance exhaustion
6. Save downloaded media on bots database

**steps to buy premium**

We Accept Upi, Coffiee, Cryto & Telegram stars as payment methord

1. Choose your plan 
2. Pay the money according to your premium plan
3. Screenshot your payment and share it @Drxew or Our [Support Chat](https://t.me/+ejeH2w5gVSAzZmE1)
4. Wait till you get approved and enjoy using bot
                             """,
            reply_markup=InlineKeyboardMarkup(
                [[InlineKeyboardButton("🔙", callback_data="buy_premium")]]
            ),
            parse_mode=ParseMode.MARKDOWN,
        )
    elif data == "get_token":
        text = """
 What is this token?

This token is your access pass to the bot's premium features for free.imple ad process, you'll unlock 12 hours of uninterrupted access to all services. No hidden fees, no catches—just seamless functionality! 🌟

👉 Tap the button below to refresh your token and get started instantly. For guidance, check out our step-by-step tutorial.

💡 Why tokens?

Tokens help us keep the bot free for everyone by supporting operational costs through a quick ad process."""
        back_button = InlineKeyboardMarkup(
            [[InlineKeyboardButton("video tutorial", url="t.me/howtodownload")]],
            [[InlineKeyboardButton("🔙", callback_data="menu")]],
        )
        await callback_query.message.edit_text(
            text,
            reply_markup=back_button,
            parse_mode=ParseMode.MARKDOWN
        )
