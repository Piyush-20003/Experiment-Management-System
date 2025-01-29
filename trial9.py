import pandas as pd
import streamlit as st
data = pd.read_csv("./Laser Power1.csv")
tims_data = pd.read_csv("./TIMS.csv")

if 'home_visible' not in st.session_state:
     st.session_state['home_visible'] = False

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

if 'Yb 168-173 ratio' not in st.session_state:
     st.session_state['Yb 168-173 ratio']=''
if 'Yb 170-173 ratio' not in st.session_state:
     st.session_state['Yb 170-173 ratio']=''
if 'Yb 171-173 ratio' not in st.session_state:
     st.session_state['Yb 171-173 ratio']=''
if 'Yb 172-173 ratio' not in st.session_state:
     st.session_state['Yb 172-173 ratio']=''
if 'Yb 174-173 ratio' not in st.session_state:
     st.session_state['Yb 174-173 ratio']=''
if 'Yb 176-173 ratio' not in st.session_state:
     st.session_state['Yb 176-173 ratio']=''

if 'Yb 168-173 rsd' not in st.session_state:
     st.session_state['Yb 168-173 rsd']=''
if 'Yb 170-173 rsd' not in st.session_state:
     st.session_state['Yb 170-173 rsd']=''
if 'Yb 171-173 rsd' not in st.session_state:
     st.session_state['Yb 171-173 rsd']=''
if 'Yb 172-173 rsd' not in st.session_state:
     st.session_state['Yb 172-173 rsd']=''
if 'Yb 174-173 rsd' not in st.session_state:
     st.session_state['Yb 174-173 rsd']=''
if 'Yb 176-173 rsd' not in st.session_state:
     st.session_state['Yb 176-173 rsd']=''

if 'Lu 176-175 ratio' not in st.session_state:
     st.session_state['Lu 176-175 ratio']=''
if 'Lu 176-175 rsd' not in st.session_state:
     st.session_state['Lu 176-175 rsd']=''


if 'Yb 168-173 final_ratio' not in st.session_state:
     st.session_state['Yb 168-173 final_ratio']=''
if 'Yb 170-173 final_ratio' not in st.session_state:
     st.session_state['Yb 170-173 final_ratio']=''
if 'Yb 171-173 final_ratio' not in st.session_state:
     st.session_state['Yb 171-173 final_ratio']=''
if 'Yb 172-173 final_ratio' not in st.session_state:
     st.session_state['Yb 172-173 final_ratio']=''
if 'Yb 174-173 final_ratio' not in st.session_state:
     st.session_state['Yb 174-173 final_ratio']=''
if 'Yb 176-173 final_ratio' not in st.session_state:
     st.session_state['Yb 176-173 final_ratio']=''

if 'Yb 168-173 final_rsd' not in st.session_state:
     st.session_state['Yb 168-173 final_rsd']=''
if 'Yb 170-173 final_rsd' not in st.session_state:
     st.session_state['Yb 170-173 final_rsd']=''
if 'Yb 171-173 final_rsd' not in st.session_state:
     st.session_state['Yb 171-173 final_rsd']=''
if 'Yb 172-173 final_rsd' not in st.session_state:
     st.session_state['Yb 172-173 final_rsd']=''
if 'Yb 174-173 final_rsd' not in st.session_state:
     st.session_state['Yb 174-173 final_rsd']=''
if 'Yb 176-173 final_rsd' not in st.session_state:
     st.session_state['Yb 176-173 final_rsd']=''

if st.sidebar.button('Home'):

     st.session_state['visible'] = False
     st.session_state['tims_visible'] = False
     st.session_state['delete_visible']= False
     st.session_state['home_visible'] = not st.session_state['home_visible']
     st.write("this is a dashboard")
     st.write(f"Number of rows in TIMS.csv: {len(tims_data)}")

if st.sidebar.button('Create New Experiment'):
     st.session_state['visible'] = not st.session_state['visible']
     st.session_state['tims_visible'] = False
     st.session_state['delete_visible']= False

if st.sidebar.button('Delete Experiment'):
     st.session_state['visible'] = False
     st.session_state['delete_visible'] = not st.session_state['delete_visible']
     st.session_state['tims_visible'] = False

if st.sidebar.button("Enter New TIMS Data"):
     st.session_state['visible'] = False
     st.session_state['tims_visible'] = not st.session_state['tims_visible']
     st.session_state['delete_visible']= False


#-----------------------------------------------------createExperiment--------------------------------------------------------
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
         updated_data.to_csv("./Laser Power1.csv", index = False)
         st.write("Successfully Created Experiment")

#-----------------------------------------------------delete Experiment---------------------------------------------------------
if st.session_state['delete_visible']:
     column = data['Experiment']
     st.session_state['delete_exp'] = st.sidebar.selectbox("Select Experiment to Delete",column)

     if st.sidebar.button('Delete'):
         condition = data['Experiment']== st.session_state['delete_exp']
         new_data = data[~condition]
         new_data.to_csv('Laser Power1.csv',index=False)

#-----------------------------------------------------TIMS Data------------------------------------------------------------------
if st.session_state['tims_visible']:
     st.header("Enter TIMS Data")
     st.write("")
     st.session_state['tims_exp'] = st.text_input("Experiment")
     st.session_state['tims_sample'] = st.text_input("Sample")
     st.session_state['tims_analysis']=st.text_input("Analysis Done By")
     st.session_state['tims_material'] = st.selectbox("Select Material",["", "Lu", "Yb"], index=0)
     st.session_state['sampl_id'] = (st.session_state['tims_exp'] + st.session_state['tims_material'] + st.session_state['tims_sample'])

     if st.session_state['tims_material'] == "Yb": 
         
         #precision1 = round(st.session_state['Yb 168-173 ratio']* (round(st.session_state['Yb 168-173 rsd'], 2) * 0.03), 3)
         tims = pd.DataFrame(
            [
                {"Ratio":st.session_state['Yb 168-173 ratio'] ,"RSD":st.session_state['Yb 168-173 rsd'],"Precision": "precision1"},
                {"Ratio":st.session_state['Yb 170-173 ratio'] ,"RSD":st.session_state['Yb 170-173 rsd'],"Precision":"This is calculated Precision"},
                {"Ratio":st.session_state['Yb 171-173 ratio'] ,"RSD":st.session_state['Yb 171-173 rsd'],"Precision":"This is calculated Precision"},
                {"Ratio":st.session_state['Yb 172-173 ratio'] ,"RSD":st.session_state['Yb 172-173 rsd'],"Precision":"This is calculated Precision"},
                {"Ratio":st.session_state['Yb 174-173 ratio'] ,"RSD":st.session_state['Yb 174-173 rsd'],"Precision":"This is calculated Precision"},
                {"Ratio":st.session_state['Yb 176-173 ratio'] ,"RSD":st.session_state['Yb 176-173 rsd'],"Precision":"This is calculated Precision"},
                     
            ]
        )

        
        
         st.data_editor(tims, 
                        column_config = 
                        {
                            "Precision": st.column_config.NumberColumn(
                                disabled = True
                            )
                        }
                       
                       )
        
         
         col1, col2, col3, col4 = st.columns(4,gap="medium")

         with col1:
             st.subheader("Ratio")

             st.session_state['Yb 168-173 ratio'] = st.text_input('Yb 168/173 ratio')
             st.session_state['Yb 170-173 ratio'] = st.text_input('Yb 170/173 ratio')
             st.session_state['Yb 171-173 ratio'] = st.text_input('Yb 171/173 ratio')
             st.session_state['Yb 172-173 ratio'] = st.text_input('Yb 172/173 ratio')
             st.session_state['Yb 174-173 ratio'] = st.text_input('Yb 174/173 ratio')
             st.session_state['Yb 176-173 ratio'] = st.text_input('Yb 176/175 ratio')

         with col2:
             st.subheader("RSD")

             try:
                 Yb_ratio1 = float(st.session_state['Yb 168-173 ratio'])
                 Yb_ratio2 = float(st.session_state['Yb 170-173 ratio'])
                 Yb_ratio3 = float(st.session_state['Yb 171-173 ratio'])
                 Yb_ratio4 = float(st.session_state['Yb 172-173 ratio'])
                 Yb_ratio5 = float(st.session_state['Yb 174-173 ratio'])
                 Yb_ratio6 = float(st.session_state['Yb 176-173 ratio'])

                 Yb_rsd1 = float(st.session_state['Yb 168-173 rsd'])
                 Yb_rsd2 = float(st.session_state['Yb 170-173 rsd'])
                 Yb_rsd3 = float(st.session_state['Yb 171-173 rsd'])
                 Yb_rsd4 = float(st.session_state['Yb 172-173 rsd'])
                 Yb_rsd5 = float(st.session_state['Yb 174-173 rsd'])
                 Yb_rsd6 = float(st.session_state['Yb 176-173 rsd'])


             except ValueError:
                 st.error("Please enter valid numeric values ratio and RSD.")
                 st.stop()

             st.session_state['Yb 168-173 rsd'] = st.text_input('Yb 168/173 rsd ')
             st.write(round(Yb_ratio1 * (round(Yb_rsd1, 2) * 0.03), 3))

             st.session_state['Yb 170-173 rsd'] = st.text_input('Yb 170/173 rsd')
             st.write(round(Yb_ratio2 * (round(Yb_rsd2, 2) * 0.03), 3))

             st.session_state['Yb 171-173 rsd'] = st.text_input('Yb 171/173 rsd')
             st.write(round(Yb_ratio3 * (round(Yb_rsd3, 2) * 0.03), 3))

             st.session_state['Yb 172-173 rsd'] = st.text_input('Yb 172/173 rsd')
             st.write(round(Yb_ratio4 * (round(Yb_rsd4, 2) * 0.03), 3))

             st.session_state['Yb 174-173 rsd'] = st.text_input('Yb 174/173 rsd')
             st.write(round(Yb_ratio5 * (round(Yb_rsd5, 2) * 0.03), 3))

             st.session_state['Yb 176-173 rsd'] = st.text_input('Yb176/175 rsd')
             st.write(round(Yb_ratio6 * (round(Yb_rsd6, 2) * 0.03), 3))

         with col3:
             st.subheader("Final Ratio")

             st.session_state['Yb 168-173 final_ratio']=st.text_input('Yb 168/173 final ratio')
             st.session_state['Yb 170-173 final_ratio']=st.text_input('Yb 170/173 final ratio')
             st.session_state['Yb 171-173 final_ratio']=st.text_input('Yb 171/173 final ratio')
             st.session_state['Yb 172-173 final_ratio']=st.text_input('Yb 172/173 final ratio')
             st.session_state['Yb 174-173 final_ratio']=st.text_input('Yb174-173 final ratio')
             st.session_state['Yb 176-173 final_ratio']=st.text_input('Yb 176-173 final ratio')

         with col4:
             st.subheader("Final Rsd")

             st.session_state['Yb 168-173 final_rsd']=st.text_input('Yb168/173 final rsd')
             st.session_state['Yb 170-173 final_rsd']=st.text_input('Yb170/173 final rsd')
             st.session_state['Yb 171-173 final_rsd']=st.text_input('Yb171/173 final rsd')
             st.session_state['Yb 172-173 final_rsd']=st.text_input('Yb172/173 final rsd')
             st.session_state['Yb 174-173 final_rsd']=st.text_input('Yb174-173 final rsd')
             st.session_state['Yb 176-173 final_rsd']=st.text_input('Yb176-173 final rsd')


     if st.session_state['tims_material'] == "Lu":
         col1, col2,col3 = st.columns(3)

         with col1:
             st.subheader("Ratio")
             st.session_state['Lu 176-175 ratio'] = st.number_input('Lu 176/175 Ratio')

         with col2:
             st.subheader("RSD")
             st.session_state['Lu 176-175 rsd'] = st.number_input('Lu 176/175 Rsd')

         with col3:
             st.subheader("Precision")
             st.header("")
             result = round(st.session_state['Lu 176-175 ratio'] * (round(st.session_state['Lu 176-175 rsd'], 2) * 0.03), 3)
             st.write(result)

     if st.button("Submit TIMS Data"):
                                                                 #
#---------_--------Prepare 6 rows of data
         rows = []
         if st.session_state['tims_material']=='Yb':
             ratios_of_interest = [168, 170, 171, 172, 174, 176]
         elif st.session_state['tims_material']=='Lu':
             ratios_of_interest = [176]
         for i in ratios_of_interest:
             row = {
                 'Exp': st.session_state['tims_exp'],
                 'Material': st.session_state['tims_material'],
                 'Sample': st.session_state['tims_sample'],
                 'Analysis Done By':st.session_state['tims_analysis'],
                 'Sample ID': st.session_state['sampl_id'],
                 'Ratio': st.session_state[f'Yb {i}-173 ratio' if st.session_state['tims_material'] == "Yb" else 'Lu 176-175 ratio'],
                 'RSD ppm': st.session_state[f'Yb {i}-173 rsd'if st.session_state['tims_material'] == "Yb" else 'Lu 176-175 rsd']
             }
             rows.append(row)

         # Append all rows to the existing TIMS data and save to CSV
         new_data = pd.concat([tims_data, pd.DataFrame(rows)], ignore_index=True)
         new_data.to_csv("./TIMS.csv", index=False)
