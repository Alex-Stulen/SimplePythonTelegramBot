from telegram import InlineKeyboardMarkup, InlineKeyboardButton


def get_help_cmd_inline_keyboard():
    inline_kb_buttons = [
        [InlineKeyboardButton(text='Контакти', callback_data='contacts_event'), ],
    ]
    return InlineKeyboardMarkup(inline_kb_buttons)


def help_back_inline_keyboard():
    inline_kb_button = [
        [InlineKeyboardButton(text='« Назад', callback_data='show_help_msg_event'), ],
    ]
    return InlineKeyboardMarkup(inline_kb_button)
