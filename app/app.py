import telebot
import time

bot_token = '1062179301:AAE9oSklFeh4JpdK8UmOjdJel1TYrp9tIt0'

bot = telebot.TeleBot(token=bot_token)

def find_at(msg):
    for text in msg:
        if '@' in text:
            return text

@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, 'Welcome! Type /help to to learn how to use it')


@bot.message_handler(commands=['help'])
def help(message):
    bot.reply_to(message, "Type some instagram account with '@' ")        

@bot.message_handler(func=lambda msg: msg.text is not None and '@' in msg.text)
def at_answer(message):
    texts = message.text.split()
    at_text = find_at(texts)
    
    bot.reply_to(message, 'http://instagram.com/{}'.format(at_text[1:]))
    print(message.json)


while True:
    try:
        print('running bot...')
        bot.polling()
    except Exception:
        time.sleep(15)
        