import telebot;
from telebot import types

bot = telebot.TeleBot('1005817495:AAH1JlVfSCb3M4C6GcrLvZl_VvDWTcK3Evc');
@bot.message_handler(content_types=['text'])
def get_text_messages(message):
if message.text == "Привет":
    bot.send_message(message.from_user.id, "Привет, чем я могу тебе помочь?")
elif message.text == "/help":
    bot.send_message(message.from_user.id, "Напиши привет")
else:
    bot.send_message(message.from_user.id, "Я тебя не понимаю. Напиши /help.")
bot.polling(none_stop=True, interval=0)
