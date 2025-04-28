from PyPDF2 import PdfMerger
import os

input_directory = "E:\Combined"
output_file = "combined_output.pdf"
pdf_files = [f for f in os.listdir(input_directory) if f.endswith(".pdf")]

# Create a PdfMerger object
merger = PdfMerger()

# Append each PDF to the merger
for file_name in pdf_files:
    merger.append(os.path.join(input_directory, file_name))

# Write the combined PDF to a file
merger.write(output_file)
merger.close()