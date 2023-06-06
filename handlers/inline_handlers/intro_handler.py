from aiogram.types import CallbackQuery
from loader import dp, db
from keyboards import intro_data, kb_intro_inline, kb_geo
from asyncio import sleep
import datetime
from texts import text1_1, answer1_1, text1_2, answer1_2, text1_3, answer1_3, text1_4, answer1_4, text_rbank, \
    text_lbank, plotina_1_2, text_ilyas, plotina_5, bebeh_user1, bebeh_user2, bebeh2, upond, ucrypt, crypt2
from photo import photo1, photo9, photo13, photo18, map, photo29
from main import d1
from texts import intro_2
from photo import photo2


def rite_user_state_callback(current_state: str, callback: CallbackQuery):
    chat_id = callback.message.chat.id
    current_state = (current_state, chat_id)
    db.user_state(current_state)


@dp.callback_query_handler(intro_data.filter(part='1'))
async def print_cb(callback: CallbackQuery):
    user_name = str(f'{callback.from_user.first_name}:\n')
    # print(callback.data)
    chat_id = callback.message.chat.id
    # mess_id = callback.message.message_id
    # print(callback.data.split(':')[3])
    if callback.data.split(':')[3] == 'Когда?':
        new_text = user_name + text1_1
        await dp.bot.send_message(chat_id=chat_id, text=new_text)
        await sleep(3)
        await dp.bot.send_photo(chat_id=chat_id, photo=photo1, caption=answer1_1, reply_markup=kb_intro_inline)
    if callback.data.split(':')[3] == '1_2':
        new_text = user_name + text1_2
        await dp.bot.send_message(chat_id=chat_id, text=new_text)
        await sleep(3)
        await dp.bot.send_photo(chat_id=chat_id, photo=map, caption=answer1_2, reply_markup=kb_intro_inline)
    if callback.data.split(':')[3] == '1_3':
        new_text = user_name + text1_3
        await dp.bot.send_message(chat_id=chat_id, text=new_text)
        await sleep(3)
        await dp.bot.send_photo(chat_id=chat_id, photo=photo1, caption=answer1_3, reply_markup=kb_intro_inline)
    if callback.data.split(':')[3] == '1_4':
        new_text = user_name + text1_4
        await dp.bot.send_message(chat_id=chat_id, text=new_text)
        await sleep(3)
        await dp.bot.send_photo(chat_id=chat_id, photo=photo1, caption=answer1_4, reply_markup=kb_intro_inline)
        if d1 < datetime.datetime.now():
            await dp.bot.send_photo(chat_id=chat_id, photo=photo2, caption=intro_2, reply_markup=kb_geo)
            await dp.bot.send_location(chat_id=chat_id, latitude=55.007479, longitude=38.785832)


@dp.callback_query_handler(intro_data.filter(part='2'))
async def print_cb(callback: CallbackQuery):
    s = int(db.load_state(callback.message.chat.id)[0])
    user_name = str(f'{callback.from_user.first_name}:\n')
    # print(callback.data)
    chat_id = callback.message.chat.id
    # mess_id = callback.message.message_id
    # print(callback.data.split(':')[3])
    if callback.data.split(':')[3] == 'rbank':
        if s == 6:
            new_text = user_name + text_rbank
            await dp.bot.send_message(chat_id=chat_id, text=new_text)
            await sleep(3)
            await dp.bot.send_photo(chat_id=chat_id, photo=photo9, caption=plotina_1_2, reply_markup=kb_geo)
            await dp.bot.send_location(callback.message.chat.id, latitude=54.969488, longitude=38.859917)

    if callback.data.split(':')[3] == 'lbank':
        if s == 6:
            new_text = user_name + text_lbank
            await dp.bot.send_message(chat_id=chat_id, text=new_text)
            await sleep(3)
            await dp.bot.send_photo(chat_id=chat_id, photo=photo9, caption=plotina_1_2, reply_markup=kb_geo)
            await dp.bot.send_location(callback.message.chat.id, latitude=54.968066, longitude=38.858904)
            current_state = str(7)
            rite_user_state_callback(current_state, callback)


@dp.callback_query_handler(intro_data.filter(part='3'))
async def print_cb(callback: CallbackQuery):
    s = int(db.load_state(callback.message.chat.id)[0])
    user_name = str(f'{callback.from_user.first_name}:\n')
    # print(callback.data)
    chat_id = callback.message.chat.id
    # mess_id = callback.message.message_id
    # print(callback.data.split(':')[3])
    if callback.data.split(':')[3] == 'ilyas':
        if s == 8:
            new_text = user_name + text_ilyas
            await dp.bot.send_message(chat_id=chat_id, text=new_text)
            await sleep(3)
            await dp.bot.send_photo(chat_id=chat_id, photo=photo13, caption=plotina_5, reply_markup=kb_geo)
            await dp.bot.send_location(callback.message.chat.id, latitude=54.92484, longitude=38.78211)

        # await gs.state7.set()


@dp.callback_query_handler(intro_data.filter(part='4'))
async def print_cb(callback: CallbackQuery):
    s = int(db.load_state(callback.message.chat.id)[0])
    user_name = str(f'{callback.from_user.first_name}:\n')
    # print(callback.data)
    chat_id = callback.message.chat.id
    # mess_id = callback.message.message_id
    # print(callback.data.split(':')[3])
    if callback.data.split(':')[3] == 'bebeh1':
        if s == 10:
            new_text = user_name + bebeh_user1
            await dp.bot.send_message(chat_id=chat_id, text=new_text)
            await sleep(3)
            await dp.bot.send_photo(chat_id=chat_id, photo=photo18, caption=bebeh2, reply_markup=kb_geo)
            await dp.bot.send_location(callback.message.chat.id, latitude=54.905107, longitude=38.764074)
            current_state = str(11)
            rite_user_state_callback(current_state, callback)
        # await gs.state10.set()
    if callback.data.split(':')[3] == 'bebeh2':
        if s == 10:
            new_text = user_name + bebeh_user2
            await dp.bot.send_message(chat_id=chat_id, text=new_text)
            await sleep(3)
            await dp.bot.send_photo(chat_id=chat_id, photo=photo18, caption=bebeh2, reply_markup=kb_geo)
            await dp.bot.send_location(callback.message.chat.id, latitude=54.905107, longitude=38.764074)
            current_state = str(11)
            rite_user_state_callback(current_state, callback)

        # await gs.state10.set()


@dp.callback_query_handler(intro_data.filter(part='5'))
async def print_cb(callback: CallbackQuery):
    s = int(db.load_state(callback.message.chat.id)[0])
    user_name = str(f'{callback.from_user.first_name}:\n')
    # print(callback.data)
    chat_id = callback.message.chat.id
    # mess_id = callback.message.message_id
    # print(callback.data.split(':')[3])
    if callback.data.split(':')[3] == 'pond':
        if s == 12:
            new_text = user_name + upond
            await dp.bot.send_message(chat_id=chat_id, text=new_text, reply_markup=kb_geo)
            await dp.bot.send_location(callback.message.chat.id, latitude=54.863801, longitude=38.755919)
            current_state = str(13)
            rite_user_state_callback(current_state, callback)
            # await gs.state12.set()


@dp.callback_query_handler(intro_data.filter(part='6'))
async def print_cb(callback: CallbackQuery):
    s = int(db.load_state(callback.message.chat.id)[0])
    user_name = str(f'{callback.from_user.first_name}:\n')
    # print(callback.data)
    chat_id = callback.message.chat.id
    # mess_id = callback.message.message_id
    # print(callback.data.split(':')[3])
    if callback.data.split(':')[3] == 'crypt':
        if s == 16:
            new_text = user_name + ucrypt
            await dp.bot.send_message(chat_id=chat_id, text=new_text)
            await sleep(5)
            await dp.bot.send_photo(chat_id=chat_id, photo=photo29, caption=crypt2)
            # current_state = str(16)
            # rite_user_state_callback(current_state, callback)
            # await gs.state15.set()
