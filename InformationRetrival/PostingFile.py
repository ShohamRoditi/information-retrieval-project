import csv
import os
import pandas as pd

from InformationRetrival.IndexingFile import append_to_index, define_name_of_file


def open_file_to_read_from_source(file):
    return open("src/" + file, "r")


def remove_unwanted_chars(file):
    s = file.read()
    chars = ('$', '%', '^', '*', '!', '@', '#', '&', '(', ')', '-', '_', '=', '+', ',', '.', ';', '/', '?', '"', ' ', ':')
    for c in chars:
        s = ''.join(s.split(c))
    file.close()
    out_file = open(file.name, 'w')
    out_file.write(s)
    out_file.close()


def sort_posting_file(file):
    s = file.read().split()
    s.sort()
    file.close()
    out_file = open(file.name, 'w')
    writer = csv.writer(out_file, delimiter='\n', dialect='excel', quoting=csv.QUOTE_NONE)
    writer.writerow(s)
    out_file.close()


def hits_calculation(file):
    f = file.read().split()
    last_term = ''
    hits = 0
    list_of_hits = []
    for row in f:
        if last_term == row:
            hits += 1
        else:
            if hits == 0:
                hits = 1
                last_term = row
                continue
            list_of_hits.append(hits)
            hits = 1
        last_term = row
    list_of_hits.append(hits)
    return list_of_hits


def remove_duplicate(file_location):
    with open(file_location, 'r') as file:
        list_of_hits = hits_calculation(file)
    with open(file_location, 'r') as file:
        f = file.read().split()
        data = {'Term': pd.Series(f)}
        df = pd.DataFrame(data)
        df = df.drop_duplicates(subset='Term')
        f = df['Term'].values.tolist()
        data = {'Term': pd.Series(f),
                'Hits': pd.Series(list_of_hits)}
        df = pd.DataFrame(data)
        df.to_csv(file_location, index=False)


def create_posting_file(amount_storage):
    src_content = os.listdir("src/")
    for file in src_content:
        name_of_file = define_name_of_file(file)
        amount_storage += 1
        csv_file_path = "posting_files/" + str(amount_storage) + '. ' + name_of_file + '.csv'

        """ copy the file to storage directory """
        with open_file_to_read_from_source(file) as f, open("storage/" + str(amount_storage) + '. ' + name_of_file + '.txt', 'w') as storage_file:
            for x in f.readlines():
                storage_file.write(x)

        """ creates a csv file to represent the posting file """
        with open_file_to_read_from_source(file) as f, open(csv_file_path, 'w') as postingFile:

            """ convert from uppercase to lowercase in the csv and write to the csv """
            stripped = ((word.lower() for word in words.split()) for words in f)
            writer = csv.writer(postingFile, delimiter='\n', dialect='excel', quotechar=' ', quoting=csv.QUOTE_ALL)
            writer.writerows(stripped)

        """ remove unwanted characters """
        remove_unwanted_chars(open(csv_file_path, 'r'))

        """ sorting the list """
        sort_posting_file(open(csv_file_path, 'r'))

        """ remove duplicated terms """
        remove_duplicate(csv_file_path)

        """ append new terms and exists terms to the index file """
        append_to_index(open(csv_file_path, 'r'))

    """ delete the file from src directory """
    for file in src_content:
        os.remove("src/" + file)
