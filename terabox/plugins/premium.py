from pyrogram import Client, filters
import requests
from terabox import app

@app.on_message(filters.text)
async def get_download_link(client, message):
    terabox_url = message.text.strip()

    try:
        response = requests.get(terabox_url, allow_redirects=False)
        if "Location" in response.headers:
            redirect_url = response.headers["Location"]
            final_response = requests.get(redirect_url, allow_redirects=True)
            print("Final URL:", final_response.url)
            
            if final_response.ok and "filename" in final_response.url:
                await message.reply(f"Here is your download link:\n{final_response.url}")
            else:
                await message.reply("Failed to extract the download link. Please check the URL.")
        else:
            await message.reply("Unable to fetch redirection link. Please ensure the URL is valid.")
    except Exception as e:
        await message.reply(f"An error occurred: {e}")
