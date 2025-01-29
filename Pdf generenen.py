from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet
import os

# Create directory for PDF if it doesn't exist
os.makedirs("PDF_INVOICE", exist_ok=True)

# Define the PDF path
pdf_path = "PDF_INVOICE/vacature_template.pdf"

# Create the PDF document
pdf = SimpleDocTemplate(pdf_path, pagesize=A4)

# Styles for the document
styles = getSampleStyleSheet()

# Elements for the PDF layout
elements = []

# Title for the vacancy template
title = Paragraph("<b>Vacature Template</b>", styles["Title"])
elements.append(title)
elements.append(Spacer(1, 12))

# Company information section
elements.append(Paragraph("<b>Bedrijfsinformatie:</b>", styles["Heading2"]))
elements.append(Paragraph("[Hier komt informatie over het bedrijf]", styles["BodyText"]))
elements.append(Spacer(1, 12))

# Job description section
elements.append(Paragraph("<b>Functieomschrijving:</b>", styles["Heading2"]))
elements.append(Paragraph("[Hier komt een omschrijving van de functie]", styles["BodyText"]))
elements.append(Spacer(1, 12))

# Requirements section
elements.append(Paragraph("<b>Functie-eisen:</b>", styles["Heading2"]))
elements.append(Paragraph("[Hier komt een lijst met vereisten]", styles["BodyText"]))
elements.append(Spacer(1, 12))

# Benefits section
elements.append(Paragraph("<b>Wat bieden wij:</b>", styles["Heading2"]))
elements.append(Paragraph("[Hier komt een lijst met voordelen en aanbiedingen]", styles["BodyText"]))
elements.append(Spacer(1, 12))

# Application section
elements.append(Paragraph("<b>Hoe solliciteren:</b>", styles["Heading2"]))
elements.append(Paragraph("[Hier komt informatie over hoe te solliciteren]", styles["BodyText"]))

# Build the PDF
pdf.build(elements)

print(f"Vacature template succesvol aangemaakt: {pdf_path}")
