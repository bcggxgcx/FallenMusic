from os import getenv

from dotenv import load_dotenv

load_dotenv()


API_ID = int(getenv("API_ID", "13285379"))
API_HASH = getenv("API_HASH", "139edb762484f991a5ef5fec2ec9640b")

BOT_TOKEN = getenv("BOT_TOKEN", "6770424765:AAG4uwJpxgraAuRfg8NIgEtzOT-0crNmDgc")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "90"))

OWNER_ID = int(getenv("OWNER_ID", "6591561758"))

PING_IMG = getenv("PING_IMG", "https://te.legra.ph/file/6f99c49bdb4679acad717.jpg")
START_IMG = getenv("START_IMG", "https://te.legra.ph/file/f8ba75bdbb9931cbc8229.jpg")

SESSION = getenv("SESSION", "BACTYfG0oze52DLzrMf4n1-E9WgeyYlQRqMt3Wz3aSoXg_upq3x90kMxppn9TnTKUB1iuO-kucA_ulD4rT4b_-oaZ8D6OxhpDME46ozOLQyzrvJtBVMq1aEzYcwG57iI3lscdbGjzMPTVQxH19svuEX7mqFz9WpIm62iNLZjhisLYCujzWp8GhE6c4lnM3YZmiNz_hhfOXleO2W4Qm_39QccmRFKZl2F5nggdv4f40R3QlJstQJcOPPABaHrbL84vvgNENmsLjo0NMzmcik5-lTlJh2ZDhwYhPnku5rM6Nf6b-Xu3WEpRK0kLdaeUVtIkJnGvjVqhSYJBUChf9MNLxbYAAAAAYjjQB4A")

SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/DevilsHeavenMF")
SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/FallenAssociation")

SUDO_USERS = list(map(int, getenv("SUDO_USERS", "6591561758").split()))


FAILED = "https://te.legra.ph/file/4c896584b592593c00aa8.jpg"
