import telebot
from telebot import types
import lists
import returns as r
import bottoken

bot = telebot.TeleBot(bottoken.token)


## Commands
@bot.message_handler(commands=['start'])
def start(m):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    games = types.KeyboardButton('🎮 Игры')
    website = types.KeyboardButton('🌐 Веб-сайт')
    write = types.KeyboardButton('✏️ Написать')
    help = types.KeyboardButton('🤔 Помощь')

    markup.add(games, website, write, help)

    bot.send_message(m.chat.id, r.command_start(m.from_user.first_name), reply_markup=markup, parse_mode='html')

@bot.message_handler(commands=['help'])
def help(m):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    website = types.KeyboardButton('🌐 Веб-сайт')
    help = types.KeyboardButton('🤔 Помощь')
    write = types.KeyboardButton('✏️ Написать')

    markup.add(website, help, write)

    bot.send_message(m.chat.id, r.command_help(), reply_markup=markup, parse_mode='html')

@bot.message_handler(commands=['website', 'site'])
def website(m):
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton("Сайт creagoo.ru", url="https://creagoo.ru"))
    bot.send_message(m.chat.id, 'Ссылка на сайт', reply_markup=markup)

## Text


## Documents

bot.polling(none_stop=True)
