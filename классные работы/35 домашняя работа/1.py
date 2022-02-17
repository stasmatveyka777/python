import telebot
from telebot import types 
import re


bot = telebot.TeleBot("TOKEN")

@bot.message_handler(commands=['start'])
def start_message(message):
    markup = types.InlineKeyboardMarkup(row_width=2)
    item1 = types.InlineKeyboardButton('Да',callback_data='1_Да')
    item2 = types.InlineKeyboardButton('Нет',callback_data='1_Нет')
    markup.row(item1,item2)
    bot.send_message(message.chat.id,f'Здраствуйте, {message.from_user.first_name}! Желаете зарегистрироваться в Google?',reply_markup=markup)


def register_surname(message):
    global user_name
    bot.send_message(message.chat.id,"Какая у тебя фамилия?")
    player_name = message.text
    bot.register_next_step_handler(message, register_age)

def register_age(message):
    global player_surname
    bot.send_message(message.chat.id,"Сколько тебе лет?")
    player_surname = message.text
    bot.register_next_step_handler(message, check_user)

def check_user(message):
    global player_age,player_describe_player
    player_age = (re.findall('\d+',message.text)[0])
    player_describe_player = f"Имя: {player_name}\nФамилия: {player_surname}\nВозраст: {player_age}\nБраузер: {player_browser}"
    markup = types.InlineKeyboardMarkup(row_width=2)
    item1 = types.InlineKeyboardButton('Да',callback_data='Да')
    item2 = types.InlineKeyboardButton('Нет',callback_data='Нет')
    markup.row(item1,item2)
    bot.send_message(message.chat.id,f"{user_describe_user}\nВерно?",reply_markup=markup)


@bot.callback_query_handler(func=lambda call:True)
def callback_inline(call):
    try:
        global user_browser
        if call.message:
            global user
            if call.data == 'Да' or call.data =='Google':
                
                bot.send_message(call.message.chat.id,"Отлично!\nКак тебя зовут")
                bot.register_next_step_handler(call.message, register_surname)
                user_browser = 'Google'

            elif  call.data =='Yandex':

                bot.send_message(call.message.chat.id,"Отлично!\nКак тебя зовут")
                bot.register_next_step_handler(call.message, register_surname)
                user_browser = 'Yandex'

            elif call.data =='Edge':

                bot.send_message(call.message.chat.id,"Отлично!\nКак тебя зовут")
                bot.register_next_step_handler(call.message, register_surname)
                player_browser = 'Edge'
                    
            elif call.data == 'Нет':
                
                markup = types.InlineKeyboardMarkup(row_width=2)
                item1 = types.InlineKeyboardButton('Google',callback_data='Google')
                item2 = types.InlineKeyboardButton('Opera',callback_data='Opera')
                item3 = types.InlineKeyboardButton('Safari',callback_data='Safari')
                markup.row(item1,item2,item3)
                
                bot.send_message(call.message.chat.id,"И все же, где вы хотите зарегестрироватья?",reply_markup=markup)
            
            elif call.data == 'Да':
                
                bot.send_message(call.message.chat.id,"Замечательно! Вы внесены в нашу базу")
            
            elif call.data == '2_Нет':

                markup = types.InlineKeyboardMarkup(row_width=2)
                item1 = types.InlineKeyboardButton('Google',callback_data='Google')
                item2 = types.InlineKeyboardButton('Opera',callback_data='Opera')
                item3 = types.InlineKeyboardButton('Safari',callback_data='Safari')
                markup.row(item1,item2,item3)
                bot.send_message(call.message.chat.id,"Давай заново...\nВыберите браузер:",reply_markup=markup)

    except Exception as e:
        print(repr(e))

bot.infinity_polling()