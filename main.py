import os
import telebot

bot = telebot.Telebot("1917309396:AAGyG22L9uzZ9BgDhUATjjZBSD6tE6MoQrU")

@bot.message_handler(commands=["start"])
def send_welcome(message):
    bot.reply_to(message,"hello i am kavees assistant bot")

@bot.message_handler(commands=["how"])
def send_message(message):
    bot.send_message(message,"i am fine")
   

bot.polling()
