import random

def command_start(username):
    return f"Здравствуйте, {username}. Добро пожаловать в телеграм бот Creagoo"

def command_help():
    return "Бот Creagoo умеет: \n- Давать доступ на скачивание игр Creagoo\n- Делиться контактом разработчика\n- Присылать разные доп. материалы и ссылки"

def text_hi(username):
    lvars = [
        'Привет',
        'Привет!',
        f'Здравствуйте, {username}',
        'Здравствуйте',
        'Здравствуйте!'
    ]

    return lvars[random.randint(0, len(lvars) - 1)]

def text_contact_me():
    lvars = [
        'Хорошо. Пожалуйста, свяжитесь с <a href="//ddybka.t.me">@ddybka</a>, чтобы я смог ответить',
        'Пожалуйста, свяжитесь с <a href="//ddybka.t.me">@ddybka</a>, чтобы я мог ответить',
        'Cвяжитесь, пожалуйста, с <a href="//ddybka.t.me">@ddybka</a> для моего ответа',
        'Я не знаю, что сказать. Напишите <a href="//ddybka.t.me">@ddybka</a>, пожалуйста',
    ]
    return lvars[random.randint(0, len(lvars) - 1)]
