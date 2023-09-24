import requests
import pandas as pd
from pandas import json_normalize

# Set display options to ensure all columns are printed
pd.set_option('display.max_columns', None)
pd.set_option('display.expand_frame_repr', False)
file_path_india = r'../Output/India.csv'
# Define the URL of the API
url = "https://randomuser.me/api?results=5000"

# Send a GET request to the API
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    # Load the JSON data from the response
    data = response.json()

    # Normalize the 'results' field in the JSON to create a DataFrame
    full_df = json_normalize(data['results'])

    # Filter the DataFrame to keep only rows where 'location.country' is 'India'
    indian_people_df = full_df[full_df['location.country'] == 'India']

    # Print the DataFrame containing only people from India
    # print(indian_people_df)
    indian_people_df.to_csv(file_path_india, index=False)
else:
    print(f"Failed to retrieve data: {response.status_code}")
