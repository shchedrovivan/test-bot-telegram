# coding=utf-8
# -*- coding: utf-8 -*-
# vim: set fileencoding=utf-8 :
import telebot

# ����� ����
bot = telebot.TeleBot("1497075277:AAFe_2hY8GRxGcgQjCLQL0W5dau84maV-04")


@bot.message_handler(content_types=['text'])
def get_text_messages(message):

   if message.text.lower() == "������":

      bot.send_message(message.from_user.id, "� ���� ������!")


bot.polling(none_stop=True, interval=0)