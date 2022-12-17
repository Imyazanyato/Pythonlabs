import telebot
import requests

bot = telebot.TeleBot('5699152262:AAHLwYNXA4hgiWRfrBK3pmrEzN8rQ8ABLMQ')


@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, 'Привет! Хочешь узнать какой нибудь интересный факт? Чтобы узнать, как это сделать, напиши мне /help')

@bot.message_handler(commands=['help'])
def help(message):
    bot.send_message(message.chat.id, 'этот бот присылает тебе случайную дату и интересный факт, который произошел в этот день. Для того, чтобы попробовать, напиши /data')

@bot.message_handler(commands=['data'])
def data(message):
    r = requests.get('http://numbersapi.com/random/date')
    url = r.url
    bot.send_message(message.chat.id, url)    

bot.polling(none_stop=True)