import os
import pandas as pd
import numpy as np
import plotly.express as px

# Step 1: Load metadata
metadata_path = "C:\\Users\\Admin1\\Downloads\\GitHub\\NASA-Battery-Analysis\\cleaned_dataset\\metadata.csv"
metadata = pd.read_csv(metadata_path)

# Step 2: Initialize variables
folder_path = "C:\\Users\\Admin1\\Downloads\\GitHub\\NASA-Battery-Analysis\\cleaned_dataset\\data"
data_frames = []

# Step 3: Load and process all CSV files
for _, row in metadata.iterrows():
    file_name = row['filename']
    file_path = os.path.join(folder_path, file_name)

    if os.path.exists(file_path):
        # Load individual data file
        data = pd.read_csv(file_path)

        # Handle missing values in the data file (numeric columns only)
        numeric_cols = data.select_dtypes(include=[np.number]).columns
        data[numeric_cols] = data[numeric_cols].fillna(data[numeric_cols].mean())

        # Extract relevant parameters
        if 'Battery_impedance' in data.columns:
            battery_impedance = np.abs(data['Battery_impedance'].apply(lambda x: complex(x.strip('()')) if isinstance(x, str) else x))
        else:
            battery_impedance = None

        if 'Re' in row and pd.notna(row['Re']):
            re = row['Re']
        else:
            re = np.mean(np.abs(battery_impedance.real)) if battery_impedance is not None else None

        if 'Rct' in row and pd.notna(row['Rct']):
            rct = row['Rct']
        else:
            rct = np.mean(np.abs(battery_impedance.imag)) if battery_impedance is not None else None

        # Add processed data to a new dataframe
        processed_data = {
            "Cycle": row['test_id'],
            "Battery_ID": row['battery_id'],
            "Battery_Impedance": battery_impedance.mean() if battery_impedance is not None else None,
            "Re": re,
            "Rct": rct,
            "Capacity": row['Capacity']
        }
        data_frames.append(processed_data)

# Step 4: Create a consolidated DataFrame
processed_df = pd.DataFrame(data_frames)

# Handle missing values in metadata (numeric columns only)
numeric_cols = processed_df.select_dtypes(include=[np.number]).columns
processed_df[numeric_cols] = processed_df[numeric_cols].fillna(processed_df[numeric_cols].mean())

# Step 5: Plot trends using Plotly
# Plot Battery Impedance
fig1 = px.line(
    processed_df, x="Cycle", y="Battery_Impedance", color="Battery_ID",
    title="Battery Impedance vs Aging (Charge/Discharge Cycles)",
    labels={"Cycle": "Cycle Number", "Battery_Impedance": "Battery Impedance (Ohms)"}
)
fig1.show()

# Plot Re (Electrolyte Resistance)
fig2 = px.line(
    processed_df, x="Cycle", y="Re", color="Battery_ID",
    title="Electrolyte Resistance (Re) vs Aging (Charge/Discharge Cycles)",
    labels={"Cycle": "Cycle Number", "Re": "Re (Ohms)"}
)
fig2.show()

# Plot Rct (Charge Transfer Resistance)
fig3 = px.line(
    processed_df, x="Cycle", y="Rct", color="Battery_ID",
    title="Charge Transfer Resistance (Rct) vs Aging (Charge/Discharge Cycles)",
    labels={"Cycle": "Cycle Number", "Rct": "Rct (Ohms)"}
)
fig3.show()
