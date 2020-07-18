import glob
import os
from app.whatsapp_parser import read_file


def loadData():
    data_files = glob.glob('./data/*')
    file_name = min(data_files, key=os.path.getctime)
    print('Reading from file ' + file_name)
    return read_file(file_name)
