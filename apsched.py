from loader import db
from aiogram import Dispatcher
from texts import intro_2
from keyboards import kb_geo
from photo import photo2


async def send_message_time(dp: Dispatcher):
    users = db.get_users()
    for i in users:
        i = str(i)
        i = i.replace(',', '')
        i = i.replace('(', '')
        i = i.replace(')', '')
        await dp.bot.send_photo(i, photo=photo2, caption=intro_2, reply_markup=kb_geo)
        await dp.bot.send_location(i, latitude=55.007479, longitude=38.785832)
