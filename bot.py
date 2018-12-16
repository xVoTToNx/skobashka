import config
import telebot
import json
import time
from random import randint


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
    return (time() - m.date) < 60

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

@bot.message_handler(content_types=['sticker'])
def fukkkk(m):
    print (m)

def main():
    bot.polling(none_stop=True)
if __name__  ==  '__main__':
    main()