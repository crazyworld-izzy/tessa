import re
import sys
from os import getenv

from dotenv import load_dotenv
from pyrogram import filters

load_dotenv()

API_ID = int(getenv("API_ID", "14569061"))
API_HASH = getenv("API_HASH", "27cdbce9ac58e83cec07e1147d9c9e05")

BOT_TOKEN = getenv("BOT_TOKEN", "6435566970:AAF4KNbZA0jXtgCFJg0ww83Na5XmT1RHJcQ")

MONGO_DB_URI = getenv("MONGO_DB_URI", "mongodb+srv://prajeenthegrate:prajeenthegrate@cluster0.kmkxk4j.mongodb.net/?retryWrites=true&w=majority")
LOG_GROUP_ID = int(getenv("LOG_GROUP_ID", "-1001939293818"))
MUSIC_BOT_NAME = getenv("MUSIC_BOT_NAME", "One Love Music")

OWNER_ID = list(map(int, getenv("OWNER_ID", "5981227724").split()))

HEROKU_API_KEY = getenv("HEROKU_API_KEY", None)
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME", None)

UPSTREAM_REPO = getenv("UPSTREAM_REPO", "https://t.me/king_of_izzyy")
UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "master")
GIT_TOKEN = getenv("GIT_TOKEN", None)

SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/melting_moon")
SUPPORT_GROUP = getenv("SUPPORT_GROUP", "https://t.me/Melting_moon")
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

STRING1 = getenv("STRING_SESSION", "BQBfIoBcMqlII7AsWKcrcjKQBYfFK8BrC-Skg6D335_d1pmvWIQWbJYPqPwoZ9Dz6GjRYHN-s4VFOtWVb_iUzn7NIARr4OOJIYw9Rdp1s3mYJolucH28KIEpjQcmOFCuy9srJ3wTLdo9evDztr74T5vyMUDwVVBIEoh491jEQb7H2TdyF7adqPay29gzVu066M38Wiq0-KfCqZfvF_jUURQhniZDWVmc7vS39zARRXjmle8rFRbgOhG1G3oHQgHstELiDjFXj73DYbGXbsAe3NsBPTqbz57Iaao8wxLuW752wn5EIqGIQ1io_oHYyy1C36O9e1dG0lGx_xneeWLtWn4dAAAAAWSCSswA")
STRING2 = getenv("STRING_SESSION2", None)
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

STREAM_IMG_URL = "https://telegra.ph/file/0e5dc7cd0eebc76abce1f.jpg"

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
