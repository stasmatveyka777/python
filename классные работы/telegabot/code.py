#                 ▄████ ▓█████▄ ▒███████▒             ██ ▄█▀  █████▒█    ██  ███▄    █ ▓█████▄
#                ██▒ ▀█▒▒██▀ ██▌▒ ▒ ▒ ▄▀░             ██▄█▒ ▓██   ▒ ██  ▓██▒ ██ ▀█   █ ▒██▀ ██▌
#               ▒██░▄▄▄░░██   █▌░ ▒ ▄▀▒░             ▓███▄░ ▒████ ░▓██  ▒██░▓██  ▀█ ██▒░██   █▌
#               ░▓█  ██▓░▓█▄   ▌  ▄▀▒   ░            ▓██ █▄ ░▓█▒  ░▓▓█  ░██░▓██▒  ▐▌██▒░▓█▄   ▌
#               ░▒▓███▀▒░▒████▓ ▒███████▒            ▒██▒ █▄░▒█░   ▒▒█████▓ ▒██░   ▓██░░▒████▓
#                 ░▒   ▒  ▒▒▓  ▒ ░▒▒ ▓░▒░▒            ▒ ▒▒ ▓▒ ▒ ░   ░▒▓▒ ▒ ▒ ░ ▒░   ▒ ▒  ▒▒▓  ▒
#                 ░   ░  ░ ▒  ▒ ░░▒ ▒ ░ ▒            ░ ░▒ ▒░ ░     ░░▒░ ░ ░ ░ ░░   ░ ▒░ ░ ▒  ▒
#               ░ ░   ░  ░ ░  ░ ░ ░ ░ ░ ░            ░ ░░ ░  ░ ░    ░░░ ░ ░    ░   ░ ░  ░ ░  ░
#                     ░    ░      ░ ░                ░  ░             ░              ░    ░
#                        ░      ░                                                       ░

import telebot
from telebot import types

token = ""
bot=telebot.TeleBot(token)
@bot.message_handler(commands=['start'])
def start_message(message):

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("ДЗ")
    item2 = types.KeyboardButton("Классаня")
    item3 = types.KeyboardButton("Code")
    markup.row(item1,item2).add(item3)

    bot.send_message(message.chat.id, "Привет ✌️, {0.first_name}!\nЯ - <b>{1.first_name}</b>, бот созданный чтобы быть помочь тебе.".format(message.from_user, bot.get_me()),
        parse_mode='html',reply_markup=markup)
    bot.send_message(message.chat.id,'Рекомендуем перед каждым использованием бота писать команду /start, т.к. очень часто выходят новые плюшечки.\nРебят, был сбой в программе и кидались не валидные архивы. Уже решили. Спасибо за оперативную инфу😃. \n[Version 1.1 || Last UPD 27.01.2022 15:45')
@bot.message_handler(content_types=['text'])
def obrob_bnts(message):
    if message.chat.type == 'private':
        if message.text == 'ДЗ':
            markup = types.InlineKeyboardMarkup(row_width=2)
            item2 = types.InlineKeyboardButton("2",callback_data='home_work_2')
            item3 = types.InlineKeyboardButton("3",callback_data='home_work_3')
            item4 = types.InlineKeyboardButton("4",callback_data='home_work_4')
            item6 = types.InlineKeyboardButton("6",callback_data='home_work_6')
            item8 = types.InlineKeyboardButton("8",callback_data='home_work_8')
            item11 = types.InlineKeyboardButton("11",callback_data='home_work_11')
            item12 = types.InlineKeyboardButton("12",callback_data='home_work_12')
            item15 = types.InlineKeyboardButton("15",callback_data='home_work_15')
            item16 = types.InlineKeyboardButton("16",callback_data='home_work_16')
            item17 = types.InlineKeyboardButton("17",callback_data='home_work_17')
            item18 = types.InlineKeyboardButton("18",callback_data='home_work_18')
            item24 = types.InlineKeyboardButton("24",callback_data='home_work_24')
            item25 = types.InlineKeyboardButton("25",callback_data='home_work_25')
            item26 = types.InlineKeyboardButton("26",callback_data='home_work_26')
            item8_15 = types.InlineKeyboardButton("8.15",callback_data='home_work_8.15')
            item8_16 = types.InlineKeyboardButton("8.16",callback_data='home_work_8.16')
            markup.row(item2,item3,item4,item6,item8,item11,item12,item15,item16,item17,item18,item24,item25,item26,item8_15,item8_16)
            bot.send_message(message.chat.id,'             Понял, выбери номер домашки или упражнения             ',reply_markup=markup)
            bot.send_message(message.chat.id,'По поводу ошибок на почту - kfund.gdz@gmail.com')
        elif message.text == 'Классаня':
            markup = types.InlineKeyboardMarkup(row_width=2)
            item0=types.InlineKeyboardButton("Exam",callback_data='class_work_0')
            item1 = types.InlineKeyboardButton("1",callback_data='class_work_1')
            item2 = types.InlineKeyboardButton("2",callback_data='class_work_2')
            item3 = types.InlineKeyboardButton("3",callback_data='class_work_3')
            item4 = types.InlineKeyboardButton("4",callback_data='class_work_4')
            item5 = types.InlineKeyboardButton("5",callback_data='class_work_5')
            item6 = types.InlineKeyboardButton("6",callback_data='class_work_6')
            item7 = types.InlineKeyboardButton("7",callback_data='class_work_7')
            item8 = types.InlineKeyboardButton("8",callback_data='class_work_8')
            item9 = types.InlineKeyboardButton("9",callback_data='class_work_9')
            item10 =types.InlineKeyboardButton("10",callback_data='class_work_10')
            item11 =types.InlineKeyboardButton("11",callback_data='class_work_11')
            item12 =types.InlineKeyboardButton("12",callback_data='class_work_12')
            item13 =types.InlineKeyboardButton("13",callback_data='class_work_13')
            item14 =types.InlineKeyboardButton("14",callback_data='class_work_14')
            item15 =types.InlineKeyboardButton("15",callback_data='class_work_15')
            item16 =types.InlineKeyboardButton("16",callback_data='class_work_16')
            item17 =types.InlineKeyboardButton("17",callback_data='class_work_17')
            item18 =types.InlineKeyboardButton("18",callback_data='class_work_18')
            item19 =types.InlineKeyboardButton("19",callback_data='class_work_19')
            item20 =types.InlineKeyboardButton("20",callback_data='class_work_20')
            item21 =types.InlineKeyboardButton("21",callback_data='class_work_21')
            item22 =types.InlineKeyboardButton("22",callback_data='class_work_22')
            item23 =types.InlineKeyboardButton("23",callback_data='class_work_23')
            item24 =types.InlineKeyboardButton("24",callback_data='class_work_24')
            item25 =types.InlineKeyboardButton("25",callback_data='class_work_25')
            item26 =types.InlineKeyboardButton("26",callback_data='class_work_26')
            item27 =types.InlineKeyboardButton("27",callback_data='class_work_27')
            item28 =types.InlineKeyboardButton("28",callback_data='class_work_28')
            item29 =types.InlineKeyboardButton("29",callback_data='class_work_29')
            item30 =types.InlineKeyboardButton("30",callback_data='class_work_30')
            item31 =types.InlineKeyboardButton("31",callback_data='class_work_31')
            item32 =types.InlineKeyboardButton("32",callback_data='class_work_32')
            markup.add(item0).row(item1,item2,item3,item4,item5,item6,item7,item8,item9,item10,item11,item12,item13,item14,item15,item16,item17,item18,item19,item20,item21,item22,item23,item24,item25,item26,item27,item28,item29,item30,item31,item32)
            bot.send_message(message.chat.id,'             Понял, выбери номер урока             ',reply_markup=markup)
            bot.send_message(message.chat.id,'По поводу ошибок на почту - kfund.gdz@gmail.com')
        elif message.text == 'Code':
            markup = types.InlineKeyboardMarkup(row_width=1)
            item0=types.InlineKeyboardButton("Code",url='https://drive.google.com/file/d/1JCF3joDAHeLdokLES1KdKSWvg6eNDJwO/view?usp=sharing',callback_data='class_work_0')
            markup.add(item0)
            bot.send_message(message.chat.id,'             Code             ',reply_markup=markup)
            bot.send_message(message.chat.id,'По поводу ошибок на почту - kfund.gdz@gmail.com')
        else:
            bot.send_message(message.chat.id,'Может быть)...')

@bot.callback_query_handler(func=lambda call:True)
def callback_inline(call):
    try:
        if call.message:

            for i in range(33):
                if call.data == f'class_work_{i}':
                    with open(f'static/lesson/ls{i}.zip', 'rb') as file:
                        bot.send_document(call.message.chat.id, file)
                    bot.send_message(call.message.chat.id, f'Лови Урок №{i}')
                elif call.data == f'home_work_{i}':
                    with open(f'static/homeworks/hw{i}.zip', 'rb') as file:
                        bot.send_document(call.message.chat.id, file)
                    bot.send_message(call.message.chat.id, f'Лови ДЗ №{i}')
                elif call.data == f'home_work_8.{i}':
                    with open(f'static/homeworks/hw8.{i}.zip', 'rb') as file:
                        bot.send_document(call.message.chat.id, file)
                    bot.send_message(call.message.chat.id, f'Лови ДЗ №8.{i}')
    except Exception as e:
        print(repr(e))
bot.infinity_polling()



#   _____           _                              _           __ _            
#  / ____|         | |                ___         | |         /_ | |           
# | |     ___  _ __| | _____ _ __    ( _ )     ___| |_ __ _ ___| | | _____ ___ 
# | |    / _ \| '__| |/ / _ \ '__|   / _ \/\  / __| __/ _` / __| | |/ / __/ __|
# | |___| (_) | |  |   <  __/ |     | (_>  <  \__ \ || (_| \__ \ |   < (__\__ \
#  \_____\___/|_|  |_|\_\___|_|      \___/\/  |___/\__\__,_|___/_|_|\_\___|___/
