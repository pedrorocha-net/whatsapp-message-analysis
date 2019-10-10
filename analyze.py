#!python3
# -*- coding: utf-8 -*-

import os
import re
from app.whatsapp_parser import collect_data, get_file_name, read_file, sort_dictionary, to_xl
from collections import OrderedDict

# To get rid of file extension when making graphs
file_split = re.compile(r'(.*)(.[a-zA-Z0-9]{3,4})')

# Read given file
file_name_with_extension = get_file_name()
file_name = file_split.search(file_name_with_extension)[1]
text_to_analyze = read_file(file_name_with_extension)

# Collect data
date_dictionary, time_dictionary, person_dictionary, word_dictionary, number_of_messages = collect_data(
    text_to_analyze
)

# Sort all Dictionaries here
word_dictionary = OrderedDict(word_dictionary.most_common(20))
date_dictionary = sort_dictionary(date_dictionary)
time_dictionary = sort_dictionary(time_dictionary, 'key')
person_dictionary = sort_dictionary(person_dictionary)

if not os.path.exists('output'):
    os.mkdir('output')

# Remove old data sheets
output_file = 'output/' + file_name + '-data.xlsx'
if os.path.isfile(output_file):
    os.unlink(output_file)

# Add to excel sheet
to_xl(date_dictionary, 'Dates', 'Date', 'No. of Messages', output_file)
to_xl(person_dictionary, 'People', 'Sender', 'No. of Messages', output_file)
to_xl(time_dictionary, 'Times', 'Time', 'No. of Messages', output_file)
to_xl(word_dictionary, 'Words', 'Word', 'No. of Occurences', output_file)
