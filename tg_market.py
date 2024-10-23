from telebot import TeleBot

TOKEN = '7651803254:AAFZJttR-BRLY_vzO9xkSShrGJXJcIOIerk'

bot = TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def welcome(message):
    chat_id = message.chat.id
    bot.send_message(chat_id, 'Добро пожаловать! В ассортименте вы найдете стильную и комфортную одежду под нашим брендом.')

bot.infinity_polling()