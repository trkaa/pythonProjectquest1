from loader import dp, db
from aiogram.types import Message
from geopy.distance import geodesic
from asyncio import sleep
from decimal import Decimal
from datetime import datetime
from geo_points import point_1, point_2, point_3, point_4, point_5, point_6, point_7, point_8, point_9, point_10, \
    point_11, point_12, point_13, point_14, point_15
from texts import u_lesnika_1, l_text_1, u_lesnika_2, u_lesnika_3, u_lesnika_4, u_lesnika_5, u_lesnika_6, l_text_2, \
    l_text_3, l_text_4, l_text_5, lesnik, u_lesnika_5_1, u_lesnika_7, u_lesnika_8, u_lesnika_9, l_text_6, l_text_7, \
    plotina_1, plotina_2, plotina_3, plotina_4, plotina_1_1, plotina_2_1, sergeyt, ilyas_1, \
    ilyas_2, ilyas_3, ilyas_4, ilyas_5, ilyas_6, ryb_ilyas_1, ryb_ilyas_2, ryb_ilyas_3, ryb_ilyas_4, ryb_home1, \
    ryb_home2, ryb_dom, bebeh1, bebeh1_1, beach1, beach2, beach3, beach4, beach5, \
    beach6, vasyat1, vasyat2, vasyat3, vasyat4, vasyat5, vasyat6, pond, npond1, npond2, npond3, fligel1, \
    fligel2, fligel3, fligel4, fligel5, fligel6, crypt1, watchman1_1, watchman1_2, watchman1_3, watchman2_1, \
    watchman2_2, watchman2_3, watchman2_4, watchman2_5, watchman2_6, crypt1_1, pond_1
from photo import lesnik, lesnik2, lesnik3, lesnik4, photo3, photo4, photo5, photo6, photo7, photo8, photo9, \
    photo10, photo11, photo12, photo14, photo15, photo16, photo17, photo19, photo20, photo21, sergey, rybar1, rybar2, \
    vasya, watchman, watchman2, watchman3, photo22, photo23, watchman4, watchman5, watchman6, photo24, photo25, \
    photo26, photo27, photo28
from aiogram.types import ReplyKeyboardRemove
from keyboards import kb_geo, kb_bank_inline, kb_ilyas_inline, kb_bebeh, kb_crypt_inline, kb_pond_inline


def get_distance(gpoint: dict, message: Message):
    i = message
    i = i['location']
    latitude1 = Decimal(i['latitude'])
    latitude1 = latitude1.quantize(Decimal('1.000000'))
    longitude1 = Decimal(i['longitude'])
    longitude1 = longitude1.quantize(Decimal('1.000000'))
    latitude2 = Decimal(gpoint['latitude'])
    latitude2 = latitude2.quantize(Decimal('1.000000'))
    longitude2 = Decimal(gpoint['longitude'])
    longitude2 = longitude2.quantize(Decimal('1.000000'))
    point_1_tuple = (latitude1, longitude1)
    user_point_tuple = (latitude2, longitude2)
    distance = geodesic(point_1_tuple, user_point_tuple).m
    return distance


def point_time(point: str, message: Message):
    time = str(datetime.now())
    user_id = message.from_user.id
    user_time = (time, user_id)
    point = str(point)
    db.point_time(point, user_time)


def rite_user_state(current_state: str, message: Message):
    user_id = message.from_user.id
    current_state = (current_state, user_id)
    db.user_state(current_state)


@dp.message_handler(content_types='location')
async def get_geo(message: Message):
    print(message['location'])
    s = int(db.load_state(message.from_user.id)[0])
    print(s)
    if s == 1:
        distance = get_distance(point_1, message)
        if distance < float(10.0):
            current_state = str(2)
            rite_user_state(current_state, message)
            point_time('intro_checkpoint', message)
            await dp.bot.send_photo(message.from_user.id, photo=photo3, caption=u_lesnika_1
                                    , reply_markup=ReplyKeyboardRemove())
            await sleep(5)
            await dp.bot.send_photo(message.from_user.id, photo=lesnik, caption=l_text_1)
            await sleep(5)
            await dp.bot.send_photo(message.from_user.id, photo=photo3, caption=u_lesnika_2)
            await sleep(5)
            await dp.bot.send_photo(message.from_user.id, photo=lesnik, caption=l_text_2)
            await sleep(5)
            await dp.bot.send_photo(message.from_user.id, photo=photo3, caption=u_lesnika_3)
            await sleep(5)
            await dp.bot.send_photo(message.from_user.id, photo=lesnik, caption=l_text_3)
            await sleep(5)
            await dp.bot.send_photo(message.from_user.id, photo=photo3, caption=u_lesnika_4)
            await sleep(5)
            await dp.bot.send_photo(message.from_user.id, photo=lesnik2, caption=l_text_4)
            await sleep(5)
            await dp.bot.send_photo(message.from_user.id, photo=photo4, caption=u_lesnika_5, reply_markup=kb_geo)
            await dp.bot.send_location(message.from_user.id, latitude=55.00221, longitude=38.80401)

        else:
            distance = format(distance, '.2f')
            await dp.bot.send_message(message.from_user.id, text=f'До точки {distance} метров.')

    if s == 2:
        distance = get_distance(point_2, message)
        if distance < 10:
            current_state = str(3)
            rite_user_state(current_state, message)
            point_time('point1', message)
            await dp.bot.send_photo(message.from_user.id, photo=photo3, caption=u_lesnika_5_1,
                                    reply_markup=ReplyKeyboardRemove())

            await sleep(5)
            await dp.bot.send_photo(message.from_user.id, photo=photo5, caption=u_lesnika_6, reply_markup=kb_geo)
            await dp.bot.send_location(message.from_user.id, latitude=55.01629, longitude=38.76638)

        else:
            distance = format(distance, '.2f')
            await dp.bot.send_message(message.from_user.id, text=f'До точки {distance} метров.')

    if s == 3:
        distance = get_distance(point_3, message)
        if distance < 10:
            current_state = str(4)
            rite_user_state(current_state, message)
            point_time('point2', message)
            await dp.bot.send_photo(message.from_user.id, photo=lesnik3, caption=l_text_5
                                    , reply_markup=ReplyKeyboardRemove())
            await sleep(5)
            await dp.bot.send_photo(message.from_user.id, photo=photo6, caption=u_lesnika_7, reply_markup=kb_geo)
            await dp.bot.send_location(message.from_user.id, latitude=55.00866, longitude=38.76090)

            # await GeoState.state3.set()
        else:
            distance = format(distance, '.2f')
            await dp.bot.send_message(message.from_user.id, text=f'До точки {distance} метров.')

    if s == 4:
        distance = get_distance(point_4, message)
        if distance < 10:
            current_state = str(5)
            rite_user_state(current_state, message)
            point_time('point3', message)
            await dp.bot.send_photo(message.from_user.id, photo=photo7, caption=u_lesnika_8
                                    , reply_markup=ReplyKeyboardRemove())
            await sleep(5)
            await dp.bot.send_photo(message.from_user.id, photo=lesnik, caption=l_text_6)
            await sleep(5)
            await dp.bot.send_photo(message.from_user.id, photo=photo8, caption=u_lesnika_9)
            await sleep(5)
            await dp.bot.send_photo(message.from_user.id, photo=lesnik4, caption=l_text_7, reply_markup=kb_geo)
            await dp.bot.send_location(message.from_user.id, latitude=54.968730, longitude=38.859713)

            # await GeoState.state4.set()
        else:
            distance = format(distance, '.2f')
            await dp.bot.send_message(message.from_user.id, text=f'До точки {distance} метров.')

    if s == 5:
        distance = get_distance(point_5, message)
        if distance < 20:
            current_state = str(6)
            rite_user_state(current_state, message)
            point_time('point4', message)
            await dp.bot.send_photo(message.from_user.id, photo=photo9, caption=plotina_1,
                                    reply_markup=ReplyKeyboardRemove())
            await sleep(5)
            await dp.bot.send_photo(message.from_user.id, photo=photo9, caption=plotina_1_1,
                                    reply_markup=kb_bank_inline)
        else:
            distance = format(distance, '.2f')
            await dp.bot.send_message(message.from_user.id, text=f'До точки {distance} метров.')

    if s == 6:
        distance = get_distance(point_6, message)
        if distance < 10:

            point_time('point5', message)
            await dp.bot.send_photo(message.from_user.id, photo=photo10, caption=plotina_2,
                                    reply_markup=ReplyKeyboardRemove())
            await sleep(5)
            await dp.bot.send_photo(message.from_user.id, photo=photo10, caption=plotina_2_1,
                                    reply_markup=kb_geo)
            await dp.bot.send_location(message.from_user.id, latitude=54.968066, longitude=38.858904)
            current_state = str(7)
            rite_user_state(current_state, message)

        else:
            distance = format(distance, '.2f')
            await dp.bot.send_message(message.from_user.id, text=f'До точки {distance} метров.')

    if s == 7:
        distance = get_distance(point_7, message)
        if distance < 10:
            current_state = str(8)
            rite_user_state(current_state, message)
            point_time('point6', message)
            await dp.bot.send_photo(message.from_user.id, photo=photo11, caption=plotina_3,
                                    reply_markup=ReplyKeyboardRemove())
            await sleep(5)
            await dp.bot.send_photo(message.from_user.id, photo=sergey, caption=sergeyt)
            await sleep(5)
            await dp.bot.send_photo(message.from_user.id, photo=photo12, caption=plotina_4,
                                    reply_markup=kb_ilyas_inline)
        else:
            distance = format(distance, '.2f')
            await dp.bot.send_message(message.from_user.id, text=f'До точки {distance} метров.')

    if s == 8:
        distance = get_distance(point_8, message)
        if distance < 10:
            current_state = str(9)
            rite_user_state(current_state, message)
            point_time('point7', message)
            await dp.bot.send_photo(message.from_user.id, photo=photo14, caption=ilyas_1,
                                    reply_markup=ReplyKeyboardRemove())
            await sleep(5)
            await dp.bot.send_photo(message.from_user.id, photo=photo15, caption=ilyas_2)
            await sleep(5)
            await dp.bot.send_photo(message.from_user.id, photo=rybar1, caption=ryb_ilyas_1)
            await sleep(5)
            await dp.bot.send_photo(message.from_user.id, photo=photo15, caption=ilyas_3)
            await sleep(5)
            await dp.bot.send_photo(message.from_user.id, photo=rybar1, caption=ryb_ilyas_2)
            await sleep(5)
            await dp.bot.send_photo(message.from_user.id, photo=photo15, caption=ilyas_4)
            await sleep(5)
            await dp.bot.send_photo(message.from_user.id, photo=rybar1, caption=ryb_ilyas_3)
            await sleep(5)
            await dp.bot.send_photo(message.from_user.id, photo=photo15, caption=ilyas_5)
            await sleep(5)
            await dp.bot.send_photo(message.from_user.id, photo=rybar1, caption=ryb_ilyas_4)
            await sleep(5)
            await dp.bot.send_photo(message.from_user.id, photo=photo15, caption=ilyas_6, reply_markup=kb_geo)
            await dp.bot.send_location(message.from_user.id, latitude=54.91566, longitude=38.74770)

            # await GeoState.state8.set()
        else:
            distance = format(distance, '.2f')
            await dp.bot.send_message(message.from_user.id, text=f'До точки {distance} метров.')

    if s == 9:
        distance = get_distance(point_9, message)
        if distance < 10:
            current_state = str(10)
            rite_user_state(current_state, message)
            point_time('point8', message)
            await dp.bot.send_photo(message.from_user.id, photo=rybar2, caption=ryb_home1,
                                    reply_markup=ReplyKeyboardRemove())
            await sleep(5)
            await dp.bot.send_photo(message.from_user.id, photo=photo16, caption=ryb_dom)
            await sleep(5)
            await dp.bot.send_photo(message.from_user.id, photo=rybar2, caption=ryb_home2, reply_markup=kb_geo)
            await dp.bot.send_location(message.from_user.id, latitude=54.905529, longitude=38.763742)

        else:
            distance = format(distance, '.2f')
            await dp.bot.send_message(message.from_user.id, text=f'До точки {distance} метров.')

    if s == 10:
        distance = get_distance(point_10, message)
        if distance < 10:
            point_time('point9', message)
            await dp.bot.send_photo(message.from_user.id, photo=photo17, caption=bebeh1,
                                    reply_markup=ReplyKeyboardRemove())
            await sleep(5)
            await dp.bot.send_photo(message.from_user.id, photo=photo17, caption=bebeh1_1, reply_markup=kb_bebeh)
        else:
            distance = format(distance, '.2f')
            await dp.bot.send_message(message.from_user.id, text=f'До точки {distance} метров.')

    if s == 11:
        distance = get_distance(point_11, message)
        if distance < 10:
            current_state = str(12)
            rite_user_state(current_state, message)
            point_time('point10', message)
            await dp.bot.send_photo(message.from_user.id, photo=photo19, caption=beach1,
                                    reply_markup=ReplyKeyboardRemove())
            await sleep(5)
            await dp.bot.send_photo(message.from_user.id, photo=vasya, caption=vasyat1)
            await sleep(5)
            await dp.bot.send_photo(message.from_user.id, photo=photo19, caption=beach2)
            await sleep(5)
            await dp.bot.send_photo(message.from_user.id, photo=vasya, caption=vasyat2)
            await sleep(5)
            await dp.bot.send_photo(message.from_user.id, photo=photo19, caption=beach3)
            await sleep(5)
            await dp.bot.send_photo(message.from_user.id, photo=vasya, caption=vasyat3)
            await sleep(15)
            await dp.bot.send_photo(message.from_user.id, photo=photo19, caption=beach4)
            await sleep(5)
            await dp.bot.send_photo(message.from_user.id, photo=vasya, caption=vasyat4)
            await sleep(15)
            await dp.bot.send_photo(message.from_user.id, photo=photo19, caption=beach5)
            await sleep(5)
            await dp.bot.send_photo(message.from_user.id, photo=vasya, caption=vasyat5)
            await sleep(5)
            await dp.bot.send_photo(message.from_user.id, photo=photo19, caption=beach6)
            await sleep(5)
            await dp.bot.send_photo(message.from_user.id, photo=vasya, caption=vasyat6, reply_markup=kb_geo)
            await dp.bot.send_location(message.from_user.id, latitude=54.864313, longitude=38.754465)

        else:
            distance = format(distance, '.2f')
            await dp.bot.send_message(message.from_user.id, text=f'До точки {distance} метров.')

    if s == 12:
        distance = get_distance(point_12, message)
        if distance < 20:
            point_time('point11', message)
            await dp.bot.send_photo(message.from_user.id, photo=photo20, caption=pond,
                                    reply_markup=ReplyKeyboardRemove())
            await sleep(5)
            await dp.bot.send_photo(message.from_user.id, photo=photo21, caption=pond_1, reply_markup=kb_pond_inline)

        else:
            distance = format(distance, '.2f')
            await dp.bot.send_message(message.from_user.id, text=f'До точки {distance} метров.')

    if s == 13:
        distance = get_distance(point_13, message)
        if distance < 10:
            current_state = str(14)
            rite_user_state(current_state, message)
            point_time('point12', message)
            await dp.bot.send_photo(message.from_user.id, photo=photo22, caption=npond1,
                                    reply_markup=ReplyKeyboardRemove())
            await sleep(5)
            await dp.bot.send_photo(message.from_user.id, photo=watchman, caption=watchman1_1)
            await sleep(5)
            await dp.bot.send_photo(message.from_user.id, photo=photo22, caption=npond2)
            await sleep(5)
            await dp.bot.send_photo(message.from_user.id, photo=watchman2, caption=watchman1_2)
            await sleep(5)
            await dp.bot.send_photo(message.from_user.id, photo=photo23, caption=npond3)
            await sleep(5)
            await dp.bot.send_photo(message.from_user.id, photo=watchman3, caption=watchman1_3, reply_markup=kb_geo)
            await dp.bot.send_location(message.from_user.id, latitude=54.863131, longitude=38.756904)

            # await GeoState.state13.set()
        else:
            distance = format(distance, '.2f')
            await dp.bot.send_message(message.from_user.id, text=f'До точки {distance} метров.')

    if s == 14:
        distance = get_distance(point_14, message)
        if distance < 10:
            current_state = str(15)
            rite_user_state(current_state, message)
            point_time('point13', message)
            await dp.bot.send_photo(message.from_user.id, photo=photo24, caption=fligel1,
                                    reply_markup=ReplyKeyboardRemove())
            await sleep(5)
            await dp.bot.send_photo(message.from_user.id, photo=watchman4, caption=watchman2_1)
            await sleep(5)
            await dp.bot.send_photo(message.from_user.id, photo=photo25, caption=fligel2)
            await sleep(5)
            await dp.bot.send_photo(message.from_user.id, photo=watchman5, caption=watchman2_2)
            await sleep(5)
            await dp.bot.send_photo(message.from_user.id, photo=photo26, caption=fligel3)
            await sleep(5)
            await dp.bot.send_photo(message.from_user.id, photo=watchman6, caption=watchman2_3)
            await sleep(5)
            await dp.bot.send_photo(message.from_user.id, photo=photo24, caption=fligel4)
            await sleep(5)
            await dp.bot.send_photo(message.from_user.id, photo=watchman5, caption=watchman2_4)
            await sleep(5)
            await dp.bot.send_photo(message.from_user.id, photo=photo25, caption=fligel5)
            await sleep(5)
            await dp.bot.send_photo(message.from_user.id, photo=watchman4, caption=watchman2_5)
            await sleep(5)
            await dp.bot.send_photo(message.from_user.id, photo=photo26, caption=fligel6)
            await sleep(5)
            await dp.bot.send_photo(message.from_user.id, photo=watchman6, caption=watchman2_6, reply_markup=kb_geo)
            await dp.bot.send_location(message.from_user.id, latitude=54.86484, longitude=38.75847)
            # await GeoState.state14.set()
        else:
            distance = format(distance, '.2f')
            await dp.bot.send_message(message.from_user.id, text=f'До точки {distance} метров.')

    if s == 15:
        distance = get_distance(point_15, message)
        if distance < 10:
            current_state = str(16)
            rite_user_state(current_state, message)
            point_time('point14', message)
            await dp.bot.send_photo(message.from_user.id, photo=photo27, caption=crypt1,
                                    reply_markup=ReplyKeyboardRemove())
            await sleep(5)
            await dp.bot.send_photo(message.from_user.id, photo=photo28, caption=crypt1_1,
                                    reply_markup=kb_crypt_inline)

        else:
            distance = format(distance, '.2f')
            await dp.bot.send_message(message.from_user.id, text=f'До точки {distance} метров.')


@dp.message_handler(commands=['up'])
async def load_game(message: Message):
    s = int(db.load_state(message.from_user.id)[0])

    if s == 2:
        await dp.bot.send_photo(message.from_user.id, photo=photo3, caption=u_lesnika_1
                                , reply_markup=ReplyKeyboardRemove())
        await sleep(5)
        await dp.bot.send_photo(message.from_user.id, photo=lesnik, caption=l_text_1)
        await sleep(5)
        await dp.bot.send_photo(message.from_user.id, photo=photo3, caption=u_lesnika_2)
        await sleep(5)
        await dp.bot.send_photo(message.from_user.id, photo=lesnik, caption=l_text_2)
        await sleep(5)
        await dp.bot.send_photo(message.from_user.id, photo=photo3, caption=u_lesnika_3)
        await sleep(5)
        await dp.bot.send_photo(message.from_user.id, photo=lesnik, caption=l_text_3)
        await sleep(5)
        await dp.bot.send_photo(message.from_user.id, photo=photo3, caption=u_lesnika_4)
        await sleep(5)
        await dp.bot.send_photo(message.from_user.id, photo=lesnik2, caption=l_text_4)
        await sleep(5)
        await dp.bot.send_photo(message.from_user.id, photo=photo4, caption=u_lesnika_5, reply_markup=kb_geo)
        await dp.bot.send_location(message.from_user.id, latitude=55.002253, longitude=38.803113)

    if s == 3:
        await dp.bot.send_photo(message.from_user.id, photo=photo3, caption=u_lesnika_5_1,
                                reply_markup=ReplyKeyboardRemove())

        await sleep(5)
        await dp.bot.send_photo(message.from_user.id, photo=photo5, caption=u_lesnika_6, reply_markup=kb_geo)
        await dp.bot.send_location(message.from_user.id, latitude=55.01629, longitude=38.76638)

    if s == 4:
        await dp.bot.send_photo(message.from_user.id, photo=lesnik3, caption=l_text_5
                                , reply_markup=ReplyKeyboardRemove())
        await sleep(5)
        await dp.bot.send_photo(message.from_user.id, photo=photo6, caption=u_lesnika_7, reply_markup=kb_geo)
        await dp.bot.send_location(message.from_user.id, latitude=55.00866, longitude=38.76090)

        # await GeoState.state3.set()

    if s == 5:
        await dp.bot.send_photo(message.from_user.id, photo=photo7, caption=u_lesnika_8
                                , reply_markup=ReplyKeyboardRemove())
        await sleep(5)
        await dp.bot.send_photo(message.from_user.id, photo=lesnik, caption=l_text_6)
        await sleep(5)
        await dp.bot.send_photo(message.from_user.id, photo=photo8, caption=u_lesnika_9)
        await sleep(5)
        await dp.bot.send_photo(message.from_user.id, photo=lesnik4, caption=l_text_7, reply_markup=kb_geo)
        await dp.bot.send_location(message.from_user.id, latitude=54.968730, longitude=38.859713)
        # await GeoState.state4.set()

    if s == 6:
        await dp.bot.send_photo(message.from_user.id, photo=photo9, caption=plotina_1,
                                reply_markup=ReplyKeyboardRemove())
        await sleep(5)
        await dp.bot.send_photo(message.from_user.id, photo=photo9, caption=plotina_1_1,
                                reply_markup=kb_bank_inline)

    # if s == 7:
    #     await dp.bot.send_photo(message.from_user.id, photo=photo1, caption=plotina_2,
    #                             reply_markup=ReplyKeyboardRemove())
    #     await sleep(5)
    #     await dp.bot.send_photo(message.from_user.id, photo=photo1, caption=plotina_2_1,
    #                             reply_markup=kb_geo)
    #     await dp.bot.send_location(message.from_user.id, latitude=54.968066, longitude=38.858904)

    # await GeoState.state6.set()

    if s == 8:
        await dp.bot.send_photo(message.from_user.id, photo=photo11, caption=plotina_3,
                                reply_markup=ReplyKeyboardRemove())
        await sleep(5)
        await dp.bot.send_photo(message.from_user.id, photo=sergey, caption=sergeyt)
        await sleep(5)
        await dp.bot.send_photo(message.from_user.id, photo=photo12, caption=plotina_4, reply_markup=kb_ilyas_inline)

    if s == 9:
        await dp.bot.send_photo(message.from_user.id, photo=photo14, caption=ilyas_1,
                                reply_markup=ReplyKeyboardRemove())
        await sleep(5)
        await dp.bot.send_photo(message.from_user.id, photo=photo15, caption=ilyas_2)
        await sleep(5)
        await dp.bot.send_photo(message.from_user.id, photo=rybar1, caption=ryb_ilyas_1)
        await sleep(5)
        await dp.bot.send_photo(message.from_user.id, photo=photo15, caption=ilyas_3)
        await sleep(5)
        await dp.bot.send_photo(message.from_user.id, photo=rybar1, caption=ryb_ilyas_2)
        await sleep(5)
        await dp.bot.send_photo(message.from_user.id, photo=photo15, caption=ilyas_4)
        await sleep(5)
        await dp.bot.send_photo(message.from_user.id, photo=rybar1, caption=ryb_ilyas_3)
        await sleep(5)
        await dp.bot.send_photo(message.from_user.id, photo=photo15, caption=ilyas_5)
        await sleep(5)
        await dp.bot.send_photo(message.from_user.id, photo=rybar1, caption=ryb_ilyas_4)
        await sleep(5)
        await dp.bot.send_photo(message.from_user.id, photo=photo15, caption=ilyas_6, reply_markup=kb_geo)
        await dp.bot.send_location(message.from_user.id, latitude=54.915379, longitude=38.747828)

        # await GeoState.state8.set()

    if s == 10:
        await dp.bot.send_photo(message.from_user.id, photo=rybar2, caption=ryb_home1,
                                reply_markup=ReplyKeyboardRemove())
        await sleep(5)
        await dp.bot.send_photo(message.from_user.id, photo=photo16, caption=ryb_dom)
        await sleep(5)
        await dp.bot.send_photo(message.from_user.id, photo=rybar2, caption=ryb_home2, reply_markup=kb_geo)
        await dp.bot.send_location(message.from_user.id, latitude=54.905529, longitude=38.763742)

        # await GeoState.state9.set()

    if s == 11:
        await dp.bot.send_photo(message.from_user.id, photo=photo17, caption=bebeh1,
                                reply_markup=ReplyKeyboardRemove())
        await sleep(5)
        await dp.bot.send_photo(message.from_user.id, photo=photo17, caption=bebeh1_1, reply_markup=kb_bebeh)

    if s == 12:
        await dp.bot.send_photo(message.from_user.id, photo=photo19, caption=beach1,
                                reply_markup=ReplyKeyboardRemove())
        await sleep(5)
        await dp.bot.send_photo(message.from_user.id, photo=vasya, caption=vasyat1)
        await sleep(5)
        await dp.bot.send_photo(message.from_user.id, photo=photo19, caption=beach2)
        await sleep(5)
        await dp.bot.send_photo(message.from_user.id, photo=vasya, caption=vasyat2)
        await sleep(5)
        await dp.bot.send_photo(message.from_user.id, photo=photo19, caption=beach3)
        await sleep(5)
        await dp.bot.send_photo(message.from_user.id, photo=vasya, caption=vasyat3)
        await sleep(15)
        await dp.bot.send_photo(message.from_user.id, photo=photo19, caption=beach4)
        await sleep(5)
        await dp.bot.send_photo(message.from_user.id, photo=vasya, caption=vasyat4)
        await sleep(15)
        await dp.bot.send_photo(message.from_user.id, photo=photo19, caption=beach5)
        await sleep(5)
        await dp.bot.send_photo(message.from_user.id, photo=vasya, caption=vasyat5)
        await sleep(5)
        await dp.bot.send_photo(message.from_user.id, photo=photo19, caption=beach6)
        await sleep(5)
        await dp.bot.send_photo(message.from_user.id, photo=vasya, caption=vasyat6, reply_markup=kb_geo)
        await dp.bot.send_location(message.from_user.id, latitude=54.864313, longitude=38.754465)

        # await GeoState.state11.set()

    if s == 13:
        await dp.bot.send_photo(message.from_user.id, photo=photo20, caption=pond,
                                reply_markup=ReplyKeyboardRemove())
        await sleep(5)
        await dp.bot.send_photo(message.from_user.id, photo=photo21, caption=pond_1, reply_markup=kb_pond_inline)

    if s == 14:
        await dp.bot.send_photo(message.from_user.id, photo=photo22, caption=npond1,
                                reply_markup=ReplyKeyboardRemove())
        await sleep(5)
        await dp.bot.send_photo(message.from_user.id, photo=watchman, caption=watchman1_1)
        await sleep(5)
        await dp.bot.send_photo(message.from_user.id, photo=photo22, caption=npond2)
        await sleep(5)
        await dp.bot.send_photo(message.from_user.id, photo=watchman2, caption=watchman1_2)
        await sleep(5)
        await dp.bot.send_photo(message.from_user.id, photo=photo23, caption=npond3)
        await sleep(5)
        await dp.bot.send_photo(message.from_user.id, photo=watchman3, caption=watchman1_3, reply_markup=kb_geo)
        await dp.bot.send_location(message.from_user.id, latitude=54.863131, longitude=38.756904)

        # await GeoState.state13.set()

    if s == 15:
        await dp.bot.send_photo(message.from_user.id, photo=photo24, caption=fligel1,
                                reply_markup=ReplyKeyboardRemove())
        await sleep(5)
        await dp.bot.send_photo(message.from_user.id, photo=watchman4, caption=watchman2_1)
        await sleep(5)
        await dp.bot.send_photo(message.from_user.id, photo=photo25, caption=fligel2)
        await sleep(5)
        await dp.bot.send_photo(message.from_user.id, photo=watchman5, caption=watchman2_2)
        await sleep(5)
        await dp.bot.send_photo(message.from_user.id, photo=photo26, caption=fligel3)
        await sleep(5)
        await dp.bot.send_photo(message.from_user.id, photo=watchman6, caption=watchman2_3)
        await sleep(5)
        await dp.bot.send_photo(message.from_user.id, photo=photo24, caption=fligel4)
        await sleep(5)
        await dp.bot.send_photo(message.from_user.id, photo=watchman5, caption=watchman2_4)
        await sleep(5)
        await dp.bot.send_photo(message.from_user.id, photo=photo25, caption=fligel5)
        await sleep(5)
        await dp.bot.send_photo(message.from_user.id, photo=watchman4, caption=watchman2_5)
        await sleep(5)
        await dp.bot.send_photo(message.from_user.id, photo=photo26, caption=fligel6)
        await sleep(5)
        await dp.bot.send_photo(message.from_user.id, photo=watchman6, caption=watchman2_6, reply_markup=kb_geo)
        await dp.bot.send_location(message.from_user.id, latitude=54.864297, longitude=38.757543)
        # await GeoState.state14.set()

    if s == 16:
        point_time('point14', message)
        await dp.bot.send_photo(message.from_user.id, photo=photo27, caption=crypt1,
                                reply_markup=ReplyKeyboardRemove())
        await sleep(5)
        await dp.bot.send_photo(message.from_user.id, photo=photo28, caption=crypt1_1,
                                reply_markup=kb_crypt_inline)
