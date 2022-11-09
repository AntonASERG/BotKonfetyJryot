#здесь главный файл для запуска

from aiogram.utils import executor

import handlers
from bot import dp

#  ас метод - в консоль сообщение, (_)!
async def on_startup(_):
    print('Бот запущен')

# /команда - выполняет после приема диспетчером
handlers.registred_handlers(dp)

# бот запущен (дП -прослушка, скип апдейтс - в спячке  сообщения не принимает, фунция он стартап)
executor.start_polling(dp, skip_updates=True, on_startup=on_startup)