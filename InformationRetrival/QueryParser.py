import collections

from InformationRetrival.Queries import *
"""search_word, search_string"""


def parse_query(query):

    precedence = {'*': 4, '!': 3, '&': 2, '|': 1, '(': 0, ')': 0}
    output = []
    operator_stack = []

    for token in query:
        if token == '(':
            operator_stack.append(token)
        elif token == ')':
            operator = operator_stack.pop()
            while operator != '(':
                output.append(operator)
                operator = operator_stack.pop()

        elif token in precedence:
            if operator_stack:
                current_operator = operator_stack[-1]
                while operator_stack and precedence[current_operator] > precedence[token]:
                    output.append(operator_stack.pop())
                    if operator_stack:
                        current_operator = operator_stack[-1]
            operator_stack.append(token)

        else:
            output.append(token.lower())
    while operator_stack:
        output.append(operator_stack.pop())
    return output


def process_query(query):
    docs = os.listdir('posting_files/')

    def reset_doc_list(docs):
        all_docs = []
        for files in docs:
            all_docs.append(files.split('.')[0])
        return all_docs

    if query[0] == '"' and query[-1] == '"':
        return search_string(query, reset_doc_list(docs))

    query = query.replace('(', ' ( ')
    query = query.replace(')', ' ) ')
    query = query.replace('*', ' *')
    query = query.split(' ')
    reverse_query = query[::-1]
    for elem in reverse_query:
        if elem == '':
            reverse_query.remove('')
    query = reverse_query[::-1]

    results_stack = []
    postfix_queue = collections.deque(parse_query(query))  # get query in postfix notation as a queue

    while postfix_queue:
        temp = postfix_queue.popleft()
        if temp != '*':
            token = temp
        result = []

        if token != '&' and token != '|' and token != '!' and temp != '*':
            exist = search_word(token)
            if exist:
                result = exist.split(',')

        elif token == '&':
            right_operand = results_stack.pop()
            left_operand = results_stack.pop()
            result = [a for a in right_operand for b in left_operand if a == b]

        elif token == '|':
            docs_location = []
            right_operand = results_stack.pop()
            left_operand = results_stack.pop()
            for item in right_operand:
                docs_location.append(item)
            for item in left_operand:
                docs_location.append(item)
            result = list(dict.fromkeys(docs_location))

        elif token == '!':
            all_docs = reset_doc_list(docs)
            right_operand = results_stack.pop()
            if right_operand is not None:
                for item in right_operand:
                    all_docs.remove(item)
            result = all_docs

        elif temp == '*':
            results_stack.pop()
            result = list(dict.fromkeys(wildcard(token, result)))
            if None in result:
                result.remove(None)
            elif 'nan' in result:
                result.remove('nan')
        results_stack.append(result)

    if len(results_stack) != 1:
        print("ERROR: Invalid Query. Please check query syntax.")  # check for errors
        return None

    return results_stack.pop()
