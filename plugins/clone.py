# Don't Remove Credit Tg - @SyD_XyZ
# Ask Doubt on telegram @Syd_XyZ

# Clone Code Credit : YT - @SyD_Xyz / TG - @GetTGLinks / GitHub - @Bot_Cracker 

from info import API_ID, API_HASH, CLONE_MODE, LOG_CHANNEL, SYD_CHANNELS
from pyrogram import Client, filters, enums
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, BotCommand
from database.users_chats_db import db
import re, os
from Script import script

async def not_subscribed(_, __, message):
    for channel in SYD_CHANNELS:
        try:
            user = await message._client.get_chat_member(channel, message.from_user.id)
            if user.status in {"kicked", "left"}:
                return True
        except UserNotParticipant:
            return True
    return False


@Client.on_message(filters.command('clone'))
async def clone_menu(client, message):
    if CLONE_MODE == False:
        return 
    not_joined_channels = []
    for channel in SYD_CHANNELS:
        try:
            user = await client.get_chat_member(channel, message.from_user.id)
            if user.status in {"kicked", "left"}:
                not_joined_channels.append(channel)
        except UserNotParticipant:
            not_joined_channels.append(channel)

    buttons = [
        [
            InlineKeyboardButton(
                text=f"📢 Join {channel.capitalize()} 📢", url=f"https://t.me/{channel}"
            )
        ]
        for channel in not_joined_channels
    ]
    buttons.append(
        [
            InlineKeyboardButton(
                text="✅ I am joined ✅", callback_data="check_subscription"
            )
        ]
    )

    text = "**Sorry, you're not joined to all required channels 😐. Please join the update channels to continue**"
    await message.reply_text(text=text, reply_markup=InlineKeyboardMarkup(buttons))


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
        await msg.edit_text(f"<b>SᴜᴄᴄᴇssғᴜʟʟY Cʟᴏɴᴇᴅ Yᴏᴜʀ Bᴏᴛ: @{bot.username}.\n\nYᴏᴜ ᴄᴀɴ ᴄᴜsᴛᴏᴍɪsᴇ ʏᴏᴜʀ ᴄʟᴏɴᴇ ʙᴏᴛ ʙʏ \n/settings ᴀɴᴅ /edit \nCᴏᴍᴍᴀɴᴅ ɪɴ ʏᴏᴜʀ ᴄʟᴏɴᴇ ʙᴏᴛ</b>\n\n<blockqoute>Nᴇᴠᴇʀ Fᴏʀɢᴇᴛ ᴛᴏ ᴇxᴩᴇʀɪᴇɴᴄᴇ ᴛʜᴇ ꜱᴜᴩᴇʀʙ ꜱᴇʀᴠɪᴄᴇᴇʜ⚡")
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
        
# Don't Remove Credit Tg - @SyD_XyZ
# Ask Doubt on telegram @Syd_XyZ
