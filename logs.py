import datetime
import json

def convert_format_message(idmessage):
    if idmessage == -2:
        return "stop bot"
    elif idmessage == -1:
        return "start bot"
    elif idmessage == 0:
        return "message"
    elif idmessage == 1:
        return "command"
    elif idmessage == 2:
        return "document"
    elif idmessage == 3:
        return "pinned"
    else:
        return "none"

def save(chatid=0, text="", formattext=0):

    dt = datetime.datetime.now()
    settime = str(dt.day) + "_" + str(dt.month) + "_" + \
            str(dt.year) + "-" + str(dt.hour) + "_" + str(dt.minute)

    list = json.dumps({
        "chatid": chatid,
        "format": convert_format_message(formattext),
        "text": text,
        "datetime": settime
    })

    with open('logs/logs.txt', 'a', encoding="utf-8") as f:
        f.write(list + "\n")
        f.close()
