import requests
from terabox import app
from pyrogram import Client, filters
from database import get_user  # Assuming a function to check user info in the database

@app.on_message(filters.private & filters.text)
async def process_terabox_link(client, message):
    user_id = message.from_user.id
    user_message = message.text.strip()

    # Check if the user is premium
    user_data = get_user(user_id)  # Fetch user info from your MongoDB
    is_premium = user_data.get("is_premium", False)

    if is_premium:
        # Use the API for premium users
        api_url = "https://ashlynn.serv00.net/Ashlynnterabox.php/"
        response = requests.get(api_url, params={"url": user_message})

        if response.status_code == 200:
            data = response.json()
            if "download_link" in data:
                download_link = data["download_link"]
                await message.reply_text(
                    f"Here is your direct download link:\n\n{download_link}"
                )
            else:
                await message.reply_text("Failed to fetch the download link.")
        else:
            await message.reply_text("Error contacting the API!")
    else:
        # Non-premium users use the old method
        if "teraboxapp.com" in user_message:
            base_url = "https://teradownloader.com/download?w=0&link="
            direct_link = base_url + user_message
            await message.reply_text(
                f"Here is your direct download link:\n\n{direct_link}\n\n"
                "Upgrade to premium for better download options!"
            )
        else:
            await message.reply_text("Please send a valid TeraBox link!")
