import telebot
from telebot import types
from config import TOKEN
from db import db, no_emoji
import random


bot = telebot.TeleBot(TOKEN)

# Меню
def main_menu(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
    item1 = types.KeyboardButton('❤️')
    item2 = types.KeyboardButton('😂')
    item3 = types.KeyboardButton('😭')
    item4 = types.KeyboardButton('😡')
    item5 = types.KeyboardButton('👍')
    item6 = types.KeyboardButton('🤦‍♀️')
    item7 = types.KeyboardButton('😘')
    item8 = types.KeyboardButton('🥳')
    item9 = types.KeyboardButton('😏')
    item10 = types.KeyboardButton('🐈 Кототерапия 🐈‍⬛')
    markup.add(item1, item2, item3, item4, item5, item6, item7, item8, item9, item10)

    bot.send_message(
        message.chat.id, "Выбирай мем\nТам внизу тыкни на emoji", reply_markup=markup
        )

# Начало работы
@bot.message_handler(commands=["start"])
def start(message):
    bot.send_message(message.chat.id, "Привет")
    main_menu(message)

# Mem'ные запросы
@bot.message_handler(content_types=['text'])
def bot_message(message):
    if message.chat.type == 'private':
        emoji = message.text
        if emoji in db.keys():
            if emoji == '🐈 Кототерапия 🐈‍⬛':
                msg = bot.send_animation(message.chat.id, random.choice(db[emoji]))
            else:
                msg = bot.send_photo(message.chat.id, random.choice(db[emoji]))
        else:
            bot.send_photo(message.chat.id, no_emoji)
            main_menu(message)


bot.infinity_polling()