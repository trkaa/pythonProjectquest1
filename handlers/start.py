from loader import dp, db
from aiogram.types import Message
from photo import photo1
from keyboards import kb_intro_inline
from .geo_handler import rite_user_state

@dp.message_handler(commands=['start'])
async def mes_start(message: Message):
    print('start')
    user_id = message.from_user.id
    user_tuple = (message.from_user.id, message.from_user.full_name)
    user_name = str(f'{message.from_user.first_name}')
    caption1 = str(f'Анастасия:\n'
                   f'Привет, {message.from_user.first_name}. Меня зовут Анастасия, можно Настенька))) '
                   'Меня интерсуют разные интересные места и происшествия.'
                   'Я узнала, что около коломны живёт человек, который видел призрака.'
                   ' Хочу узнать про это подробней. Может быть тоже увидеть приведение)))'
                   'Если тебе интересно, присоединяйся.')
    if db.user_exist(user_id) is None:
        db.new_user(user_tuple)
    await dp.bot.send_photo(message.from_user.id, photo=photo1, caption=caption1, reply_markup=kb_intro_inline)
    current_state = str(1)
    rite_user_state(current_state, message)
    # await dp.bot.send_photo(message.from_user.id, photo=photo1, caption=caption1, reply_markup=kb_geo)
