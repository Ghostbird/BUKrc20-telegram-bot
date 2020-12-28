# Python Telegram bot tutorial

In this tutorial you're going to learn how to use Python to make a telegram bot.

## Requirements

For this tutorial you need a computer with Python 3.7 or higher installed. You can  download it directly from the [Python website](https://python.org/).

Pay attention that on *Windows* the Python installer must be run as *Administrator* to correctly install `pip` into your `PATH` to simplify the next step.

Next you'll need to install the `python-telegram-bot` library that provides most of the Telegram bot functionality. If your environment is set up correctly you can do that by running the command:

```bash
pip install python-telegram-bot
```

Finally you'll need a programming environment. While you can use any text editor and terminal combination, In this tutorial I use [Visual Studio Code](https://code.visualstudio.com/). Once you have VSCode installed, click the *Extensions* menu or press <kbd>Ctrl</kbd><kbd>Shift</kbd><kbd>X</kbd> and search for and install the *Python* extension by Microsoft.

## Getting started

Next you're going to have to download this project's [start point](https://github.com/Ghostbird/BUKrc20-telegram-bot/archive/0-getting-started.zip). Extract the ZIP somewhere on you computer.

Now open VSCode and select *File* » *Open Folder* and open the folder that you just extracted.

### Ensure it runs

Open the file `bot.py` and press <kdb>F5</kbd>. If everything went well, you should see a message that says:

> `Exception has occurred: InvalidToken`

That means the program starts correctly and you're ready to create your Telegram bot.

## Create your bot

To create your own bot you'll need to do two things. You need to register a bot with Telegram.
Then you need to make the Python program connect to Telegram and log in as that bot.

### An offer you can't refuse

To create a telegram bot, search for *Botfather* on Telegram and enter a conversation with him.

Botfather is the original Telegram bot and talking to him is currently the only way to create new Telegram bots.

Use the `/newbot` command to start the process of creating a new bot.

Next enter a display name for your bot. I'm going to use *BUK Telegram tutorial*.

Then enter a username for the bot. Keep in mind that it *must* end with `bot`.

Once you've done that, the Botfather will give you a *Token*.

**Keep the token secret!** This token acts as a combined username and password for your bot. If someone else has it, they can impersonate your bot. If someone has stolen your token, you can talk to the Botfather and generate a new token. This is like a password change. The old token stops working, and the Bothfather gives you a new token for your bot.

This is why I can safely show my token in the video tutorial. I have already replaced it with a new one after recording the video.

You might have noticed that the Python program contains a line that says:

```python3
TOKEN = 'YOUR TOKEN HERE'
```

Insert your token there between the quotes.

### First run

Now that you have registered you bot and added the token to the program, test that it works.

Press <kbd>F5</kbd> to start the bot program.

Search for your bot in Telegram. Once you find it, open the conversation and click the *Start* button. This is actually a security feature. No bot is allowed to talk to you unless you *Start* to talk to it first.

Once you have started the conversation, you can now send `/hello` to the bot. If everything works correctly, the bot should reply.

### Register the command

Talk to the Botfather and tell him `/setcommands`. He'll ask you to specify the commands in a specific format. In this case send:
```
hello - A simple greeting
```
Now when you click the <kbd>/</kbd> button in Telegram the `/hello` command will be available with explanation.

It is not necessary, nor always practical, to register commands, but it can be nice to users of your bot.

## Actual functionality

To make a bot useful, it needs to actually provide some interesting service. One of the reasons this tutorial is a bit more advanced, is that you'll have to decide for yourself what exactly you bot is going to do. However before you can do that, you'll need to understand the basics of how to handle Telegram messages.

### Handlers

Having a look at the current program, you'll see the line:

```python3
updater.dispatcher.add_handler(CommandHandler('hello', hello))
```

Here we add a *handler*. In this case we add a command handler that runs the `hello` function when the user sends the *command* `hello` to the bot.

If you want to know more about what handlers are available, check [documentation](https://python-telegram-bot.readthedocs.io/en/stable/telegram.html#handlers) of the telegram-bot-api library.

If you're serious about writing a Telegram bot, you're going to spend some time digging through that documentation. However, that is very technical documentation. Once you really are going to write your own thing I can recommend first looking at:

- The [python-telegram-bot examples](https://github.com/python-telegram-bot/python-telegram-bot/tree/master/examples)
- The [python-telegram-bot code snippets](https://github.com/python-telegram-bot/python-telegram-bot/wiki/Code-snippets#general-code-snippets) on the wiki


For now let's instead focus on what we can do inside the handler's function. The current hello function looks like this:

```python3
def hello(update: Update, context: CallbackContext) -> None:
  update.message.reply_text(f'Hello {update.effective_user.first_name}')
```

What you can see here is that you receive two things in the handler. The `update` and the `context`. In this case we only use the `update` to send a textual reply using the `update.message.reply_text` function. The text we send is `Hello ` followed by the value of `update.effective_user.first_name`. Which is the first name of the user that sent the hello command that caused this function to start.

### Message handling

Let's add a different handler. The basic MessageHandler handles any kind of message, but we can filter those to only handle specific messages. In this case, we're going to add a handler that simply echoes back whatever the user said.

For this we need to do three things:

- Define an echo function
- Handle messages using the echo function
- Import the necessary parts from the library to make it work

First we'll write the echo function, you can place it below the `hello` function:

```python3
def echo(update: Update, context: CallbackContext) -> None:
    update.message.reply_text(update.message.text)
```

As you can see, it simply replies with the text value of the received message.

Next we'll have to make sure that we run this function when we receive a message that contains text and is *not a command*. Add this below the line where we add the hello CommandHandler:

```python3
updater.dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, echo))
```

This adds a message handler that executes the `echo` function but only for incoming messagest that match the filters `text` and not `command`.

Finally to make this actually work, we need to immport the correct parts of the library.

Change the `import from telegram.ext` line near the top of the file, to read:
```python3
from telegram.ext import Updater, CommandHandler, CallbackContext, MessageHandler, Filters
```

Now start you bot and see whether it works. If you did it correctly, whenever you send it `/hello` it will reply as it did before. When you send it something else, it will repeat that text back.

### Adding sarcasm

An echo bot is nice, but we can do better. We can make the bot sarcastic.

![sarcasm](https://user-images.githubusercontent.com/1202149/103220507-52ac5300-4918-11eb-8b27-a408fa0e7132.jpg)

Let's change the echo function to:

```python3
def echo(update: Update, context: CallbackContext) -> None:
    update.message.reply_text(
        ''.join([l.upper() if i % 2 == 0 else l for (i, l) in enumerate(update.message.text)])
    )
```

Now that's quite a compact piece of code, that warrants some explanation.

`enumerate(update.message.text)` changes the input text into a list of pairs. These pairs consist of an index and the letter. So the text `echo` is turned into `[(0, 'e'), (1, 'c'), (2, 'h'), (3, '0')]`.
The `for (i, l) in enumerate...` part states that we're going to loop over those pairs. In each pair we call the first entry, the number, `i` and the second entry, the letter, `l`.
`l.upper() if i % 2 == 0 else l` is run for each of those `i, l` pairs and checks whether `i` is even by using `% 2` to get the remainder after division by two, then using `== 0` to ensure the remainder is zero. If that is true, it turns makes `l` into an upper case letter. `else l` means that if `i` is odd, `l` is not changed.
This means that `[(0, 'e'), (1, 'c'), (2, 'h'), (3, '0')]` is turned into `['E', 'c', 'H', 'o']`. Finally the surrounding `''.join(...)` takes the list of letters we now have and turns them back into a single line of text by putting `''` (nothing) in between each part of the list. Hence `['E', 'c', 'H', 'o']` is turned into `EcHo`.

Now you have made you first bot that actually does somthing with the information the user sent you. Give it a try!

## Callback query handling

One nice feature of Telegram is that you can send people buttons that they can click. Another nice feature is that you can send an emoji to make a random number. Let's combine those to make a command that lets you choose the random number emoji to use.

First the `random` function. This function sends you a text reply that asks you to choose one of the options.
It also shows an `InlineKeyboardMarkup` which contains several `InlineKeyboardButton`s. On the first row we have a button that reads *Basketball* and whose value is the basketball emoji.
On the second line we have first a button for *Dice* whose value is a die emoji and next a button for *Darts* whose value is a bullseye emoji.

```python3
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
```

Don't forget to add the command handler:

```python3
updater.dispatcher.add_handler(CommandHandler('random', random))
```

Your imports should start with:

```python3
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
```

If we try this now, we can see the buttons, clicking them shows a clock icon on the clicked button, but nothing happens. We should add a handler for the button click.

Once such a button is pressed, the result should be handled in another function. Here we first mark the *question* we posed by showing the buttons as answered by calling `update.callback_query.answer()`. Telegram requires that we do this.
Next we edit the original message where we showed the buttons, and we replace the list of buttons with an empty list. This removes the buttons, so that the user can only click them once.
Finally we reply to the button click by sending the emoji value of the button that was pressed using `send_dice` to use it as a random number generation animation.

```python3
def button(update: Update, context: CallbackContext) -> None:
    # Must call answer!
    update.callback_query.answer()
    # Remove buttons
    update.callback_query.message.edit_reply_markup(
        reply_markup=InlineKeyboardMarkup([])
    )
    update.callback_query.message.reply_dice(emoji=update.callback_query.data)
```

Don't forget to add these handlers:

```python3
updater.dispatcher.add_handler(CallbackQueryHandler(button))
```

And make sure you have all these imports:

```python3
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler, CallbackContext, MessageHandler, Filters, CallbackQueryHandler
```

Give it a try. First send `/random`. Then click one of the buttons. If everything went well, the buttons are replaced by an animated random number of your choice.

## It's all about the context

Now we have learned to talk back and forth about with the bot. However it would be nice if the bot could reply based on something we told it before.

The library we're using provides the `context.user_data` for this purpose. Let's make use of it.

This function checks what it knows about the user, and lists it. Then it asks for more information.

```python3
def personal(update: Update, context: CallbackContext) -> int:
    reply_list = [f'Hello {update.effective_user.first_name}']
    if context.user_data:
        reply_list.append('I know these things about you')
        reply_list.extend([f'Your {key} {value_pair[0]} {value_pair[1]}' for (key, value_pair) in context.user_data.items()])
    else:
        reply_list.append('I don\'t know anything about you.')
    reply_list.extend([
        'Please tell me about yourself.',
        'Use the format: My X is/have/are Y'
    ])
    update.message.reply_text('\n'.join(reply_list))
```

Let's run that command whenever the user starts talking to the bot or runs the `/start` command:

```python3
updater.dispatcher.add_handler(CommandHandler('start', personal))
```

If you try it out, you'll quickly realise that you only get sarcastic remarks back from your bot. We haven't actually written functionality that lets us tell the bot something about ourselves.

This function works on messages matching the given *Regular expression*. Which is a method of expressing very simple grammars for text. The `INFO_REGEX` matches sentences such as *My head is large*, *My parents have children*, *My shoes are too small*. Besides that, thanks to the placement of the brackets, it will save the parts inside the brackets as *capture groups*. Hence the sentence *My shoes are too small* yields these groups: `['shoes', 'are', 'too small']

We save this to the `context.user_data` in such a way that the sentence *My hands are too large* results in the data being saved as if we executed: `context.user_data['hands'] = ('are', 'too large')`

```python3
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
```

Now we add a handler that runs this function, but the filter specifies that the function should only be executed for messages that match the `INFO_REGEX`.

**Important** Put this line *before* the line that adds the sarcastic reply handler. Because the first matching handler is used. And the sarcastic reply matches any text that is not a command.

```python3
updater.dispatcher.add_handler(MessageHandler(Filters.regex(INFO_REGEX), receive_info))
```

Finally to make regular expressions work we must import that functionality by adding this line to imports:

```python3
import re
```

Start you bot, and if everything went well, you can run `/start` and it will tell you that it knows nothing about you. You can then tell it things about you.
If you run `/start` again, he will reply with what he knows about you.
