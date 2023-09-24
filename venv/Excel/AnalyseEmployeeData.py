import pandas as pd

# Set display options to ensure all columns are printed
pd.set_option('display.max_columns', None)
pd.set_option('display.expand_frame_repr', False)

# Specify the file path
file_path_employees = r'../Input/employees.csv'
file_path_departments = r'../Input/departments.csv'

# Read the CSV files into DataFrames
employees_df = pd.read_csv(file_path_employees)
departments_df = pd.read_csv(file_path_departments)

# Sort the employees_df DataFrame first by MANAGER_ID and then by SALARY, both in descending order
sorted_df = employees_df.sort_values(by=['MANAGER_ID', 'SALARY'], ascending=[False, False])

# Merge sorted_df with departments_df
merged_sorted_df = pd.merge(sorted_df, departments_df, how='left', on=['DEPARTMENT_ID', 'MANAGER_ID'])

# Display the first few rows of the merged_sorted_df DataFrame
print("Merged Sorted DataFrame:")
print(merged_sorted_df.head())
print("\n")

# Calculate and display various salary statistics on the merged_sorted_df DataFrame
salary_stats = merged_sorted_df['SALARY'].describe().round(2)
salary_variance = merged_sorted_df['SALARY'].var().round(2)
salary_mode = merged_sorted_df['SALARY'].mode().round(2)

print("Salary Statistics:")
print(salary_stats)
print("Salary Variance:", salary_variance)
print("Salary Mode:", salary_mode.iloc[0])
