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
# Skip the first row and treat it as data, not header
food_waste_df = pd.read_csv(food_waste_file, encoding='ANSI', usecols=[0, 1], header=None, skiprows=[0])

# Read only the first and 42nd column of the GDP per Capita CSV file into a dataframe
# Skip the first two rows and treat them as data, not header
gdp_per_capita_df = pd.read_csv(gdp_per_capita_file, encoding='ANSI', usecols=[0, 41], header=None, skiprows=[0, 1])

# Reset the index after reading the CSV files
food_waste_df.reset_index(drop=True, inplace=True)
gdp_per_capita_df.reset_index(drop=True, inplace=True)

# Rename the columns
food_waste_df.columns = ["country", "kg_per_capita"]
gdp_per_capita_df.columns = ["country", "gdp_per_capita"]

# Merge the dataframes on the "country" column
wealth_to_waste = pd.merge(food_waste_df, gdp_per_capita_df, on="country")

# Display the first few rows of the merged dataframe (optional)
print("Wealth to Waste Dataframe:")
print(wealth_to_waste.head())
