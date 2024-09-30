import telebot
import os

Token = os.environ["Auth"]
bot = telebot.TeleBot(Token)


@bot.message_handler(content_types="text")
def message_reply(message):
  if message.reply_to_message == None:
    bot.forward_message("1906998334",message.chat.id,message.message_id)
  else:
    bot.send_message(message.reply_to_message.forward_from.id,message.text)
  

#sejsjjsjsjsj

bot.infinity_polling()
