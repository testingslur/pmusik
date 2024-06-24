import asyncio

from Auput import app
from pyrogram import filters
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message
from config import MUSIC_BOT_NAME, OWNER_USERNAME, SUPPORT_CHANNEL

@app.on_message(filters.command("alive", ["/", ".", "!"]))
async def kontolmasukmemek(client: Client, message: Message):
    await message.reply_video(
        video=f"https://telegra.ph//file/9246a6b587d88e493ced0.jpg",
        caption=f"💖 Hei {message.from_user.mention}\n\n I am {MUSIC_BOT_NAME}\n\n✨ I am Fast and Powerful music player bot with some awesome features.\n\n━━━━━━━━━━━━━━━━━━❄",
        reply_markup=InlineKeyboardMarkup(
            [
               [
            InlineKeyboardButton(
                text="『ⒶⓁⒷⓎ』", url=f"https://t.me/{OWNER_USERNAME}"
            ),
            InlineKeyboardButton(
                text="ᴄʜᴀɴɴᴇʟ", url=f"{SUPPORT_CHANNEL}"
            ),
        ],
                [
                    InlineKeyboardButton(
                        "ᴄʟᴏsᴇ", callback_data="close"
                    )
                ],
            ]
        )
    )
