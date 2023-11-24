from os import getenv

from dotenv import load_dotenv

load_dotenv()


API_ID = int(getenv("API_ID", "13949344"))
API_HASH = getenv("API_HASH", "408723003ad67fa8ab01ccc7f53e24ad")

BOT_TOKEN = getenv("BOT_TOKEN", "6817393512:AAHksFyaUfon-fsR-zFMakciRK5rdlzd4wE")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "90"))

OWNER_ID = int(getenv("OWNER_ID", "6539691387"))

PING_IMG = getenv("PING_IMG", "https://te.legra.ph/file/6f99c49bdb4679acad717.jpg")
START_IMG = getenv("START_IMG", "https://te.legra.ph/file/f8ba75bdbb9931cbc8229.jpg")

SESSION = getenv("SESSION", "BAA4dkPOjfy7HFoxJQNA2hnk7sFXoZQ5lcgiULbpp1DThNT7Wk9mnzYXI2h3zB96VwWD1vXMApDBfng6h2tB088GxUkfvpX5g4q2fu6MzD8DEAn9Zx1AbAKfjyMz5fBiZ9kjOLFVEQOLimmlwvbDHXtidsOABw9Q5yZ7eQ9HyUTIzEOpi03v-EXkL-AanyHna9xF1ZPfHlZY8-IOJBTkx3OyXolmM61wsl4TBeZJ1r6AbaNEG2TLs803rOMhjTflvuiI6rmkvMM8_xd2v848YX6SYYZyArIpHYQAGk2w5VJP69dN1torBqrxpr_4H17hqG342e-nzuw_XXT1gWsj8EZUAAAAAYXLxXsA")

SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/DevilsHeavenMF")
SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/FallenAssociation")

SUDO_USERS = list(map(int, getenv("SUDO_USERS", "6539691387").split()))


FAILED = "https://te.legra.ph/file/4c896584b592593c00aa8.jpg"
