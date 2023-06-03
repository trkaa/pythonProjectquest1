from aiogram import Bot, Dispatcher
import os
from data_base import DataBase
from aiogram.contrib.fsm_storage.memory import MemoryStorage

memory = MemoryStorage()



bot = Bot(os.getenv('TOKEN'))
dp = Dispatcher(bot, storage=memory)
db = DataBase()
