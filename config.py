# devgagan
# Note if you are trying to deploy on vps then directly fill values in ("")

from os import getenv

# VPS --- FILL COOKIES 🍪 in """ ... """ 

INST_COOKIES = """
# wtite up here insta cookies
"""

YTUB_COOKIES = """
# write here yt cookies
"""

API_ID = int(getenv("API_ID", "28806791"))
API_HASH = getenv("API_HASH", "426ca904148df8f69ae24f9933dd1845")
BOT_TOKEN = getenv("BOT_TOKEN", "7624738382:AAHuAZpEFkk9So9aSS4xQFIpHq5BihtBNLg")
OWNER_ID = list(map(int, getenv("OWNER_ID", "1273640919").split()))
MONGO_DB = getenv("MONGO_DB", "mongodb+srv://gohilrahil7:95sgTUpWKd7BJ0eb@cluster0.kuivr1c.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
LOG_GROUP = getenv("LOG_GROUP", "-1002515456203")
CHANNEL_ID = int(getenv("CHANNEL_ID", ""))
FREEMIUM_LIMIT = int(getenv("FREEMIUM_LIMIT", "100"))
PREMIUM_LIMIT = int(getenv("PREMIUM_LIMIT", "500"))
WEBSITE_URL = getenv("WEBSITE_URL", "upshrink.com")
AD_API = getenv("AD_API", "52b4a2cf4687d81e7d3f8f2b7bc2943f618e78cb")
STRING = getenv("STRING", None)
YT_COOKIES = getenv("YT_COOKIES", YTUB_COOKIES)
DEFAULT_SESSION = getenv("DEFAUL_SESSION", None)  # added old method of invite link joining
INSTA_COOKIES = getenv("INSTA_COOKIES", INST_COOKIES)
