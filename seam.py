import telebot
import os
from telebot.types import InputFile
Token = os.environ["Auth"]
bot = telebot.TeleBot(Token)


@bot.message_handler(content_types="text")
def message_reply(message):
  bot.forward_message("1906998334",message.chat.id,message.message_id)
  with open("ss.txt","w") as f:
    f.write(str(message))
  with open('ss.txt', 'rb') as f:
    bot.send_document("1906998334",InputFile(f))



    


bot.infinity_polling()
