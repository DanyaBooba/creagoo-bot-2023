import random


## COMMANDS
def start(num):
    l = {
        0: "Привет! ",
        1: "Здравствуй! ",
        2: "Привет. ",
        3: "Здравствуй. ",
        4: "Здравствуйте! ",
        5: "Здравствуйте. "
    }

    s1 = "Добро пожаловать в телеграм бота Creagoo."
    s2 = "С чего Вы хотите начать? Воспользуйтесь кнопками внизу."

    if num == 0:
        return l[random.randint(0, len(l) - 1)] + s1

    return s2

def help():
    return """Телеграм бот Creagoo умеет:
    - помогать скачивать игры Creagoo
    - читать статьи игр на сайте
    - получать информацию о играх
    - делиться контактами главного разработчика."""


## PINNED
def pinned_message():
    l = {
        0: "Ого. Вам так понравилось сообщение?",
        1: "Мне приятно, что Вы закрепили сообщение",
        2: "По всей видимости, это была интересная мысль...",
        3: "А можно и я закреплю сообщение?",
        4: "Закрепили сообщение"
    }

    return l[random.randint(0, len(l) - 1)]


## PHOTO
def sended_photo():
    l = {
        0: "Отправили фотографию",
        1: "Я же бот и не могу посмотреть фотографю",
        2: "Я бы очень хотел посмотреть...",
        3: "Я бот и не смогу посмотреть фотографию",
        4: "Вы можете отправить фотографию разработчику: <a href='//ddybka.t.me'>@ddybka</a>"
    }

    return l[random.randint(0, len(l) - 1)]


## TEXT
def text_hello(name):
    l = {
        0: "Здравствуйте",
        1: f"Здрвствуйте, {name}",
        2: "Привет",
        3: f"Привет, {name}",
        4: "Здравствуйте!",
        5: "Привет!",
        6: "Приветствую Вас",
        7: "Я рад Вас видеть!",
        8: f"{name}, Вы снова здесь!"
    }

    return l[random.randint(0, len(l) - 1)]


def text_else():
    return "К сожалению, я не могу ответить"


## GAMES
def descgame_babkaonthehunt2dclassic():
    return "<b>Babka On The Hunt: 2D Классика</b>\n\nИграйте за русскую бабушку Дусю! Гуляйте по Павловскому Посаду. БЕЙТЕ гопников. Полетите в КОСМОС. Копите БАБЛО. И покупайте красивые вещи."

def descgame_babkaonthehuntlight():
    return "<b>Babka On The Hunt Light</b>\n\n"

def descgame_babkaonthehunt():
    return "<b>Babka On The Hunt</b>\n\n"

def descgame_guess():
    return "<b>Guess</b>\n\n"

def descgame_tictactoe():
    return "<b>Tic Tac Toe</b>\n\n"

def descgame_rockpaperscissors():
    return "<b>Камень ножницы бумага</b>\n\n"

def descgame_rememberthesecards():
    return "<b>Запомни эти карты</b>\n\n"

def descgame_buttonpusher():
    return "<b>Button pusher</b>\n\n"

def descgame_sweetness():
    return "<b>Sweetness</b>\n\n"