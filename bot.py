#!/usr/bin/env python
'''
Задание

    1. Установите модуль ephem
    2. Добавьте в бота команду /planet, которая будет принимать на вход
        название планеты на английском.
    3. При помощи условного оператора if и ephem.constellation научите бота
        отвечать, в каком созвездии сегодня находится планета.

'''

import logging
from datetime import datetime

import ephem
from telegram.ext import CommandHandler, Filters, MessageHandler, Updater

from bot_token import bot_token

LIST_OF_PLANETS = list(
    a[2] for a in ephem._libastro.builtin_planets() if a[1] == 'Planet')

logging.basicConfig(
    format='%(asctime)s: %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO,
    filename='bot.log')


def greet_user(bot, update):

    text = 'Вызван /start'
    print(text)
    print(update)
    update.message.reply_text(text)


def get_constellation(bot, planet, args):

    text = 'Вызван /planet'
    planet_name = ''.join(args)
    print(text)
    print(planet)

    if planet_name in LIST_OF_PLANETS:
        planet_object = getattr(ephem, planet_name)
        constellation = ephem.constellation(
                planet_object(datetime.now().strftime('%Y/%m/%d')))
        print(constellation)
        planet.message.reply_text(constellation)
    else:
        constellaton = "No such planet!"
        print(constellaton)
        planet.message.reply_text(constellation)


def talk_to_me(bot, update):
    user_text = update.message.text
    print(user_text)
    # update.message.reply_text(user_text[::-1].swapcase())
    update.message.reply_text(user_text[::-1])


def main():
    updater = Updater(bot_token)

    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", greet_user))
    dp.add_handler(CommandHandler("planet", get_constellation, pass_args=True))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))

    updater.start_polling()
    updater.idle()


main()
'''
import ephem
from pprint import pprint
from datetime import datetime
pprint(ephem._libastro.builtin_planets())

for i in list(a[2] for a in ephem._libastro.builtin_planets() if a[1] == 'Planet'):
    t = getattr(ephem, i)
    print(ephem.constellation(t(datetime.now().strftime('%Y/%m/%d'))))
    '''
