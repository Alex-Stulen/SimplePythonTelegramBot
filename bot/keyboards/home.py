from telegram import ReplyKeyboardMarkup, KeyboardButton, WebAppInfo


def get_home_menu_keyboard():
    keyboard_buttons = [
        [KeyboardButton('Поповнити рахунок'), KeyboardButton(text='Допомога'), ],
    ]
    return ReplyKeyboardMarkup(keyboard_buttons, resize_keyboard=True)


def get_back_home_menu_keyboard():
    keyboard_buttons = [
        [KeyboardButton('Головне меню'), ],
    ]
    return ReplyKeyboardMarkup(keyboard_buttons, resize_keyboard=True)
