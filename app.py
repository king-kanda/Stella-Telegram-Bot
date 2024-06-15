import os
from telegram.ext import Application, CommandHandler
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Get the token from the environment variable
telegram_token = os.getenv('token')

if not telegram_token:
    raise ValueError("No TELEGRAM_TOKEN found in environment variables")

# Create an Application object with the token
application = Application.builder().token(telegram_token).build()

def start(update, context):
    update.message.reply_text('Hello! Welcome to anandsdata BOT! Enjoy the resource!')
    update.message.reply_text('Type /help for the content to display!')
    update.message.reply_text('Happy Learning!')

def help(update, context):
    update.message.reply_text(
        """
        /start -> Welcome to the anandsdata BOT!
        /help -> This particular message
        /position -> Current position in the roster
        /contact -> contact information
        """
    )

def contact(update, context):
    update.message.reply_text('Blog link: https://okandasteven.com')

# Add command handlers to the application
application.add_handler(CommandHandler('start', start))
application.add_handler(CommandHandler('help', help))
application.add_handler(CommandHandler('contact', contact))

# Start the bot
application.run_polling()
