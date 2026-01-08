

from os import environ

API_ID = int(environ.get("API_ID", "25158505"))
API_HASH = environ.get("API_HASH", "902aabefb27ed4c0e330e39f8fd6c559")
BOT_TOKEN = environ.get("BOT_TOKEN", "8504136547:AAHV5MgebRSQfRGx0Nannva7oDwuAgeK-XU")

# Force Subscribe Configuration
FORCE_SUB_CHANNEL = environ.get("FORCE_SUB_CHANNEL", "NOOB_CBSE")  # Channel username without @, 
FORCE_SUB_CHANNEL_LINK = environ.get("FORCE_SUB_CHANNEL_LINK", "https://t.me/NOOB_CBSE")  # Channel link

# Admin Configuration
ADMINS = list(map(int, environ.get("ADMINS", "6963567931").split()))

# Optional: Bot Owner ID
OWNER_ID = int(environ.get("OWNER_ID", "6963567931"))

# Database URL (if you want to add database support later)
DATABASE_URL = environ.get("DATABASE_URL", "")




