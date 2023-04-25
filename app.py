from telegram.ext.updater import Updater
from telegram.update import Update
from telegram.ext.callbackcontext import CallbackContext
from telegram.ext.commandhandler import CommandHandler
from telegram.ext.messagehandler import MessageHandler
from telegram.ext.filters import Filters

# initialize API token - Telegram
telegram_token = '3237:yVpuk'

# create an Updater object with the token
updater = Updater(token=telegram_token, use_context=True)
dispatcher = updater.dispatcher

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
      """)
  
def contact(update, context):
  update.message.reply_text('Blog link: https://okandasteven.com')
  

dispatcher = updater.dispatcher
updater.dispatcher.add_handler(CommandHandler('start', start))
updater.dispatcher.add_handler(CommandHandler('help', help))

updater.dispatcher.add_handler(CommandHandler('contact',contact))
updater.start_polling()  # Start the bot
updater.idle() # Wait for the script to be stopped; this will stop the bot
