from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
import os

# Prompt user for text input
text = input("Enter the text for your PDF: ")

# Ensure the directory exists
directory = "PDF_INVOICE"
os.makedirs(directory, exist_ok=True)

# Define PDF path
pdf_file_path = os.path.join(directory, "output.pdf")

# Create the PDF using reportlab
pdf_canvas = canvas.Canvas(pdf_file_path, pagesize=A4)
pdf_canvas.drawString(100, 800, text)  # Draw the text at coordinates (x, y)
pdf_canvas.save()

print(f"PDF successfully created at: {pdf_file_path}")
