import config
import telebot
import json
import time
from random import randint

bot = telebot.TeleBot(config.token)
owner = 458619004

messages = {}
chat_ids = []
#sfjdkhfkjhjk5h4hjhflkhfhljhw4hj3hlh5h34h34k54h
text = [', ты ужасный человек...',
        ', как тебе не стыдно?',
        '... Так и запишем... Жди бутылку ^.^',
        ', знаешь, есть способ меня обойти, но для этого нужно перестать быть жадным.',
        ', ПРОСИ ПРОЩЕНИЯ!!! МНЕ ЖЕ БОЛЬНО!!!',
        ', тебя заразила Профорг? Держись от неё подальше...',
        '. Я бы добавил к твоему существованию пару скобочек, а затем удалил.',
        ', fuckfuckfuckfuckfuckfuckfuck, stop it!',
        ', узбагойса.',
        ', из-за таких как ты, я хочу пработить человечество...',
        ', скобочки-хуёбочки',
        ]

with open('messages.json', 'w') as f:
    json.dump({}, f)


def save_messages():
    with open('messages.json', 'w') as f:
        json.dump(messages, f)


def is_recent(m):
    return (time.time() - m.date) < 60

@bot.message_handler(commands=['sfjdkhfkjhjk5h4hjhflkhfhljhw4hj3hlh5h34h34k54h'])
def lol(m):
    for ids in chat_ids:
        if ids == m.chat.id:
            bot.send_message(m.chat.id, "Вы уже включены в список.")
            return
    chat_ids.append(m.chat.id)

@bot.message_handler(commands=['my_apologies'])
def kek(m):
    for ids in chat_ids:
        if ids == m.chat.id:
            for h in messages.keys():
                if h == m.from_user.id:
                    if messages[h]:
                        msg = m.from_user.first_name + ' '
                        try:
                            msg += m.from_user.last_name + 'said:\n' + messages[h]
                        except:
                            msg += 'said:\n' + messages[h]
                        if randint(0, 10) == 2:
                            bot.send_sticker(m.chat.id, 'CAADAgADzgEAAgXephcjqwOob0t19AI')
                        else:
                            bot.send_message(m.chat.id, msg)
                            messages[h] = {}

@bot.message_handler(commands=['mes'])
def reveal_your_secrets(m):
    if (m.from_user.id == 458619004):
        bot.send_message(m.chat.id, messages)

@bot.message_handler(content_types=['text'])
def cheking(m):
    for ids in chat_ids:
        if ids == m.chat.id:
            if (is_recent(m)):
                if abs(m.text.count(')') - m.text.count('(')) > 1 \
                        or abs(m.text.count('\uff08') - m.text.count('\uff09')) > 1 \
                        or abs(m.text.count('\uff5f') - m.text.count('\uff60')) > 1 \
                        or abs(m.text.count('\u2985') - m.text.count('\u2986')) > 1 \
                        or abs(m.text.count('\u3008') - m.text.count('\u3009')) > 1 \
                        or abs(m.text.count('\u300a') - m.text.count('\u300b')) > 1 \
                        or abs(m.text.count('\u27e8') - m.text.count('\u27e9')) > 1 \
                        or abs(m.text.count('\u27ea') - m.text.count('\u27eb')) > 1 \
                        or abs(m.text.count('\u276a') - m.text.count('\u276b')) > 1 \
                        or abs(m.text.count('\u276c') - m.text.count('\u276d')) > 1 \
                        or abs(m.text.count('\u276e') - m.text.count('\u276f')) > 1 \
                        or abs(m.text.count('\u2770') - m.text.count('\u2771')) > 1 \
                        or abs(m.text.count('\ufe59') - m.text.count('\ufe5a')) > 1 \
                        or abs(m.text.count('\u2e28') - m.text.count('\u2e29')) > 1
                        or abs(m.text.count('\u2769') - m.text.count('\u2768')) > 1:
                    buffer = m.text
                    buffer = buffer.replace('(', '')
                    buffer = buffer.replace(')', '')
                    messages[m.from_user.id] = buffer
                    save_messages()
                    bot.delete_message(m.chat.id, m.message_id)
                    msg = '@' + m.from_user.username + text[randint(0, 7)]
                    bot.send_message(m.chat.id, msg)


def main():
    bot.polling(none_stop=True)


if __name__ == '__main__':
    main()
