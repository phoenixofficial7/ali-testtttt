from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, ForceReply, CallbackQuery
import humanize
from helper.txt import mr
from helper.database import  insert 
from helper.utils import not_subscribed 

@Client.on_message(filters.private & filters.create(not_subscribed))
async def is_not_subscribed(client, message):
    await message.reply_text(
       text="**ππΎπππ π³ππ³π΄ ππΎππ π½πΎπ πΉπΎπΈπ½π³ πΌπ π²π·π°π½π½π΄π». πΏπ»π΄π°ππ΄ πΉπΎπΈπ½ πΌπ π²π·π°π½π½π΄π» ππΎ πππ΄ ππ·πΈπ π±πΎπ π **",
       reply_markup=InlineKeyboardMarkup([
           [ InlineKeyboardButton(text="π’πΉπππ πΌπ’ ππππππ π²πππππππ’", url=client.invitelink)]
           ])
       )
    
@Client.on_message(filters.private & filters.command(["start"]))
async def start(client, message):
    insert(int(message.chat.id))
    await message.reply_photo(
       photo="https://te.legra.ph/file/ebdd449b177a948315a87.jpg",
       caption=f"""π Hai {message.from_user.mention} \nπΈ'π π° ππππππ π΅πππ ππππππ+π΅πππ ππ πππππ π²πππππππ π±πΎπ ππππ πΏππππππππ πππππππππ & π²πππππ π²ππππππ πππππππ! """,
       reply_markup=InlineKeyboardMarkup( [[
           InlineKeyboardButton("πΌ π³π΄ππ πΌ", callback_data='dev')
           ],[
           InlineKeyboardButton('π’ ππΏπ³π°ππ΄π', url='https://t.me/PhoenixBotz'),
           InlineKeyboardButton('π πππΏπΏπΎππ', url='https://t.me/PhoenixXGuardians')
           ],[
           InlineKeyboardButton('π π°π±πΎππ', callback_data='about'),
           InlineKeyboardButton('βΉοΈ π·π΄π»πΏ', callback_data='help')
           ]]
          )
       )
    return

@Client.on_message(filters.private &( filters.document | filters.audio | filters.video ))
async def send_doc(client, message):
    file = getattr(message, message.media.value)
    filename = file.file_name
    filesize = humanize.naturalsize(file.file_size)
    fileid = file.file_id
    await message.reply_text(
        f"__What do you want me to do with this file?__\n**File Name** :- `{filename}`\n**File Size** :- `{filesize}`",
        reply_to_message_id = message.id,
        reply_markup = InlineKeyboardMarkup([[ InlineKeyboardButton("π ππ΄π½π°πΌπ΄",callback_data = "rename")],
        [InlineKeyboardButton("π²π°π½π²π΄π» βοΈ",callback_data = "cancel")  ]]))


@Client.on_callback_query()
async def cb_handler(client, query: CallbackQuery):
    data = query.data 
    if data == "start":
        await query.message.edit_text(
            text=f"""π Hai {query.from_user.mention} \nπΈ'π π° ππππππ π΅πππ ππππππ+π΅πππ ππ πππππ π²πππππππ π±πΎπ ππππ πΏππππππππ πππππππππ & π²πππππ π²ππππππ πππππππ! """,
            reply_markup=InlineKeyboardMarkup( [[
                InlineKeyboardButton("πΌ π³π΄ππ πΌ", callback_data='dev')
                ],[
                InlineKeyboardButton('π’ ππΏπ³π°ππ΄π', url='https://t.me/PhoenixBotz'),
                InlineKeyboardButton('π πππΏπΏπΎππ', url='https://t.me/PhoenixXGuardians')
                ],[
                InlineKeyboardButton('π π°π±πΎππ', callback_data='about'),
                InlineKeyboardButton('βΉοΈ π·π΄π»πΏ', callback_data='help')
                ]]
                )
            )
        return
    elif data == "help":
        await query.message.edit_text(
            text=mr.HELP_TXT,
            reply_markup=InlineKeyboardMarkup( [[
               InlineKeyboardButton("π π²π»πΎππ΄", callback_data = "close"),
               InlineKeyboardButton("βοΈ π±π°π²πΊ", callback_data = "start")
               ]]
            )
        )
    elif data == "about":
        await query.message.edit_text(
            text=mr.ABOUT_TXT.format(client.mention),
            disable_web_page_preview = True,
            reply_markup=InlineKeyboardMarkup( [[
               InlineKeyboardButton("π π²π»πΎππ΄", callback_data = "close"),
               InlineKeyboardButton("βοΈ π±π°π²πΊ", callback_data = "start")
               ]]
            )
        )
    elif data == "dev":
        await query.message.edit_text(
            text=mr.DEV_TXT,
            reply_markup=InlineKeyboardMarkup( [[
               InlineKeyboardButton("π π²π»πΎππ΄", callback_data = "close"),
               InlineKeyboardButton("βοΈ π±π°π²πΊ", callback_data = "start")
               ]]
            )
        )
    elif data == "close":
        await query.message.delete()
        try:
            await query.message.reply_to_message.delete()
        except:
            pass





