import PyPDF2:

pdf = open("some pdf", 'rb')
reader = PyPDF2.PdfFileReader(pdf)
page = reader.getPage(0)
print(page.extractText())


#wa.me/917385821801