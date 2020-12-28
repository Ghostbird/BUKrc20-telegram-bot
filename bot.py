#!/usr/bin/env python3
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler, CallbackContext, MessageHandler, Filters, CallbackQueryHandler

TOKEN = 'YOUR TOKEN HERE'

# This function replies with 'Hello <user.first_name>'
def hello(update: Update, context: CallbackContext) -> None:
    update.message.reply_text(f'Hello {update.effective_user.first_name}')

def echo(update: Update, context: CallbackContext) -> None:
    update.message.reply_text(
        ''.join([l.upper() if i % 2 == 0 else l for (i, l) in enumerate(update.message.text)])
    )

def random(update: Update, context: CallbackContext) -> None:
    reply_buttons = InlineKeyboardMarkup([
        [InlineKeyboardButton("Basketball", callback_data='🏀')],
        [
            InlineKeyboardButton("Dice", callback_data='🎲'),
            InlineKeyboardButton("Darts", callback_data='🎯'),
        ]
    ])
    update.message.reply_text(
        f'Hello {update.effective_user.first_name}, please choose an option:',
        reply_markup=reply_buttons
    )


def button(update: Update, context: CallbackContext) -> None:
    # Must call answer!
    update.callback_query.answer()
    # Remove buttons
    update.callback_query.message.edit_reply_markup(
        reply_markup=InlineKeyboardMarkup([])
    )
    update.callback_query.message.reply_dice(emoji=update.callback_query.data)

# Insert your token here
updater = Updater(TOKEN)

# Make the hello command run the hello function
updater.dispatcher.add_handler(CommandHandler('hello', hello))
updater.dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, echo))
updater.dispatcher.add_handler(CommandHandler('random', random))
updater.dispatcher.add_handler(CallbackQueryHandler(button))

# Connect to Telegram and wait for messages
updater.start_polling()

# Keep the program running until interrupted
updater.idle()
