import PyPDF2
import sys


merger = PyPDF2.PdfFileMerger()
amount = int(input ("how many pdf will you merge?"))

try:
	for i in range(amount):
		merger.append(PyPDF2.PdfFileReader(input("write pdf name"), 'rb'))
	merger.write('merged.pdf')
except:
	print ("THE FILE IS NOT FOUND")



