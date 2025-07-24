import pandas as pd
from fpdf import FPDF
import os

# File path
DATA_PATH = "data/sample_data.csv"
OUTPUT_DIR = "reports"

# Ensure reports folder exists
os.makedirs(OUTPUT_DIR, exist_ok=True)

# Read CSV data
df = pd.read_csv(DATA_PATH)
# Create PDF object
pdf = FPDF()
pdf.set_auto_page_break(auto=True, margin=15)

# Add title page
pdf.add_page()
pdf.set_font("Arial", 'B', 16)
pdf.cell(0, 10, "Student Report", ln=True, align='C')
pdf.ln(10)

# Table headings
pdf.set_font("Arial", 'B', 12)
pdf.cell(60, 10, "Name", 1)
pdf.cell(60, 10, "Subject", 1)
pdf.cell(60, 10, "Marks", 1)
pdf.ln()

# Table rows from CSV
pdf.set_font("Arial", '', 12)
for index, row in df.iterrows():
    pdf.cell(60, 10, str(row["Name"]), 1)
    pdf.cell(60, 10, str(row["Subject"]), 1)
    pdf.cell(60, 10, str(row["Marks"]), 1)
    pdf.ln()

# Save the PDF
output_path = os.path.join(OUTPUT_DIR, "student_report.pdf")
pdf.output(output_path)

print("✅ Report Generated Successfully:", output_path)
