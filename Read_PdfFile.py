#required module to import
import PyPDF2
#creating pdf file object
pdf_file_obj=open('flask_tutorial.pdf','rb')
#creating pdf reader object
pdf_file_reader=PyPDF2.PdfFileReader(pdf_file_obj)
#number of pages in pdf file
print('Number of pages in given pdf file: ',pdf_file_reader.numPages)
#getting particular page from pdf file
speific_page=pdf_file_reader.getPage(10)
#retriving data from particular page
print(speific_page.extractText())


