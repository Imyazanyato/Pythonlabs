import telebot
import requests

bot = telebot.TeleBot('5699152262:AAHLwYNXA4hgiWRfrBK3pmrEzN8rQ8ABLMQ')


@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, 'Привет! Хочешь новые обои на телефон? Чтобы узнать, как это сделать, напиши мне /help')

@bot.message_handler(commands=['help'])
def help(message):
    bot.send_message(message.chat.id, 'этот бот присылает тебе случайную картинку. Для того, чтобы попробовать, напиши /go')

@bot.message_handler(commands=['go'])
def data(message):
    r = requests.get('https://random.imagecdn.app/900/1600')
    bot.send_photo(message.chat.id, r.url)

bot.polling(none_stop=True)
