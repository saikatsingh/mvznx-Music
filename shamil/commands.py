
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram import Client, filters



HOME_TEXT = "<b>Helo, [{}](tg://user?id={})\n\nā¢ Iam A Bot Project ny MoviZenX\nā¢ I Can Manage Group VC's\n\nā¢ Hit /help to know about available commands.</b>"
HELP = """

<b>š¤ Read The Below Commands š¤</b>

**Common Commands**:

**/p**  Reply to an audio file or YouTube link to play it or use /p <song name>.
**/d** Play music from Deezer, Use /d <song name>
**/c**  Show current playing song.
**/help** Show help for commands
**/q** Shows the playlist.

**Admin Commands**:
**/sk** [n] ...  Skip current or n where n >= 2
**/j**  Join voice chat.
**/l**  Leave current voice chat
**/mzx**  Check which VC is joined.
**/sp**  Stop playing.
**/r** Start Radio.
**/sr** Stops Radio Stream.
**/rp**  Play from the beginning.
**/cl** Remove unused RAW PCM files.
**/ps** Pause playing.
**/rs** Resume playing.
**/m**  Mute in VC.
**/um**  Unmute in VC.
**/update** Updates the Bot.
"""



@Client.on_message(filters.command('start'))
async def start(client, message):
    buttons = [
        [
        InlineKeyboardButton('š­ Developer š­ļø', url='https://t.me/AnnihilusOP'),
                ],[
                InlineKeyboardButton('š¤ Updates', url='https://t.me/movizenx'),
                InlineKeyboardButton('šļø Movies', url='https://t.me/movizenix'),
                InlineKeyboardButton('š» Songs', url='https://t.me/MZX_SUPPORT'),
               ],[
                InlineKeyboardButton('š Developer š', url='https://t.me/AnnihilusOP'),
    ]
    ]
    reply_markup = InlineKeyboardMarkup(buttons)
    await message.reply(HOME_TEXT.format(message.from_user.first_name, message.from_user.id), reply_markup=reply_markup)



@Client.on_message(filters.command("help"))
async def show_help(client, message):
    buttons = [
        [
            InlineKeyboardButton('š­ Developer š­ļø', url='https://t.me/AnnihilusOP'),
                ],[
                InlineKeyboardButton('š¤ Updates', url='https://t.me/movizenx'),
                InlineKeyboardButton('šļø Movies', url='https://t.me/movizenix'),
                InlineKeyboardButton('š» Songs', url='https://t.me/mzx_support'),
               ],[
                InlineKeyboardButton('š Creator š', url='https://t.me/AnnihilusOP'),
        ]
    ]
    reply_markup = InlineKeyboardMarkup(buttons)
    await message.reply_text(
        HELP,
        reply_markup=reply_markup
        )
