import telebot

bot = telebot.TeleBot('TOKEN')

@bot.message_handler(commands=['start'])
def welcome(message):
	bot.send_message(message.chat.id, 'bot is working')

bot.polling(none_stop=True, interval=0)