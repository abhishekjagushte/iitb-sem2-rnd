import os
import pandas as pd

# Folder containing .out files
folder_path = "./bypassing_l2/complete_bypass/victima"

# Initialize list to store final dataframe data
final_data = []

# Process each .out file in the folder
for file in os.listdir(folder_path):
    if file.endswith(".out"):
        trace_name = file.replace(".out", "")
        file_path = os.path.join(folder_path, file)
        
        # Read the .out file and extract relevant data
        data = []
        with open(file_path, "r") as f:
            for line in f:
                if "Occupancy in L2:" in line:
                    parts = line.strip().split(": ")[1].split(", ")
                    data.append([int(parts[0]), int(parts[1]), int(parts[2])])
        
        # Create a dataframe for the trace
        df = pd.DataFrame(data, columns=["num_data_blocks", "num_pte_blocks", "num_tlb_blocks"])
        
        # Compute average occupancy values for the bottom half
        bottom_half = df.iloc[len(df)//2:]
        total_blocks = bottom_half.sum(axis=1)
        avg_data_occupancy = ((bottom_half["num_data_blocks"] / total_blocks) * 100).mean()
        avg_pte_occupancy = ((bottom_half["num_pte_blocks"] / total_blocks) * 100).mean()
        avg_tlb_occupancy = ((bottom_half["num_tlb_blocks"] / total_blocks) * 100).mean()
        
        # Store the results for the final dataframe
        final_data.append([trace_name, avg_data_occupancy, avg_pte_occupancy, avg_tlb_occupancy])

# Create final dataframe
final_df = pd.DataFrame(final_data, columns=["trace", "avg_data_occupancy", "avg_pte_occupancy", "avg_tlb_occupancy"])

# Sort by trace name
final_df = final_df.sort_values(by="trace")

# Save to CSV
final_df.to_csv("occupancy_summary.csv", index=False)

print("CSV file 'occupancy_summary.csv' has been created.")
