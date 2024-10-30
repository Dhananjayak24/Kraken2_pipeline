import pandas as pd

file_path = r"<path to the file in local>"

# Initializing total class reads and an empty list for abundance data
columns = ['abundance', 'rank', 'scientific_name']
abundance_data = pd.DataFrame(columns= columns)


# Open the report file and extract data
with open(file_path, 'r') as report:
    for each_line in report:
        line = each_line.strip().split('\t')
        #print(line)

        #for every iteration we store it in a df which will be appended to final df
        new_row = pd.DataFrame({
            #'percentage_covered' : [line[0]],
            'abundance' : [line[1]],
            #'fragments_directly_covered' : [line[2]],
            'rank' : [line[3]],
            #'taxonomic_ID' : [line[4]],
            'scientific_name' : [line[5]]
        })
        abundance_data = pd.concat([abundance_data, new_row], ignore_index= True)

#print(abundance_data)

#splitting data frame into different groups

domain_gp = abundance_data[abundance_data['rank'] == 'D'].reset_index(drop = True)
kingdom_gp = abundance_data[abundance_data['rank'] == 'K'].reset_index(drop = True)
phylum_gp = abundance_data[abundance_data['rank'] == 'P'].reset_index(drop = True)
class_gp = abundance_data[abundance_data['rank'] == 'C'].reset_index(drop = True)
order_gp = abundance_data[abundance_data['rank'] == 'O'].reset_index(drop = True)
family_gp = abundance_data[abundance_data['rank'] == 'F'].reset_index(drop = True)
genus_gp = abundance_data[abundance_data['rank'] == 'G'].reset_index(drop = True)
species_gp = abundance_data[abundance_data['rank'] == 'S'].reset_index(drop = True)

#print(species_gp)

def calculate_rel_abundance(group):
    # Convert the abundance column to a list of numeric values
    total_reads = group['abundance'].astype(int).sum()  
    # Summing the abundance values
    
    # Calculatin relative abundance for each row and add it as a new column
    group['relative_abundance'] = group['abundance'].astype(float) / total_reads * 100
    
    return group

#calling the method
calculate_rel_abundance(species_gp)

#print(species_gp)

#downloading the output into local disk using to_csv
species_gp.to_csv(r'<path to the output file>\species_abundance.csv', index= False)
