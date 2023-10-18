import PyPDF2

uploaded_file = 'path of your file'



pdf_reader = PyPDF2.PdfFileReader(uploaded_file)

text = ''

for page_number in range(pdf_reader.numPages):
    page = pdf_reader.getPage(page_number)
    text += page.extractText()

if text:
    print("Extracted text from the PDF:")
    print(text)