import os
from InformationRetrival.IndexingFile import create_index_file


def check_index_existence():
    dir_index = os.listdir("index/")
    for file in dir_index:
        if file == "index.csv":
            return
    create_index_file()


def count_posting_files():
    dir_content = os.listdir("posting_files/")
    counter = 0
    for file in dir_content:
        counter += 1
    return int(counter)


