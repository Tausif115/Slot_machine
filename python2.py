from PyPDF2 import PdfMerger
import os

input_directory = "E:\\Combined"
output_file = "E:\\Combined\\combined_output.pdf"

pdf_files = sorted([f for f in os.listdir(input_directory) if f.endswith(".pdf")])

if not pdf_files:
    print("No PDF files found in the directory.")
    exit()

merger = PdfMerger()

for file_name in pdf_files:
    print(f"Adding: {file_name}")
    merger.append(os.path.join(input_directory, file_name))

try:
    merger.write(output_file)
    merger.close()
    print(f"PDF created successfully: {output_file}")
    os.startfile(output_file)  # Open the merged PDF
except Exception as e:
    print(f"An error occurred: {e}")




