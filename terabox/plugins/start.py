from terabox import app
from pyrogram import Client, filters
from datetime import datetime, timedelta
from database import update_user, get_user

from terabox import app
from pyrogram import Client, filters
from datetime import datetime, timedelta
from database import update_user, get_user

@app.on_message(filters.command("start") & filters.private)
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
                    new_expiry = datetime.now() + timedelta(hours=3)
                    update_user(int(referred_by), {"session_expiry": new_expiry.timestamp(), "referrals": 0})
                    await client.send_message(
                        int(referred_by),
                        "Congratulations! You referred 5 users and earned 3 hours of free premium access! click below button to buy premium and get contents on telegram",
                        reply_markup=InlineKeyboardMarkup([
                            [InlineKeyboardButton("Subscribe to premium", callback_data="buy_premium")]
                        ])
                    )
        elif parameter == "free_session": 
            session_expiry = datetime.now() + timedelta(hours=3)
            update_user(user_id, {"session_expiry": session_expiry.timestamp()})
            await message.reply_text(
                "Added 3 hours of usage token! subscribe to premium on just 50 rs for more features.",
                reply_markup=InlineKeyboardMarkup([
                            [InlineKeyboardButton("Subscribe to premium", callback_data="buy_premium")]
                        ])
            )

    
    user_data = get_user(user_id)
    if not user_data:
        update_user(user_id, {"session_expiry": 0, "referrals": 0, "referred_by": referred_by})

    await message.reply_text(
        "Hi! Send me a TeraBox link, and I'll generate a direct download link for you!\n\n"
        "Refer the bot to 5 users and get free premium access for 3 hours"
        "Purchase premium for more premium features Click subscribe premium to know about premium features",
                reply_markup=InlineKeyboardMarkup([
                    [InlineKeyboardButton("subscribe Premium", callback_data="buy_premium")],
                    [InlineKeyboardButton("Refer for free premium", url=f"https://t.me/{client.me.username}?start={user_id}")],
                    [InlineKeyboardButton("Get token", url="https://t.me/TeraboxVideoDlRobot?start=free_session")]
                ])
    )
