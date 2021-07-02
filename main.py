# © BugHunterCodeLabs ™
# © bughunter0
# 2021
# Copyright - https://en.m.wikipedia.org/wiki/Fair_use

import os 
from os import error
import speedtest   
import logging
import pyrogram
import math
from decouple import config
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram.types import User, Message

    
bughunter0 = Client(
    "SpeedTestBot",
    bot_token = os.environ["BOT_TOKEN"],
    api_id = int(os.environ["API_ID"]),
    api_hash = os.environ["API_HASH"]
)


@bughunter0.on_message(filters.command(["start"]))
async def start(bot, update):
 txt = await update.reply_text("ചത്തോന്ന് അറിയാൻ വന്നതാവും ല്ലേ !!")

@bughunter0.on_message(filters.private)
async def download_upload(bot, message):
     alert = await message.reply_text("Processing....")
     Speed = speedtest.Speedtest() 
     await alert.delete()
     dlspeed = await message.reply_text("Checking Download Speed ...")
     downloadspeed = math.round(Speed.download())
     downloadspeed = downloadspeed/1000000 # bit to kbps
     await dlspeed.edit_text(f"`Download Speed : {downloadspeed} kbps`")
     upspeed = await message.reply_text("Checking Upload Speed")
     uploadspeed = math.round(Speed.upload())
     uploadspeed = uploadspeed/1000000 # bit to kbps
     await upspeed.edit_text(f"`Upload Speed : {uploadspeed} kbps`")

bughunter0.run()
