import pandas as pd
from fpdf import FPDF
from fpdf import FPDF, XPos, YPos

# Create instance of FPDF class
pdf = FPDF('L','cm','A4')

# Add a page
pdf.add_page()

# Set font to Helvetica (or any other core font supported by FPDF)
pdf.set_font('Helvetica', '', 16)
pdf.cell(5,3,'Hello World',new_x=XPos.LMARGIN, new_y=YPos.NEXT,align='C')
TABLE_DATA = (
     ("First name", "Last name", "Age", "City"),
     ("Jules", "Smith", "34", "San Juan"),
     ("Mary", "Ramos", "45", "Orlando"),
     ("Carlson", "Banks", "19", "Los Angeles"),
     ("Lucas", "Cimon", "31", "Saint-Mathurin-sur-Loire"),
)

user_data = pd.DataFrame({
     'Sample Id': ['E16 Yb CP', 'E17 Yb CA', 'E19 Yb RS', 'E20 Yb CS', 'E20 Yb RP'],
     '168/173': ['1', '2', '3', '4', '5'],
     '170/173': ['6', '7', '8', '9','10'],
     '171/173': ['6', '7', '8', '9','10'],
     '172/173': ['6', '7', '8', '9','10'],
     '174/173': ['6', '7', '8', '9','10'],
     '176/173': ['6', '7', '8', '9','10'],
})

#with pdf.table() as table:
#     for row_data in TABLE_DATA:
#         row=table.row()
#         for row_item in row_data:
#             row.cell(row_item)
#
with pdf.table() as table:
    row=table.row()
    for i in user_data.keys():
        row.cell(i)
    for index, row_set in user_data.iterrows():
        
         row=table.row()
         for i in user_data.keys():
             row.cell(row_set[i])


pdf.output('pdf_1.pdf')