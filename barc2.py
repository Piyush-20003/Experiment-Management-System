import pandas as pd
import streamlit as st
import os
from fpdf import FPDF
from fpdf import FPDF, XPos, YPos
from datetime import *
from PIL import Image, UnidentifiedImageError

data = pd.read_csv("./Laser Power.csv")
tims_data = pd.read_csv("./TIMS.csv")
TEMP_DIR = "./temp_files"
os.makedirs(TEMP_DIR, exist_ok=True)

if 'home_visible' not in st.session_state:
     st.session_state['home_visible'] = True

if 'visible' not in st.session_state:
     st.session_state['visible'] = False
if 'experiment_name' not in st.session_state:
     st.session_state['experiment_name'] = ''
if 'material' not in st.session_state:
     st.session_state['material'] = ''
if 'date' not in st.session_state:
     st.session_state['date'] = ''
if 'num_days' not in st.session_state:
     st.session_state['num_days'] = 0

if 'laser_edit_visible' not in st.session_state:
     st.session_state['laser_edit_visible']=False

if 'delete_exp' not in st.session_state:
     st.session_state['delete_exp'] = ''
if 'delete_visible' not in st.session_state:
     st.session_state['delete_visible']= False

if 'tims_visible' not in st.session_state:
     st.session_state['tims_visible']= False
if 'tims_exp' not in st.session_state:
     st.session_state['tims_exp']=''
if 'tims_sample' not in st.session_state:
     st.session_state['tims_sample']=''
if 'tims_analysis' not in st.session_state:
     st.session_state['tims_analysis']=''
if 'sampl_id' not in st.session_state:
     st.session_state['sampl_id'] = ''
if 'tims_material' not in st.session_state:
     st.session_state['tims_material'] = ''
if 'tims_identifier' not in st.session_state:
     st.session_state['tims_identifier'] = ''

if 'tims_delete_visible' not in st.session_state:
     st.session_state['tims_delete_visible']=''
if 'tims_delete_exp' not in st.session_state:
     st.session_state['tims_delete_exp']=''

if 'tims_report_section' not in st.session_state:
     st.session_state['tims_report_section']=False
if 'report_visible' not in st.session_state:
     st.session_state['report_visible']=False

if 'ion_collection_rep' not in st.session_state:
     st.session_state['ion_collection_rep']=False

if 'ion_estimation_rep' not in st.session_state:
    st.session_state['ion_estimation_rep']=False

if "Laser_df" not in st.session_state:
     st.session_state.Laser_df = pd.read_csv("./Laser Power.csv")
     st.session_state.Laser_df['Date'] = pd.to_datetime(st.session_state.Laser_df['Date'])

if st.sidebar.button('Home'):
    st.session_state['home_visible'] = not st.session_state['home_visible']
    st.session_state['visible'] = False
    st.session_state['tims_visible'] = False
    st.session_state['laser_edit_visible']= False
    st.session_state['delete_visible']= False
    st.session_state['tims_delete_visible'] = False
    st.session_state['tims_report_section']=False
    st.session_state['ion_collection_rep']=False
    st.session_state['ion_estimation_rep']= False

if st.sidebar.button('Create New Experiment'):
    st.session_state['home_visible'] = False
    st.session_state['visible'] = not st.session_state['visible']
    st.session_state['tims_visible'] = False
    st.session_state['laser_edit_visible']= False
    st.session_state['delete_visible']= False
    st.session_state['tims_delete_visible'] = False
    st.session_state['tims_report_section']=False
    st.session_state['ion_collection_rep']=False
    st.session_state['ion_estimation_rep']= False

if  st.sidebar.button("Edit Laser Data"):
    st.session_state['home_visible'] = False
    st.session_state['visible'] = False
    st.session_state['tims_visible'] = False
    st.session_state['laser_edit_visible']= not st.session_state['laser_edit_visible']
    st.session_state['delete_visible']= False
    st.session_state['tims_delete_visible'] = False
    st.session_state['tims_report_section']=False
    st.session_state['ion_collection_rep']=False
    st.session_state['ion_estimation_rep']= False

if st.sidebar.button('Delete Experiment'):
    st.session_state['home_visible'] = False
    st.session_state['visible'] = False
    st.session_state['laser_edit_visible']= False
    st.session_state['delete_visible'] = not st.session_state['delete_visible']
    st.session_state['tims_visible'] = False
    st.session_state['tims_delete_visible'] = False
    st.session_state['tims_report_section']=False
    st.session_state['ion_collection_rep']=False
    st.session_state['ion_estimation_rep']= False

if st.sidebar.button("Enter New TIMS Data"):
    st.session_state['home_visible'] = False
    st.session_state['visible'] = False
    st.session_state['laser_edit_visible']= False
    st.session_state['tims_visible'] = not st.session_state['tims_visible']
    st.session_state['delete_visible']= False
    st.session_state['tims_delete_visible'] = False
    st.session_state['tims_report_section']=False
    st.session_state['ion_collection_rep']=False
    st.session_state['ion_estimation_rep']= False

if st.sidebar.button('Delete TIMS Data'):
    st.session_state['home_visible'] = False
    st.session_state['visible'] = False
    st.session_state['laser_edit_visible']= False
    st.session_state['delete_visible']= False
    st.session_state['tims_visible'] = False
    st.session_state['tims_delete_visible'] = not st.session_state['delete_visible']
    st.session_state['tims_report_section']=False
    st.session_state['ion_collection_rep']=False
    st.session_state['ion_estimation_rep']= False

if st.sidebar.button('TIMS Report'):
    st.session_state['home_visible'] = False
    st.session_state['visible'] = False
    st.session_state['laser_edit_visible']= False
    st.session_state['delete_visible']= False
    st.session_state['tims_visible'] = False
    st.session_state['tims_delete_visible'] = False
    st.session_state['tims_report_section']= not st.session_state['tims_report_section']
    st.session_state['ion_collection_rep']=False
    st.session_state['ion_estimation_rep']= False


if st.sidebar.button("Ion Collection Report"):
    st.session_state['home_visible'] = False
    st.session_state['visible'] = False
    st.session_state['laser_edit_visible']= False
    st.session_state['delete_visible']= False
    st.session_state['tims_visible'] = False
    st.session_state['tims_delete_visible'] = False
    st.session_state['tims_report_section']= False
    st.session_state['ion_collection_rep']= not st.session_state['ion_collection_rep']
    st.session_state['ion_estimation_rep']= False
    
if st.sidebar.button("Ion Estimation Report"):
    st.session_state['home_visible'] = False
    st.session_state['visible'] = False
    st.session_state['laser_edit_visible']= False
    st.session_state['delete_visible']= False
    st.session_state['tims_visible'] = False
    st.session_state['tims_delete_visible'] = False
    st.session_state['tims_report_section']= False
    st.session_state['ion_collection_rep']= False
    st.session_state['ion_estimation_rep']= not st.session_state['ion_estimation_rep']
#-----------------------------------------------------Dashboard--------------------------------------------------------------
st.write("")
if st.session_state['home_visible']:

     if "custom1" not in st.session_state:
         st.session_state['custom1']=''
     if "custom2" not in st.session_state:
         st.session_state['custom2']=''
     if "customv" not in st.session_state:        # v stands for visibility
         st.session_state['customv']=False

     custom_filter = []
     custom_df = pd.DataFrame()
     filtered_period = []
     chart_df = pd.DataFrame()
     monthly_filter_period = []
     monthly_df = pd.DataFrame()
     laser_dates =[]

     dash_col1,dash_col2 = st.columns(2)
     with dash_col1:
         user_choice = st.radio("Choose an option",options=["Custom","Monthly","Yearly"])
     with dash_col2:
         mat_choice = st.radio("Choose Material",["Lu","Yb","Both"])
     st.write("")
    
     for i in data["Date"]:
         laser_dates.append(pd.Period(i,freq="D"))

     period_series=pd.Series(laser_dates)

     if user_choice == "Custom":
         st.session_state['customv']= True

     if user_choice == "Monthly":
         st.session_state['customv']= False
         st.write("")
         for i in range(len(period_series)):
             if period_series[i].month == date.today().month:
                 monthly_filter_period.append(period_series[i])

     #st.write(pd.Series(monthly_filter_period))
         mfp = pd.Series(monthly_filter_period).unique()

         for i in range(len(mfp)):
             if mat_choice == "Lu":
                 monthly_df = pd.concat([monthly_df,data[(data["Date"] == str(mfp[i])) & (data["Material"] == "Lu")] ])
             elif mat_choice == "Yb":
                 monthly_df = pd.concat([monthly_df,data[(data["Date"] == str(mfp[i])) & (data["Material"] == "Yb")] ])
             elif mat_choice == "Both":
                 monthly_df = pd.concat([monthly_df,data[(data["Date"] == str(mfp[i])) & ((data["Material"] == "Lu") | (data["Material"] == "Yb")) ] ])
         
         st.write("No. of Experiments in this month: ",len(monthly_df["Experiment"]))
         monthly_mat=0
         for i in monthly_df["Qty (mg)"]:
             monthly_mat=monthly_mat+int(i)
         st.write("Total Material Collected: ",monthly_mat," mg")

         if not monthly_df.empty:
             st.bar_chart(monthly_df, x="Date", y="Qty (mg)")

     if user_choice == "Yearly":
         st.session_state['customv'] = False
         start_date = pd.Period(date(date.today().year-1,date.today().month,date.today().day),freq="D")
         end_date = pd.Period(date.today(),freq="D")

         filtered_period = [i for i in period_series if start_date <= i <= end_date]

         fps = pd.Series(filtered_period).unique()

         for i in range(len(fps)):
         #data[data["Date"] == str(fps[i])]
             if mat_choice == "Lu":
                 chart_df = pd.concat([chart_df,data[(data["Date"] == str(fps[i])) & (data["Material"] == "Lu")] ])
             elif mat_choice == "Yb":
                 chart_df = pd.concat([chart_df,data[(data["Date"] == str(fps[i])) & (data["Material"] == "Yb")] ])
             elif mat_choice == "Both":
                 chart_df = pd.concat([chart_df,data[(data["Date"] == str(fps[i])) & ((data["Material"] == "Lu") | (data["Material"] == "Yb")) ] ])

         st.write(f"No. of Experiments from {start_date.strftime('%d-%m-%Y')}  to  {end_date.strftime('%d-%m-%Y')} : ",str(len(chart_df["Experiment"])))

         sum_of_qty=0
         for i in chart_df["Qty (mg)"]:
             sum_of_qty=sum_of_qty+int(i)

         st.write("Total Material Collected: ",sum_of_qty," mg")
         if not chart_df.empty:
             st.bar_chart(chart_df, x="Date", y="Qty (mg)")

     if st.session_state['customv']:

         try:
             st.session_state['custom1'],st.session_state['custom2'] = st.date_input("Enter Custom Date",[date.today(),date.today()],format="DD-MM-YYYY")
         except ValueError:
             st.write("This is try block, Exception Handled")
         pass

         custom_range = pd.period_range(start=st.session_state['custom1'],end=st.session_state['custom2'],freq="D")
     #st.write(custom_range.strftime("%d-%m-%Y"))

         custom1 = pd.Period(st.session_state['custom1'],freq="D")
         custom2 = pd.Period(st.session_state['custom2'],freq="D")

         custom_filter = [i for i in custom_range if custom1 <= i <= custom2]

         if mat_choice == "Lu":
             for i in range(len(custom_filter)):
                 custom_df = pd.concat([custom_df,data[(data["Date"] == str(custom_filter[i])) & (data["Material"] == "Lu")] ])
         elif mat_choice == "Yb":
             for i in range(len(custom_filter)):
                 custom_df = pd.concat([custom_df,data[(data["Date"] == str(custom_filter[i])) & (data["Material"] == "Yb")] ])

         elif mat_choice == "Both":
             for i in range(len(custom_filter)):
                 custom_df = pd.concat([custom_df,data[(data["Date"] == str(custom_filter[i])) & ((data["Material"] == "Lu") | (data["Material"] == "Yb")) ] ])

         #custom_df = pd.concat([custom_df,data[data["Date"] == str(custom_filter[i])] ])
     #st.write(custom_df)
         st.write(f"No. of Experiments from  {custom1.strftime('%d-%m-%Y')}  to  {custom2.strftime('%d-%m-%Y')}: ",len(custom_df["Experiment"]) )
         custom_mat=0
         for i in custom_df["Qty (mg)"]:
             custom_mat = custom_mat+int(i)

         st.write("Total Material Collected: ",custom_mat," mg")
         if not custom_df.empty:
             st.bar_chart(custom_df, x="Date", y="Qty (mg)")

#-----------------------------------------------------create Experiment--------------------------------------------------------

if st.session_state['visible']:
     st.session_state['experiment_name'] = st.text_input("Name of Experiment")
     st.session_state['material'] = st.selectbox("Material", ["Lu","Yb"])
     st.session_state['date'] = st.date_input("Date")
     st.session_state['num_days'] = st.number_input("Number of Days",1,100)

     if st.button('Submit'):
         user_data = {
             'Material':[st.session_state['material']],
             'Experiment':[st.session_state['experiment_name']],
             'Date':[st.session_state['date']],
             'Days':[st.session_state['num_days']]
         }
         new_row = pd.DataFrame(user_data)

         updated_data = pd.concat([data, new_row], ignore_index=True)
         updated_data.to_csv("./Laser Power.csv", index = False)
         st.write("Successfully Created Experiment")
#-----------------------------------------------------------Edit Laser Experiment--------------------------------------------------
if st.session_state['laser_edit_visible']:
    # Laser_df = pd.DataFrame(data)
    # Laser_df['Date'] = pd.to_datetime(Laser_df['Date'])
    
    def update():       
        for idx, change in st.session_state.changes["edited_rows"].items():
            for label, value in change.items():
                st.session_state.Laser_df.loc[idx, label] = value

    if st.button("Refresh"):
        st.session_state.Laser_df = None
        st.session_state.Laser_df = pd.read_csv("./Laser Power.csv")
        st.session_state.Laser_df['Date'] = pd.to_datetime(st.session_state.Laser_df['Date'])
        st.write("Refresh clicked")

    st.session_state.Laser_df['Date'] = pd.to_datetime(st.session_state.Laser_df['Date'])
    
    edited_laser_data = st.data_editor(st.session_state.Laser_df,key="changes",on_change=update,width=900,hide_index=True,num_rows="dynamic",
        column_config={
            "Date": st.column_config.DateColumn(format="DD-MM-YYYY"),
            "Report Status": st.column_config.SelectboxColumn(options=["Released", "Pending"])
        }
    )

    # Save the edited data back to the CSV file
    if st.button("Confirm changes"):
        edited_laser_data.to_csv("./Laser Power.csv", index=False)
        st.write("Changes Confirmed")
#-----------------------------------------------------delete Experiment---------------------------------------------------------
if st.session_state['delete_visible']:
     column = data['Experiment']
     st.session_state['delete_exp'] = st.sidebar.selectbox("Select Experiment to Delete",column)

     if st.sidebar.button('Delete'):
         condition = data['Experiment']== st.session_state['delete_exp']
         new_data = data[~condition]
         new_data.to_csv('Laser Power.csv',index=False)

#-----------------------------------------------------TIMS Data------------------------------------------------------------------
if st.session_state['tims_visible']:
     st.header("Enter TIMS Data")
     st.write("")
     st.session_state['tims_exp'] = st.text_input("Experiment")
     st.session_state['tims_sample'] = st.text_input("Sample")
     st.session_state['tims_analysis']=st.selectbox("Analysis Done By",["","RUS","TAB","PM"])
     st.session_state['tims_material'] = st.selectbox("Select Material",["", "Lu", "Yb"], index=0)
     st.session_state['sampl_id'] = (st.session_state['tims_exp'] +" "+st.session_state['tims_material'] +" "+st.session_state['tims_sample'])
     st.session_state['tims_identifier'] = st.selectbox("Choose Identifier",['',"A","B","C","D","E","G","H"])

     if st.session_state['tims_material'] == "Yb":

         def update():
             for idx, change in st.session_state.changes["edited_rows"].items():
                 for label, value in change.items():
                     st.session_state.Yb_df.loc[idx, label] = value

         if "Yb_df" not in st.session_state:
             st.session_state.Yb_df = pd.DataFrame({"index":["168/173","170/173","171/173","172/173","174/173","176/173"],
                                                 "Raw Ratio":['0','0','0','0','0','0'],
                                                 "Raw RSD":['0','0','0','0','0','0'],
                                                 "Precision":[0,0,0,0,0,0],
                                                 "Final Ratio":['0','0','0','0','0','0' ],
                                                 "Final RSD ppm":['0','0','0','0','0','0' ] })

         try:
             st.session_state.Yb_df["Precision"] = round(st.session_state.Yb_df["Raw Ratio"].astype(float) * round(st.session_state.Yb_df["Raw RSD"].astype(float), 2) * 0.000003, 6)
         except ValueError:
             st.warning('Enter Valid Input, Input Must be a Number')

         st.data_editor(st.session_state.Yb_df, key="changes",on_change=update,width=700,hide_index=True,
                column_config= {
                    "index":st.column_config.TextColumn(width="small",disabled=True,label=""),
                    "Precision":st.column_config.TextColumn(disabled=True),
                    "Raw Ratio":st.column_config.TextColumn(),
                    "Raw RSD":st.column_config.TextColumn()
                })
         edited_data = st.session_state.Yb_df[['index','Final Ratio','Final RSD ppm']]

     if st.session_state['tims_material'] == "Lu":
         def update():
             for idx, change in st.session_state.changes["edited_rows"].items():
                 for label, value in change.items():
                     st.session_state.Lu_df.loc[idx, label] = value

         if "Lu_df" not in st.session_state:
             st.session_state.Lu_df = pd.DataFrame({"index":["176/175"],
                                                 "Raw Ratio":['0'],
                                                 "Raw RSD":['0'],
                                                 "Precision":[0],
                                                 "Final Ratio":['0'],
                                                 "Final RSD ppm":['0'] })

         try:
             st.session_state.Lu_df["Precision"] = round(st.session_state.Lu_df["Raw Ratio"].astype(float) * round(st.session_state.Lu_df["Raw RSD"].astype(float), 2) * 0.000003, 6)
         except ValueError:
             st.warning('Enter Valid Input, Input Must be a Number')

         st.data_editor(st.session_state.Lu_df, key="changes",on_change=update,width=700, hide_index=True,
                column_config= {
                    "index":st.column_config.TextColumn(width="small",disabled=True,label=""),
                    "Precision":st.column_config.TextColumn(width="None",disabled=True,label="Precision"),
                    "Raw Ratio":st.column_config.TextColumn(),
                    "Raw RSD":st.column_config.TextColumn()
                })
         edited_data = st.session_state.Lu_df[['index','Final Ratio','Final RSD ppm']]


     if st.button("Submit TIMS Data"):
         final_data = {
             'Exp':st.session_state['tims_exp'],
             'Sample':st.session_state['tims_sample'],
             'Analysis Done By':st.session_state['tims_analysis'],
             'Material':st.session_state['tims_material'],
             'Sample ID': st.session_state['sampl_id'],
             'Identifier':st.session_state['tims_identifier'],
             'Ratio':edited_data['Final Ratio'],
             'RSD ppm':edited_data['Final RSD ppm'],
             'FINAL':edited_data['index']
         }
         # Append edited data to the existing data and save to CSV
         updated_data = pd.concat([tims_data, pd.DataFrame(final_data)],ignore_index=True)
         updated_data.to_csv("./TIMS.csv", index=False)

         data_to_laser = pd.concat([data,pd.DataFrame({
             "Experiment":[st.session_state['tims_exp']]
         })],ignore_index=True)

         if st.session_state['tims_exp'] in set(data["Experiment"]):
             st.write(f"Experiment {st.session_state['tims_exp']} already in Laser Power")

         else:
             data_to_laser.to_csv("./Laser Power.csv", index=False)
             st.session_state.Laser_df = None
             st.session_state.Laser_df = pd.DataFrame(data)
         st.write("Data Submitted")
#---------------------------------------------------------Delete TIMS DATA--------------------------------------------------------
if st.session_state['tims_delete_visible']:
     sample_id_column = tims_data['Sample ID']
     st.session_state['tims_delete_exp'] = st.sidebar.selectbox("Select Sample ID to Delete",sample_id_column)
     st.sidebar.warning("This will Delete all the matching Sample ID entries with the selected one ")

     if st.sidebar.button('Delete Selected TIMS Data'):
         tims_condition = tims_data['Sample ID']== st.session_state['tims_delete_exp']
         tims_new_data = tims_data[~tims_condition]
         tims_new_data.to_csv('TIMS.csv',index=False)
         st.sidebar.write("Selected Sample ID Deleted")

#------------------------------------------------------TIMS Report------------------------------------------------------------------

if st.session_state['tims_report_section']:

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

     for i in range(sample_no):
         with col1:
             mat = st.selectbox(" ", ["", "Yb", "Lu"], key=f"mat{i}", placeholder="Material")

         with col2:
             new_data = tims_data[tims_data['Material'] == mat]
             options_exp = [""] + new_data['Exp'].unique().tolist()
             selected_exp = st.selectbox(" ",options_exp, key=f"exp{i}")

         with col3:
             sample_data = new_data[new_data['Exp'] == selected_exp]['Sample']
             selected_sample = st.selectbox(" ", sample_data.unique(), key=f"samp{i}")

         with col4:
             try:
                 samp_id = f"{st.session_state[f'exp{i}']} {st.session_state[f'mat{i}']} {st.session_state[f'samp{i}']}"
            # st.text_input("", value=samp_id,key=f"sample_key{i}",disabled=True)
             except TypeError:
                 pass

             selected_identifier = st.selectbox(" ",tims_data[tims_data['Sample ID'] == samp_id]['Identifier'].unique(),key=f"identity{i}")

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
             "FINAL":[row['FINAL']]
             })], ignore_index=True)

     if not label_df.empty:
         st.data_editor(label_df,column_config={
             "Sample ID":st.column_config.TextColumn(disabled=True),
             "Ratio":st.column_config.TextColumn(disabled=True),
             "RSD ppm":st.column_config.TextColumn(disabled=True),

             })

     try:

         grouped = label_df.groupby('Sample ID')
     # Iterate over groups
         for sample_id, group_data in grouped:
     # Get unique Identifiers for the current SampleID
             identifiers = group_data['Identifier'].unique()

     # Create a row for each Identifier
             for identifier in identifiers:
         # Filter data for the current SampleID and Identifier
                 filtered_data = group_data[group_data['Identifier'] == identifier]

             # Initialize a dictionary to hold ratios
                 if 'Lu' in sample_id:
                     ratios={
                         '176/175':None
                     }
                 elif 'Yb' in sample_id:
                     ratios = {
                 '168/173': None,
                 '170/173': None,
                 '171/173': None,
                 '172/173': None,
                 '174/173': None,
                 '176/173': None

                     }

         # Update ratios with available values
                 for final, ratio,rsd in zip(filtered_data['FINAL'],filtered_data['Ratio'],filtered_data['RSD ppm'] ):
                     ratios[final] = str(ratio) +"  ±  "+ str(rsd)

         # Create a DataFrame for the current Identifier and ratios
                 identifier_df = pd.DataFrame({
                 'Sample ID': [sample_id],
                 **ratios  # Unpack the dictionary into columns
             })

         # Append the current Identifier DataFrame to the main df±
                 df = pd.concat([df, identifier_df], ignore_index=True)

# Fill NaN values with blank spaces
         data_for_report = df.fillna('-')
         st.write("#### Table Report:")

         st.data_editor(data_for_report,key='report',disabled=True,column_config={
             "Sample ID":st.column_config.TextColumn(disabled=True),
             "168/173":st.column_config.TextColumn(disabled=True),
             "170/173":st.column_config.TextColumn(disabled=True),
             "171/173":st.column_config.TextColumn(disabled=True),
             "172/173":st.column_config.TextColumn(disabled=True),
             "174/173":st.column_config.TextColumn(disabled=True),
             "176/173":st.column_config.TextColumn(disabled=True)
         })

         if st.button("Generate report"):
             pdf = FPDF('L','cm','A4')
             pdf.add_page()

             pdf.set_font('Helvetica', 'B',10)
             pdf.cell(0,0.5,'Electromagnetic Application & Instrumentation Division',new_x=XPos.LMARGIN,new_y=YPos.NEXT,align='C',border=False)
             pdf.cell(0,0.5,'Physics Group',new_x=XPos.LMARGIN,new_y=YPos.NEXT,align='C',border=False)
             if 'Lu' in sample_id:
                 pdf.cell(0,0.5,'Report on Isotopic Analysis of Lu Samples',new_x=XPos.LMARGIN, new_y=YPos.NEXT,align='C',border=False)
             if 'Yb' in sample_id:
                 pdf.cell(0,0.5,'Report on Isotopic Analysis of Yb Samples',new_x=XPos.LMARGIN, new_y=YPos.NEXT,align='C',border=False)

             pdf.cell(0,0.4,f'Date: {date.today().strftime("%d-%m-%Y")} ',new_x=XPos.LMARGIN, new_y=YPos.NEXT,align='R',border=False)
             pdf.cell(0,0.7,'Isotopic Ratio',new_x=XPos.LMARGIN,new_y=YPos.NEXT,align='C',border=True)

             pdf.set_font('Helvetica', '',10)
             srno= pd.DataFrame({
             "S.No.":[]
             },dtype=str)

             for i in range(len(data_for_report["Sample ID"])):
                 srno.loc[i, 'S.No.'] = str(i + 1)

             df_report = pd.concat([pd.DataFrame(srno),pd.DataFrame(data_for_report)],axis=1)
             print(df_report)
             with pdf.table() as table:
                 row=table.row()
                 for i in df_report.keys():
                     row.cell(i,align="C")
                 for index, row_set in df_report.iterrows():

                      row=table.row()
                      for i in df_report.keys():
                         row.cell(row_set[i],align="C")


             pdf.cell(0,1," ",new_x=XPos.LMARGIN, new_y=YPos.NEXT)
             pdf.cell(0,0,' Technique used: Thermal Ionization Mass Spectrometry',align='L',border=False)
             pdf.cell(0,0,'Instrument used: Indigenous compact TIMS',new_x=XPos.LMARGIN, new_y=YPos.NEXT,align='R',border=False)
             pdf.cell(0,2.5," ",new_x=XPos.LMARGIN, new_y=YPos.NEXT)
             pdf.cell(pdf.w/2,0.5,f'Dr. R. K Bhatia,SO/G,',align='C',border=False)
             pdf.cell(pdf.w/2,0.5,f'Shri D. R. Das,SO/G,',new_x=XPos.LMARGIN, new_y=YPos.NEXT,align='C',border=False)
             pdf.cell(pdf.w/2,0.5,'AMSS/EmA&ID',align='C',border=False)
             pdf.cell(pdf.w/2,0.5,'IPDS, ATLAD, BTDG',new_x=XPos.LMARGIN,new_y=YPos.NEXT,align='C',border=False)

             pdf.cell(0,1.5," ",new_x=XPos.LMARGIN, new_y=YPos.NEXT)
             pdf.cell(0,0.5,'Approved by: Shri Natraju V.,',new_x=XPos.LMARGIN, new_y=YPos.NEXT,align='C',border=False)
             pdf.cell(0,0.5,'Head, AMSS/ EmA&ID',new_x=XPos.LMARGIN,new_y=YPos.NEXT,align='C',border=False)
             pdf.cell(0,1," ",new_x=XPos.LMARGIN, new_y=YPos.NEXT)
             pdf.cell(0,0.5,'Sample Preparation, Sample loading and Sample analysis by Shri R U Satpute, SA/F, Smt. Tripti A Barnwal,SA/E,Smt. Priya M.,SA/D,Shri Sunil Dehade,T/H,ATLAD,BTDG',new_x=XPos.LMARGIN, new_y=YPos.NEXT,border=False)
             #pdf.cell(0,0.5,"")
             pdf.output('pdf_2.pdf')
             st.success("Report Generated")
             with open("pdf_2.pdf", "rb") as pdf_file:
                 PDFbyte = pdf_file.read()

             st.download_button( label="Download Report",
                                 data=PDFbyte,
                                 file_name="TIMS.pdf",
                                 mime='application/octet-stream')
     except:
         pass
#----------------------------------------------ION Collection Report----------------------------------------------------------------------
if st.session_state['ion_collection_rep']:
     def save_uploaded_file(uploaded_file):
         if uploaded_file is not None:
         # Generate a unique filename using timestamp
             timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
             file_name, file_extension = os.path.splitext(uploaded_file.name)
             unique_file_name = f"{file_name}_{timestamp}{file_extension}"

             file_path = os.path.join(TEMP_DIR, unique_file_name)

             with open(file_path, "wb") as f:
                 f.write(uploaded_file.getbuffer())

             return file_path

         return None

     def cleanup_temp_files():
         """Remove all files in the TEMP_DIR."""
         for filename in os.listdir(TEMP_DIR):
             file_path = os.path.join(TEMP_DIR, filename)
             if os.path.isfile(file_path):
                 os.remove(file_path)

     exp = st.text_input("Enter Experiment")
     if exp:
         st.write(f" Data Analyisis of {exp} Lu LIS run")

     dates=[] #date = pd.to_datetime(dates)
     ion_report_data={
         "Date":[],
         "Duration(mins)":[],
         "Estimated Ion Collection":[],
         }
     ion_report_img=[]
     image_paths = []
     days = st.number_input("Enter No. of Days",step=1)

     label_ion1, label_ion2, label_ion3 = st.columns(3)

     with label_ion1:
         st.write("Date")
     with label_ion2:
         st.write("Duration(mins)")
     with label_ion3:
         st.write("Ion collection Estimation (mg)")

     for i in range(days):
         ion_col1, ion_col2, ion_col3  = st.columns(3)

         with ion_col1:
             ion_date = st.date_input(" ",format="MM.DD.YYYY",key=f"date{i}")

         with ion_col2:
             duration = st.number_input(" ",key=f"duration{i}")

         with ion_col3:
             ion_collection = st.number_input(" ",key=f"collect_ion{i}")

         ion_report_data["Date"].append(str(ion_date))
         ion_report_data["Duration(mins)"].append(str(duration))
         ion_report_data["Estimated Ion Collection"].append(str(ion_collection)+' mg')

         uploaded_file = st.file_uploader(' ',key=f"file{i}")
         ion_report_img.append(uploaded_file)
         image_paths.append(save_uploaded_file(uploaded_file))


         st.write(" ")
         st.write(" ")
     if not pd.DataFrame(ion_report_data).empty:
         st.write("#### Table Report")
         st.data_editor(pd.DataFrame(ion_report_data),hide_index=True,disabled=True)
    
     try:
         for idx,img in enumerate(ion_report_img):
             st.image(img)
        
         if st.button("Generate Report") and days>0:
             pdf = FPDF('L','cm','A4')
             pdf.add_page()
             pdf.set_font('Helvetica', 'B',17)
             
             pdf.cell(0,1,f"Data Analysis of {exp} Lu LIS run",new_x=XPos.LMARGIN, new_y=YPos.NEXT)
             pdf.set_font('Helvetica', 'B',15)
             pdf.cell(0,1,'Experiment Result:',new_x=XPos.LMARGIN,new_y=YPos.NEXT,border=False)
             pdf.cell(0,1,f"Date: {date.today().strftime('%d-%m-%Y')}",new_x=XPos.RMARGIN,new_y=YPos.NEXT,align='R')
             pdf.set_font('Helvetica', '',10)
             
             srno= pd.DataFrame({
                 "Day":[]
            },dtype=str)

             for i in range(len(ion_report_data["Date"])):
                 srno.loc[i, 'Day'] = "Day "+ str(i + 1)

             df_report= pd.concat([pd.DataFrame(srno),pd.DataFrame(ion_report_data)],axis=1)
             print(df_report)
             with pdf.table() as table:
                 row=table.row()
                 for i in df_report.keys():
                     row.cell(i,align="C")
                 for index, row_set in df_report.iterrows():

                      row=table.row()
                      for i in df_report.keys():
                         row.cell(row_set[i],align="C")

             pdf.cell(0,1," ",new_x=XPos.LMARGIN, new_y=YPos.NEXT)
             pdf.set_margin(0)
             i=0
             for image_path,date in zip(image_paths,ion_report_data["Date"]):
                 pdf.cell(0,1.5," ",new_x=XPos.LMARGIN, new_y=YPos.NEXT)
                 pdf.image(image_path, h=10, w=23,x=3.8)
                 pdf.cell(0,1.5,f"Figure  {i+1}:  Ion  Collection  Plot on  {date}",new_x=XPos.LMARGIN, new_y=YPos.NEXT,align='C')
                 i=i+1

             pdf.output('pdf_3.pdf')
             st.success("Report Prepared")
             with open("pdf_3.pdf", "rb") as pdf_file:
                     PDFbyte = pdf_file.read()

             st.download_button( label="Download Report",
                                 data=PDFbyte,
                                 file_name="Ion Collection Report.pdf",
                                 mime='application/octet-stream')
             cleanup_temp_files()       
             
     except UnidentifiedImageError:
         st.write("#### Please Enter Valid Image")
     except:
         pass
#---------------------------------------------------------------ION Estimation Report------------------------------------------------------------------
if st.session_state['ion_estimation_rep']:
    ion_data = pd.read_csv("./ion_report.csv")
    
    if 'qt' not in st.session_state:
         st.session_state['qt']=None
    
    if 'xf' not in st.session_state:
         st.session_state['xf']=None
         
    repo_date1,repo_date2 = st.columns(2)
    with repo_date1:
        exp_conducted = st.text_input("Enter Dates when Experiment was conducted")
    with repo_date2:
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
             mat = st.selectbox(" ", ["", "Yb", "Lu"], key=f"mat{i}", placeholder="Material")

         with col2:
             new_data = tims_data[tims_data['Material'] == mat]
             options_exp = [""] + new_data['Exp'].unique().tolist()
             selected_exp = st.selectbox(" ",options_exp, key=f"exp{i}")
    
         with col3:
             sample_data = new_data[new_data['Exp'] == selected_exp]['Sample']
             selected_sample = st.selectbox(" ", sample_data.unique(),key=f"samp{i}")
    
         with col4:
             try:
                 samp_id = f"{st.session_state[f'exp{i}']} {st.session_state[f'mat{i}']} {st.session_state[f'samp{i}']}"
                # st.text_input("", value=samp_id,key=f"sample_key{i}",disabled=True)
             except TypeError:
                 pass
    
             selected_identifier = st.selectbox(" ",tims_data[tims_data['Sample ID'] == samp_id]['Identifier'].unique(),key=f"identity{i}")
    
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
        
                 # Update the DataFrame with calculated values
                 st.session_state.ion_df2.loc[idx, "Qty of Ions"] = qty_of_ions
                 st.session_state.ion_df2.loc[idx, "Qty of Neutrals"] = qty_of_neutrals
        
        edited_ion_data = st.session_state.ion_df2
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
         #st.write("Exception Caught, handled !")
         pass
        
    uni = list(dict.fromkeys(exp_list))
    
    for row in uni:
         i = 0
         for indx,row_match in data["Experiment"].items():
             if str(row_match) in str(row):
                 #st.write("match found at index "+str(indx)+" :- "+str(row_match))
                 
                 laser_parameter = pd.concat([laser_parameter,pd.DataFrame({
                     " ":[f"Day{i+1} ({data[data['Experiment'] == row_match].iloc[i]['Date']})"],
                     "P1":[data[data['Experiment'] == row_match].iloc[i]['Laser power 1 (W)']],
                     "P2":[data[data['Experiment'] == row_match].iloc[i]['Laser power 2 (W)']],
                     "P3":[data[data['Experiment'] == row_match].iloc[i]['Laser power 3 (W)']],
                     "CG":[data[data['Experiment'] == row_match].iloc[i]['Voltages (CG)']],
                     "CP":[data[data['Experiment'] == row_match].iloc[i]['Voltages (CP)']],
                     "RP":[data[data['Experiment'] == row_match].iloc[i]['Voltages (RP)']],
                     "RG":[data[data['Experiment'] == row_match].iloc[i]['Voltages (RG)']],
                     "Tails":[data[data['Experiment'] == row_match].iloc[i]['Voltages (Tails)']],
                     "CA":[data[data['Experiment'] == row_match].iloc[i]['Voltages (CA)']]
    
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
             for indx, row_match in data["Experiment"].items():
                 if str(row_match) in str(row):
                     xt = data[data["Experiment"] == row_match].iloc[i]['xt']
                     tails_qty = data[data["Experiment"] == row_match].iloc[i]['Tails_Qty']
                     xf = data[data["Experiment"] == row_match].iloc[i]['xf']
                     #ions = edited_ion_data[edited_ion_data["Sample ID"] == row].iloc[i]['Qty of Ions']""
                     xp = data[data["Experiment"] == row_match].iloc[i]['xp']
                     ions_predicted = data[data["Experiment"] == row_match].iloc[i]['Ions predicted']
                     actual_ions = data[data["Experiment"] == row_match].iloc[i]['Ions']
        
                     neutrals_dev = (((xt-xf)/100)/((xf/100)-1))*tails_qty
                     ion_account = actual_ions*100/neutrals_dev
                     stripping_eff = (xf-xt)*100/0.52
        
                     st.write(f" xf = {xf}, xt = {xt}, xp = {xp}, tails_qty = {tails_qty}, ion = {actual_ions}")
                     #st.write(f"Neutrals deviations = {neutrals_dev}")
                     st.write(f"Ion Accounting = {ion_account}")
                     st.write(f"Stripping Effieciency = {stripping_eff}")
                     break
    except:
        pass
        #st.write("Error Caught")
    #st.write(st.session_state['exp1'])
    try:
        if st.button("Prepare Report"):
            pdf = FPDF('L','cm','A4')
            pdf.add_page()
            pdf.set_font('Helvetica', 'B',13)
        
            pdf.cell(0,0.5,f'Date: {report_date.strftime("%d-%m-%Y")}',new_x=XPos.LMARGIN, new_y=YPos.NEXT,align='R')
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
            st.success("Report Generated")
            with open("pdf_4.pdf", "rb") as pdf_file:
                     PDFbyte = pdf_file.read()
            st.download_button( label="Download Report",
                                 data=PDFbyte,
                                 file_name="Ion Estimation Report.pdf",
                                 mime='application/octet-stream')
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
