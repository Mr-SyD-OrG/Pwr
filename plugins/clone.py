# Don't Remove Credit Tg - @VJ_Botz
# Subscribe YouTube Channel For Amazing Bot https://youtube.com/@Tech_VJ
# Ask Doubt on telegram @KingVJ01

# Clone Code Credit : YT - NSyD_Xyz / TG - @GetTGLinks / GitHub - @Bot_Cracker 

from info import API_ID, API_HASH, CLONE_MODE, LOG_CHANNEL
from pyrogram import Client, filters, enums
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, BotCommand
from database.users_chats_db import db
import re
from Script import script

@Client.on_message(filters.command('clone'))
async def clone_menu(client, message):
    if CLONE_MODE == False:
        return 
    if await db.is_clone_exist(message.from_user.id):
        return await message.reply("**ʏᴏᴜ ʜᴀᴠᴇ ᴀʟʀᴇᴀᴅʏ ᴄʟᴏɴᴇᴅ ᴀ ʙᴏᴛ ᴅᴇʟᴇᴛᴇ ғɪʀsᴛ ɪᴛ ʙʏ /deleteclone**")
    else:
        pass
    techvj = await client.ask(message.chat.id, "<b>1) sᴇɴᴅ <code>/newbot</code> ᴛᴏ @BotFather\n2) ɢɪᴠᴇ ᴀ ɴᴀᴍᴇ ꜰᴏʀ ʏᴏᴜʀ ʙᴏᴛ.\n3) ɢɪᴠᴇ ᴀ ᴜɴɪǫᴜᴇ ᴜsᴇʀɴᴀᴍᴇ.\n4) ᴛʜᴇɴ ʏᴏᴜ ᴡɪʟʟ ɢᴇᴛ ᴀ ᴍᴇssᴀɢᴇ ᴡɪᴛʜ ʏᴏᴜʀ ʙᴏᴛ ᴛᴏᴋᴇɴ.\n5) ꜰᴏʀᴡᴀʀᴅ ᴛʜᴀᴛ ᴍᴇssᴀɢᴇ ᴛᴏ ᴍᴇ.\n\n/cancel - ᴄᴀɴᴄᴇʟ ᴛʜɪs ᴘʀᴏᴄᴇss.</b>")
    if techvj.text == '/cancel':
        await techvj.delete()
        return await message.reply('<b>Cᴀɴᴄᴇʟᴇᴅ ᴛʜɪs ᴘʀᴏᴄᴇss 🚫</b>')
    if techvj.forward_from and techvj.forward_from.id == 93372553:
        try:
            bot_token = re.findall(r"\b(\d+:[A-Za-z0-9_-]+)\b", techvj.text)[0]
        except:
            return await message.reply('<b>Sᴏᴍᴇᴛʜɪɴɢ ᴡᴇɴᴛ ᴡʀᴏɴɢ 😕</b>')
    else:
        return await message.reply('<b>Nᴏᴛ ꜰᴏʀᴡᴀʀᴅᴇᴅ ꜰʀᴏᴍ @BotFather 😑</b>')
    user_id = message.from_user.id
    msg = await message.reply_text("**Wᴀɪᴛ ᴀ ᴍɪɴᴜᴛᴇ ɪ ᴀᴍ ᴄʀᴇᴀᴛɪɴɢ ʏᴏᴜʀ ʙᴏᴛ,**")
    try:
        vj = Client(
            f"{bot_token}", API_ID, API_HASH,
            bot_token=bot_token,
            plugins={"root": "MrSyDClone"}
        )
        await vj.start()
        bot = await vj.get_me()
        await db.add_clone_bot(bot.id, user_id, bot_token)
        await msg.edit_text(f"<b>SᴜᴄᴄᴇssғᴜʟʟY Cʟᴏɴᴇᴅ Yᴏᴜʀ Bᴏᴛ: @{bot.username}.\n\nYᴏᴜ ᴄᴀɴ ᴄᴜsᴛᴏᴍɪsᴇ ʏᴏᴜʀ ᴄʟᴏɴᴇ ʙᴏᴛ ʙʏ \n/settings ᴀɴᴅ /edit \nCᴏᴍᴍᴀɴᴅ ɪɴ ʏᴏᴜʀ ᴄʟᴏɴᴇ ʙᴏᴛ</b><blockqoute>Nᴇᴠᴇʀ Fᴏʀɢᴇᴛ ᴛᴏ ᴇxᴩᴇʀɪᴇɴᴄᴇ ᴛʜᴇ ꜱᴜᴩᴇʀʙ ꜱᴇʀᴠɪᴄᴇᴇʜ⚡")
    except BaseException as e:
        await msg.edit_text(f"⚠️ <b>Bᴏᴛ Eʀʀᴏʀ:</b>\n\n<code>{e}</code>\n\n**Tʀʏ ᴀɢᴀɪɴ ʟᴀᴛᴇʀ ⚡ ᴏʀ Kɪɴᴅʟʏ ꜰᴏʀᴡᴀʀᴅ ᴛʜɪꜱ ᴍᴇꜱꜱᴀɢᴇ ᴛᴏ @SyD_XyZ ᴛᴏ ɢᴇᴛ ᴀꜱꜱɪꜱᴛᴀɴᴄᴇ.**")

@Client.on_message(filters.command('deleteclone'))
async def delete_clone_menu(client, message):
    if await db.is_clone_exist(message.from_user.id):
        await db.delete_clone(message.from_user.id)
        await message.reply("**sᴜᴄᴄᴇssғᴜʟʟʏ ᴅᴇʟᴇᴛᴇᴅ ʏᴏᴜʀ ᴄʟᴏɴᴇ ʙᴏᴛ, ʏᴏᴜ ᴄᴀɴ ᴄʀᴇᴀᴛᴇ ᴀɢᴀɪɴ ʙʏ /clone**")
    else:
        await message.reply("**ɴᴏ ᴄʟᴏɴᴇ ʙᴏᴛ ғᴏᴜɴᴅ**")

async def restart_bots():
    bots_cursor = await db.get_all_bots()
    bots = await bots_cursor.to_list(None)
    for bot in bots:
        bot_token = bot['bot_token']
        try:
            vj = Client(
                f"{bot_token}", API_ID, API_HASH,
                bot_token=bot_token,
                plugins={"root": "MrSyDClone"},
            )
            await vj.start()
        except Exception as e:
            print(f"Error while restarting bot with token {bot_token}: {e}")
        
