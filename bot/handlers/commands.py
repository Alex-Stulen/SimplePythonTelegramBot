from telegram import Update
from telegram.ext import CommandHandler, MessageHandler, CallbackQueryHandler, filters, ContextTypes

from conf import USERS_BANK
from bot.keyboards import home as kb_home
from bot.keyboards import help as kb_help
from utils.history import write_history_message, get_history_messages


async def cmd_start(update: Update, context):
    write_history_message(update)
    await update.message.reply_text('Привіт! Оберіть, що вас цікавить:', reply_markup=kb_home.get_home_menu_keyboard())


async def cmd_help(update: Update, context):
    write_history_message(update)
    await update.message.reply_text('This is help text!', reply_markup=kb_help.get_help_cmd_inline_keyboard())


async def show_cmd_help_event(update: Update, context):
    query = update.callback_query
    await query.edit_message_text('This is help text!', reply_markup=kb_help.get_help_cmd_inline_keyboard())


async def get_contacts_event(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    msg = 'Contacts:\n\n' \
          'Phones:\n' \
          '+380666666666\n' \
          '+380665555555\n\n' \
          'Email:\n' \
          'support@email.com'
    await query.edit_message_text(text=msg, reply_markup=kb_help.help_back_inline_keyboard())


async def cmd_get_history(update: Update, context):
    write_history_message(update)
    history = get_history_messages()
    for message in history:
        await update.message.reply_text(message)


async def cmd_income(update: Update, context):
    # /income 100
    _, number = update.message.text.split(' ')
    number = float(number)

    if update.effective_user.id not in USERS_BANK:
        USERS_BANK[update.effective_user.id] = 0

    user_bank_money = USERS_BANK.get(update.effective_user.id, 0)
    user_bank_money += number
    USERS_BANK[update.effective_user.id] = user_bank_money

    msg = f'Ваш рахунок: {user_bank_money}'
    await update.message.reply_text(msg)


def get_handlers():
    cmd_income_filter = filters.Regex(r'(^\/income\s)') & filters.Regex(r'\d+$')

    return [
        CommandHandler('start', cmd_start),

        CommandHandler('help', cmd_help),
        MessageHandler(filters.Text(['Допомога', ]), cmd_help),

        CommandHandler('history', cmd_get_history),

        MessageHandler(cmd_income_filter, cmd_income),

        CallbackQueryHandler(callback=get_contacts_event, pattern='contacts_event'),
        CallbackQueryHandler(callback=show_cmd_help_event, pattern='show_help_msg_event')
    ]
