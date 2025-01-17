import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt

# Step 1: Read data from CSV file
data = pd.read_csv('D:/drug repurposing/drug_sam_kg.csv')

# Step 2: Define entities and relationships
drugs = list(data['Drugs'].unique())
diseases = list(data['Disease'].unique())
targets = list(data['Target'].unique())

drug_disease_relationships = [(row['Drugs'], row['Disease']) for index, row in data.iterrows()]
drug_target_relationships = [(row['Drugs'], row['Target']) for index, row in data.iterrows()]

# Step 3: Create a directed graph
G = nx.DiGraph()

# Step 4: Add nodes and edges
for drug in drugs:
    G.add_node(drug, type='Drugs')

for disease in diseases:
    G.add_node(disease, type='Disease')

for target in targets:
    G.add_node(target, type='Target')

for drug, disease in drug_disease_relationships:
    G.add_edge(drug, disease, type='Drug-Disease')

for drug, target in drug_target_relationships:
    G.add_edge(drug, target, type='Drug-Target')

# Step 5: Visualize the graph with different node colors
plt.figure(figsize=(10, 6))
pos = nx.spring_layout(G)

# Assigning colors to different node types
node_color = []
for node in G.nodes():
    if G.nodes[node]['type'] == 'Drugs':
        node_color.append('yellow')
    elif G.nodes[node]['type'] == 'Disease':
        node_color.append('pink')
    elif G.nodes[node]['type'] == 'Gene':
        node_color.append('orange')

nx.draw(G, pos, with_labels=True, node_size=2000, node_color=node_color, font_size=10, font_weight='bold')
plt.title("Knowledge Graph for Drug Repurposing")
plt.show()
