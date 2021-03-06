import telebot
import gtts
from PIL import Image
import config

bot = telebot.TeleBot(config.TOKEN)

code_extensions = ['.py', '.cpp']


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


@bot.message_handler(content_types=['document'])
def reply_document(message):
    # bot.send_message(message.from_user.id, message)
    file_info = bot.get_file(message.document.file_id)
    downloaded_file = bot.download_file(file_info.file_path)
    src = 'received_files/' + message.document.file_name
    with open(src, 'wb') as file:
        file.write(downloaded_file)
    for suffix in code_extensions:
        if file_info.file_path.endswith(suffix):
            with open(src, 'r') as file:
                text = file.read()
                text = f"```{text}```"
                bot.send_message(message.from_user.id, text)
            return
    bot.send_message(message.from_user.id, downloaded_file)


@bot.message_handler(content_types=['photo'])
def reply_photo(message):
    # bot.send_message(message.from_user.id, message)
    fileID = message.photo[-1].file_id
    file = bot.get_file(fileID)
    file_path = file.file_path
    download = bot.download_file(file_path)
    with open('received_files/nature.png', 'wb') as file:
        file.write(download)
    nature = Image.open('received_files/nature.png')
    px = nature.load()
    nature_wb = Image.new('RGB', nature.size)
    for i in range(nature.size[0]):
        for j in range(nature.size[1]):
            grey = (px[i, j][0] + px[i, j][1] + px[i, j][2]) // 3
            nature_wb.putpixel((i, j), (grey, grey, grey))
    nature_wb.save('pillow/nature_wb.png')
    with open('pillow/nature_wb.png', 'rb') as photo:
        bot.send_photo(message.from_user.id, photo)


@bot.message_handler(content_types=['sticker'])
def reply_sticker(message):
    bot.send_sticker(message.from_user.id, message.sticker.file_id)
    bot.send_message(message.from_user.id, message.sticker.emoji)

bot.polling(none_stop=True)