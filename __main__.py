from pyrogram import Client
import os
from dotenv import load_dotenv 

load_dotenv() 

app_name = os.getenv('APP_NAME')
api_id = os.getenv('API_ID')
api_hash = os.getenv('API_HASH')
bot_token = os.getenv('API_TOKEN')

app = Client(
    name=app_name,
    api_id=api_id, 
    api_hash=api_hash,
    bot_token=bot_token,
    plugins=dict(root="plugins")
)


app.run()