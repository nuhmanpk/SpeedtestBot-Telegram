# © BugHunterCodeLabs ™
# © bughunter0
# 2021
# Copyright - https://en.m.wikipedia.org/wiki/Fair_use

import os 
from os import error
import speedtest   
import logging
import pyrogram
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
async def download(bot, message):
     downloadSpeed = speedtest.Speedtest() 
     txt = await message.reply_text(f"{downloadSpeed.download()} Mbps")
     txt1 = await message.reply_text(f"{downloadSpeed.upload} Mbps")

bughunter0.run()
