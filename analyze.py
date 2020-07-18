#!python3
# -*- coding: utf-8 -*-

import os
import re
from pprint import pprint
# from app.wap_extract import getMessages
import app.data_handling as WAPData
import app.whatsapp_parser as WAParser
from collections import OrderedDict

# To get rid of file extension when making graphs
file_split = re.compile(r'(.*)(.[a-zA-Z0-9]{3,4})')

text_to_analyze = WAPData.loadData()

# Collect data
date_dictionary, time_dictionary, person_dictionary, word_dictionary, number_of_messages = WAParser.collect_data(
    text_to_analyze
)

# Sort all Dictionaries here
word_dictionary = OrderedDict(word_dictionary.most_common(20))
date_dictionary = WAParser.sort_dictionary(date_dictionary)
time_dictionary = WAParser.sort_dictionary(time_dictionary, 'key')
person_dictionary = WAParser.sort_dictionary(person_dictionary)

if not os.path.exists('output'):
    os.mkdir('output')

pprint(person_dictionary)

# # Remove old data sheets
# output_file = 'output/' + file_name + '-data.xlsx'
# if os.path.isfile(output_file):
#     os.unlink(output_file)

# # Add to excel sheet
# to_xl(date_dictionary, 'Dates', 'Date', 'No. of Messages', output_file)
# to_xl(person_dictionary, 'People', 'Sender', 'No. of Messages', output_file)
# to_xl(time_dictionary, 'Times', 'Time', 'No. of Messages', output_file)
# to_xl(word_dictionary, 'Words', 'Word', 'No. of Occurences', output_file)
#
# # filename = './chat.txt'
# # parsedData = getMessages(filename)
# parsedData = {'Teste': 1}
# to_xl(parsedData, 'Teste', 'Teste', 'No. of Occurences', output_file)
# # pprint(parsedData)
