import pandas as pd
import os

# Get the current script's directory
script_dir = os.path.dirname(os.path.abspath(__file__))

# Define the relative paths to the CSV files within the "data" folder
food_waste_relative_path = os.path.join("data", "food_waste_by_country.csv")
gdp_per_capita_relative_path = os.path.join("data", "gdp_per_capita_current_prices.csv")

# Construct the absolute paths
food_waste_file = os.path.join(script_dir, food_waste_relative_path)
gdp_per_capita_file = os.path.join(script_dir, gdp_per_capita_relative_path)

# Read only the first two columns of the food waste CSV file into a dataframe
# Skip the first row
food_waste_df = pd.read_csv(food_waste_file, encoding='ANSI', usecols=[0, 1], skiprows=[0])

# Read only the first and 42nd column of the GDP per Capita CSV file into a dataframe
# Skip the first two rows
gdp_per_capita_df = pd.read_csv(gdp_per_capita_file, encoding='ANSI', usecols=[0, 41], skiprows=[0, 1])

# Display the first few rows of each dataframe (optional)
print("Food Waste Dataframe:")
print(food_waste_df.head())

print("\nGDP per Capita Dataframe:")
print(gdp_per_capita_df.head())