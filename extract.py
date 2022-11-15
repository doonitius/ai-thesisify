import nltk
import string
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.stem import snowball
from nltk.corpus import stopwords
import PyPDF2
from glob import glob, glob1
nltk.download('punkt')
nltk.download('stopwords')

stemmer = snowball.SnowballStemmer('english')
stwords = set(stopwords.words('english'))
string.punctuation += '–'




def visitor_body(text, cm, tm, fontDict, fontSize):
    y = tm[5]
    if y > 550 and y < 750:
        parts.append(text)


# for i in glob("/content/data/*.pdf"):
#     parts = []

#     splitSlash = i.split("/")[-1]
#     txtFileName = splitSlash.split(".")[-2]
#     print(txtFileName)
#     pdfFileObj = open(i, 'rb')

#     pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
#     page = pdfReader.pages[2]

#     page.extract_text(visitor_text=visitor_body)
#     text_body = "".join(parts)
#     print(text_body)

#     token = sent_tokenize(text_body)
#     # token = word_tokenize(pageObj.extractText())
#     # print(len(token))
#     # print(token)
#     with open('/txtFile/' + txtFileName + '.txt', 'w', encoding='utf-8') as f:
#         for line in token:
#             f.write(line)
#             f.write('\n')
#     # print(glob('/content/data/*.pdf'))

count = 0
for pdf in glob1('./data/', '*'):
    count += 1
    parts = []
    path = './data/'
    # print(i)
    # splitSlash = i.split("/")[-1]
    # print(splitSlash)
    # txtFileName = splitSlash.split(".")[-2]
    # print(txtFileName)
    # pdfFileObj = open(i, 'rb')
    # print(path + pdf)
    pdfReader = PyPDF2.PdfReader(path + pdf)
    page = pdfReader.pages[2]
    # titlePage = pdfReader.pages[0]
    # title = titlePage.extract_text()
    text = page.extract_text()
    # page.extract_text(visitor_text=visitor_body)
    # text_body = "".join(parts)
    print("----------", count, "------------")
    # print(title)
    # print(pdf)
    print(text)
    print("----------", count, "------------\n")

    # # token = nltk.sent_tokenize(text_body)
    # token = word_tokenize(text)
    # # print(len(token))
    # print(token[0] , "\n")
    # print("----------", count, "------------\n")
    # print(token)
    # atAbstract = False
    # Abstract_word = []
    # for i in token:
    #     # print(i)
    #     if i == 'Abstract':
    #         atAbstract = True
    #         continue
    #     if i == 'Keywords':
    #         break
    #     if atAbstract is True:
    #         word_lower = i.lower()
    #         if word_lower not in stwords:
    #             word_stem = stemmer.stem(word_lower)
    #             if not word_stem.isdigit():
    #                 punct_detected = False
    #                 for x in word_stem:
    #                     if x in string.punctuation:
    #                         punct_detected = True
    #                 if punct_detected is False:
    #                     Abstract_word.append(word_stem)
    # print(Abstract_word)

    txtFileName = pdf.split('.')[-2]
    # print(txtFileName)
    txtFileNoSpace = txtFileName.replace(" ", "_")
    running_no = str(count)
    txtFile = running_no
    print(txtFile)
    pathTxt = './txtFile/'
    with open(pathTxt + txtFile + '.txt', 'w', encoding='utf-8') as f:
    #     # for line in token:
    #     #   f.write(line)
    #     #   f.write('\n')
        f.write(text)
    # print(glob('/content/data/*.pdf'))
