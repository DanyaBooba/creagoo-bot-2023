from telebot import types
import telebot
import lists
import returns
import tokenbot

bot = telebot.TeleBot(tokenbot.token)

## COMMANDS
@bot.message_handler(commands=['start'])
def start(m):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    games = types.KeyboardButton('Смотреть игры')
    help = types.KeyboardButton('Помощь')
    contact = types.KeyboardButton('Связаться')
    links = types.KeyboardButton('Ссылки')

    markup.add(games, help, contact, links)

    bot.send_message(m.chat.id, returns.start(0), reply_markup=markup)
    bot.send_message(m.chat.id, returns.start(1), reply_markup=markup)

@bot.message_handler(commands=['help'])
def help(m):
    bot.send_message(m.chat.id, returns.help())

    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton("creagoo.ru", url="https://creagoo.ru"))
    bot.send_message(m.chat.id, 'Ссылка на сайт Creagoo', reply_markup=markup)

    markup1 = types.InlineKeyboardMarkup()
    markup1.add(types.InlineKeyboardButton("@ddybka", url="https://ddybka.t.me"))
    bot.send_message(m.chat.id, 'Связаться с автором', reply_markup=markup1)


## DOC
@bot.message_handler(content_types=['photo'])
def photo(m):
    bot.send_message(m.chat.id, returns.sended_photo(), parse_mode='html')


## PINNED
@bot.message_handler(content_types=['pinned_message'])
def get_pin_message(m):
    bot.send_message(m.chat.id, returns.pinned_message())


## TEXT
@bot.message_handler(content_types=['text'])
def get_text(m):
    usertext = m.text.lower()

    if usertext in lists.list_hello:
        bot.send_message(m.chat.id, returns.text_hello(m.from_user.first_name))

    elif usertext in lists.list_lookatgames:
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        markup.add(types.KeyboardButton("Babka On The Hunt: 2D Классика"))
        markup.add(types.KeyboardButton("Запомни эти карты"))
        markup.add(types.KeyboardButton("Камень ножницы бумага"))
        markup.add(types.KeyboardButton("Крестики нолики"))
        markup.add(types.KeyboardButton("Sweetness"))
        markup.add(types.KeyboardButton("Guess"))
        markup.add(types.KeyboardButton("Button pusher"))
        markup.add(types.KeyboardButton("Вернуться на главную"))
        bot.send_message(m.chat.id, 'Выберите интересующую игру Creagoo', reply_markup=markup)

    elif usertext in lists.text_help:
        bot.send_message(m.chat.id, returns.help())

        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton("creagoo.ru", url="https://creagoo.ru"))
        bot.send_message(m.chat.id, 'Ссылка на сайт Creagoo', reply_markup=markup)

        markup1 = types.InlineKeyboardMarkup()
        markup1.add(types.InlineKeyboardButton("@ddybka", url="https://ddybka.t.me"))
        bot.send_message(m.chat.id, 'Связаться с автором', reply_markup=markup1)

    elif usertext in lists.list_contact:
        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton("creagoo.ru", url="https://creagoo.ru"))
        bot.send_message(m.chat.id, 'Ссылка на сайт Creagoo', reply_markup=markup)

        markup1 = types.InlineKeyboardMarkup()
        markup1.add(types.InlineKeyboardButton("@ddybka", url="https://ddybka.t.me"))
        bot.send_message(m.chat.id, 'Связаться с автором', reply_markup=markup1)

        markup2 = types.InlineKeyboardMarkup()
        markup2.add(types.InlineKeyboardButton("it.dybka.ru", url="https://it.dybka.ru"))
        bot.send_message(m.chat.id, 'Другие разработки', reply_markup=markup2)

    elif usertext in lists.text_getlinks:
        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton("Сайт Creagoo", url="https://creagoo.ru"))
        markup.add(types.InlineKeyboardButton("Телеграм канал", url="https://creagoo.t.me"))
        markup.add(types.InlineKeyboardButton("Вконтакте паблик", url="https://vk.com/creagoo"))
        markup.add(types.InlineKeyboardButton("Читать новости", url="https://news.dybka.ru"))
        markup.add(types.InlineKeyboardButton("Слушать подкаст", url="https://youtu.be/lKLuwC9qb-w"))
        bot.send_message(m.chat.id, 'Ссылки Creagoo', reply_markup=markup)

    elif usertext in lists.text_getmainscreen:
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        games = types.KeyboardButton('Смотреть игры')
        help = types.KeyboardButton('Помощь')
        contact = types.KeyboardButton('Связаться')
        links = types.KeyboardButton('Ссылки')

        markup.add(games, help, contact, links)
        bot.send_message(m.chat.id, 'Вы вернулись на главную', reply_markup=markup)

    elif usertext in lists.list_games:
        if usertext in lists.game_babkaonthehunt2dclassic:
            bot.send_message(m.chat.id, returns.descgame_babkaonthehunt2dclassic(), parse_mode='html')
            ## прикрепить фотографии
            ## прикрепить ссылки на скачивание

        elif usertext in lists.game_tictactoe:
            bot.send_message(m.chat.id, returns.descgame_tictactoe(), parse_mode='html')

        elif usertext in lists.game_babkaonthehuntlight:
            bot.send_message(m.chat.id, returns.descgame_babkaonthehuntlight(), parse_mode='html')

        elif usertext in lists.game_babkaonthehunt:
            bot.send_message(m.chat.id, returns.descgame_babkaonthehunt(), parse_mode='html')

        elif usertext in lists.game_guess:
            bot.send_message(m.chat.id, returns.descgame_guess(), parse_mode='html')

        elif usertext in lists.game_rememberthesecards:
            bot.send_message(m.chat.id, returns.descgame_rememberthesecards(), parse_mode='html')

        elif usertext in lists.game_sweetness:
            bot.send_message(m.chat.id, returns.descgame_sweetness(), parse_mode='html')

        elif usertext in lists.game_buttonpusher:
            bot.send_message(m.chat.id, returns.descgame_buttonpusher(), parse_mode='html')

        elif usertext in lists.game_rockpaperscissors:
            bot.send_message(m.chat.id, returns.descgame_rockpaperscissors(), parse_mode='html')

    else:
        bot.send_message(m.chat.id, returns.text_else())


bot.polling(none_stop=True)