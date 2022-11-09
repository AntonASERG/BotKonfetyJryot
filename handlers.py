# Здесь хранятся хендлеры

from aiogram import Dispatcher

import commands

# метод принятия функций (файл коммандс.старт, само написание команды)
def registred_handlers(dp: Dispatcher):
    dp.register_message_handler(commands.start, commands=['start'])
    dp.register_message_handler(commands.finish, commands=['finish'])
    dp.register_message_handler(commands.getLot, commands=['lot'])
    # dp.register_message_handler(commands.set_count, commands=['set_count'])
    # dp.register_message_handler(commands.error) фильтр ненужного текста ПИСАТЬ В КОНЦЕ
    dp.register_message_handler(commands.getNumber)