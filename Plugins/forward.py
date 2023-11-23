# Don't Remove Credit @VJ_Botz
# Subscribe YouTube Channel For Amazing Bot @Tech_VJ
# Ask Doubt on telegram @KingVJ01


import logging
logger = logging.getLogger(__name__)

import asyncio
import time
from pyrogram import filters, Client, enums
from bot import channelforward
from pyrogram.errors import FloodWait
from config import Config

@channelforward.on_message((filters.private | filters.channel | filters.group) & (filters.document | filters.video ), group=4)
async def forward(client, message):
    # Forwarding the messages to the channel
   try:
      for id in Config.CHANNEL:
         from_channel, to_channel = id.split(":")
         if int(to_channel) == int(to_channel):
            func = message.forward
            await asyncio.sleep(2)
            await func(int(to_channel))
            logger.info("Forwarded a message from", from_channel, "to", to_channel)
   except Exception as e:
       logger.exception(e)

