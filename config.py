import re
import sys
from os import getenv

from dotenv import load_dotenv
from pyrogram import filters

load_dotenv()

API_ID = int(getenv("API_ID", "14569061"))
API_HASH = getenv("API_HASH", "27cdbce9ac58e83cec07e1147d9c9e05")

BOT_TOKEN = getenv("BOT_TOKEN", "5984358830:AAGmE69I4TDub4vhpXwU1EXP4tktzWVGrL8")

MONGO_DB_URI = getenv("MONGO_DB_URI", "mongodb+srv://ammu:fradu@cluster0.h0nt8me.mongodb.net/?retryWrites=true&w=majority")
LOG_GROUP_ID = int(getenv("LOG_GROUP_ID", "-1001830069963"))
MUSIC_BOT_NAME = getenv("MUSIC_BOT_NAME", "One Love Music")

OWNER_ID = list(map(int, getenv("OWNER_ID", "5737614771 5429263714").split()))

HEROKU_API_KEY = getenv("HEROKU_API_KEY", None)
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME", None)

UPSTREAM_REPO = getenv("UPSTREAM_REPO", "https://t.me/king_of_izzyy")
UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "master")
GIT_TOKEN = getenv("GIT_TOKEN", None)

SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/melting_mooon")
SUPPORT_GROUP = getenv("SUPPORT_GROUP", "https://t.me/Melting_mooonn")
SUPPORT_HEHE = SUPPORT_GROUP.split("me/")[1]

DURATION_LIMIT_MIN = int(getenv("DURATION_LIMIT", "999"))
SONG_DOWNLOAD_DURATION = int(getenv("SONG_DOWNLOAD_DURATION_LIMIT", "180"))

AUTO_LEAVING_ASSISTANT = getenv("AUTO_LEAVING_ASSISTANT", "False")
AUTO_LEAVE_ASSISTANT_TIME = int(
    getenv("ASSISTANT_LEAVE_TIME", "5400")
)

AUTO_DOWNLOADS_CLEAR = getenv("AUTO_DOWNLOADS_CLEAR", "True")

PRIVATE_BOT_MODE = getenv("PRIVATE_BOT_MODE", None)

YOUTUBE_DOWNLOAD_EDIT_SLEEP = int(getenv("YOUTUBE_EDIT_SLEEP", "5"))
TELEGRAM_DOWNLOAD_EDIT_SLEEP = int(getenv("TELEGRAM_EDIT_SLEEP", "3"))

SPOTIFY_CLIENT_ID = getenv("SPOTIFY_CLIENT_ID", "cf6365361b7041b4a51036553acd9d4f")
SPOTIFY_CLIENT_SECRET = getenv("SPOTIFY_CLIENT_SECRET", "8b96133fe3d942faae5066be2f3cde91")

VIDEO_STREAM_LIMIT = int(getenv("VIDEO_STREAM_LIMIT", "5"))
SERVER_PLAYLIST_LIMIT = int(getenv("SERVER_PLAYLIST_LIMIT", "50"))
PLAYLIST_FETCH_LIMIT = int(getenv("PLAYLIST_FETCH_LIMIT", "50"))

CLEANMODE_DELETE_MINS = int(getenv("CLEANMODE_MINS", "9999"))

TG_AUDIO_FILESIZE_LIMIT = int(getenv("TG_AUDIO_FILESIZE_LIMIT", "104857600"))
TG_VIDEO_FILESIZE_LIMIT = int(getenv("TG_VIDEO_FILESIZE_LIMIT", "999999999"))
# https://www.gbmb.org/mb-to-bytes

STRING1 = getenv("STRING_SESSION", "BQADblIBPGjRuwwWHaDf0Drcp4EtjRXfGSWkedp4IjU3GKesF6iHb8T92Kter28_B6HwmlY6nNBsyGi4RxunUIFGxz1l7NiqBf5oZGVsVAyPtNSjlAkRinqZ54RNJMXWUd5ygKIAl0MGRdAynrlVoFODqG2nml8Xg4-gqUq5t4SBQF7_YkEXQgmrLhH6V3fpWlGGO-jQMaQkR8Ucjy6xLqZewQ8IX3j_5xdtRR6x5NpjCXiYkiN1ABEYc04yuZ0-LFx7-meX4v2v72249CDPnI2hzH0WcDP16qajcVY8Pca8WaZBB51XJ8_aDeRYx_NyzsKbse1O1pR_OHvgrBNNH25FAAAAAV16JmsA")
STRING2 = getenv("STRING_SESSION2", "BQCnSli2qP-j4XCa83HaQheRN_9rRhOXSzhxyMccgWD3AaXxEj2JiFpII6sK4XmWJohcJl9UadqayugKaFEMlGPfFw3eJdFQamPb6r8QwLdSoGmcywmKp8LVn3sVGgyztRDGXeIFreqpGxcneiXojooH2KH2qvejC0ZiUFelr3D_uqoufPf-V7m_vplABq64rfsvRDm3VYwyEprbU8Nq0r9qP6i2UWsojr5XVHs8Wnt0zcXFEVYjTSbThJRQA0xIY98esz6jpdtL9tjxKS81JuRcN1RqPoaYdkaZ7A3BreFCDVZ929hHoVG49eQ1HiUnwCCJlbBiYQ3UTzXs1y4tMOlFAAAAATUG0NIA")
STRING3 = getenv("STRING_SESSION3", None)
STRING4 = getenv("STRING_SESSION4", None)
STRING5 = getenv("STRING_SESSION5", None)

BANNED_USERS = filters.user()
YTDOWNLOADER = 1
LOG = 2
LOG_FILE_NAME = "logs.txt"
adminlist = {}
lyrical = {}
chatstats = {}
userstats = {}
clean = {}
autoclean = []


START_IMG_URL = getenv("START_IMG_URL", "https://telegra.ph/file/0e5dc7cd0eebc76abce1f.jpg"
)

PING_IMG_URL = getenv(
    "PING_IMG_URL",
    "https://telegra.ph/file/0e5dc7cd0eebc76abce1f.jpg",
)

PLAYLIST_IMG_URL = "https://telegra.ph/file/0e5dc7cd0eebc76abce1f.jpg"

GLOBAL_IMG_URL = "https://telegra.ph/file/0e5dc7cd0eebc76abce1f.jpg"

STATS_IMG_URL = "https://telegra.ph/file/0e5dc7cd0eebc76abce1f.jpg"

TELEGRAM_AUDIO_URL = "https://telegra.ph/file/0e5dc7cd0eebc76abce1f.jpg"

TELEGRAM_VIDEO_URL = "https://telegra.ph/file/0e5dc7cd0eebc76abce1f.jpg"

STREAM_IMG_URL = "https://telegra.ph/file/66a7875e70ffacb7b34aa.jpg"

SOUNCLOUD_IMG_URL = "https://telegra.ph/file/0e5dc7cd0eebc76abce1f.jpg"

YOUTUBE_IMG_URL = "https://telegra.ph/file/0e5dc7cd0eebc76abce1f.jpg"

SPOTIFY_ARTIST_IMG_URL = "https://telegra.ph/file/0e5dc7cd0eebc76abce1f.jpg"

SPOTIFY_ALBUM_IMG_URL = "https://telegra.ph/file/0e5dc7cd0eebc76abce1f.jpg"

SPOTIFY_PLAYLIST_IMG_URL = "https://telegra.ph/file/0e5dc7cd0eebc76abce1f.jpg"

def time_to_seconds(time):
    stringt = str(time)
    return sum(
        int(x) * 60**i
        for i, x in enumerate(reversed(stringt.split(":")))
    )


DURATION_LIMIT = int(time_to_seconds(f"{DURATION_LIMIT_MIN}:00"))
SONG_DOWNLOAD_DURATION_LIMIT = int(
    time_to_seconds(f"{SONG_DOWNLOAD_DURATION}:00")
)


if UPSTREAM_REPO:
    if not re.match("(?:http|https)://", UPSTREAM_REPO):
        print(
            "[ERROR] - Your UPSTREAM_REPO url is wrong. Please ensure that it starts with https://"
        )
        sys.exit()

if PING_IMG_URL:
    if PING_IMG_URL != "assets/Ping.jpeg":
        if not re.match("(?:http|https)://", PING_IMG_URL):
            PING_IMG_URL = "https://telegra.ph/file/56d1760224589ee370186.jpg"

if START_IMG_URL:
    if START_IMG_URL != "assets/Ping.jpeg":
        if not re.match("(?:http|https)://", START_IMG_URL):
            START_IMG_URL = "https://te.legra.ph/file/56d1760224589ee370186.jpg"
