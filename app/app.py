import telebot
import time

bot_token = '996467832:AAGy_XcT24VReF1Xz9uUuf1roCBfL26Vz9A'

bot = telebot.TeleBot(token=bot_token)



def find_at(msg):
    for text in msg:
        if '@' in text:
            return text

@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, 'Buscador de instagram')
    bot.reply_to(message,'digite um nome com @ no começo:')


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
        