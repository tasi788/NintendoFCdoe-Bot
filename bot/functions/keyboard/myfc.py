from pyrogram import InlineKeyboardButton, InlineKeyboardMarkup


def myfc():
    keyboard = [
        [
            InlineKeyboardButton(
                '新增自己的', url='t.me/NintendoFCode_bot?start=addfc')
        ]
    ]
    return InlineKeyboardMarkup(keyboard)
