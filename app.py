import PyPDF2

pdfFileObj = open('i1.pdf', 'rb')

# creating a pdf reader object
pdfReader = PyPDF2.PdfFileReader(pdfFileObj)

# printing number of pages in pdf file
print(pdfReader.numPages)

# creating a page object
pageObj = pdfReader.getPage(2)

# extracting text from page
print(pageObj.extractText())

# closing the pdf file object
pdfFileObj.close()
