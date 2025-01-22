import asyncio
import importlib
from pathlib import Path
from pyrogram import idle
from pinterest import LOGGER, app
from .plugins import ALL_MODULES
from concurrent.futures import ThreadPoolExecutor
executor = ThreadPoolExecutor(max_workers=200) 
async def init():
    await app.start()
    plugins_path = Path("terabox/plugins")
    for module_path in plugins_path.glob("*.py"):
        module_name = module_path.stem 
        importlib.import_module(f"terabox.plugins.{module_name}")
    
    LOGGER("terabox.plugins").info("Successfully imported all modules.")
    await idle()
    await app.stop()
    LOGGER("music").info("Stopping the bot...")

if __name__ == "__main__":  
    asyncio.get_event_loop().run_until_complete(init())
