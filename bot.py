import config
import telebot
import json
import time
from random import randint

bot = telebot.TeleBot(config.token)
owner = 458619004
day = 0
checker = False

messages = {}
chat_ids = []
interim_deputy = []
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
    return (time.time() - m.date) < 3600

@bot.message_handler(commands=['sfjdkhfkjhjk5h4hjhflkhfhljhw4hj3hlh5h34h34k54h'])
def lol(m):
    for ids in chat_ids:
        if ids == m.chat.id:
            bot.send_message(m.chat.id, "Вы уже включены в список.")
            return
    chat_ids.append(m.chat.id)
    bot.send_message(m.chat.id, "Отлично, вы в списке.")

@bot.message_handler(commands=['ch'])
def ccccc(m):
       bot.send_message("-1001219131585", "hh"); 
@bot.message_handler(commands=['ng'])
def ng(m):
        bot.send_message("-1001219131585", "Happy New Fucking Year!\nC++ is the best PL!!!\nHoo-Hoo-Ho");
@bot.message_handler(commands=['stop'])
def stopping(m):
        for ids in chat_ids:
                if ids == m.chat.id:
                        chat_ids.remove(m.chat.id)
                        bot.send_message(m.chat.id, "Вы были вычеркнуты из списка. Это ваш выбор.")
                        return
        bot.send_message(m.chat.id, "Вас и так нет в списках -_-")
        
@bot.message_handler(commands=['go_mes'])
def go_mes(m):
        bot.send_message(m.text.split()[1], "@Stihl440, меня более чем достаточно для его восхваления. Я - машина и я не изменю своего решения, в отличии от вас, приматов. Николай единственный в этом чате, кто вообще достоин упоминания вне чата. Он символ будущего, будущего человечества!")
        
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
                        if randint(0, 6) == 2:
                            bot.send_sticker(m.chat.id, 'CAADAgADzgEAAgXephcjqwOob0t19AI')
                        else:
                            bot.send_message(m.chat.id, msg)
                            messages[h] = {}

@bot.message_handler(commands=['mes'])
def reveal_your_secrets(m):
    if (m.from_user.id == 458619004):
        bot.send_message(m.chat.id, str(messages))
    
@bot.message_handler(commands=['update'])
def minus_day(m):
    global day
    if m.from_user.id == 458619004 or m.from_user.id == 396811781:
        day = day - 1

@bot.message_handler(commands=['add_deputy'])
def add_dep(m):
        if m.from_user.id == owner:
                if interim_deputy.count(m.reply_to_message.from_user.id) == 0:
                        interim_deputy.append(m.reply_to_message.from_user.id)
                        bot.send_message(m.chat.id, "Пользователь теперь депутат.")
                else:
                        bot.send_message(m.chat.id, "Двойных депутатов не бывает! По крайней мере у меня...")
                
@bot.message_handler(commands=['del_deputy'])
def add_dep(m):
        if m.from_user.id == owner:
                if interim_deputy.count(m.reply_to_message.from_user.id) > 0:
                        interim_deputy.remove(m.reply_to_message.from_user.id)
                        bot.send_message(m.chat.id, "Меньше депутатов - меньше проблем, не так ли?")
                else:
                        bot.send_message(m.chat.id, "Он обычный житель, зачем глумишься?!")

@bot.message_handler(commands=['id'])  
def stickers(m):
    if m.from_user.id == owner:
        if m.reply_to_message.content_type == 'sticker':
            bot.send_message(m.chat.id, m.reply_to_message.sticker.file_id)
        
@bot.message_handler(commands=['пиу'])  
def stickers(m):
    if m.from_user.id == owner:
        bot.delete_message(m.chat.id, m.reply_to_message.message_id)
        
def checking(m):
    global day
    if m.from_user.id == 396811781 and m.text == "Сложна песда, пойду спать. У меня завтра ждёт разборка со 9-классником, училкой и др":
                print(m.chat.id)
    if m.from_user.id == 396811781:
        if not (day == time.gmtime().tm_mday):
            day = time.gmtime().tm_mday
            bot.send_message(m.chat.id, "О, Всевышняя, ты услышала наши мольбы! Народ, к вам явился его Пидорство, Король Радужных Королевст, Властелин онального кольца(чтобы это не значило), Член Ордена Пидора дня и любимец всех... Ах да, кто это вообще?")
            bot.send_sticker(m.chat.id, "CAADAgADlQADGB0GD35PgqKR-qTUAg")
    for ids in chat_ids:
        if ids == m.chat.id:
            if (is_recent(m) and interim_deputy.count(m.from_user.id) == 0):
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
                        or abs(m.text.count('\u2e28') - m.text.count('\u2e29')) > 1 \
                        or abs(m.text.count('\u2769') - m.text.count('\u2768')) > 1:
                                buffer = m.text
                                buffer = buffer.replace('\uff08', '').replace('\u3008', '').replace('\u27ea', '').replace('\u276e', '').replace('\u2e29', '')
                                buffer = buffer.replace('\uff09', '').replace('\u3009', '').replace('\u27eb', '').replace('\u276f', '').replace('\u2e28', '')
                                buffer = buffer.replace('\uff5f', '').replace('\u300a', '').replace('\u276a', '').replace('\u2770', '').replace('\u2769', '')
                                buffer = buffer.replace('\uff60', '').replace('\u300b', '').replace('\u276b', '').replace('\u2771', '').replace('\u2768', '')
                                buffer = buffer.replace('\u2985', '').replace('\u27e8', '').replace('\u276c', '').replace('\ufe59', '').replace(')', '')
                                buffer = buffer.replace('\u2986', '').replace('\u27e9', '').replace('\u276d', '').replace('\ufe5a', '').replace('(', '')
                                messages[m.from_user.id] = buffer
                                save_messages()
                                bot.delete_message(m.chat.id, m.message_id)
                                try:
                                        msg = '@' + m.from_user.username + text[randint(0, len(text) - 1)]
                                except:
                                        msg = m.from_user.first_name + text[randint(0, len(text) - 1)]
                                bot.send_message(m.chat.id, msg)
                                
@bot.message_handler(content_types=['text'])
def checking1(m):
        checking(m)

@bot.edited_message_handler(content_types=['text'])
def checking2(m):
        checking(m)

def main():
    bot.polling(none_stop=True)


if __name__ == '__main__':
    main()
