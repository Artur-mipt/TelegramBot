# -*- coding: utf-8 -*-
from BaseCommands.Describe import describe
from BaseCommands.DescribeWord import describe_word
from BaseCommands.StopWords import stop_words
from BaseCommands.TopN import top_n
from BaseCommands.WordCloud import word_cloud
from BaseCommands.Help import help
from BaseCommands.Start import start
from ParsingPage.BuildingJson import build_json
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import logging
import os


logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)
logger = logging.getLogger(__name__)

TOKEN='TOKEN'
REQUEST_KWARGS={
    'proxy_url': 'http://190.117.115.150:65103',
    # 'urllib3_proxy_kwargs': {
    #    'username': 'telegram',
    #    'password': 'telegram',
    # }
}


def main():

    # using proxy
    updater = Updater(token=TOKEN, request_kwargs=REQUEST_KWARGS)

    dispatcher = updater.dispatcher

    # getting url and depth
    dispatcher.add_handler(MessageHandler(Filters.text, build_json))

    # adding commands to dispatcher
    dispatcher.add_handler(CommandHandler('start', start))
    dispatcher.add_handler(CommandHandler('help', help))
    dispatcher.add_handler(CommandHandler('stop_words', stop_words))
    dispatcher.add_handler(CommandHandler('top', top_n))
    dispatcher.add_handler(CommandHandler('word_cloud', word_cloud))
    dispatcher.add_handler(CommandHandler('describe', describe))
    dispatcher.add_handler(CommandHandler('describe_word', describe_word))

    # starting bot
    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()
