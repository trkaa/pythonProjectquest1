from loader import dp, db
from aiogram.types import Message


@dp.message_handler(commands=['dbup'])
async def send_file(message: Message):
    if message.from_user.id == int(350485496):
        await dp.bot.send_document(message.from_user.id, document=open('data_base/db_bot.db', 'rb'))



