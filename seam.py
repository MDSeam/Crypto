import telebot
Token = "6600626960:AAHr-8qG0VEhlLmhI5hsCnMayUpymcL07-8"
bot = telebot.TeleBot(Token)


@bot.message_handler(content_types="text")
def message_reply(message):
  bot.forward_message(message.chat.id,"1906998334",message.message_id)


bot.infinity_polling()
