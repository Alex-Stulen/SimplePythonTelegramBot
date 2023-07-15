from datetime import datetime

from telegram import Update

from conf import HISTORY_FILEPATH


def write_history_message(update: Update):
    """ Ця функція приймає апдейт хендлера і записує дані в історію.
        Історія зберігається в файлі.

        формат історії: f'{datetime.now()} | {update.effective_user.id} | {update.message.text}'
     """
    with open(HISTORY_FILEPATH, mode='a', encoding='utf-8') as file:
        history_message = f'{datetime.now()} | {update.effective_user.id} | {update.message.text}'
        file.write(history_message)


def get_history_messages():
    history = []
    with open(HISTORY_FILEPATH, mode='r', encoding='utf-8') as file:
        for line in file.readlines():
            history.append(line.strip())
    return history
