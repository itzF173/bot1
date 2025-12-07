from telebot import TeleBot, types
import parser
from datetime import datetime
import time
import pandas as pd
from pandas import pandas
import os
BOTTOKEN = "8244416237:AAHezGXRITlbKHsNQXFJIFWG2dNheB8gR70"
import threading
bot = TeleBot(BOTTOKEN) #связь с ботом

notifyList = []
notifyBooks = []


@bot.message_handler(commands=['start'])
def cmdStart(m):
    bot.send_message(m.chat.id,"Hello, i'm simple Telegram bot!")
    bot.send_sticker(m.chat.id,"CAACAgIAAxkBAAEP2tdpI0HuYLIz7BGyfCBKdfRlQS6EFQAC9jEAAngl6UreoGr8WA6x7TYE")

@bot.message_handler(commands=["info"])
def cmdInfo(m):
    kb1 = types.InlineKeyboardMarkup()
    kb2 = types.ReplyKeyboardMarkup()
    btn1 = types.InlineKeyboardButton("/start", callback_data="start")
    btn2 = types.InlineKeyboardButton("/info",callback_data="info")
    btn3 = types.InlineKeyboardButton("/image",callback_data="image")
    btn4 = types.InlineKeyboardButton("/parse",callback_data="parse")

    btn5 = types.KeyboardButton("/start")
    btn6 = types.KeyboardButton("/info")
    btn7 = types.KeyboardButton("/image")
    btn8 = types.KeyboardButton("/parse")

    kb1.add(btn1, btn2, btn3, btn4)
    kb2.add(btn5, btn6, btn7, btn8)
    bot.send_message(m.chat.id,"Список команд: ", reply_markup=kb1)
    bot.send_message(m.chat.id, "/start - старт бота\n" \
    "/info - информация о боте\n" \
    "/image - генерация сообщений\n" \
    "/parse - поиск товара\n"
    "/notify - подписка на рассылку", reply_markup=kb2)

#@bot.message_handler(commands=["lol"])
def tr():
    #print("Aa")
    while(True):
        #print("A")
        notify()
        #print("A")
        #bot.process_new_poll()
        
        time.sleep(1)
        #bot.stop_polling()
@bot.message_handler(commands=["notify"])
def cmdnotify(m):
    if(len(notifyList)==0 or notifyList.index(m.chat.id)==-1):
        notifyList.append(m.chat.id)
        bot.send_message(m.chat.id, "Please, send calendar document (.xlsx)")
        
    else:
        bot.send_message(m.chat.id, "You always subscribed to notifies!")
    #if(str.find(m.text, "Book.xlsx", 0, len(m.text)-1)):
    
    # if(m.document != None):
    #     b = os.open("Books")
    #     b.__add__(m.document)
    #     notifyList.add(m.chat.id)
    #     print(m.document)
    
@bot.message_handler(content_types=["document"])
def getDocument(m):
    if(notifyList.index(m.chat.id, 0, len(notifyList))!=-1):
        #os.open(m.document.file_name, 1)
        ind = notifyList.index(m.chat.id, 0, len(notifyList))
        
        if(os.path.exists(f"Books\\D{ind}.xlsx")):
            return
        file = bot.get_file(m.document.file_id)
        content = bot.download_file(file.file_path)

        name = m.document.file_name
        newName = os.path.join("Books", name)
        
        with open(newName, "wb") as new_file:
            new_file.write(content)
        #os.rename(new_file.name, f"Books\\D{ind}.xlsx")
        
        bot.send_message(m.chat.id,"Your excel document will use for notify!")
        #os.rename(m.document.file_name,f"Books\\D{ind}.xlsx")
        notifyBooks.append(f"Books\\D{ind}.xlsx")
        #os.close()
        print(m.document.file_name)
        print(m)

@bot.message_handler(content_types=["text"])
def txtHandler(m):
    
    if(str.find(m.text,"/parse", 0, len(m.text)-1)!=-1):
        parser.simpleParser.Parce(m)
        bot.polling()

def checkTime():
    return datetime.now()

def notify():
    g = 0
    print(len(notifyBooks))
    while (g<len(notifyBooks)):
        k = pd.read_excel(notifyBooks[g])
        print(k["WeekDay"][0])
        #0 -> 6
        listChT = k["WeekDay"]
        i = 0
        while (i < len(listChT)):
            hr = str.split(str(k["Time"][i]), ":", 2)[0]
            mn = str.split(str(k["Time"][i]), ":", 2)[1]
            print(hr + " " + str(checkTime().hour))
            print(mn + " " + str(checkTime().minute) + " min")#int(checkTime().minute) == int(mn)
            print(k["NotifyType"][0])
            if(k["NotifyType"][0] == "If"):
                if(int(checkTime().hour) == int(hr)):
                    if(int(checkTime().minute) == int(mn)):
                        print("Alo")
                        bot.send_message(notifyList[g],k["NotifyMSG"][i])
            elif(k["NotifyType"][0] == "While"):
                if(int(checkTime().hour) == int(hr)):
                    #print(int(checkTime().hour) == int(hr))
                    #print(28 == int(mn))
                    #print(checkTime().hour == hr and 28 == int(mn))
                    while(int(checkTime().minute) == int(mn)):
                        #print("Alo2")
                        bot.send_message(notifyList[g],k["NotifyMSG"][i])
                        time.sleep(float(k["NotifyType"][1]))
            i+=1
        g+=1

    # hr = str.split(k["Time"][checkTime().weekday()], "/", 1)[0]
    # mn = str.split(k["Time"][checkTime().weekday()], "/", 1)[1]
    # if(len(listChT)!=-1 and checkTime().hour == hr and checkTime().min == mn):
    #     i = 0
    #     while (i < len(notifyList)):
    #         bot.send_message(notifyList[i], k["Notify"][checkTime().weekday()])
    #         i+=1
def main_thread():
    th = threading.Thread(target=tr)
    th.daemon = True
    th.start()
if __name__ == "__main__":
    print("main")
    print("Бот запущен")
    main_thread()
    bot.polling(non_stop=True)
    #tr()
    

