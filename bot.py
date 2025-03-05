import os
import telebot
from dotenv import load_dotenv
from testWeather import get_weather

load_dotenv()
BOT_TOKEN = os.getenv('BOT_TOKEN')
bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(commands=['start', 'hello'])
def send_welcome(message):
    bot.reply_to(message, "Hello! I am a CLOUDFATHER\n\nEnter the CITY you want weather information for")


@bot.message_handler(commands=['City'])
def city_handler(message):
    city = message.text
    weather_info = get_weather(city)
    text = 'Getting weather information for' + city
    sent_msg = bot.reply_to(message.chat.id, text, parse_mode='Markdown')
    

bot.infinity_polling()