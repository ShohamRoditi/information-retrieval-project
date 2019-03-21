import os
import pandas as pd


def define_name_of_file(file):
    head, tail = os.path.split(file)
    return os.path.splitext(tail)[0]


def create_index_file():
    labels = ['Term', 'Amount of Files', 'Doc Location']
    df = pd.DataFrame([], columns=labels)
    with open('index/index.csv', 'w') as f:
        df.to_csv(f, index=False)


def index_without_stoplist(df_index):
    stop_list = \
        ["a", "as", "able", "about", "above", "according", "accordingly", "across", "actually", "after", "afterwards",
         "again", "against", "aint", "all", "allow", "allows", "almost", "alone", "along", "already", "also",
         "although", "always", "am", "among", "amongst", "an", "and", "another", "any", "anybody", "anyhow", "anyone",
         "anything", "anyway", "anyways", "anywhere", "apart", "appear", "appreciate", "appropriate", "are", "arent",
         "around", "as", "aside", "ask", "asking", "associated", "at", "available", "away", "awfully", "be", "became",
         "because", "become", "becomes", "becoming", "been", "before", "beforehand", "behind", "being", "believe",
         "below", "beside", "besides", "best", "better", "between", "beyond", "both", "brief", "but", "by", "cmon",
         "cs", "came", "can", "cant", "cannot", "cant", "cause", "causes", "certain", "certainly", "changes", "clearly",
         "co", "com", "come", "comes", "concerning", "consequently", "consider", "considering", "contain", "containing",
         "contains", "corresponding", "could", "couldnt", "course", "currently", "definitely", "described", "despite",
         "did", "didnt", "different", "do", "does", "doesnt", "doing", "dont", "done", "down", "downwards", "during",
         "each", "edu", "eg", "eight", "either", "else", "elsewhere", "enough", "entirely", "especially", "et", "etc",
         "even", "ever", "every", "everybody", "everyone", "everything", "everywhere", "ex", "exactly", "example",
         "except", "far", "few", "ff", "fifth", "first", "five", "followed", "following", "follows", "for", "former",
         "formerly", "forth", "four", "from", "further", "furthermore", "get", "gets", "getting", "given", "gives",
         "go", "goes", "going", "gone", "got", "gotten", "greetings", "had", "hadnt", "happens", "hardly", "has",
         "hasnt", "have", "havent", "having", "he", "hes", "hello", "help", "hence", "her", "here", "heres",
         "hereafter", "hereby", "herein", "hereupon", "hers", "herself", "hi", "him", "himself", "his", "hither",
         "hopefully", "how", "howbeit", "however", "i", "id", "ill", "im", "ive", "ie", "if", "ignored", "immediate",
         "in", "inasmuch", "inc", "indeed", "indicate", "indicated", "indicates", "inner", "insofar", "instead", "into",
         "inward", "is", "isnt", "it", "itd", "itll", "its", "its", "itself", "just", "keep", "keeps", "kept", "know",
         "knows", "known", "last", "lately", "later", "latter", "latterly", "least", "less", "lest", "let", "lets",
         "like", "liked", "likely", "little", "look", "looking", "looks", "ltd", "mainly", "many", "may", "maybe", "me",
         "mean", "meanwhile", "merely", "might", "more", "moreover", "most", "mostly", "much", "must", "my", "myself",
         "name", "namely", "nd", "near", "nearly", "necessary", "need", "needs", "neither", "never", "nevertheless",
         "new", "next", "nine", "no", "nobody", "non", "none", "noone", "nor", "normally", "not", "nothing", "novel",
         "now", "nowhere", "obviously", "of", "off", "often", "oh", "ok", "okay", "old", "on", "once", "one", "ones",
         "only", "onto", "or", "other", "others", "otherwise", "ought", "our", "ours", "ourselves", "out", "outside",
         "over", "overall", "own", "particular", "particularly", "per", "perhaps", "placed", "please", "plus",
         "possible", "presumably", "probably", "provides", "que", "quite", "qv", "rather", "rd", "re", "really",
         "reasonably", "regarding", "regardless", "regards", "relatively", "respectively", "right", "said", "same",
         "saw", "say", "saying", "says", "second", "secondly", "see", "seeing", "seem", "seemed", "seeming", "seems",
         "seen", "self", "selves", "sensible", "sent", "serious", "seriously", "seven", "several", "shall", "she",
         "should", "shouldnt", "since", "six", "so", "some", "somebody", "somehow", "someone", "something", "sometime",
         "sometimes", "somewhat", "somewhere", "soon", "sorry", "specified", "specify", "specifying", "still", "sub",
         "such", "sup", "sure", "ts", "take", "taken", "tell", "tends", "th", "than", "thank", "thanks", "thanx",
         "that", "thats", "thats", "the", "their", "theirs", "them", "themselves", "then", "thence", "there", "theres",
         "thereafter", "thereby", "therefore", "therein", "theres", "thereupon", "these", "they", "theyd", "theyll",
         "theyre", "theyve", "think", "third", "this", "thorough", "thoroughly", "those", "though", "three", "through",
         "throughout", "thru", "thus", "to", "together", "too", "took", "toward", "towards", "tried", "tries", "truly",
         "try", "trying", "twice", "two", "un", "under", "unfortunately", "unless", "unlikely", "until", "unto", "up",
         "upon", "us", "use", "used", "useful", "uses", "using", "usually", "value", "various", "very", "via", "viz",
         "vs", "want", "wants", "was", "wasnt", "way", "we", "wed", "well", "were", "weve", "welcome", "well", "went",
         "were", "werent", "what", "whats", "whatever", "when", "whence", "whenever", "where", "wheres", "whereafter",
         "whereas", "whereby", "wherein", "whereupon", "wherever", "whether", "which", "while", "whither", "who",
         "whos", "whoever", "whole", "whom", "whose", "why", "will", "willing", "wish", "with", "within", "without",
         "wont", "wonder", "would", "would", "wouldnt", "ye", "yes", "yet", "you", "youd", "youll", "youre", "youve",
         "your", "yours", "yourself", "yourselves", "zero"]

    for item in stop_list:
        df_index = df_index[df_index.Term != item]
    df_index.to_csv('index/index_stoplist.csv', index=False)


def append_to_index(posting_file):
    file_name = define_name_of_file(str(posting_file))
    file_number = file_name.split('.').pop(0)
    df_posting = pd.read_csv(posting_file)
    df_index = pd.read_csv('index/index.csv')
    index_term_list = df_index['Term'].values.tolist()
    index_amount_list = df_index['Amount of Files'].values.tolist()
    index_location_list = df_index['Doc Location'].values.tolist()
    posting_term_list = df_posting['Term'].values.tolist()
    flag_term_found = 0
    for posting_item in posting_term_list:
        for index_item in range(len(index_term_list)):
            if posting_item == index_term_list[index_item]:
                index_amount_list[index_item] += 1
                index_location_list[index_item] = str(index_location_list[index_item]) + ',' + str(file_number)
                flag_term_found = 1
                break
        if flag_term_found != 1:
            index_term_list.append(posting_item)
            index_amount_list.append(1)
            index_location_list.append(file_number)
        flag_term_found = 0
    index_data = {'Term': pd.Series(index_term_list),
            'Amount of Files': pd.Series(index_amount_list),
            'Doc Location': pd.Series(index_location_list)}
    df_new_index = pd.DataFrame(index_data).sort_values('Term')
    df_new_index.to_csv('index/index.csv', index=False)
    index_without_stoplist(df_new_index)
