# Extract Accession Number from UniProt REST API Using Protein Name and Save to CSV
# Use ThreadPoolExecutor to Process a Large Number of Protein Names
import requests
import pandas as pd
from concurrent.futures import ThreadPoolExecutor, as_completed

def get_uniprot_accession_id(protein_name):
    url = "https://rest.uniprot.org/uniprotkb/search"
    params = {"query": protein_name, "format": "json", "fields": "accession"}
    response = requests.get(url, params=params)

    if response.status_code == 200:
        data = response.json()
        try:
            accession = data['results'][0]['primaryAccession']
            return accession
        except (KeyError, IndexError):
            return 'Accession number not found'
    else:
        return f"Error: {response.status_code}, {response.text}"

def fetch_accessionsId_from_csv(input_csv, output_csv):
    # Read the input CSV file
    df = pd.read_csv(input_csv)

    # Check if the input CSV has a column named 'Protein Name'
    if 'Protein Name' not in df.columns:
        raise ValueError("Input CSV must contain a 'Protein Name' column")

    # Create a ThreadPoolExecutor to speed up the process
    with ThreadPoolExecutor(max_workers=10) as executor:
        # Submit all tasks to the executor
        future_to_protein = {executor.submit(get_uniprot_accession_id, protein): protein for protein in df['Protein Name']}

        # Create a list to hold the results
        results = []
        for future in as_completed(future_to_protein):
            protein = future_to_protein[future]
            try:
                accession = future.result()
                results.append((protein, accession))
            except Exception as exc:
                results.append((protein, str(exc)))

    # Create a new DataFrame from the results
    result_df = pd.DataFrame(results, columns=['Protein Name', 'Accession Number'])

    # Save the results to a new CSV file
    result_df.to_csv(output_csv, index=False)

if __name__ == "__main__":
    input_csv = "D:\drug repurposing\TTD_ASSIGNMENT\protein_name_.csv"  # Replace with the path to your input CSV file
    output_csv = 'D:\drug repurposing\TTD_ASSIGNMENT\Visual_studio_run.csv'
    fetch_accessionsId_from_csv(input_csv, output_csv)
