from fpdf import FPDF

# Create an instance of FPDF class
pdf = FPDF()

# Add a new page
pdf.add_page()

# Set font: Arial, bold, size 16
pdf.set_font("Arial", 'B', 16)

# Add your name to the PDF
pdf.cell(200, 10, txt="Adrian Hromec", ln=True, align='C')

# Save the PDF with a custom file name
pdf.output("mip.pdf")

print("PDF generated successfully: mip.pdf")