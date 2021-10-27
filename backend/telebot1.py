from logging import lastResort
import telebot
import time
import requests as rq
from telebot import types
from comands import bot_commands

#-------------------------------
TOKEN = '2088510344:AAHeQKqIb2xcpNyYFI2GGl0URyv58X_17xw'
bot = telebot.TeleBot(TOKEN)
#-------------------------------

@bot.message_handler(commands = ['start'])
def start(message):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item1 = types.KeyboardButton(bot_commands['start'])
        markup.add(item1)
        bot.send_message(message.chat.id,'AI RLEX : ',reply_markup = markup) 
                                         
@bot.message_handler(content_types = ['text'])
def bot_message(message):   
    if message.text in bot_commands :
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        if len(bot_commands[message.text]) == 3 :
            item1 = types.KeyboardButton(bot_commands[message.text][2]) 
            markup.add(item1)
             
        if len(bot_commands[message.text]) == 4 :
            item1 = types.KeyboardButton(bot_commands[message.text][4])
            item2 = types.KeyboardButton(bot_commands[message.text][3])  
            markup.add(item1,item2) 
            
        if len (bot_commands[message.text]) == 5:
            item1 = types.KeyboardButton(bot_commands[message.text][2])
            item2 = types.KeyboardButton(bot_commands[message.text][3])
            item3 = types.KeyboardButton(bot_commands[message.text][4])                         
            markup.add(item1,item2,item3)
            
        if len (bot_commands[message.text]) == 6 :
            item1 = types.KeyboardButton(bot_commands[message.text][2])
            item2 = types.KeyboardButton(bot_commands[message.text][3])
            item3 = types.KeyboardButton(bot_commands[message.text][4]) 
            item4 = types.KeyboardButton(bot_commands[message.text][5])
            markup.add(item1,item2,item3,item4)
            
        bot.send_message(message.chat.id,bot_commands[message.text][0],reply_markup=markup)   
    else:
        bot.send_message(message.chat.id, f"{message.text} - неизвестная команда" )

#-------------------------------
 
bot.polling(none_stop=True)