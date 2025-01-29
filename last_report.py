import streamlit as st
import pandas as pd
from fpdf import FPDF
from fpdf import FPDF, XPos, YPos
from datetime import date

# Load your data
tims_data = pd.read_csv("./TIMS.csv")
ion_data = pd.read_csv("./ion_report.csv")
laser_power = pd.read_csv("./Laser Power.csv")

if 'qt' not in st.session_state:
     st.session_state['qt']=None

if 'xf' not in st.session_state:
     st.session_state['xf']=None
    
exp_conducted = st.text_input("Enter Dates when Experiment was conducted")
report_date = st.date_input("Enter Report Date",format="DD/MM/YYYY")

report_col1,report_col2,report_col3 = st.columns(3)

with report_col1:
     report_no = st.text_input("Enter Report No.")
with report_col2:
     qty_report_date = st.date_input("Enter Qty Report Date",format="DD/MM/YYYY")
with report_col3:
     tims_report_date = st.date_input("Enter TIMS Report Date",format="DD/MM/YYYY")

sample_no = st.number_input("Enter no. of samples", step=1)

label_col1, label_col2, label_col3, label_col4 = st.columns(4)

with label_col1:
     st.write("Material")
with label_col2:
     st.write("Experiment")
with label_col3:
     st.write("Sample")
with label_col4:
     st.write("Identifier")

col1, col2, col3, col4  = st.columns(4)

label_df = pd.DataFrame({})  # Initialize an empty DataFrame
selected_df=pd.DataFrame({})
df = pd.DataFrame()
ionization_df=pd.DataFrame({})
laser_parameter = pd.DataFrame({})

exp_list=[]

for i in range(sample_no):
     with col1:
         mat = st.selectbox("", ["", "Yb", "Lu"], key=f"mat{i}", placeholder="Material")

     with col2:
         new_data = tims_data[tims_data['Material'] == mat]
         options_exp = [""] + new_data['Exp'].unique().tolist()
         selected_exp = st.selectbox("",options_exp, key=f"exp{i}")

     with col3:
         sample_data = new_data[new_data['Exp'] == selected_exp]['Sample']
         selected_sample = st.selectbox("", sample_data.unique(),key=f"samp{i}")

     with col4:
         try:
             samp_id = f"{st.session_state[f'exp{i}']} {st.session_state[f'mat{i}']} {st.session_state[f'samp{i}']}"
            # st.text_input("", value=samp_id,key=f"sample_key{i}",disabled=True)
         except TypeError:
             pass

         selected_identifier = st.selectbox("",tims_data[tims_data['Sample ID'] == samp_id]['Identifier'].unique(),key=f"identity{i}")

     exp_list.append(st.session_state[f"exp{i}"])
     # Retrieve data directly using .iloc[0]
     matching_row = tims_data.loc[(tims_data['Sample ID'] == samp_id) & (tims_data['Identifier']== st.session_state[f"identity{i}"])]

     # Append data to label_df
     # Append each row separately to label_df
     for index, row in matching_row.iterrows():

         label_df = pd.concat([label_df, pd.DataFrame({
             "Sample ID": [row['Sample ID']],
             "Ratio": [row['Ratio']],
             "RSD ppm": [row['RSD ppm']],
             "Identifier":[row['Identifier']],
             "FINAL":[row['FINAL']],
             "Quantity":[st.session_state['qt']],
             "xf":[st.session_state['xf']],
             "Concentration":[round((row["Ratio"] * 100)/(1 + row["Ratio"]),1)],
             "Qty of Ions":[None],
             "Qty of Neutrals":[None]
         })], ignore_index=True)

if "ion_df24" not in st.session_state:
     st.session_state.ion_df24 = pd.DataFrame({
                                            "Sample ID":[],
                                            "Ratio":[],
                                            "RSD ppm":[],
                                            "Identifier":[],
                                            "FINAL":[],
                                            "Quantity":[],
                                            "xf":[],
                                            "Concentration":[],
                                            "Qty of Ions":[],
                                            "Qty of Neutrals":[]
                                            })

def update_ion22():
     ion_df = st.session_state.ion_df2

     for idx, row in ion_df.iterrows():
         quantity = row["Quantity"]
         xf = row["xf"]
         concentration = row["Concentration"]

         if xf == 1:  # Avoid division by zero if xf equals 1
             qty_of_ions = 0
         else:
             qty_of_ions = quantity * ((concentration - xf) / (1 - xf))

         qty_of_neutrals = quantity - qty_of_ions

         # Update the DataFrame with calculated values
         ion_df.loc[idx, "Qty of Ions"] = round(qty_of_ions,2)
         ion_df.loc[idx, "Qty of Neutrals"] = round(qty_of_neutrals,2)

         # Print statements for debugging (optional)
         print(f"Updated row {idx}: Qty of Ions = {qty_of_ions}, Qty of Neutrals = {qty_of_neutrals}")

     # Return the updated DataFrame
     return ion_df

def update_ion():
     for idx, change in st.session_state.changes["edited_rows"].items():
         for label, value in change.items():
             st.session_state.ion_df2.loc[idx, label] = value

     #return st.session_state.ion_df2

# Use st.data_editor with on_change
if not label_df.empty:
    st.write("")
    st.write("Enter Quantity and xf in below table")
    edited_ion_data = st.data_editor(label_df, width=616, key="changes", 
        column_config={
         "Sample ID": st.column_config.TextColumn(disabled=True),
         "Ratio": st.column_config.TextColumn(disabled=True),
         "RSD ppm": st.column_config.TextColumn(disabled=True),
         "Identifier": st.column_config.TextColumn(disabled=True),
         "FINAL": st.column_config.TextColumn(disabled=True),
         "Quantity": st.column_config.NumberColumn(disabled=False),
         "xf": st.column_config.NumberColumn(disabled=False),
         "Concentration": st.column_config.NumberColumn(label='xp',disabled=True,width="small"),
         "Qty of Ions": st.column_config.NumberColumn(disabled=True,width="small"),
         "Qty of Neutrals": st.column_config.NumberColumn(disabled=True,width="small"),
    })

    st.session_state.ion_df2 = pd.DataFrame(edited_ion_data)

    for idx, row in st.session_state.ion_df2.iterrows():
         if row["Quantity"] == None or row["xf"]==None:
             st.session_state.ion_df2.loc[idx, "Qty of Ions"] = None
             st.session_state.ion_df2.loc[idx, "Qty of Neutrals"] = None
         else:
             quantity = row["Quantity"]
             xf = row["xf"]
             concentration = row["Concentration"]
             qty_of_ions = round(quantity * (((concentration/100) - (xf/100)) / (1 - (xf/100) ) ),2)
             qty_of_neutrals = round(quantity - qty_of_ions,2)
             #neutrals_dev = ( (xt-xf)/(xf-1) ) * tails
    
             # Update the DataFrame with calculated values
             st.session_state.ion_df2.loc[idx, "Qty of Ions"] = qty_of_ions
             st.session_state.ion_df2.loc[idx, "Qty of Neutrals"] = qty_of_neutrals
    
             # Print statements for debugging (optional)
             print(f"Updated row {idx}: Qty of Ions = {qty_of_ions}, Qty of Neutrals = {qty_of_neutrals}")
    
    edited_ion_data = st.session_state.ion_df2
#st.data_editor(edited_ion_data)
try:
     required_data = st.session_state.ion_df2[['Quantity','xf','Concentration','Qty of Ions','Qty of Neutrals']]
     data_for_report = st.session_state.ion_df2[['Sample ID','Quantity','Concentration','Qty of Ions','Qty of Neutrals','xf']]
     st.write("")
     for idx,row in data_for_report.iterrows():

         if row['Quantity'] == None:
             qty = None
         else:
             qty = f"{row['Quantity']} mg @ {row['Concentration']}% (Equivalent to {round(row['Quantity']*row['Concentration']/74,2)} mg @ 74%)"

         ionization_df = pd.concat([ionization_df, pd.DataFrame({
             'Fraction':[row['Sample ID']],
             'Quantity':[qty],
             '175 Lu':[round(100 - row['Concentration'],2)],
             '176 Lu':[row['Concentration']],
             'Estimated Qty of Lu 176 as ions':[row['Qty of Ions']],
             'Estimated Qty of Neutrals':[row['Qty of Neutrals']],
             #'Stripping eff':[(row["xf"]-row["Concentration"])/52]
             #'neutrals_dev':[laser_power[if laser_power['Experiment'] in row['Sample ID']].iloc[i]]['xt']
             })], ignore_index = True)

     final_ionization_report = st.data_editor(ionization_df.fillna('-'),column_config={
         'Fraction':st.column_config.TextColumn(disabled=False),
         'Quantity':st.column_config.TextColumn(disabled=True),
         '175 Lu':st.column_config.NumberColumn(disabled=True),
         '176 Lu':st.column_config.NumberColumn(disabled=True),
         'Estimated Qty of Lu 176 as ions':st.column_config.TextColumn(disabled=True),
         'Estimated Qty of Neutrals':st.column_config.TextColumn(disabled=True),
     }, hide_index = True)

except:
     st.write("Exception Caught, handled !")
     pass

uni = list(dict.fromkeys(exp_list))

for row in uni:
     i = 0
     for indx,row_match in laser_power["Experiment"].items():
         if str(row_match) in str(row):
             #st.write("match found at index "+str(indx)+" :- "+str(row_match))
             #st.write("index: " +str(indx))
             #st.write(row_match["Laser power 1 (W)"])
             #st.write("CG: "+laser_power[laser_power['Experiment'] == row_match].iloc[i]['Voltages (CG)'])
             #st.write("CP: "+laser_power[laser_power['Experiment'] == row_match].iloc[i]['Voltages (CP)'])
             #st.write("RP: "+laser_power[laser_power['Experiment'] == row_match].iloc[i]['Voltages (RP)'])
             #st.write("RG: "+laser_power[laser_power['Experiment'] == row_match].iloc[i]['Voltages (RG)'])
             #st.write("Tails: "+laser_power[laser_power['Experiment'] == row_match].iloc[i]['Voltages (Tails)'])
             #st.write("CA: "+laser_power[laser_power['Experiment'] == row_match].iloc[i]['Voltages (CA)'])

             #st.write(f"Day{i+1}: "+laser_power[laser_power['Experiment'] == row_match].iloc[i]['Date'])
             #st.write("P1 = "+laser_power[laser_power['Experiment'] == row_match].iloc[i]['Laser power 1 (W)'])
             #st.write("P2 = "+laser_power[laser_power['Experiment'] == row_match].iloc[i]['Laser power 2 (W)'])
             #st.write("P3 = "+laser_power[laser_power['Experiment'] == row_match].iloc[i]['Laser power 3 (W)'])

             laser_parameter = pd.concat([laser_parameter,pd.DataFrame({
                 " ":[f"Day{i+1} ({laser_power[laser_power['Experiment'] == row_match].iloc[i]['Date']})"],
                 "P1":[laser_power[laser_power['Experiment'] == row_match].iloc[i]['Laser power 1 (W)']],
                 "P2":[laser_power[laser_power['Experiment'] == row_match].iloc[i]['Laser power 2 (W)']],
                 "P3":[laser_power[laser_power['Experiment'] == row_match].iloc[i]['Laser power 3 (W)']],
                 "CG":[laser_power[laser_power['Experiment'] == row_match].iloc[i]['Voltages (CG)']],
                 "CP":[laser_power[laser_power['Experiment'] == row_match].iloc[i]['Voltages (CP)']],
                 "RP":[laser_power[laser_power['Experiment'] == row_match].iloc[i]['Voltages (RP)']],
                 "RG":[laser_power[laser_power['Experiment'] == row_match].iloc[i]['Voltages (RG)']],
                 "Tails":[laser_power[laser_power['Experiment'] == row_match].iloc[i]['Voltages (Tails)']],
                 "CA":[laser_power[laser_power['Experiment'] == row_match].iloc[i]['Voltages (CA)']]

             })],ignore_index=True)

             i = i+1
         #else:
             #st.write("Match not found for: "+row)

laser_parameter.index = [f"{i+1}" for i in range(len(laser_parameter))]
if not laser_parameter.empty:
    st.dataframe(laser_parameter)
try:
    for idx,row in edited_ion_data["Sample ID"].items():
         i=0
         for indx, row_match in laser_power["Experiment"].items():
             if str(row_match) in str(row):
                 xt = laser_power[laser_power["Experiment"] == row_match].iloc[i]['xt']
                 tails_qty = laser_power[laser_power["Experiment"] == row_match].iloc[i]['Tails_Qty']
                 xf = laser_power[laser_power["Experiment"] == row_match].iloc[i]['xf']
                 #ions = edited_ion_data[edited_ion_data["Sample ID"] == row].iloc[i]['Qty of Ions']""
                 xp = laser_power[laser_power["Experiment"] == row_match].iloc[i]['xp']
                 ions_predicted = laser_power[laser_power["Experiment"] == row_match].iloc[i]['Ions predicted']
                 actual_ions = laser_power[laser_power["Experiment"] == row_match].iloc[i]['Ions']
    
                 neutrals_dev = (((xt-xf)/100)/((xf/100)-1))*tails_qty
                 ion_account = actual_ions*100/neutrals_dev
                 stripping_eff = (xf-xt)*100/0.52
    
                 st.write(f" xf = {xf}, xt = {xt}, xp = {xp}, tails_qty = {tails_qty}, ion = {actual_ions}")
                 st.write(f"Neutrals deviations = {neutrals_dev}")
                 st.write(f"Ion Accounting = {ion_account}")
                 st.write(f"Stripping Effieciency = {stripping_eff}")
                 st.write("Try block")
                 break
except:
    st.write("Error Caught")
#st.write(st.session_state['exp1'])
try:
    if st.button("Prepare Report"):
        pdf = FPDF('L','cm','A4')
        pdf.add_page()
        pdf.set_font('Helvetica', 'B',13)
    
        pdf.cell(0,0.5,f'{report_date.strftime("%d-%m-%Y")}',new_x=XPos.LMARGIN, new_y=YPos.NEXT,align='R')
        pdf.cell(0,0.5,f"Results of seperation experiment {selected_exp} carried out on {exp_conducted}",new_x=XPos.LMARGIN, new_y=YPos.NEXT,align='C')
        pdf.set_font('Helvetica', '',10)
        pdf.cell(0,0.5,"",new_x=XPos.LMARGIN, new_y=YPos.NEXT)
        
        with pdf.table(width=27.7,col_widths=(10, 25,10,10,10,10)) as table:
            row=table.row()
            for i in final_ionization_report.keys():
                row.cell(i,align="C")
            for index, row_set in final_ionization_report.iterrows():
                row=table.row()
                for i in final_ionization_report.keys():
                    row.cell(str(row_set[i]),align="C")
                    
        pdf.cell(0,0.5,"",new_x=XPos.LMARGIN, new_y=YPos.NEXT)
        pdf.set_font('Helvetica', 'B',10)
        pdf.cell(0,1,"Note:",new_x=XPos.LMARGIN, new_y=YPos.NEXT)
        pdf.set_font('Helvetica', '',10)
        with pdf.table(width=20,col_widths=(30,15,15,15,15,15,15,15,15,15),align='L') as table:
            row=table.row()
            for i in laser_parameter.keys():
                row.cell(i,align="C")
            for index, row_set in laser_parameter.iterrows():
                row=table.row() 
                for i in laser_parameter.keys():
                    row.cell(str(row_set[i]),align="C")
    
        pdf.cell(0,0.5,"",new_x=XPos.LMARGIN, new_y=YPos.NEXT)
        pdf.cell(0,0.5,"1. The tail quantity is as per weight difference of tail plate before and after the experiment along with peeled-off material collected and the multiplication factors for loss thru QTM",new_x=XPos.LMARGIN, new_y=YPos.NEXT)
        pdf.cell(0,0.5,"    opening is taken as 1.1",new_x=XPos.LMARGIN,new_y=YPos.NEXT)
        pdf.cell(0,0.1,"",new_x=XPos.LMARGIN, new_y=YPos.NEXT)
        pdf.cell(1,0.5,f"2. Stripping Effeciency = {round(stripping_eff,1)}% of addressable population of Lu-176; which itself is only ~0.52% total lutetium vapour. The calculations based on change in isotpoic compostion",new_x=XPos.LMARGIN, new_y=YPos.NEXT)
        pdf.cell(0,0.5,f"    of fraction near to the natural abundance should be considered with utmost care.",new_x=XPos.LMARGIN,new_y=YPos.NEXT)
        pdf.cell(0,0.7,f"3. The total ion collection estimated as per V-t product was {round(ions_predicted,1)} mg and the actual ion collection is {actual_ions} mg",new_x=XPos.LMARGIN, new_y=YPos.NEXT)
        pdf.cell(0,0.7,f"4. Ion Accounting = {round(ion_account,1)}%",new_x=XPos.LMARGIN, new_y=YPos.NEXT)
        pdf.cell(0,0.7,f"5. Estimated quantity is based on reults from ACD vide report no.{report_no}, dated {qty_report_date.strftime('%d-%m-%Y')}.",new_x=XPos.LMARGIN,new_y=YPos.NEXT)
        pdf.cell(0,0.7,f"6. Isotopic compostion of Lu-176 is based on its isotopic ratios with respect to Lu-175 as analysed at EmA&ID vide report dated {tims_report_date.strftime('%d-%m-%Y')}.",new_x=XPos.LMARGIN,new_y=YPos.NEXT)
        pdf.cell(0,0.7,f"7. Equivalent quantity has been calculated as (xp * P)/0.7; where 'xp' is product stream concentration and 'P' is product quantity/flow rate.",new_x=XPos.LMARGIN, new_y=YPos.NEXT)
        pdf.cell(0,0.7,f"8. Isoptopic compostion of natural Lutetium is as per measured feed compostion.",new_x=XPos.LMARGIN, new_y=YPos.NEXT)
    
        pdf.set_font('Helvetica', 'B',10)
        pdf.cell(0,1,"",new_x=XPos.LMARGIN, new_y=YPos.NEXT)
        pdf.set_margin(0)
        pdf.cell(pdf.w/4,1, "Prepared by:",align="C")
        pdf.cell(pdf.w/4,1, "Checked by:",align="C")
        pdf.cell(pdf.w/4,1, "Reviewed by:",align="C")
        pdf.cell(pdf.w/4,1, "Issued by:",new_x=XPos.LMARGIN,new_y=YPos.NEXT,align="C")
        pdf.cell(pdf.w/4,0.5, "Sutanwi Lahiri, IPDS",align="C")
        pdf.cell(pdf.w/4,0.5, "Dev Ranjan Das, IPDS",align="C")
        pdf.cell(pdf.w/4,0.5, "Anumpama Prabhala, IPDS",align="C")
        pdf.cell(pdf.w/4,0.5, "Sanjay Sethi, Head, IPDS, ATLAD",align="C")
    
        pdf.output("pdf_4.pdf")
except:
    st.write("Coludn't prepare report")
    st.write("Enter complete details which matches Laser Database.")
try:
    if st.button("Submit to Database"):
         updated_ion_data = pd.concat([ion_data, required_data], ignore_index=True)
         updated_ion_data.to_csv("./ion_report.csv", index=False)
         st.write("Report submitted")
except:
    st.write("Could not submit data to Database")
    pass