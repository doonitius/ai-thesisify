import nltk
import PyPDF2
import string
from collections import defaultdict
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.corpus import stopwords
from nltk.stem import snowball
from pprint import pprint

nltk.download('punkt')
nltk.download('stopwords')
stemmer = snowball.SnowballStemmer('english')
stwords = set(stopwords.words('english'))
pdfFileObj = open('Thesis Miss Aye.pdf', 'rb')

example = "Hello, Welcome to python pool. Hope you are doing well"
# tokens = nltk.sent_tokenize(pageObj.extractText())

pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
string.punctuation += '–'
corpus = []

# def tfidf(word, sentence):
#     print

def process_and_search(query):
    matched_documents = set()
    for word in word_tokenize(query):
        word_lower = word.lower()
        if word_lower not in stwords:
            word_stem = stemmer.stem(word_lower)
            matches = inverted_index.get(word_stem)
            if matches:
                # The operator |= is a short hand for set union
                matched_documents |= matches
    return matched_documents

tokens = []
for i in range(0, pdfReader.numPages):
    pageObj = pdfReader.getPage(i)
    doonPage = pageObj.extractText()
    corpus.append(doonPage)
    tokens += nltk.word_tokenize(doonPage)

print(len(corpus))
# Our index is a map of word -> documents it is found in
inverted_index = defaultdict(set)
word_dic = defaultdict(set)

word_array = []
word_count = []
word_percent = []

# We maintain the reference to the document by its index in the corpus list
for docid, c in enumerate(corpus):
    for sent in sent_tokenize(c):
        for word in word_tokenize(sent):
            word_lower = word.lower()
            if word_lower not in stwords:
                word_stem = stemmer.stem(word_lower)
                if not word_stem.isdigit():
                    punct_detected = False  
                    for x in word_stem:
                        if x in string.punctuation:
                            punct_detected = True
                    if punct_detected is False:
                        inverted_index[word_stem].add(docid)
                        if len(word_array) == 0:
                            word_array.append(word_stem)
                        else:
                            if word_stem in word_array:
                                break;
                            else: word_array.append(word_stem)
                                
#print(word_array[0])
#print(len(word_array)) 
#print(len(inverted_index.keys()))

for word in word_array:
    word_count.append(len(inverted_index[word]))
    #print(len(inverted_index[word]))
#print(word_count)
#print(len(tokens))
count = 0
for word in word_count:
    word = word / len(tokens)
    word_percent.append(word)
    word_dic[word_array[count]].add(word)
    count += 1
pprint(word_dic)
#pprint(word_percent)
#print(string.punctuation)
# print(stwords)

# pprint(inverted_index, width = 200)

# for i in range(0, corpus):
#     tfidf(corpus[i])
#result = process_and_search("solving")

#print(result)

# for id, val in enumerate(result):
#     print(id, corpus[val])