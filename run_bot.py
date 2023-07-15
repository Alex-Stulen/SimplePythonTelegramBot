from telegram.ext import Application

from conf import BOT_TOKEN
from bot.handlers import get_all_handlers


def main():
    """ Запускаємо бота """

    application_builder = Application.builder()
    application_token = application_builder.token(BOT_TOKEN)
    application = application_token.build()

    for handler in get_all_handlers():
        application.add_handler(handler)

    application.run_polling()


if __name__ == '__main__':
    main()
