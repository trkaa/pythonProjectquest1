from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

btn_geo = KeyboardButton('GEOLOCATION', request_location=True)

btn_o = KeyboardButton('-')

kb_geo = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
kb_geo.add(btn_geo)

kb_o = ReplyKeyboardMarkup(resize_keyboard=True)
kb_o.add(btn_o)