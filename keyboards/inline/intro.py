from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from .call_back import intro_data

btn_1_1 = InlineKeyboardButton(text='Спросить про дату', callback_data=intro_data.new(part='1', picture='no',
                                                                                      text='Когда?'))
btn_1_2 = InlineKeyboardButton(text='Спросить про область поисков', callback_data=intro_data.new(part='1', picture='no'
                                                                                                 , text='1_2'))
btn_1_3 = InlineKeyboardButton(text='Узнать подробности', callback_data=intro_data.new(part='1', picture='no',
                                                                                       text='1_3'))
btn_1_4 = InlineKeyboardButton(text='Я в деле', callback_data=intro_data.new(part='1', picture='no', text='1_4'))

btn_lbank = InlineKeyboardButton(text='Посмотреть на левом берегу', callback_data=intro_data.new(part='2', picture='no',
                                                                                                 text='lbank'))
btn_rbank = InlineKeyboardButton(text='Посмотреть на правом берегу', callback_data=intro_data.new(part='2', picture='no'
                                                                                                  , text='rbank'))
btn_ilyas = InlineKeyboardButton(text='Спросить про Ильясы', callback_data=intro_data.new(part='3', picture='no'
                                                                                          , text='ilyas'))
btn_bebeh1 = InlineKeyboardButton(text='Крутое место', callback_data=intro_data.new(part='4', picture='no'
                                                                                    , text='bebeh1'))
btn_bebeh2 = InlineKeyboardButton(text='Да, так себе ', callback_data=intro_data.new(part='4', picture='no'
                                                                                     , text='bebeh2'))
btn_pond = InlineKeyboardButton(text='Вон стоит кто-то ', callback_data=intro_data.new(part='5', picture='no'
                                                                                       , text='pond'))
btn_crypt = InlineKeyboardButton(text='Интересное место ', callback_data=intro_data.new(part='6', picture='no'
                                                                                       , text='crypt'))

kb_intro_inline = InlineKeyboardMarkup(row_width=1)
kb_intro_inline.add(btn_1_1, btn_1_2, btn_1_3, btn_1_4)

kb_bank_inline = InlineKeyboardMarkup(row_width=1)
kb_bank_inline.add(btn_lbank, btn_rbank)

kb_ilyas_inline = InlineKeyboardMarkup(row_width=1)
kb_ilyas_inline.add(btn_ilyas)

kb_bebeh = InlineKeyboardMarkup(row_width=1)
kb_bebeh.add(btn_bebeh1, btn_bebeh2)

kb_pond_inline = InlineKeyboardMarkup(row_width=1)
kb_pond_inline.add(btn_pond)

kb_crypt_inline = InlineKeyboardMarkup(row_width=1)
kb_crypt_inline.add(btn_crypt)
