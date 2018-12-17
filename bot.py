import config
import telebot
import json
import time
import os
import tornado.httpserver
import tornado.ioloop
import tornado.web
from random import randint
from flask import Flask, request

server = Flask(__name__)

bot = telebot.TeleBot(config.token)

messages = {}
text = [', ты ужасный человек...',
        ', как тебе не стыдно?',
        '... Так и запишем... Жди бутылку ^.^',
        ', знаешь, есть способ меня обойти, но для этого нужно перестать быть жадным.',
        ', ПРОСИ ПРОЩЕНИЯ!!! МНЕ ЖЕ БОЛЬНО!!!',
        ', тебя заразила Профорг? Держись от неё подальше...',
        '. Я бы добавил к твоему существованию пару скобочек, а затем удалил.',
        ', fuckfuckfuckfuckfuckfuckfuck, stop it!'
        ]

with open('messages.json', 'w') as f:
    json.dump({}, f)

def save_messages():
    with open('messages.json', 'w') as f:
        json.dump(messages, f)

def is_recent(m):
    return (time.time() - m.date) < 60

@bot.message_handler(commands=['my_apologies'])
def kek(m):
    for h in messages.keys():
        if h == m.from_user.id:
            if messages[h]:
                msg = m.from_user.first_name + ' '
                try:
                    msg += m.from_user.last_name + 'said:\n' + messages[h]
                except:
                    msg += 'said:\n' + messages[h]
                if randint(0,10) == 2:
                    bot.send_sticker(m.chat.id, 'CAADAgADzgEAAgXephcjqwOob0t19AI')
                elif randint(0,10) == 1:
                    bot.send_sticker(m.chat.id, 'AAQCABMKd_MOAARqa9mUkcfOqGsfAAIC')
                    time.sleep(1)
                    bot.send_sticker(m.chat.id, 'AAQCABMpnvQOAATggzQPqnTPHFAdAAIC')
                else:
                    bot.send_message(m.chat.id, msg)
                    messages[h] = {}

@bot.message_handler(content_types=['text'])
def fuck(m):
        bot.send_message(m.chat,"sdfsdfd")
        print(m)
        if(is_recent(m)):
                if abs(m.text.count(')') - m.text.count('(')) > 1:
                        buffer = m.text
                        buffer = buffer.replace('(','')
                        buffer = buffer.replace(')','')
                        messages[m.from_user.id] = buffer
                        save_messages()
                        bot.delete_message(m.chat.id, m.message_id)
                        msg = '@' + m.from_user.username + text[randint(0,7)]
                        bot.send_message(m.chat.id, msg)
                

@server.route("/bot", methods=['POST'])
def getMessage():
    bot.process_new_updates([telebot.types.Update.de_json(request.stream.read().decode("utf-8"))])
    return "!", 200

@server.route("/")
def webhook():
    bot.remove_webhook()
    bot.set_webhook(url="https://" + config.token + "/bot")
    return "!", 20         
        
def main():
        while True:
            try:
                bot.polling(none_stop=True)
            except Exception as e:
                time.sleep(15)

        

if __name__  ==  '__main__':
    main()

server.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))  
