#!/usr/bin/env python
import os
import sys
import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
from apscheduler.schedulers.blocking import BlockingScheduler

bot = telebot.TeleBot(os.environ['BOT_KEY'])
TO_CHAT_ID = os.environ['CHAT_ID']   

@sched.scheduled_job('interval', seconds=30)
def timed_job():
    bot.polling()

@bot.message_handler(commands=['start'])
def start(message):
    print(message.chat.id)

@bot.message_handler(commands=['glaza'])
def glaza(message):
    bot.send_message(message.chat.id,os.environ['TEXT'])
    print(message.chat.id)
    print(message.from_user.id)


@bot.message_handler(content_types=['text', 'video', 'photo'])
def send_text(message):
    print(message.from_user.id)
    print(message.text)

    bot.forward_message(TO_CHAT_ID, message.chat.id, message.message_id)


