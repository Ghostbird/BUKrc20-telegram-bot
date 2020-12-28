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
