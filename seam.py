import telebot
import os
Token = os.environ["Auth"]
bot = telebot.TeleBot(Token)


@bot.message_handler(content_types="text" and func=lambda message: message.reply_to_message is None)
def message_reply(message):
  bot.forward_message("1906998334",message.chat.id,message.message_id)

# Handler for reply messages to forwarded messages
@bot.message_handler(func=lambda message: message.reply_to_message is not None)
def reply_with_forwarded_info(message):
    original_message = message.reply_to_message
    
    # Check if the original message was forwarded
    if original_message.forward_from or original_message.forward_from_chat:
        forward_info = "This message was forwarded from:\n"
        
        if original_message.forward_from:
            forward_info += f"User: {original_message.forward_from.first_name} (ID: {original_message.forward_from.id})\n"
        if original_message.forward_from_chat:
            forward_info += f"Chat: {original_message.forward_from_chat.title} (ID: {original_message.forward_from_chat.id})\n"
        
        forward_info += f"Message text: {original_message.text}"
    else:
        forward_info = "This message is not a forwarded message."
    
    bot.reply_to(message, forward_info)
    


bot.infinity_polling()
