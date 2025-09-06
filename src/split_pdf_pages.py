import sys
from PyPDF2 import PdfReader, PdfWriter
import os

# Usage: python split_pdf_pages.py input.pdf output_dir

def main():
    if len(sys.argv) != 3:
        print("Usage: python split_pdf_pages.py input.pdf output_dir")
        sys.exit(1)

    input_pdf = sys.argv[1]
    output_dir = sys.argv[2]

    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    reader = PdfReader(input_pdf)
    num_pages = len(reader.pages)

    for i in range(num_pages):
        writer = PdfWriter()
        writer.add_page(reader.pages[i])
        output_path = os.path.join(output_dir, f"page_{i+1}.pdf")
        with open(output_path, "wb") as out_f:
            writer.write(out_f)
        print(f"Created: {output_path}")

if __name__ == "__main__":
    main()
