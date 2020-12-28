#!/usr/bin/env python3
from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext

TOKEN = 'YOUR TOKEN HERE'

# This function replies with 'Hello <user.first_name>'
def hello(update: Update, context: CallbackContext) -> None:
    update.message.reply_text(f'Hello {update.effective_user.first_name}')

# Insert your token here
updater = Updater(TOKEN)

# Make the hello command run the hello function
updater.dispatcher.add_handler(CommandHandler('hello', hello))

# Connect to Telegram and wait for messages
updater.start_polling()

# Keep the program running until interrupted
updater.idle()
