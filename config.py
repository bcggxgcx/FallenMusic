from os import getenv

from dotenv import load_dotenv

load_dotenv()


API_ID = int(getenv("API_ID", "13949344"))
API_HASH = getenv("API_HASH", "408723003ad67fa8ab01ccc7f53e24ad")

BOT_TOKEN = getenv("BOT_TOKEN", "6901906356:AAGQ6KrpNzn36MdkQU29Uu1Ed9S0TP-HsPQ")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "90"))

OWNER_ID = int(getenv("OWNER_ID", "6539691387"))

PING_IMG = getenv("PING_IMG", "https://te.legra.ph/file/6f99c49bdb4679acad717.jpg")
START_IMG = getenv("START_IMG", "https://te.legra.ph/file/f8ba75bdbb9931cbc8229.jpg")

SESSION = getenv("SESSION", "BAAazQmIudUYiXrpAqTMsTwJbQDJPGZlu4T-dfb3dbIAxR60BnGIN5ZmdvxSAtyssqPncCobQ8pniuHNbPhGoL_O0wO5jH4ewJYGEt3Wvf6rMv13Th1b3pgKsxjZ08kKNzfl0xkONvRKx_6tMMH7zPQ6VVI_rVT1kIyWC7uYA6dLFZvucRpLwXV-vQ7t1Z_BET37nybOfxDAMicRBD_mnUBrIFX1KwHkDRvUx7vPjFTTfAI7LDnotossLzQR6FMNAidj2j9cyOrNZjlmb2rkhH1NMvpMOZsQW5gVD2cMcaigIKymYK4N92KoQZKJosB2onZIuP6rlqs-FK2pTC72fRAeAAAAAYXLxXsA")

SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/DevilsHeavenMF")
SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/FallenAssociation")

SUDO_USERS = list(map(int, getenv("SUDO_USERS", "6539691387").split()))


FAILED = "https://te.legra.ph/file/4c896584b592593c00aa8.jpg"
