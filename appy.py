import telebot
from config import *
from extensions import *


bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start'])
def start(message: telebot.types.Message):
    text = 'Hello! Welcome to AmiXE bot. The bot will help you to search \
the currency exchange price of €, $ and ₽ using the service from CryptoCompare.com. Please enter /help command for further information.'
    bot.reply_to(message, text)


@bot.message_handler(commands=['help'])
def help(message: telebot.types.Message):
    text = 'Please enter the command in the following format: \n<currency name> \
<which currency to convert> \
<amount of currency to be converted> \
<(e.g. dollar ruble 1)>\nTo see a list of all available currencies, please use the following command: /values'
    bot.reply_to(message, text)


@bot.message_handler(commands=['values'])
def values(message: telebot.types.Message):
    text = 'The following available currencies:'
    for key in keys.keys():
        text = '\n'.join((text, key, ))
    bot.reply_to(message, text)


@bot.message_handler(content_types=['text', ])
def get_price(message: telebot.types.Message):
    try:
        values = message.text.split(' ')

        if len(values) != 3:
            raise ConvertionException('There are to many parameters.')

        quote, base, amount = values
        total_base = CryptoConverter.get_price(quote, base, amount)
    except ConvertionException as e:
        bot.reply_to(message, f'User error.\n{e}')
    except Exception as e:
        bot.reply_to(message, f'It is impossible to process the command.\n{e}')
    else:
        text = f'Price {amount} {quote} in {base} - {total_base}'
        bot.send_message(message.chat.id, text)


bot.polling()
