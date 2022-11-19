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
    corpus = ""
    # print(i)
    # splitSlash = i.split("/")[-1]
    # print(splitSlash)
    # txtFileName = splitSlash.split(".")[-2]
    # print(txtFileName)
    # pdfFileObj = open(i, 'rb')
    # print(path + pdf)
    pdfReader = PyPDF2.PdfReader(path + pdf)
    numPages = pdfReader.numPages
    # wantToDelete = ["ACKNOWLEDGEMENT"]
    # wantToRead = ["Abstract"]
    # keepText = []
    # condition_read = 0
    for i in range(0, numPages):
        condition_read = 0
        page = pdfReader.pages[i]


    # titlePage = pdfReader.pages[0]
    # title = titlePage.extract_text()
        ####line = j.strip()
        text = page.extract_text()
        # print(text)
        # splitText = text.split()
        # print(splitText)
        # for j in range(len(splitText)):
        #     if(splitText[j] in wantToDelete):
        #         condition_read = 0
        #     if(splitText[j] in wantToRead):
        #         condition_read = 1
        #         if(splitText[j] in wantToDelete):
        #             condition_read = 0
        #     if(condition_read == 1):
        #         keepText.append(splitText[j])
            # else:
            #     condition_delete == 0
            #     keepText.append(splitText[j])
    #         # print(splitText[j])
    #     # print(newTextstr)
    # newTextstr = " ".join(keepText)
    # print(newTextstr)
        corpus += "".join(text)
    # print(type(corpus))
    # break
    # page.extract_text(visitor_text=visitor_body)
    # text_body = "".join(parts)
    #     print("----------", count, "------------")
    # # print(title)
    # # print(pdf)
    #     print(text)
    #     print("----------", count, "------------\n")
        # corpus += text
    # print(corpus)
    # break
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

    # # ตรงนี้คือพออ่านเสร็จแล้วก็ยัดเข้าไฟล์ .txt
    # txtFileName = pdf.split('.')[-2]
    # # print(txtFileName)
    # txtFileNoSpace = txtFileName.replace(" ", "_")
    # running_no = str(count)
    # if len(running_no) < 2:
    #     running_no = '0' + running_no
    # txtFile = running_no
    # print(txtFile)
    # pathTxt = './txtFile2/'
    # with open(pathTxt + txtFile + '.txt', 'w', encoding='utf-8') as f:
    # #     for line in corpus:
    # #         f.write(corpus[line])
    # #         f.write('\n')
    #     f.write(corpus)
    # # print(glob('/content/data/*.pdf'))




# ไอลินลอกโค๊ด
   # ตรงนี้คือพออ่านเสร็จแล้วก็ยัดเข้าไฟล์ .txt

    # newTextstr = "".join(keepText)
    # print(newTextstr)


    txtFileName = pdf.split('.')[-2]
    # print(txtFileName)
    txtFileNoSpace = txtFileName.replace(" ", "_")
    running_no = str(count)
    if len(running_no) < 2:
        running_no = '0' + running_no
    txtFile = running_no
    print(txtFile)
    pathTxt = './txtFile4/'
    with open(pathTxt + txtFile + '.txt', 'w', encoding='utf-8') as f:
    #     for line in corpus:
    #         f.write(corpus[line])
    #         f.write('\n')
        f.write(corpus)
    # print(glob('/content/data/*.pdf'))
