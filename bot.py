#!/usr/bin/env python3
import re
import os
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler, CallbackContext, MessageHandler, Filters, CallbackQueryHandler, PicklePersistence

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

def personal(update: Update, context: CallbackContext) -> int:
    # Start building a reply
    reply_list = [f'Hello {update.effective_user.first_name}']
    # If there is user_data in the context
    if context.user_data:
        reply_list.append('I know these things about you')
        # Add all known user_data to the reply
        reply_list.extend([f'Your {key} {value_pair[0]} {value_pair[1]}' for (key, value_pair) in context.user_data.items()])
    else:
        reply_list.append('I don\'t know anything about you.')
    reply_list.extend([
        'Please tell me about yourself.',
        'Use the format: My X is/have/are Y'
    ])
    # Send the built list of reply sentences separated by newline characters
    update.message.reply_text('\n'.join(reply_list))

INFO_REGEX = r'^My (.+) (is|have|are) (.+)$'
def receive_info(update: Update, context: CallbackContext) -> int:
    # Extract the three capture groups
    info = re.match(INFO_REGEX, update.message.text).groups()
    # Using the first capture group as key, the second and third capture group are saved as a pair to the context.user_data
    context.user_data[info[0]] = (info[1], info[2])

    # Quote the information in the reply
    update.message.reply_text(
        f'So your {info[0]} {info[1]} {info[2]}, how interesting'
    )

updater = Updater(os.environ['TOKEN'], persistence=PicklePersistence(filename='bot_data'))

# Make the hello command run the hello function
updater.dispatcher.add_handler(CommandHandler('start', personal))
updater.dispatcher.add_handler(MessageHandler(Filters.regex(INFO_REGEX), receive_info))
updater.dispatcher.add_handler(CommandHandler('hello', hello))
updater.dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, echo))
updater.dispatcher.add_handler(CommandHandler('random', random))
updater.dispatcher.add_handler(CallbackQueryHandler(button))

# Connect to Telegram and wait for messages
updater.start_polling()

# Keep the program running until interrupted
updater.idle()
