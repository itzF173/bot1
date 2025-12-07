from telebot import types, TeleBot

BOT_API_KEY = "8228930032:AAEP0GbWn7NGGianqeRkWg5cAQODtqyp6Ug"

bot = TeleBot(BOT_API_KEY)

@bot.message_handler(commands=["start"])
def start(message):
    inlineKeyboard = types.InlineKeyboardMarkup() #Создает клавиатуру
    btn1 = types.InlineKeyboardButton("Test",callback_data="btn1")
    btn2 = types.InlineKeyboardButton("Test2",callback_data="btn2")
    #btn3 = types.InlineKeyboardButton("Test3",url="@itzF173_itz")
    inlineKeyboard.row(btn1, btn2)
    #inlineKeyboard.add(btn3)

    #inlineKeyboard.add(btn1)
    #inlineKeyboard.add(btn2)
    bot.send_message(message.chat.id,"Hello",reply_markup=inlineKeyboard)
    #message.chat.get_reply_markup()


@bot.message_handler(commands=['info'])
def cmdInfo(m):
    kl = types.ReplyKeyboardMarkup()
    btn1 = types.KeyboardButton("Test1")
    btn2 = types.KeyboardButton("Test2")
    btn3 = types.KeyboardButton("Test3")
    btn4 = types.KeyboardButton("Test4")
    kl.add(btn1,btn2)
    kl.add(btn3, btn4)
    bot.send_message(m.chat.id, "Ответ", reply_markup=kl)

@bot.message_handler(commands=["doc"])
def docGet(message):
    with open("testPDF.pdf", "rb") as f:
        bot.send_document(message.chat.id,f,visible_file_name="DZ_Po_geometrii.pdf")

@bot.message_handler(commands=["fireImage"])
def fireImage(message):
    with open("justAFire.png", "rb") as f:
        bot.send_photo(message.chat.id, f)




#CONTENTS_TYPES ------------------------------------------------------------------------------
@bot.message_handler(content_types=["text"])
def hello(message):
    #message
    if (message.text == "Kill" or message.text == "Убить"):

        #bot.send_message(message.chat.id,killerName)
        bot.send_message(message.chat.id,"@"+message.from_user.username+" убил "+"@"+message.reply_to_message.from_user.username)
        bot.send_sticker(message.chat.id,"CAACAgIAAxkBAAEPheFo4qceNW4p_wABp3Mc14k_AuvbcxQAAroAAxYtzTx2-eKxl6YmBDYE")
        #print(message)

#m.chat.id
#m.from_user
#m.reply_to_message
#m.from_user.language_code
#m.location
#m.sticker
#m.photo
#m.contact


#----------------------------------------------------------------------------
# @bot.callback_query_handler(func=lambda c:c.data == "btn1")
# def doBtn1(c):
#     bot.send_message(c.message.chat.id,"Ответ на inline кнопку 1")
#
# def isbtn2(message):
#     return message.data == "btn2"
# @bot.callback_query_handler(func=isbtn2)
# def doBtn2(c):
#     bot.send_message(c.message.chat.id, "Ответ на inline кнопку 2")
#



bot.infinity_polling()