import requests
from bs4 import BeautifulSoup
from pyrogram.types import InputMediaVideo
from database import get_user

@app.on_message(filters.private & filters.text)
async def process_terabox_link(client, message):
    user_id = message.from_user.id
    user_message = message.text.strip()

    # Fetch user data
    user = get_user(user_id)
    is_premium = user.get("is_premium", False)

    # Check if it's a valid link
    if "teraboxapp.com" in user_message or "xdisk.site" in user_message:
        if is_premium:
            try:
                # Fetch the video URL from the xdisk link
                video_url = extract_video_url(user_message)

                # Download and send the video file
                await download_and_send_video(client, message, video_url)
            except Exception as e:
                await message.reply_text(f"Failed to process the link: {e}")
        else:
            await message.reply_text(
                "This feature is available for premium users only. Please subscribe to premium to enjoy this feature!"
            )
    else:
        await message.reply_text("Please send a valid TeraBox or xdisk link!")

async def download_and_send_video(client, message, video_url):
    """Download the video and send it to the user."""
    try:
        # Stream and download the video
        response = requests.get(video_url, stream=True)
        response.raise_for_status()

        # Save the video temporarily
        video_path = "downloaded_video.mp4"
        with open(video_path, "wb") as video_file:
            for chunk in response.iter_content(chunk_size=8192):
                video_file.write(chunk)

        # Send the video to the user
        await client.send_video(
            chat_id=message.chat.id,
            video=video_path,
            caption="Here is your downloaded video!"
        )
    except Exception as e:
        await message.reply_text(f"Error downloading the video: {e}")
    finally:
        # Clean up temporary file
        import os
        if os.path.exists(video_path):
            os.remove(video_path)

def extract_video_url(link):
    """Extract the video URL from the 'Watch Online' button."""
    response = requests.get(link)
    response.raise_for_status()

    # Parse HTML to find the video URL
    soup = BeautifulSoup(response.text, "html.parser")
    button = soup.find("a", text="Watch Online")  # Adjust selector as needed
    if not button:
        raise ValueError("Watch Online button not found!")

    video_url = button["href"]
    return video_url
