

import os
from PyPDF2 import PdfFileReader, PdfFileMerger, PdfMerger

# Set the parent directory
parent_dir = '/path/to/test'

# Walk through all subfolders of the parent directory
for root, dirs, files in os.walk(parent_dir):
    # Check if the current folder contains a "Licenses" folder
    if "Licenses" in dirs:
        licenses_folder = os.path.join(root, "Licenses")
        # Get a list of all PDF files in the "Licenses" folder
        pdf_files = [f for f in os.listdir(licenses_folder) if f.endswith(".pdf")]
        if len(pdf_files) > 0:
            # Merge the PDF files into a single file
            merger = PdfMerger()
            for pdf_file in pdf_files:
                pdf_path = os.path.join(licenses_folder, pdf_file)
                merger.append(pdf_path)
            # Save the merged PDF file with the project folder name
            project_folder = os.path.basename(root)
            merged_filename = project_folder + ".pdf"
            merged_path = os.path.join(os.path.join(root, "Licenses"), merged_filename)
            with open(merged_path, "wb") as merged_file:
                merger.write(merged_file)

