import telebot
import os
Token = os.environ["Auth"]
bot = telebot.TeleBot(Token)


@bot.message_handler(content_types="text" and func=lambda message: message.reply_to_message is None)
def message_reply(message):
  bot.forward_message("1906998334",message.chat.id,message.message_id)
  bot.send_message("1906998334", message)


    


bot.infinity_polling()
