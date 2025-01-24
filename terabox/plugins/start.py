
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery
from terabox import app
from pyrogram import Client, filters
from datetime import datetime, timedelta
from database import update_user, get_user
from pyrogram.enums import ParseMode

@app.on_message(filters.command("start"))
async def start_command(client, message):
    user_id = message.from_user.id
    referred_by = None

    if len(message.command) > 1:
        referred_by = message.command[1]
        parameter = message.command[1]

        if referred_by.isdigit(): 
            referrer_data = get_user(int(referred_by))
            if referrer_data:
                referrer_data["referrals"] = referrer_data.get("referrals", 0) + 1
                update_user(int(referred_by), {"referrals": referrer_data["referrals"]})

                if referrer_data["referrals"] >= 5:
                    new_expiry = datetime.now() + timedelta(hours=24)
                    update_user(int(referred_by), {"session_expiry": new_expiry.timestamp(), "referrals": 0})
                    await client.send_message(
                        int(referred_by),
                        "Congratulations! You referred 5 users and earned 24hours of free premium access! click below button to buy premium and get videos on telegram",
                        reply_markup=InlineKeyboardMarkup([
                            [InlineKeyboardButton("Subscribe to premium", callback_data="buy_premium")]
                        ])
                    )
        elif parameter == "free_session": 
            session_expiry = datetime.now() + timedelta(hours=24)
            update_user(user_id, {"session_expiry": session_expiry.timestamp()})
            await message.reply_text(
                "Added 24hours of usage token!",
                reply_markup=InlineKeyboardMarkup([
                            [InlineKeyboardButton("Subscribe to premium", callback_data="buy_premium")]
                        ])
            )

    
    user_data = get_user(user_id)
    if not user_data:
        update_user(user_id, {"session_expiry": 0, "referrals": 0, "referred_by": referred_by})

    await message.reply_text(
    "Hi welcome to terabox downloader bot. This tool helps you to download terabox content easily on telegram\n"
    "•Send a TeraBox link, to start downloading\n"
    "•Refresh token if your token is expired.\n"
    "•Get 24 hour free token refering 5 people to this bot",
    reply_markup=InlineKeyboardMarkup([
        [InlineKeyboardButton("Refer 5 people for token", callback_data="referal")],
        [InlineKeyboardButton("➕Add To Your Groups", url="https://t.me/TeraboxVideoDlRobot?startgroup=true")]
    ]),
    parse_mode=ParseMode.MARKDOWN
)

