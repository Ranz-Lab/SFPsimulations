import pandas as pd
import random

# Load Table 1 from a CSV file
table_1 = pd.read_csv('Table1_1.csv')

# Define the structure for Table 2
subnetworks = ['n1', 'n2', 'n3', 'n4', 'n5', 'n6']
ages = ['A', 'B', 'C', 'D', 'E']
table_2_template = pd.DataFrame([(subnet, age) for subnet in subnetworks for age in ages], columns=['SubNetwork', 'age'])
table_2_template['yes'] = 0
table_2_template['no'] = 0
table_2_template['both'] = 0

# Generate the observed values for Table 2 based on the original Table 1
for (network, age), group in table_1.groupby(['network', 'age']):
    yes_count = group['rep?'].value_counts().get('yes', 0)
    no_count = group['rep?'].value_counts().get('no', 0)
    both_count = yes_count + no_count
    idx = (table_2_template['SubNetwork'] == network) & (table_2_template['age'] == age)
    table_2_template.loc[idx, 'yes'] = yes_count
    table_2_template.loc[idx, 'no'] = no_count
    table_2_template.loc[idx, 'both'] = both_count

# Extract observed values for the IF conditions
observed_values = table_2_template['both'].tolist()
print("Observed values: ", observed_values)

# Define the resampling function
def resample_and_generate_table_2(original_table_1, template, observed_values, n_samples=100000):
    results = []
    
    for sample_num in range(n_samples):
        # Create a copy of the original table for each resampling
        table_1 = original_table_1.copy()
        
        # Resample the age column
        age_values = table_1['age'].tolist()
        resampled_age = random.choices(age_values, k=len(age_values))
        table_1['age'] = resampled_age
        
        # Generate Table 2 based on the resampled Table 1
        table_2 = template.copy()
        table_2[['yes', 'no', 'both']] = 0  # Reset the counts for each iteration
        for (network, age), group in table_1.groupby(['network', 'age']):
            yes_count = group['rep?'].value_counts().get('yes', 0)
            no_count = group['rep?'].value_counts().get('no', 0)
            both_count = yes_count + no_count
            idx = (table_2['SubNetwork'] == network) & (table_2['age'] == age)
            table_2.loc[idx, 'yes'] += yes_count
            table_2.loc[idx, 'no'] += no_count
            table_2.loc[idx, 'both'] += both_count
        
        # Append the current Table 2 to the file
        with open('Table2_1.txt', 'a') as f_table2:
            f_table2.write(f"Table 2 for sample {sample_num + 1}:\n")
            table_2.to_csv(f_table2, index=False)
            f_table2.write("\n")
        
        # Evaluate the IF conditions based on the 'both' column
        resampled_values = table_2['both'].tolist()
        if_conditions = [1 if resampled_values[i] >= observed_values[i] else 0 for i in range(len(observed_values))]
        
        # Debug: Print resampled and observed values
        if(sample_num + 1 % 1000 == 0):
            print(f"Sample {sample_num + 1}")
        #print("Resampled values:", resampled_values)
        #print("Observed values:", observed_values)
        #print("IF conditions:", if_conditions)
        #print("\n")
        
        results.append(if_conditions)
    
    return results

# Perform the resampling and get the results
results = resample_and_generate_table_2(table_1, table_2_template, observed_values)

# Save the results to a text file
output_file_path = 'resampling_results.txt'
with open(output_file_path, 'w') as f:
    for res in results:
        f.write(','.join(map(str, res)) + '\n')

print(f"Resampling completed. Results saved to {output_file_path} and Table2.txt.")
