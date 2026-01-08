# Don't Remove Credit Tg - https://t.me/J1T3SH
# Subscribe YouTube Channel For Amazing Bot https://youtube.com/@TeamLeakageUnOfficial
# Ask Doubt on telegram https://t.me/J1T3SH

import logging
from logging.handlers import RotatingFileHandler

logging.basicConfig(
    level=logging.ERROR,
    format=
    "%(asctime)s - %(levelname)s - %(message)s [%(filename)s:%(lineno)d]",
    datefmt="%d-%b-%y %H:%M:%S",
    handlers=[
        RotatingFileHandler("logs.txt", maxBytes=50000000, backupCount=10),
        logging.StreamHandler(),
    ],
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)


logging = logging.getLogger()

