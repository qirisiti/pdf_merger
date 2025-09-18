import os
import re
from pypdf import PdfWriter

folder = input("Enter folder path (e.g., '.'): ").strip()
if not os.path.exists(folder):
    print("Folder not found.")
    exit()

pdfs = []
for file in os.listdir(folder):
    if file.lower().endswith('.pdf'):
        match = re.match(r'(\d+)', file)
        if match:
            num = int(match.group(1))
            pdfs.append((num, os.path.join(folder, file)))

pdfs.sort(key=lambda x: x[0])
if not pdfs:
    print("No numbered PDFs found.")
    exit()

merger = PdfWriter()
for num, path in pdfs:
    print(f"Merging {path}")
    merger.append(path)

output = os.path.join(folder, "merged.pdf")
merger.write(output)
merger.close()
print(f"Merged into {output}")