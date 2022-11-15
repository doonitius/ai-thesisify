import nltk
import string
import pandas as pd
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.stem import snowball
from nltk.corpus import stopwords
import PyPDF2
from glob import glob, glob1
nltk.download('punkt')
nltk.download('stopwords')

path = './txtFile/'

data = pd.DataFrame(columns=['id','abstract','keywords'])


for i in glob1('./txtFile/', '*'):
    with open(path + i, 'r', encoding='utf8') as f:
        doc_id = i.split('.')[-2]
        readingAbstract = False
        readingKeywords = False
        abstract_sent = []
        keyword_list = []
        keyword_clean = []
        for j in f:
            line = j.strip()
            if line == 'Keywords:' and readingKeywords is False:
                readingKeywords = True
                readingAbstract = False
                continue
            if line == 'Abstract' and readingAbstract is False:
                readingAbstract = True
                continue
            if readingAbstract is True:
                abstract_sent.append(line)
            if readingKeywords is True:
                keyword_list.append(line)
        abstract_para = ' '.join(abstract_sent)
        keyword_split = keyword_list[0].split(',')
        # print(abstract_para)
        # print(keyword_split)
        for x in keyword_split:
            keyword_lower = x.lower()
            keyword_no_space = keyword_lower.replace(' ', '')
            keyword_underscore = keyword_no_space.replace('_', ' ')
            keyword_clean.append(keyword_underscore)
        # print(keyword_clean)

        data = data.append({"id":doc_id, "abstract":abstract_para, "keywords": keyword_clean}, ignore_index = True)
    f.close()

print(data)

