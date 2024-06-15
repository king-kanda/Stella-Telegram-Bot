import os
from telegram.ext import Application, CommandHandler
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Get the token from the environment variable
TELEGRAM_TOKEN = os.getenv('token')

def handle_message(update, context):
  chat_id = update.effective_chat.id
  text = "Hello! "
  context.bot.send_message(chat_id=chat_id, text=text)

def main():
  updater = telegram.Updater(token=TELEGRAM_TOKEN)
  dispatcher = updater.dispatcher

  # Handle any message with the `handle_message` function
  dispatcher.add_handler(telegram.ext.MessageHandler(telegram.ext.Filters.text, handle_message))

  updater.start_polling()
  updater.idle()