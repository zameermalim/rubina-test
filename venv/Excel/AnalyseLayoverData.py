import pandas as pd
import matplotlib.pyplot as plt

# Read the Excel file
file_path = '../Input/DomesticLayoverAllowance.xlsx'
domesticLayoverAllowance_df = pd.read_excel(file_path)

# Extract the numeric layover count from the "LAYOVERCOUNT" column
domesticLayoverAllowance_df['Numeric Layover'] = domesticLayoverAllowance_df['LAYOVERCOUNT'].apply(
    lambda x: int(x.split(' ')[0])
)

# Define a function to calculate the layover range
def calculate_layover_range(layover_count):
    lower_bound = (layover_count // 3) * 3
    if lower_bound == layover_count:
        lower_bound = lower_bound - 3
    upper_bound = lower_bound + 3
    return f'{lower_bound + 1}-{upper_bound} LAYOVERS'

# Create a new column "LAYOVER RANGE" based on the "Numeric Layover" column
domesticLayoverAllowance_df['LAYOVER RANGE'] = domesticLayoverAllowance_df['Numeric Layover'].apply(calculate_layover_range)

# Drop the temporary "Numeric Layover" column
domesticLayoverAllowance_df.drop(columns=['Numeric Layover'], inplace=True)

# Group by "CREWBASE" and get the count distribution of "LAYOVER RANGE"
layover_distribution = domesticLayoverAllowance_df.groupby('CREWBASE')['LAYOVER RANGE'].value_counts().unstack(fill_value=0)

# Plot the layover distribution
ax = layover_distribution.plot(kind='bar', stacked=True, figsize=(10, 10), colormap='viridis')
plt.title('Layover Range Distribution by Crew Base')
plt.xlabel('Crew Base')
plt.ylabel('Count')
plt.legend(title='Layover Range')

# Add a table with the data below the graph
cell_text = []
columns = layover_distribution.columns
for row in range(len(layover_distribution)):
    cell_text.append([f'{x:1d}' for x in layover_distribution.iloc[row]])

# bbox parameter adjusted to place the table lower
table = plt.table(cellText=cell_text, rowLabels=layover_distribution.index, colLabels=columns, cellLoc = 'center', loc='bottom', bbox=[0.0, -0.5, 1.0, 0.3])

# Adjust layout to make room for the table
plt.subplots_adjust(left=0.2, bottom=0.5)

# Show the plot
plt.show()
