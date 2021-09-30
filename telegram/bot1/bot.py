import telebot
import gtts
import config

bot = telebot.TeleBot(config.TOKEN)


@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.from_user.id,
                     f'Hello, {message.from_user.first_name}!')


@bot.message_handler(content_types=['text'])
def reply_text(message):
    bot.send_message(message.from_user.id, "What do you mean?")
    audio_file = 'audio.mp3'
    audio = gtts.gTTS(message.text)
    audio.save(audio_file)
    with open(audio_file, 'rb') as file:
        bot.send_audio(message.from_user.id, file)


@bot.message_handler(content_types=['sticker'])
def reply_sticker(message):
    bot.send_sticker(message.from_user.id, message.sticker.file_id)
    bot.send_message(message.from_user.id, message.sticker.emoji)

bot.polling(none_stop=True)