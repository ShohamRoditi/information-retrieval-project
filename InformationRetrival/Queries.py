import pandas as pd
import os


def wildcard(string, result):
    index = pd.read_csv('index/index.csv')
    index_terms = index['Term'].values.tolist()
    for term in range(len(index_terms)):
        if index_terms[term].startswith(string):
            temp = search_word(index_terms[term])
            if temp is None:
                result.append(temp)
            else:
                doc = temp.split(',')
                for sub_item in doc:
                    result.append(sub_item)
    return result


def search_string(query, all_docs):
    string_len = len(query)
    string = ''
    docs_list = []
    result = []

    """ remove the '"' from the beginning and from the ending of the sentence """
    for char in range(string_len-2, 0, -1):
        string += query[char].lower()

    """ look for every term in the sentence, in which file it can be found by the index file """
    search_for_list = string[::-1].split()
    index = pd.read_csv('index/index.csv')
    term_list = index['Term'].values.tolist()
    doc_location_list = index['Doc Location'].values.tolist()
    for searched_item in search_for_list:
        for term in range(len(term_list)):
            if term_list[term] == searched_item:
                docs_list.append(doc_location_list[term])

    """ process AND operator between all the terms in the sentence and equals it to all the docs in the storage file """
    """ making a new list which contains the files number that all terms may be found in """
    found_docs = all_docs
    for word_list in docs_list:
        found_docs = [a for a in word_list for b in found_docs if a == b]

    """ search for the whole sentence if it may be found as is in the files found in the -found_docs- """
    storage = os.listdir('storage/')
    for doc in found_docs:
        for file in storage:
            if file.split('.')[0] == doc:
                with open('storage/' + file, 'r') as f:
                    file_content = f.read().lower()
                    if string[::-1] in file_content:
                        result.append(doc)
    return list(dict.fromkeys(result))


def search_word(word):
    if os.path.isfile("index/hide_index_stoplist.csv"):
        index = pd.read_csv("index/hide_index_stoplist.csv")
    else:
        index = pd.read_csv("index/index_stoplist.csv")
    for term in range(len(index['Term'])):
        if index['Term'][term] == word:
            print(str(index['Doc Location'][term]))
            return str(index['Doc Location'][term])
    return None
