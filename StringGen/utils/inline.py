from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from config import SUPPORT_CHAT


keyboard = InlineKeyboardMarkup(
    [
        [InlineKeyboardButton(text="اضغط هنا للستخراج ", callback_data="gensession")],
        [
            InlineKeyboardButton(text="قناة السورس", url=SUPPORT_CHAT),
            InlineKeyboardButton(
                text="مبرمج السورس ", url="https://t.me/S_1_02"
            ),
        ],
    ]
)

gen_key = InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton(text="ᴩʏʀᴏɢʀᴀᴍ v1", callback_data="pyrogram1"),
            InlineKeyboardButton(text="ᴩʏʀᴏɢʀᴀᴍ v2", callback_data="pyrogram"),
        ],
        [InlineKeyboardButton(text="ᴛᴇʟᴇᴛʜᴏɴ", callback_data="telethon")],
    ]
)

retry_key = InlineKeyboardMarkup(
    [[InlineKeyboardButton(text="ᴛʀʏ ᴀɢᴀɪɴ", callback_data="gensession")]]
)
