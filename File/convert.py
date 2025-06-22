import os
from fpdf import FPDF

folder_path = './my_texts'

for filename in os.listdir(folder_path):
    if filename.endswith('.txt'):
        file_path = os.path.join(folder_path, filename)
        with open(file_path, 'r') as f:
            text = f.read()
        
        pdf = FPDF()
        pdf.add_page()
        pdf.set_auto_page_break(auto=True, margin=15)
        pdf.set_font('Arial', size=12)
        pdf.multi_cell(0, 10, text)
        
        pdf_filename = filename.replace('.txt', '.pdf')
        pdf.output(os.path.join(folder_path, pdf_filename))
        print(f'Converted: {filename} -> {pdf_filename}')

print('All .txt files converted to .pdf')

