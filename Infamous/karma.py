# https://github.com/akshayxt/XtManager
#  
# https://t.me/O_okarma

# <============================================== IMPORTS =========================================================>
from pyrogram.types import InlineKeyboardButton as ib
from telegram import InlineKeyboardButton

from XtManager import BOT_USERNAME, OWNER_ID, SUPPORT_CHAT

# <============================================== CONSTANTS =========================================================>
START_IMG = [
    "https://telegra.ph/file/f3b2776b2766e911383f0.jpg",
    "https://graph.org/file/08db66a4374af926c9bd3.jpg",
    "https://graph.org/file/7d9eaee9efe95444fb5e3.jpg",
    "https://telegra.ph/file/f71f13dc4755349c13a70.jpg",
    "https://telegra.ph/file/0b99d9768000b9fbc7a28.jpg",
    "https://telegra.ph/file/6af06601caadb0e88e8fe.jpg",
    "https://telegra.ph/file/0cd3fdfb1c37e35860167.jpg",
    "https://telegra.ph/file/0cd3fdfb1c37e35860167.jpg",
    "https://graph.org/file/a45b214adabcd86401152.jpg",
]

HEY_IMG = "https://graph.org/file/3740819ccb58317741e8e.jpg"

ALIVE_ANIMATION = [
    "https://telegra.ph/file/3274b73a7ba7b94c2bd7e.mp4",
    "https://telegra.ph/file/2bf047379d9bfa80e0238.mp4",
    "https://graph.org/file/47b7a9c0a71aabd5aac4d.mp4",
    "https://graph.org/file/d1837bc46a5ac7a192823.mp4",
    "https://graph.org/file/95b7f8b32eec311f836c2.mp4",
    "https://graph.org/file/95b7f8b32eec311f836c2.mp4",
    "https://graph.org/file/95b7f8b32eec311f836c2.mp4",
    "https://graph.org/file/788e7f7f5bd24908c219f.mp4",
]

FIRST_PART_TEXT = "✨ *ʜᴇʟʟᴏ* `{}` . . ."

PM_START_TEXT = "✨ *ɪ ᴀᴍ Rax, @Team_XT_support ʀᴏʙᴏᴛ ᴡʜɪᴄʜ ᴄᴀɴ ʜᴇʟᴘ ʏᴏᴜ ᴛᴏ ᴍᴀɴᴀɢᴇ ᴀɴᴅ ꜱᴇᴄᴜʀᴇ ʏᴏᴜʀ ɢʀᴏᴜᴘ ᴡɪᴛʜ ʜᴜɢᴇ ɢʀᴏᴜᴘ ᴍᴀɴᴀɢᴇᴍᴇɴᴛ 🚀 𝓘𝓷𝓽𝓻𝓸𝓭𝓾𝓬𝓲𝓷𝓰 𝓡𝓪𝔁 𝓐𝓘 𝓜𝓾𝓼𝓲𝓬 𝓪𝓷𝓭 𝓒𝓱𝓪𝓽 𝓑𝓸𝓽 𝓯𝓸𝓻 𝓣𝓮𝓵𝓮𝓰𝓻𝓪𝓶 - 𝓨𝓸𝓾𝓻 𝓤𝓵𝓽𝓲𝓶𝓪𝓽𝓮 𝓜𝓾𝓼𝓲𝓬𝓪𝓵 𝓒𝓸𝓶𝓹𝓪𝓷𝓲𝓸𝓷! 🎵 𝓔𝓶𝓫𝓪𝓻𝓴 𝓸𝓷 𝓪 𝓻𝓮𝓿𝓸𝓵𝓾𝓽𝓲𝓸𝓷𝓪𝓻𝔂 𝓳𝓸𝓾𝓻𝓷𝓮𝔂 𝔀𝓲𝓽𝓱 𝓡𝓪𝔁 𝓐𝓘, 𝓪 𝓼𝓽𝓪𝓽𝓮-𝓸𝓯-𝓽𝓱𝓮-𝓪𝓻𝓽 𝓶𝓾𝓼𝓲𝓬 𝓫𝓸𝓽 𝓭𝓮𝓼𝓲𝓰𝓷𝓮𝓭 𝓽𝓸 𝓽𝓻𝓪𝓷𝓼𝓯𝓸𝓻𝓶 𝔂𝓸𝓾𝓻 𝓣𝓮𝓵𝓮𝓰𝓻𝓪𝓶 𝓬𝓱𝓪𝓽𝓼 𝓲𝓷𝓽𝓸 𝓪𝓷 𝓲𝓶𝓶𝓮𝓻𝓼𝓲𝓿𝓮 𝓶𝓾𝓼𝓲𝓬𝓪𝓵 𝓱𝓪𝓿𝓮𝓷! 🤖🎶*"

START_BTN = [
    [
        InlineKeyboardButton(
            text="⇦ ADD ME ⇨",
            url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
        ),
    ],
    [
        InlineKeyboardButton(text="HELP", callback_data="help_back"),
    ],
    [
        InlineKeyboardButton(text="DETAILS", callback_data=" Rax_"),
        InlineKeyboardButton(text="AI", callback_data="ai_handler"),
        InlineKeyboardButton(text="SOURCE", callback_data="git_source"),
    ],
    [
        InlineKeyboardButton(text="CREATOR", url=f"tg://user?id={OWNER_ID}"),
    ],
]

GROUP_START_BTN = [
    [
        InlineKeyboardButton(
            text="⇦ ADD ME ⇨",
            url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
        ),
    ],
    [
        InlineKeyboardButton(text="SUPPORT", url=f"https://t.me/{SUPPORT_CHAT}"),
        InlineKeyboardButton(text="CREATOR", url=f"tg://user?id={OWNER_ID}"),
    ],
]

ALIVE_BTN = [
    [
        ib(text="UPDATES", url="https://t.me/team_x_t_support"),
        ib(text="SUPPORT", url="https://t.me/team_x_t"),
    ],
    [
        ib(
            text="⇦ ADD ME ⇨",
            url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
        ),
    ],
]

HELP_STRINGS = """
🫧 *Yae- Rax* 🫧

☉ *Here, you will find a list of all the available commands.*

ᴀʟʟ ᴄᴏᴍᴍᴀɴᴅs ᴄᴀɴ ʙᴇ ᴜsᴇᴅ ᴡɪᴛʜ : /
"""
