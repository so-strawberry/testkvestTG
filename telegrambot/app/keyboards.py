from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton
from aiogram import types
from aiogram.types.web_app_info import WebAppInfo

start = InlineKeyboardMarkup( inline_keyboard=[
    [InlineKeyboardButton(text='Начать игру!', callback_data='start_game')]
])


site = InlineKeyboardMarkup( inline_keyboard=[
    [InlineKeyboardButton(text='Сайт', web_app = WebAppInfo( url = f'https://rutube.ru/') )]
])

perehod1 = InlineKeyboardMarkup( inline_keyboard=[
    [InlineKeyboardButton(text= 'Спать дальше', callback_data='Gameover'), InlineKeyboardButton(text= 'Читать дневник', callback_data='dnevnik1') ]
])

perehod2 = InlineKeyboardMarkup( inline_keyboard=[
    [InlineKeyboardButton(text= 'Закрыть дневник', callback_data='closednevnik1')]
])

perehod3 = InlineKeyboardMarkup( inline_keyboard=[
    [InlineKeyboardButton(text= 'Осмотреть СНИЛС', callback_data='snils')],
    [InlineKeyboardButton(text= 'Осмотреть Паспорт', callback_data='pasport')],
    [InlineKeyboardButton(text= 'Осмотреть Пропуск', callback_data='propusk')]
])

osmotr = InlineKeyboardMarkup( inline_keyboard=[
    [InlineKeyboardButton(text='Осмотреть комнату', callback_data='osmotr')]
])

osmotr1 = InlineKeyboardMarkup( inline_keyboard=[
    [InlineKeyboardButton(text='Осмотреть гостиную', callback_data='osmotr1')]
])

osmotr2 = InlineKeyboardMarkup( inline_keyboard=[
    [InlineKeyboardButton(text='Вернуться в спальню', callback_data='osmotr2')]
])

osmotr3 = InlineKeyboardMarkup( inline_keyboard=[
    [InlineKeyboardButton(text='Приподнять угол ковра', callback_data='osmotr3')]
])

osmotr4 = InlineKeyboardMarkup( inline_keyboard=[
    [InlineKeyboardButton(text='Вернуться в гостиную', callback_data='osmotr4')]
])

day2 = InlineKeyboardMarkup( inline_keyboard=[
    [InlineKeyboardButton(text='Далее...', callback_data='day2')]
])

son = InlineKeyboardMarkup( inline_keyboard=[
    [InlineKeyboardButton(text='...', callback_data='son')]
])

osm_propusk = InlineKeyboardMarkup( inline_keyboard=[
    [InlineKeyboardButton(text='Осмотреть пропуск', callback_data='osm')]
])





prob = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='Осмотреть СНИЛС')],
    [KeyboardButton(text='Осмотреть Паспорт')],
    [KeyboardButton(text='Осмотреть Пропуск')]

],
                                        resize_keyboard= True,
                                        input_field_placeholder='Что бы этот шифр мог значить?')

deletekeyboard = reply_markup=types.ReplyKeyboardRemove()