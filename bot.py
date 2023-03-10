import telebot
from telebot import types
bot = telebot.TeleBot('6292723133:AAGm6XQXBH7I7beN9xBmU6Cf7NU94RXC9O0')

@bot.message_handler(commands=['start',])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
    item1 = types.KeyboardButton('ОП')
    item2 = types.KeyboardButton('ВМ')
    item3 = types.KeyboardButton('Алгоритмы')
    item4 = types.KeyboardButton('Дискретка')
    item5 = types.KeyboardButton('Будова ПК')
    item6 = types.KeyboardButton('ОПЗ')
    item7 = types.KeyboardButton('ООП')
    item8 = types.KeyboardButton('Основи ІПЗ')

    markup.add(item1, item2, item3, item4, item5, item6, item7, item8 )

    bot.send_message(message.chat.id, 'Привет, {0.first_name}'.format(message.from_user), reply_markup =markup)

@bot.message_handler(content_types = ['text'])
def bot_message(message):
    if message.chat.type in ["group", "private"]:
        if message.text == 'ОП':
            bot.send_message(message.chat.id, 'https://us02web.zoom.us/j/3508337995?pwd=cEtER01Wc1JRQ005Y2haK0lTVkNIQT09',reply_markup=types.ReplyKeyboardRemove())
        elif message.text == 'ВМ':
            bot.send_message(message.chat.id, 'https://us04web.zoom.us/j/9465832762?pwd=MEJ0TlFXRk9RMk5NblFIZnNRYVF0Zz09',reply_markup=types.ReplyKeyboardRemove())                 
        elif message.text == 'Алгоритмы':
            bot.send_message(message.chat.id, 'https://us02web.zoom.us/j/3508337995?pwd=cEtER01Wc1JRQ005Y2haK0lTVkNIQT09',reply_markup=types.ReplyKeyboardRemove()) 
        elif message.text == 'Дискретка':
            bot.send_message(message.chat.id, 'https://us04web.zoom.us/j/6608785248?pwd=T2tXU3RiZitXMCtUdmc2RSs5K3UrZz09',reply_markup=types.ReplyKeyboardRemove())
        elif message.text == 'Будова ПК':
            bot.send_message(message.chat.id, 'https://us02web.zoom.us/j/2011158305?pwd=dm5yckxqdFdkZlhrcytCTFpZbGhkZz09',reply_markup=types.ReplyKeyboardRemove())
        elif message.text == 'ОПЗ':
            bot.send_message(message.chat.id, ' https://us04web.zoom.us/j/6608785248?pwd=T2tXU3RiZitXMCtUdmc2RSs5K3UrZz09',reply_markup=types.ReplyKeyboardRemove())     
        elif message.text == 'ООП':
            bot.send_message(message.chat.id, ' https://us04web.zoom.us/j/76959695211?pwd=RGVTc3FFK0toSVhlWnFaWTFtcGpLZz09',reply_markup=types.ReplyKeyboardRemove()) 
        elif message.text == 'Основи ІПЗ':
            bot.send_message(message.chat.id, 'https://us02web.zoom.us/j/3508337995?pwd=cEtER01Wc1JRQ005Y2haK0lTVkNIQT09',reply_markup=types.ReplyKeyboardRemove())                                                                                                   
bot.polling(none_stop=True)    