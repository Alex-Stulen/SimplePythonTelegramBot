from telegram import Update
from telegram.ext import MessageHandler, filters

from utils.history import write_history_message


async def process_unknown_message_type(update: Update, context):
    write_history_message(update)
    await update.message.reply_text('Можна відправляти тільки текст!')


async def process_unknown_message(update: Update, context):
    write_history_message(update)
    await update.message.reply_text('Вибач, я тебе не розумію :(')


def get_handlers():
    return [
        MessageHandler(~ filters.TEXT, process_unknown_message_type),
        MessageHandler(filters.ALL, process_unknown_message)
    ]
