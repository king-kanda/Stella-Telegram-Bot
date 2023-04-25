from telegram import Update
from telegram.ext import Updater, CommandHandler
import sys

# Initialize API token - Telegram
telegram_token = '5###########################k'

# Creating objects to perform a task
updater = Updater(telegram_token , use_context=True)
dispatcher = updater.dispatcher

# Define function to handle /start command
def start(update, context):
    update.message.reply_text('Hello! Welcome to the Stella BOT! Enjoy the resource!')
    update.message.reply_text('Type /help for the content to display!')
    update.message.reply_text('Happy Learning!')

# Define function to handle /help command
def help(update, context):
    update.message.reply_text(
        """
        /start -> Welcome to the Stella BOT!
        /help -> This particular message
        /position -> Current position in the roster
        /contact -> contact information
        """)

# Define function to handle /contact command
def contact(update, context):
    update.message.reply_text('Blog link: https://okandasteven.com')

# Add handlers for commands
dispatcher.add_handler(CommandHandler('start', start))
dispatcher.add_handler(CommandHandler('help', help))
dispatcher.add_handler(CommandHandler('contact', contact))

# Start the bot
updater.start_polling()

# Run the bot until you press Ctrl-C
updater.idle()
