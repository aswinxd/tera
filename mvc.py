import asyncio
import os
from pyrogram import Client, filters
from pyrogram.types import Message
from pytgcalls import PyTgCalls, StreamType
from pytgcalls.types.input_stream import AudioPiped
from yt_dlp import YoutubeDL

API_ID = "22710783"
API_HASH = "616ea341acfed51f916506c20b8a0a44"
BOT_TOKEN = "7558230173:AAGVx9CIJGh5QG96sbaSypFhz7e0SsS9jmM"
SESSION_STRING = "BQGCzhoAKeE4RWl9YaPkNcMeHQEDQQq-ivci5xNDlNMdybqSC7BaaWli0nEU1whOzGh9eQ2rI8Ky8s0nYR6dm7KL48ETsYUucRDWC-lK8YzfSGTabYnO9TtPKqQF25LVxPwhfRoNyomq-zXgiPmqbVnRwRCyojGzQNIhCC-KpKro-CjX5kg7EZtenX-GHSBiQjhy8G6__4DfO7yPDLZv8ZwgZ0jWRHuYcs_f_s05e1p1FwQLI9yDRqty1vMw8yzJDnmJNvzruA8X1zPGYYtgIJn3VCZzeob7EQD6M-GHdetrK1x3la5IzQoILy1lrEXNiaJz-d8i2_KMaGXSRYlTq0gBFvwcDAAAAAFvEOseAA"  # Generate using pyrogram
app = Client("music_bot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)
assistant = Client("assistant", api_id=API_ID, api_hash=API_HASH, session_string=SESSION_STRING)
pytgcalls = PyTgCalls(assistant)

ydl_opts = {
    'format': 'bestaudio/best',
    'quiet': True,
    'outtmpl': 'downloads/%(id)s.%(ext)s',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '192',
    }],
}

@app.on_message(filters.command("play") & filters.group)
async def play(client: Client, message: Message):
    query = " ".join(message.command[1:])
    if not query:
        return await message.reply("Please provide a song name or URL.")
    
    chat_id = message.chat.id
    try:
        await message.reply("Searching and downloading...")
        with YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(f"ytsearch:{query}", download=False)['entries'][0]
            ydl.download([info['webpage_url']])
            file_path = f"downloads/{info['id']}.mp3"
        
        await message.reply(f"Playing: {info['title']}")
        await pytgcalls.join_group_call(
            chat_id,
            AudioPiped(file_path),
            stream_type=StreamType().local_stream
        )
    except Exception as e:
        await message.reply(f"An error occurred: {str(e)}")

@app.on_message(filters.command("stop") & filters.group)
async def stop(client: Client, message: Message):
    chat_id = message.chat.id
    try:
        await pytgcalls.leave_group_call(chat_id)
        await message.reply("Stopped playing.")
    except Exception as e:
        await message.reply(f"An error occurred: {str(e)}")

@app.on_message(filters.command("pause") & filters.group)
async def pause(client: Client, message: Message):
    chat_id = message.chat.id
    try:
        await pytgcalls.pause_stream(chat_id)
        await message.reply("Paused.")
    except Exception as e:
        await message.reply(f"An error occurred: {str(e)}")

@app.on_message(filters.command("resume") & filters.group)
async def resume(client: Client, message: Message):
    chat_id = message.chat.id
    try:
        await pytgcalls.resume_stream(chat_id)
        await message.reply("Resumed.")
    except Exception as e:
        await message.reply(f"An error occurred: {str(e)}")

@app.on_message(filters.command("skip") & filters.group)
async def skip(client: Client, message: Message):
    chat_id = message.chat.id
    try:
        # Implement queue handling if needed
        await message.reply("Skipping to next song...")
    except Exception as e:
        await message.reply(f"An error occurred: {str(e)}")

@app.on_message(filters.command("help"))
async def help_command(client: Client, message: Message):
    help_text = (
        "/play <song name or URL> - Play music in voice chat.\n"
        "/stop - Stop the music.\n"
        "/pause - Pause the music.\n"
        "/resume - Resume the music.\n"
        "/skip - Skip the current track.\n"
    )
    await message.reply(help_text)

async def main():
    try:
        await assistant.start()
        await pytgcalls.start()
        print("Bot is running...")
        await app.start()
        await asyncio.Event().wait()
    finally:
        await assistant.stop()
        await pytgcalls.stop()
        await app.stop()
        
if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
