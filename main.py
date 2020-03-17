from telebot import TeleBot, apihelper
from telebot.types import Message
from random import choice


bot = TeleBot('1067102276:AAFej5UUXLYoJVWZjEPqb2gVvbg73GFVSWE')
bot_id = bot.get_me().id
bot_alias = bot.get_me().username
running = True


@bot.message_handler(content_types=['text'])
def stop_bot(message: Message):
    if message.text == '/kill@' + bot_alias:
        global running
        running = False


@bot.message_handler(content_types=['new_chat_members'])
def new_members(message: Message):
    if message.new_chat_member.id == bot_id:
        while running:
            bot.send_message(message.chat.id, choice(['Привет', 'День добрый', 'Здрасьте', 'Рад знакомству',
                                                      'Я бот', 'Приятно познакомиться', 'Здравия желаю', 'Здоровья']))


bot.polling()
