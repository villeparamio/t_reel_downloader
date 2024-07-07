import os
import re
import logging
import instaloader
import telebot

# Inicializa Instaloader
L = instaloader.Instaloader()

BOT_TOKEN = 'YOUR_TOKEN_HERE'
bot = telebot.TeleBot(BOT_TOKEN)

# Configura el logger
logging.basicConfig(filename='insta_bot.log', level=logging.INFO, format='%(asctime)s - %(name)s - %(message)s')
logging.info(f"Bot iniciado")

def is_valid_reel_url(url):
    pattern = r'^https?://(www\.)?instagram\.com/reel/[A-Za-z0-9_-]+/?(\?.*)?$'
    return re.match(pattern, url) is not None

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Hola! Envíame el enlace de un reel de instagram y te lo descargaré")

@bot.message_handler(commands=['help'])
def send_welcome(message):
    bot.reply_to(message, "Hola! Envíame el enlace de un reel de instagram y te lo descargaré")

@bot.message_handler(commands=['chatid'])
def send_chatid(message):
    chat_id = message.chat.id
    bot.reply_to(message, f"Your chat ID is: {chat_id}")


@bot.message_handler(func=lambda message: True)
def handle_message(message):
    reel_url = message.text
    user = message.from_user
    user_info = f"Usuario: {user.id}, Username: {user.username}, Nombre: {user.first_name} {user.last_name}"
    logging.info(f"{user_info} - URL recibida: {reel_url}")
    if is_valid_reel_url(reel_url):
        try:
            bot.reply_to(message, f"Procesando descarga: {reel_url}")
            shortcode = reel_url.split("/")[-2]
            post = instaloader.Post.from_shortcode(L.context, shortcode)
            L.download_post(post, target=shortcode)
            downloaded_files = os.listdir(shortcode)
            video_file = None
            for file in downloaded_files:
                if file.endswith('.mp4'):
                    video_file = os.path.join(shortcode, file)
                    break
            
            if video_file and os.path.exists(video_file):
                with open(video_file, 'rb') as video:
                    bot.send_video(message.chat.id, video)
                logging.info(f"{user_info} - Reel Descargado")
                for file in downloaded_files:
                    os.remove(os.path.join(shortcode, file))
                os.rmdir(shortcode)
            else:
                bot.reply_to(message, "Ha habido un problema con la descarga. El archivo de vídeo no existe.")
                logging.error(f"{user_info} - Descarga fallida. El archivo de video no existe.")
        except Exception as e:
            bot.reply_to(message, f"Ha ocurrido un error: El reel no existe o es de un perfil privado")
            logging.error(f"{user_info} - Ha ocurrido un error: {e}")
    else:
        bot.reply_to(message, "No has enviado un enlace de reel válido. Asegurate que se vea como este: \nhttps://www.instagram.com/reel/C5UiWfWtvEI/?igsh=eXdxZ2JjMXp3OHk3")
        logging.warning(f"{user_info} - URL no valida: {reel_url}")

bot.polling()