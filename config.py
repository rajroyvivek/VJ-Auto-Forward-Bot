from os import getenv

class Config(object):
      API_HASH = getenv("API_HASH", "a1a06a18eb9153e9dbd447cfd5da2457")
      API_ID = int(getenv("API_ID", "20389440"))
      session_string = int(getenv("session_string", "")
      AS_COPY = True if getenv("AS_COPY", True) == "`{file_name}`" else True
      BOT_TOKEN = getenv("BOT_TOKEN", "6564513574:AAGDqUaEmeu0m4DjLDetNc4nooVTWYT7Fzo")
      CHANNEL = list(x for x in getenv("CHANNEL_ID", "1:-1002031514094").replace("\n", " ").split(' '))


# Don't Remove Credit @VJ_Botz
# Subscribe YouTube Channel For Amazing Bot @Tech_VJ
# Ask Doubt on telegram @KingVJ01
