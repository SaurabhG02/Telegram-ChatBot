import logging
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import  apiai
import  json

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.DEBUG)

logger = logging.getLogger(__name__)
updater = Updater(token='1031902285:AAGHOSKOdiiNH7Ml13P8UuB7qBWfpCGVq30')
dispatcher = updater.dispatcher

def startCommand(bot, context):
    bot.send_message(chat_id=context.message.chat_id, text='Hello  Saurabh')

def textMessage(bot, context):
    request = apiai.ApiAI('68a7726c463a449f916d10e02b3552ed').text_request()
    request.lang = 'en'
    request.session_id = 'TextAiBot'
    request.query = context.message.text
    #bot.send_message(chat_id=context.message.chat_id, text=response)

    response_json = json.loads(request.getresponse().read().decode('utf-8'))
    response = response_json['result']['fulfillment']['speech']

    if response:
        bot.send_message(chat_id=context.message.chat_id, text=response)
    else:
        bot.send_message(chat_id=context.me.chat_id, text='I do not understand you')

#Handler
start_command_handler = CommandHandler('hello', startCommand)
text_message_handler = MessageHandler(Filters.text, textMessage)

dispatcher.add_handler(start_command_handler)
dispatcher.add_handler(text_message_handler)

updater.start_polling(clean=True)

updater.idle()