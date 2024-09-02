import os

import asyncio

from aiogram import types

import logging
from aiogram import Bot, Dispatcher, types

from aiogram.types.web_app_info import WebAppInfo

import aiogram.types as types
from aiogram import F, Router
from aiogram.filters import CommandStart, Command
from aiogram.types import Message, CallbackQuery, FSInputFile, InputMediaAnimation, InputMediaPhoto
import app.keyboards as kb

day = 0

router = Router()


@router.message(F.text.lower().contains('сайт'))
async def tydoma(message: Message):
    await message.answer('Чтобы перейти на сайт нажми на кнопку', reply_markup= kb.site)


@router.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer(f'Здравствуй, {message.from_user.first_name}! Желаешь ли ты начать игру?' , 
                         reply_markup=kb.start)


@router.callback_query(F.data == 'start_game')
async def start_game(callback: CallbackQuery):
    await callback.answer()
    await callback.message.edit_text('ДЕНЬ ПЕРВЫЙ.\n Проснувшись, Джон ощутил непреодолимое желание заглянуть в свои заметки. Он не помнил, почему это так важно, но чувство было настолько сильным, что он не мог его игнорировать.', reply_markup= kb.perehod1)
    day == 1 

@router.callback_query(F.data == 'Gameover')
async def Gameover(callback: CallbackQuery):
    await callback.answer('Игра окончена', show_alert= True)
    await callback.message.edit_text('ВЫ ПРОИГРАЛИ', reply_markup=kb.start)
    day == 0




@router.callback_query(F.data == 'dnevnik1')
async def dnevnik1(callback: CallbackQuery):
    await callback.answer()
    await callback.message.edit_text('ДЕНЬ ПЕРВЫЙ.\n Проснувшись, Джон ощутил непреодолимое желание заглянуть в свои заметки. Он не помнил, почему это так важно, но чувство было настолько сильным, что он не мог его игнорировать.')
    await callback.message.answer('Дорогой я,  Мою, твою, нашу жену убили. Я не думал, что так сложно писать самому себе. Ты не помнишь, но я уже неделю веду это расследование. Всё, что удалось, — это придумать способ не забыть всё и найти обрывок фотографии убийцы. Следующее, что тебе нужно сделать, — осмотреть мой... наш дом. Я чувствую, у меня остаётся мало времени. Осмотрись…', reply_markup= kb.perehod2)

    
@router.callback_query(F.data == 'closednevnik1')
async def closednevnik1(callback: CallbackQuery):
    await callback.answer()
    await callback.message.edit_text('Дорогой я,  Мою, твою, нашу жену убили. Я не думал, что так сложно писать самому себе. Ты не помнишь, но я уже неделю веду это расследование. Всё, что удалось, — это придумать способ не забыть всё и найти обрывок фотографии убийцы. Следующее, что тебе нужно сделать, — осмотреть мой... наш дом. Я чувствую, у меня остаётся мало времени. Осмотрись…')
    await callback.message.answer('Почувствовав что-то в кармане своих брюк, я засунул туда руку и нащупал что-то плотное. Вытащив, обнаружил аккуратно сложенные документы, завернутые в зип-пакет.')
    await callback.message.answer_photo(photo=FSInputFile('pictures\hodka.png'))
    await callback.message.answer('Вскрыв его, нашел три важных документа: СНИЛС, паспорт и пропуск в нефтяную компанию.', reply_markup= kb.prob)
   
#@router.callback_query(F.data == 'snils')
#async def snils(callback: CallbackQuery):
#    await callback.answer()
#    await callback.message.edit_text('Здесь нет ничего примечательного для моего расследования...', reply_markup= kb.perehod3)

#@router.callback_query(F.data == 'pasport')
#async def pasport(callback: CallbackQuery):
#    await callback.answer()
#    await callback.message.edit_text('- Имя и фамилия: Джон Данглер\n- Дата рождения: 23.04.2000\n- Место жительства: ул. Пскова, д. 66\n\n В левом верхнем углу страницы Джон заметил какую-то грязь. Присмотревшись внимательнее, он увидел, что это не просто пятно. Грязь образовывала странные символы, похожие на шифр: "- -.-- / -.. --- -- .-".', reply_markup= kb.perehod3)
#    await callback.message.answer('Что бы мог означать этот шифр?')

#@router.callback_query(F.data == 'propusk')
#async def propusk(callback: CallbackQuery):
#    await callback.answer()
#    await callback.message.edit_text('-Компания «НефтьГазНаш»\n-Пропуск 1 уровня/ Отдел логистики \n-№4438 ', reply_markup= kb.perehod3)


@router.message(F.text == 'Осмотреть СНИЛС')
async def snils(message: Message):
    await message.answer('Здесь нет ничего примечательного для моего расследования...')

@router.message(F.text == 'Осмотреть Паспорт' )
async def snils(message: Message):
    await message.answer_photo(photo=FSInputFile('pictures\pasport.jpg'))
    await message.answer('В левом верхнем углу страницы я заметил какую-то грязь. Присмотревшись внимательнее, увидел, что это не просто пятно. Грязь образовывала странные символы, похожие на шифр: "- -.-- / -.. --- -- .-".' )

@router.message(F.text == 'Осмотреть Пропуск')
async def snils(message: Message):
    await message.answer_photo(photo=FSInputFile('pictures\propusk.jpg'))
    

@router.message(F.text.lower().contains('ты дома'))
async def tydoma(message: Message):
    await message.answer('...', reply_markup= kb.deletekeyboard)
    await message.answer('Интересно то есть это мой дом, но я его не помню, я вообще не помню своего дома… Здесь происходит что то странное.', reply_markup= kb.osmotr)
        

@router.callback_query(F.data == 'osmotr')
async def osmotr(callback: CallbackQuery):
    await callback.answer()
    await callback.message.edit_text('Интересно то есть это мой дом, но я его не помню, я вообще не помню своего дома… Здесь происходит что то странное.')
    await callback.message.answer('Спальня выглядела как замерзшая сцена из прошлого. В центре стояла большая двуспальная кровать с выцветшим покрывалом. Прикроватные тумбочки с книгами и журнальными изданиями были покрыты пылью, а старая лампа с тканевым абажуром тускло освещала комнату. \nШкаф с зеркальными дверцами был полон старой одеждой, а на кресле у окна виднелись следы от растворителя. Место под картиной было запорошено песком, напоминающим размельченный бетон. Тяжелые шторы плотно закрывали окно, создавая полумрак. Пол был покрыт старым ковром, который в одном углу был приподнят, открывая деревянное основание.')
    await callback.message.answer('Думаю я осмотрел комнату полностью', reply_markup=kb.osmotr1)

@router.callback_query(F.data == 'osmotr1')
async def osmotr(callback: CallbackQuery):
    await callback.answer()
    await callback.message.edit_text('Я вышел из спальни в гостиную. Передо мной открылось помещение, похожее на гостиницу, с такими же обоями, как и в спальне, и видимой неряшливостью интерьера. Везде лежала пыль, особенно на книжном столике, который, казалось, давно использовался не по назначению. На столике стоял пыльный телевизор. В другой части комнаты возвышался диван, явно предназначенный для семейных посиделок перед телевизором. Его кожа давно сморщилась, словно лицо старушки, в мелкие морщины. ')
    await callback.message.answer('Обстановка казалась скудной, словно жильцы этого места давно забыли, что слово "гостиная" происходит от слова "гости". ')
    await callback.message.answer('Но тут мое внимание привлек пол. На нем был виден едва различимый силуэт ковра, который когда-то здесь находился, но теперь отсутствовует.', reply_markup=kb.osmotr2 )


@router.callback_query(F.data == 'osmotr2')
async def osmotr(callback: CallbackQuery):
    await callback.answer()
    await callback.message.edit_text('Но тут мое внимание привлек пол. На нем был виден едва различимый силуэт ковра, который когда-то здесь находился, но теперь отсутствует.')
    await callback.message.answer('Я решил рассмотреть ковер повнимательнее и заметил похожие разводы, что и на кресле, словно кто-то пытался его отчистить.', reply_markup=kb.osmotr3)


@router.callback_query(F.data == 'osmotr3')
async def osmotr(callback: CallbackQuery):
    await callback.answer()
    await callback.message.edit_text('Я решил рассмотреть ковер повнимательнее и заметил похожие разводы, что и на кресле, словно кто-то пытался его отчистить.')
    await callback.message.answer_photo(photo=FSInputFile('pictures\kover.jpg'), caption='О БОЖЕ...', reply_markup=kb.osmotr4)
    #await callback.message.answer('О, Боже...', reply_markup=kb.osmotr4)









@router.callback_query(F.data == 'osmotr4')
async def osmotr(callback: CallbackQuery):
    await callback.answer()
    await callback.message.edit_media(media=InputMediaPhoto(media=(FSInputFile('pictures\kover.jpg')), caption='О БОЖЕ...'))
   # await callback.message.edit_text('О, Боже...')
    await callback.message.answer('Вернувшись в гостиную, я заметил, как деревянный пол местами потускнел, образуя след, который вел к выходу на улицу. Я вышел наружу, но тут яркие лучи солнца ослепили меня, и я, потеряв координацию, упал у крыльца. Когда я поднял голову, передо мной предстала новая деталь: на углу крыльца виднелась несмытая кровь. Пазл в моей голове начал складываться. Но вот незадача: след, тянувшийся по полу, полностью исчез на земле.\n\nНадо собрать мысли в кучу...\nСамое время сделать пару заметок на следующий день')
    await callback.message.answer('*Тут появляется анимация или сборка фоток в виде заметок в дневнике ГГ*', reply_markup=kb.day2)


@router.callback_query(F.data == 'day2')
async def osmotr(callback: CallbackQuery):
    await callback.answer()
    await callback.message.edit_text('Передо мной медленно проявляется картина, словно через пелену сна. Я вижу зеркало, и в нем отражается часть моего тела — джинсовые штаны и нижняя часть синей клетчатой рубашки. ')
    await callback.message.answer_photo(photo=FSInputFile('pictures\son.jpg'))
    await callback.message.answer('Образ начинает таять, и я вдруг просыпаюсь.', reply_markup=kb.son) 

@router.callback_query(F.data == 'son')
async def osmotr(callback: CallbackQuery):
    await callback.answer()
    await callback.message.edit_text('Образ начинает таять, и я вдруг просыпаюсь.')
    await callback.message.answer('Надо вспомнить заметку... Вчера я наконец решился посетить то место, куда давал мне доступ пропуск, найденный в зип-пакете. Но куда идти?', reply_markup=kb.osm_propusk)

@router.callback_query(F.data == 'osm')
async def osmotr(callback: CallbackQuery):
    await callback.answer()
    await callback.message.edit_text('Надо вспомнить заметку... Вчера я наконец решился посетить то место, куда давал мне доступ пропуск, найденный в зип-пакете. Но куда идти?')
    await callback.message.answer_photo(photo=FSInputFile('pictures\propusk.jpg'))

adresses = [
    'улица ричмонда дом 138',
    'ул. ричмонда, дом 138',
    'ул. ричмонда, д.138',
    'ул. ричмонда, д 138',
    'ул ричмонда, д 138',
    'ул ричмонда д 138',
    'ул ричмонда дом 138'
]


# @router.message(F.text.lover().contains(adresses))
# #@router.message(F.text == 'Улица Ричмонда дом 138')
# async def adress(message: Message):
#     await message.answer('Теперь я знаю адрес, и мне нужно отправиться туда.\nПродолжение следует...')   


@router.message()
async def adress(message: Message):
    text_received = message.text.lower()
    if any(adress in text_received for adress in adresses):
        await message.answer('Теперь я знаю адрес, и мне нужно отправиться туда.\nПродолжение следует...')
    else:
        await message.answer('Это не правильный ответ, попробуй что то другое...')   

