import pandas as pd

# Load the first CSV file
df1 = pd.read_csv('D:\drug repurposing\TTD_ASSIGNMENT\FINAL_TARGET_DRUG.csv')

# Load the second CSV file
df2 = pd.read_csv('D:\drug repurposing\TTD_ASSIGNMENT\protein_accessions.csv')

# Specify the column on which you want to merge the two DataFrames


# Merge the DataFrames on the specified column
merged_df = pd.merge(df1, df2, on='UNIPROID')

# Save the merged DataFrame to a new CSV file
merged_df.to_csv('D:\drug repurposing\merge___.csv', index=True)

print("Merging completed and saved to merged_file.csv")
