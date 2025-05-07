import os
from PyPDF2 import PdfWriter

merger = PdfWriter()

pdfs = []
n = int(input("Enter the number of pdfs you want to merge: "))

# Folder where PDFs are stored
pdf_folder = "merge pdf using python"

for i in range(n):
    name = input(f"Enter the name of pdf {i + 1}: ")  # you just type 'second.pdf' etc
    full_path = os.path.join(pdf_folder, name)
    pdfs.append(full_path)

for pdf in pdfs:
    merger.append(pdf)

merger.write("merged-pdf.pdf")
merger.close()
