import asyncio
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery
from pyrogram import Client, filters, enums 
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram.enums import ParseMode
import html
from strings.string import premium_text
from terabox import app
@app.on_callback_query()
async def handle_callback_query(client, callback_query):
    data = callback_query.data
    user_id = callback_query.from_user.id 

    if data == "menu":
        text = await callback_query.message.edit_text(
                              """
Hi welcome to terabox downloader bot. This tool helps you to download terabox content easily on telegram
•Send a TeraBox link, to start downloading
•Refresh token if your token is expired.
•Get 24 hour free token refering 5 people to this bot
""",
        reply_markup = InlineKeyboardMarkup([
            [InlineKeyboardButton("subscribe Premium ₹50", callback_data="buy_premium")],
            [InlineKeyboardButton("What is token", callback_data="get_token")],
            [InlineKeyboardButton("Refresh token", url="https://modijiurl.com/o4MXhr")]
        ]
        ),
        parse_mode=ParseMode.MARKDOWN,
        )

    elif data == "buy_premium":
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
3. Screenshot your payment and share it @Aiiwavn or Our [Support Chat](https://t.me/+I7lL7lVhDGAzMjVl)
4. Wait till you get approved and enjoy using bot
                             """,
            reply_markup=InlineKeyboardMarkup(
            [
                [InlineKeyboardButton("Pay using UPI", callback_data="pay_upi")],
                [InlineKeyboardButton("🔙", callback_data="buy_premium")],
            ]
        ),
        parse_mode=ParseMode.MARKDOWN,
    )
    elif data == "pay_upi":
      await callback_query.message.edit_text(
          """
**How to pay using upi.**
**Click to copy upi id**
**Upi Id** = `psaswin70@okaxis`

1. Click the given upi id to copy it and paste it on your payment app.
2. Pay the subscription amount 50 rs.
3. After payment send screenshot to @Aiiwavn or  [Support Chat](https://t.me/+I7lL7lVhDGAzMjVl)
4. We will verify your payment and you will get notified after verification by bot. """,
    reply_markup=InlineKeyboardMarkup(
        [[InlineKeyboardButton("🔙", callback_data="premium_steps")]]
    ),
    parse_mode=ParseMode.MARKDOWN,
    )
      
      
    elif data == "get_token":
        text = """
 What is this token?

This token is your access pass to the bot's premium features for free.imple ad process, you'll unlock 24hours of uninterrupted access to all services. No hidden fees, no catches—just seamless functionality! 🌟

👉 Tap the button below to refresh your token and get started instantly. For guidance, check out our step-by-step tutorial.

💡 Why tokens?

Tokens help us keep the bot free for everyone by supporting operational costs through a quick ad process."""
        back_button = InlineKeyboardMarkup(
            [
            [InlineKeyboardButton("video tutorial", url="https://t.me/TeraboxHelpChannel/2")],
            [InlineKeyboardButton("🔙", callback_data="menu")]
            ]
        )
        await callback_query.message.edit_text(
            text,
            reply_markup=back_button,
            parse_mode=ParseMode.MARKDOWN
        )
    elif data == "referal":
        text = await callback_query.message.edit_text(
             f"Here is your referal link share it to get free premium trial.\nclick to copy \n\n`https://t.me/TeraboxVideoDlRobot?start={user_id}`",
reply_markup=InlineKeyboardMarkup(
        [[InlineKeyboardButton("🔙", callback_data="menu")]]
    ),
    parse_mode=ParseMode.MARKDOWN,
    )

         
