import telebot
Token = ${{secrets.Auth}}
bot = telebot.TeleBot(Token)


@bot.message_handler(content_types="text")
def message_reply(message):
  bot.forward_message("1906998334",message.chat.id,message.message_id)


bot.infinity_polling()
