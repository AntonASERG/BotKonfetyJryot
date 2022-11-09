#Здесь создается бот и хранится его токен

from aiogram import Bot
from aiogram.dispatcher import Dispatcher


bot = Bot(token='5735127732:AAGEuHFlP8hJnDazCfiPTvjKmLuZtG4sGBk')
# программа - слушаетель - ждет сообщения и принимает
dp = Dispatcher(bot)