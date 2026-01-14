import telebot

bot = telebot.TeleBot("8595334950:AAHpM8CNSUYkcnhoBtwECtfgOWBnjKwBWl4", parse_mode='MarkdownV2')

@bot.message_handler(commands=['start'])
def send_welcome(message):
	bot.reply_to(message, "/help")

@bot.message_handler(commands=['obb'])
def send_welcome(message):
	bot.reply_to(message, "Вот вам obb на пабг [СЮДА](https://t.me/obb_ot_luksika)")

@bot.message_handler(commands=['PoSuiCN'])
def send_welcome(message):
	bot.reply_to(message, "Вот вам PoSuiCN на пабг [СЮДА](https://t.me/PoSuiCN_luksik)")
	
@bot.message_handler(commands=['help'])
def send_welcome(message):
	bot.reply_to(message, "/obb /PoSuiCN")
	
bot.infinity_polling()
