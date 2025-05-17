"""
Small File Merger
Author: Daniyyell
Date: 17/05/2025
Python Version: 3.7+
"""

import os
from PyPDF2 import PdfMerger
from PIL import Image
from pyfiglet import Figlet
from rich.console import Console

console = Console()

# Step 0: Show colorful welcome header using pyfiglet and rich
fig = Figlet(font='slant')
console.print(fig.renderText('Small File Merger'), style="bold cyan")
console.print("Supported file types: .jpg, .jpeg, .pdf\n", style="green")

# Step 1: Prompt for input folder
input_dir = input("📂 Enter the full path to the folder with your files: ").strip()
while not os.path.isdir(input_dir):
    input_dir = input("[red]❌ Invalid folder. Please re-enter the full path:[/red] ").strip()

# Step 2: Prompt for output PDF name
output_name = input("📄 Enter your desired output PDF filename (without .pdf): ").strip()
if not output_name.lower().endswith('.pdf'):
    output_name += '.pdf'
final_pdf_path = os.path.join(input_dir, output_name)

# Step 3: Convert image files to temporary PDFs
temp_pdfs = []
for file in sorted(os.listdir(input_dir)):
    if file.lower().endswith(('.jpg', '.jpeg')):
        img_path = os.path.join(input_dir, file)
        temp_pdf_path = os.path.join(input_dir, f"{file}.temp.pdf")

        if not os.path.exists(temp_pdf_path):
            img = Image.open(img_path).convert('RGB')
            img.save(temp_pdf_path, "PDF")
        temp_pdfs.append(temp_pdf_path)

# Step 4: Gather original PDF files (excluding temp ones)
original_pdfs = [
    os.path.join(input_dir, f) for f in sorted(os.listdir(input_dir))
    if f.lower().endswith('.pdf') and not f.endswith('.temp.pdf')
]

# Step 5: Merge all into one final PDF
merger = PdfMerger()
for pdf in temp_pdfs + original_pdfs:
    merger.append(pdf)

merger.write(final_pdf_path)
merger.close()

# Step 6: Clean up temp files
for temp in temp_pdfs:
    try:
        os.remove(temp)
    except Exception as e:
        console.print(f"[yellow]⚠️ Failed to delete temporary file {temp}: {e}[/yellow]")

# Done!
console.print(f"\n✅ Done! Combined PDF saved as: {final_pdf_path}", style="bold green")
