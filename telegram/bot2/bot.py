import telebot
import requests
import json
import mysql.connector
from game import Game

bot = telebot.TeleBot('2013196815:AAFY68aUD7PlnXJtoNvxDk-Lf8-z9NuUCaQ')

game = None


@bot.message_handler(commands=['start'])
def start(message):
    global game
    game = Game()
    # bot.send_message(message.from_user.id, game.word)
    bot.send_message(message.from_user.id, "Game is started")


@bot.message_handler(commands=['guess'])
def guess1(message):
    msg = bot.send_message(message.from_user.id, 'Enter the letter')
    bot.register_next_step_handler(msg, guess2)


def guess2(message):
    res = game.guess(message.text)
    bot.send_message(message.from_user.id, f"{game.lives} lives left")
    bot.send_message(message.from_user.id, res['message'])
    bot.send_message(message.from_user.id, res['word'])


bot.polling(none_stop=True)