from fpdf import FPDF

pdf = FPDF()

pdf.add_page()

pdf.set_font("Arial", size=25)

# create a cell
file = open("data.txt", "r")

# insert the texts in pdf
for g in file:
    pdf.cell(200, 10, txt=g, ln=1, align='C')

pdf.output("PDF.pdf")
