import pandas as pd
import matplotlib.pyplot as plt

# Specify the file path
file_path = r'../Input/employees.csv'

# Read the CSV file into a DataFrame
employees_df = pd.read_csv(file_path)

# Sort the DataFrame by SALARY
employees_df = employees_df.sort_values(by='SALARY', ascending=False)

# Find the indices for splitting the data into 60%, 30%, and 10% segments
total_count = len(employees_df)
top_10_index = total_count // 10
middle_30_index = top_10_index + (total_count * 3 // 10)

# Assign colors based on the 60-30-10 rule
colors = ['gold'] * top_10_index + ['silver'] * (middle_30_index - top_10_index) + ['gray'] * (total_count - middle_30_index)

# Create a bar plot of the salaries against the employee IDs
plt.figure(figsize=(10, 6))
bars = plt.bar(employees_df['FIRST_NAME'].astype(str), employees_df['SALARY'], color=colors)
plt.xlabel('FIRST_NAME')
plt.ylabel('Salary')
plt.title('Salary of Employees')
plt.xticks(rotation=90)
plt.tight_layout()

# Add a legend
plt.legend([bars[0], bars[top_10_index], bars[middle_30_index]], ['Top 10%', 'Middle 30%', 'Bottom 60%'])

plt.show()
