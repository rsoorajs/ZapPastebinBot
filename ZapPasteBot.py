from urllib import request, parse
from telebot import types
import telebot
import random
import json
token = "939385469:AAEwKg2nPGGsqn2GjN2kc2Nsp6SMEsLWOls"
# Обходим блокировку с помощью прокси
telebot.apihelper.proxy = {'https': 'socks5h://geek:socks@t.geekclass.ru:7777'}
ran = 0
# подключаемся к телеграму
bot = telebot.TeleBot(token=token)

@bot.message_handler(commands=['start'])
def start(message):

    pastes = json.load(open('past.json','r'))
    markup = types.ReplyKeyboardMarkup()
    i = 0
    pastes_keys=list(pastes.keys())
    while(i<len(pastes_keys)):
        if(i<len(pastes_keys)-1):
            markup.row(pastes_keys[i]+" - "+pastes[pastes_keys[i]])
            markup.row(pastes_keys[i+1]+" - "+pastes[pastes_keys[i+1]])
        else:
            markup.row(pastes_keys[i]+" - "+pastes[pastes_keys[i]])
        i=i+2
        bot.send_message(message.chat.id,"Выберете ссылку",reply_markup=markup)
    

@bot.message_handler(commands=['ZNA'])
def admin(message):

    sent = bot.send_message(message.chat.id, 'Пиши уже паст')
    bot.register_next_step_handler(sent, hello)


def hello(message):
    m = json.load(open('past.json', 'r'))
    m[message.text.split()[0]] = message.text.split()[1]
    json.dump(m, open('past.json', 'w'))



@bot.message_handler(content_types=['text'])
def echo(message):
    print()
    
    


bot.polling(none_stop=True)
