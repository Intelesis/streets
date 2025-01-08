import pandas as pd
import os

input_folder = "/mnt/c/Users/Noel Liverton/OneDrive/Desktop/Noel/Pub Maps/The Knowledge/DATA"
output_file = "greater_london_filtered_streets.csv"

# Initialize an empty DataFrame to store filtered data
filtered_data = pd.DataFrame()

for file in os.listdir(input_folder):
    if file.endswith(".csv"):
        file_path = os.path.join(input_folder, file)
        data = pd.read_csv(file_path, low_memory=False)
        
        # Filter rows for Greater London and Streets/Roads
        london_data = data[
                (data.iloc[:, 24] == 'Greater London') &
                (data.iloc[:, 7].str.contains('Street|Road', na=False))
        ]
        
        filtered_data = pd.concat([filtered_data, london_data])
        
pickle_file = "filtered_data.pkl"
filtered_data.to_pickle(pickle_file)

# Save the filtered data to a new CSV
filtered_data.to_csv(output_file, index=False)

