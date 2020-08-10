import os
from PyPDF2 import PdfFileReader, PdfFileWriter
import sys

if len(sys.argv) < 2:
    print("Usage:")
    print("{} <dir>".format(sys.argv[0]))

PATH = sys.argv[1]

for f in os.listdir(PATH):

    file_name = PATH + f

    dir = os.path.splitext(file_name)[0]
    
    print(file_name)

    os.mkdir(dir)

    pdf_reader = PdfFileReader(file_name, "rb")

    for page in range(0, pdf_reader.getNumPages()):
        pdf_writer = PdfFileWriter()

        pdf_writer.addPage(pdf_reader.getPage(page))

        output_fname = dir + '/' +str(page+1).zfill(5) + ".pdf"

        with open(output_fname, 'wb') as out:
            pdf_writer.write(out)
 

