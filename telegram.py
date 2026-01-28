from telebot import TeleBot
from config import TELEGRAM_TOKEN
from model import ask_question

bot = TeleBot(token=TELEGRAM_TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, "Hi! I am your QA bot. Ask me anything.")

@bot.message_handler(func=lambda message: True)
def handle_message(message):
    question = message.text
    chat_id = message.chat.id 
    answer = ask_question(question, chat_id)
    bot.send_message(chat_id, answer)

bot.polling()
