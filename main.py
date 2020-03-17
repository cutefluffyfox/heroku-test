from telebot import TeleBot, apihelper
from telebot.types import Message


bot = TeleBot('1067102276:AAFej5UUXLYoJVWZjEPqb2gVvbg73GFVSWE')


@bot.message_handler(content_types=['text'])
def get_message(message: Message):
    bot.send_message(message.chat.id, message.text)


bot.polling()
