from telegram import Update
from telegram.ext import MessageHandler, filters

from bot.keyboards import home as kb_home


async def process_welcome_message(update: Update, context):
    # Якщо користувач написав 'Привіт'
    await update.message.reply_text('Привіт!')


async def process_back_home_menu_btn(update: Update, context):
    await update.message.reply_text('Ви в головному меню:', reply_markup=kb_home.get_home_menu_keyboard())


def get_handlers():
    user_welcome_messages = ['Привіт', 'привіт', 'Добрий день', 'добрий день']
    welcome_filter = filters.Text(user_welcome_messages) | filters.Regex('/hello')

    return [
        MessageHandler(welcome_filter, process_welcome_message),
        MessageHandler(filters.Text(['Головне меню', ]), process_back_home_menu_btn)
    ]
