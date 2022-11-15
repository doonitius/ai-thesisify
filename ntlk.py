from nltk.tokenize import word_tokenize
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

for i in range(0, pdfReader.numPages):
    pageObj = pdfReader.getPage(i)
    corpus.append(pageObj.extractText())

print(len(corpus))
# Our index is a map of word -> documents it is found in
inverted_index = defaultdict(set)


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

print(len(inverted_index.keys()))
print(string.punctuation)
# print(stwords)
# print(inverted_index)
# pprint(inverted_index, width = 200)
print(inverted_index.get('solv'))
# for i in range(0, corpus):
#     tfidf(corpus[i])
result = process_and_search("solving")

print(result)

# for id, val in enumerate(result):
#     print(id, corpus[val])

# nltk.download('punkt')

# pdfFileObj = open('Thesis Miss Aye.pdf', 'rb')

# example = "Hello, Welcome to python pool. Hope you are doing well"
# # tokens = nltk.sent_tokenize(pageObj.extractText())

# pdfReader = PyPDF2.PdfFileReader(pdfFileObj)

# # print(pdfReader.numPages)

# # pageObj = pdfReader.getPage(3)

# # tokens = word_tokenize(pageObj.extractText())
# # print(tokens)

# for i in range(0, pdfReader.numPages):
#     pageObj = pdfReader.getPage(i)
#     token = nltk.sent_tokenize(pageObj.extractText())
#     # token = word_tokenize(pageObj.extractText())
#     print(len(token))
#     print(token)
#     with open('Thesis Miss Aye.txt', 'a', encoding='utf-8') as f:
#         for line in token:
#             f.write(line)
#             f.write('\n')
