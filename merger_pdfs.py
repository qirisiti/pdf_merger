import os
import re
from pypdf import PdfWriter

folder = input("Enter folder path (e.g., '.'): ").strip()
if not os.path.exists(folder):
    print("Folder not found.")
    exit()

output_name = input("Enter output PDF name (e.g., 'merged.pdf'): ").strip()
if not output_name.lower().endswith('.pdf'):
    output_name += '.pdf'

pdfs = []
for file in os.listdir(folder):
    if file.lower().endswith('.pdf'):
        match = re.match(r'(\d+)', file)
        num = int(match.group(1)) if match else float('inf')
        base_name = file.lower()
        pdfs.append((num, base_name, file))

pdfs.sort(key=lambda x: (x[0], x[1]))

if not pdfs:
    print("No PDFs found.")
    exit()

merger = PdfWriter()
for num, _, file in pdfs:
    path = os.path.join(folder, file)
    print(f"Merging {path}")
    merger.append(path)

output = os.path.join(folder, output_name)
merger.write(output)
merger.close()
print(f"Merged into {output}")