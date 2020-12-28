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
