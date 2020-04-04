from pyrogram import Client, Filters, Message


def check_func(_, message: Message):
    if Filters.forwarded(message):
        return False
    if Filters.command('help')(message):
        return True
    if Filters.command('start')(message):
        if len(message.command) == 1:
            return True
    if Filters.edited(message):
        return False


@Client.on_message(Filters.create(check_func))
def helpme(client: Client, message: Message):
    text = '使用方式：\n' \
        '更新或新增您的好友代碼\n' \
        '範例：`/add SW-XXXX-XXXX-XXXX-XXXX`\n' \
        '範例：`/addfc SW-XXXX-XXXX-XXXX-XXXX`\n\n' \
        '查詢別人的好友代碼\n' \
        '範例：`/findfc @username`\n\n' \
        '顯示自己的好友代碼\n' \
        '範例: `/myfc`\n' \
        '隱私設定，決定是否讓好友代碼被他人查詢' \
        '範例: `/findfc`\n' \
        '綁定特定遊戲，目前僅支援動物森友會' \
        '範例：`/bindgame`' \
        '此工具啟發自 @NintendoFCPool_bot 並加以延伸。'
    message.reply_text(text, parse_mode='markdown')
