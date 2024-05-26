from pyrogram import Client, filters
from pyrogram.types import Message

@Client.on_message(filters.command("start"))
def start(client: Client, message: Message):
    message.reply_text("Hello welcome UpWork Feed BOT 👨‍💻")
