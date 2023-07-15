from . import client, commands, utils


def get_all_handlers():
    return client.get_handlers() + commands.get_handlers() + utils.get_handlers()
