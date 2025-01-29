import streamlit as st
import pandas as pd
from fpdf import FPDF
from datetime import date

# Load your data
tims_data = pd.read_csv("./TIMS.csv")
ion_data = pd.read_csv("./ion_report.csv")

# Initialize session state variables
if 'report_visible' not in st.session_state:
    st.session_state['report_visible'] = False

if 'report_data' not in st.session_state:
    st.session_state['report_data'] = ''

if 'try' not in st.session_state:
    st.session_state['try'] = False

if "ion_df" not in st.session_state:
    st.session_state.ion_df = pd.DataFrame(columns=[
        "Sample ID", "Ratio", "RSD ppm", "Identifier", "FINAL", "Quantity", "xf", "Concentration", "Qty of Ions", "Qty of Neutrals"
    ])

# Number of samples
sample_no = st.number_input("Enter no. of samples", step=1)

label_col1, label_col2, label_col3, label_col4, label_col5 = st.columns(5)

with label_col1:
    st.write("Material")
with label_col2:
    st.write("Experiment")
with label_col3:
    st.write("Sample")
with label_col4:
    st.write("Identifier")
with label_col5:
    st.write("Quantity")

col1, col2, col3, col4, col5 = st.columns(5)

label_df = pd.DataFrame()
df = pd.DataFrame()

for i in range(sample_no):
    with col1:
        mat = st.selectbox("", ["", "Yb", "Lu"], key=f"mat{i}", placeholder="Material")

    with col2:
        new_data = tims_data[tims_data['Material'] == mat]
        options_exp = [""] + new_data['Exp'].unique().tolist()
        selected_exp = st.selectbox("", options_exp, key=f"exp{i}")

    with col3:
        sample_data = new_data[new_data['Exp'] == selected_exp]['Sample']
        selected_sample = st.selectbox("", sample_data.unique(), key=f"samp{i}")

    with col4:
        try:
            samp_id = f"{st.session_state[f'exp{i}']} {st.session_state[f'mat{i}']} {st.session_state[f'samp{i}']}"
        except TypeError:
            samp_id = ""

        selected_identifier = st.selectbox("", tims_data[tims_data['Sample ID'] == samp_id]['Identifier'].unique(), key=f"identity{i}")

    with col5:
        quantity = st.number_input("", key=f"quantity{i}")

    # Retrieve data directly using .iloc[0]
    matching_row = tims_data.loc[(tims_data['Sample ID'] == samp_id) & (tims_data['Identifier'] == selected_identifier)]

    # Append data to label_df
    for index, row in matching_row.iterrows():
        label_df = pd.concat([label_df, pd.DataFrame({
            "Sample ID": [row['Sample ID']],
            "Ratio": [row['Ratio']],
            "RSD ppm": [row['RSD ppm']],
            "Identifier": [row['Identifier']],
            "FINAL": [row['FINAL']],
            "Quantity": [quantity],
            "xf": [0.0],  # Default value, can be edited later
            "Concentration": [(row["Ratio"] * 100) / (1 + row["Ratio"])],
            "Qty of Ions": [0.0],  # Calculated later
            "Qty of Neutrals": [0.0]  # Calculated later
        })], ignore_index=True)

# Function to update session state DataFrame
def update():
    for idx, change in st.session_state.changes["edited_rows"].items():
        for label, value in change.items():
            st.session_state.ion_df.at[idx, label] = value

    # Recalculate dependent columns
    st.session_state.ion_df["Concentration"] = (st.session_state.ion_df["Ratio"] * 100) / (1 + st.session_state.ion_df["Ratio"])
    st.session_state.ion_df["Qty of Ions"] = st.session_state.ion_df["Quantity"].astype(float) * (
        (st.session_state.ion_df["Concentration"].astype(float) - st.session_state.ion_df["xf"].astype(float)) /
        (1 - st.session_state.ion_df["xf"].astype(float))
    )
    st.session_state.ion_df["Qty of Neutrals"] = st.session_state.ion_df["Quantity"].astype(float) - st.session_state.ion_df["Qty of Ions"].astype(float)

# Display the editable table
edited_ion_data = st.data_editor(pd.DataFrame(label_df), key="changes", on_change=update, column_config={
    "Sample ID": st.column_config.TextColumn(disabled=True),
    "Ratio": st.column_config.TextColumn(disabled=True),
    "RSD ppm": st.column_config.TextColumn(disabled=True),
    "Identifier": st.column_config.TextColumn(disabled=True),
    "FINAL": st.column_config.TextColumn(disabled=True),
    "Quantity": st.column_config.NumberColumn(disabled=False),
    "xf": st.column_config.NumberColumn(disabled=False),
    "Concentration": st.column_config.NumberColumn(disabled=True),
    "Qty of Ions": st.column_config.NumberColumn(disabled=True),
    "Qty of Neutrals": st.column_config.NumberColumn(disabled=True),
})

# Populate the session state DataFrame with edited data
if not st.session_state.ion_df.empty:
    for i, row in edited_ion_data.iterrows():
        st.session_state.ion_df.at[i, "Quantity"] = row["Quantity"]
        st.session_state.ion_df.at[i, "xf"] = row["xf"]

# Ensure calculations are correct
st.session_state.ion_df["Concentration"] = (st.session_state.ion_df["Ratio"] * 100) / (1 + st.session_state.ion_df["Ratio"])
st.session_state.ion_df["Qty of Ions"] = st.session_state.ion_df["Quantity"].astype(float) * (
    (st.session_state.ion_df["Concentration"].astype(float) - st.session_state.ion_df["xf"].astype(float)) /
    (1 - st.session_state.ion_df["xf"].astype(float))
)
st.session_state.ion_df["Qty of Neutrals"] = st.session_state.ion_df["Quantity"].astype(float) - st.session_state.ion_df["Qty of Ions"].astype(float)

# Display the updated session state DataFrame
st.data_editor(st.session_state.ion_df)
