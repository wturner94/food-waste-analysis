import pandas as pd
import os
import matplotlib.pyplot as plt
import seaborn as sns



# get the current working directory
script_dir = os.getcwd()

# define the relative paths to the CSV files within the "data" folder
food_waste_relative_path = os.path.join("data", "food_waste_by_country.csv")
wealth_relative_path = os.path.join("data", "gdp_per_capita_current_prices.csv")
pop_density_relative_path = os.path.join("data", "pop_density_by_country.csv")
food_insecurity_relative_path = os.path.join("data", "food_insecurity_by_country.csv")

# construct the absolute paths
food_waste_file = os.path.join(script_dir, food_waste_relative_path)
wealth_file = os.path.join(script_dir, wealth_relative_path)
pop_density_file = os.path.join(script_dir, pop_density_relative_path)
food_insecurity_file = os.path.join(script_dir, food_insecurity_relative_path)



# read the FOOD WASTE .csv file into a dataframe
food_waste_df = pd.read_csv(food_waste_file)

# read the GDP PER CAPITA .csv file into a dataframe
wealth_df = pd.read_csv(wealth_file)

# read the POPULATION DENSITY .csv file into a dataframe
pop_density_df = pd.read_csv(pop_density_file)

# read the FOOD INSECURITY .csv file into a dataframe
food_insecurity_df = pd.read_csv(food_insecurity_file)



# define list of column names to drop from FOOD WASTE dataframe
food_waste_cols_to_drop = ['Household estimate (kg/capita/year)',
       'Household estimate (tonnes/year)', 'Retail estimate (kg/capita/year)',
       'Retail estimate (tonnes/year)',
       'Food service estimate (kg/capita/year)',
       'Food service estimate (tonnes/year)', 'Confidence in estimate',
       'M49 code', 'Source']

# drop the columns from the FOOD WASTE dataframe
food_waste_df = food_waste_df.drop(columns=food_waste_cols_to_drop)

# rename the remaining columns
food_waste_df.columns = ["country", "food_wasted", "region"]

# print first few rows to verify columns were dropped & renamed
print(food_waste_df.head())


# drop the first row, which contains no data
wealth_df = wealth_df.drop(0, axis=0)

# define list of column names to drop from WEALTH dataframe
wealth_cols_to_drop = ['1980',
       '1981', '1982', '1983', '1984', '1985', '1986', '1987', '1988', '1989',
       '1990', '1991', '1992', '1993', '1994', '1995', '1996', '1997', '1998',
       '1999', '2000', '2001', '2002', '2003', '2004', '2005', '2006', '2007',
       '2008', '2009', '2010', '2011', '2012', '2013', '2014', '2015', '2016',
       '2017', '2018', '2019', '2021', '2022', '2023', '2024', '2025',
       '2026', '2027', '2028']

# drop the columns from the WEALTH dataframe
wealth_df = wealth_df.drop(columns=wealth_cols_to_drop)

# rename the remaining columns
wealth_df.columns = ["country", "wealth"]

# print first few rows to verify columns were dropped & renamed
print(wealth_df.head())


# define list of column names to drop from POPULATION DENSITY dataframe
pop_density_cols_to_drop = ['Series Name', 'Series Code', 'Country Code',
       '1990 [YR1990]', '2000 [YR2000]', '2013 [YR2013]', '2014 [YR2014]',
       '2015 [YR2015]', '2016 [YR2016]', '2017 [YR2017]', '2018 [YR2018]',
       '2019 [YR2019]', '2021 [YR2021]', '2022 [YR2022]']

# drop the columns from the POPULATION DENSITY dataframe
pop_density_df = pop_density_df.drop(columns=pop_density_cols_to_drop)

# rename the remaining columns
pop_density_df.columns = ["country", "pop_density"]

# print first few rows to verify columns were dropped & renamed
print(pop_density_df.head())


# define list of column names to drop from FOOD INSECURITY dataframe
food_insecurity_cols_to_drop = ['Series Name', 'Series Code', 'Country Code',
       '1990 [YR1990]', '2000 [YR2000]', '2013 [YR2013]', '2014 [YR2014]',
       '2015 [YR2015]', '2016 [YR2016]', '2017 [YR2017]', '2018 [YR2018]',
       '2019 [YR2019]', '2021 [YR2021]', '2022 [YR2022]']

# drop the columns from the FOOD INSECURITY dataframe
food_insecurity_df = food_insecurity_df.drop(columns=food_insecurity_cols_to_drop)

# rename the remaining columns
food_insecurity_df.columns = ["country", "food_insecurity"]

# print first few rows to verify columns were dropped & renamed
print(food_insecurity_df.head())


# merge the dataframes on the COUNTRY column
waste_analysis = pd.merge(food_waste_df, wealth_df, on="country", how="left")
waste_analysis = pd.merge(waste_analysis, pop_density_df, on="country", how="left")
waste_analysis = pd.merge(waste_analysis, food_insecurity_df, on="country", how="left")

# convert to numeric, set non-numeric values to NaN
waste_analysis['wealth'] = pd.to_numeric(waste_analysis['wealth'], errors='coerce')
waste_analysis['food_wasted'] = pd.to_numeric(waste_analysis['food_wasted'], errors='coerce')
waste_analysis['pop_density'] = pd.to_numeric(waste_analysis['pop_density'], errors='coerce')
waste_analysis['food_insecurity'] = pd.to_numeric(waste_analysis['food_insecurity'], errors='coerce')

# reorder the columns in the overall WASTE ANALYSIS dataframe
waste_analysis = waste_analysis[['country', 'food_wasted', 'wealth', 'pop_density', 'food_insecurity', 'region']]

# print the first 5 rows of the overall WASTE ANALYSIS dataframe to verify successful merge & reordering of columns
print(waste_analysis.head())


# create a new column called "food_waste_rank" wherein countries are assigned a rank based on their position in the list when sorted in descending order by FOOD WASTE
waste_analysis['food_waste_rank'] = waste_analysis['food_wasted'].rank(ascending=False, method='min').astype(int)

# Display the DataFrame sorted by 'food_waste_rank', dropping the index for a cleaner display
print(waste_analysis[['country', 'food_wasted', 'food_waste_rank']].sort_values(by='food_waste_rank').reset_index(drop=True))

print(waste_analysis.head())


# Calculate regional averages for food waste
avg_region_data = waste_analysis.groupby('region').agg({'food_wasted': 'mean', 'wealth': 'mean', 'food_insecurity': 'mean',})
print(avg_region_data)


# calculate a ratio that compares the food waste generated by a country to its economic output
# add that value to a new column called "waste_to_wealth_ratio"
waste_analysis['waste_to_wealth_ratio'] = waste_analysis['food_wasted'] / waste_analysis['wealth']

# print the first 5 rows of the updated WASTE ANALYSIS dataframe
print(waste_analysis.head())


# Select relevant columns for correlation analysis
correlation_data = waste_analysis[['food_wasted', 'wealth', 'pop_density', 'food_insecurity']]

# Calculate correlation matrix, rounded to the nearest thousandth for tidier output
correlation_matrix = correlation_data.corr().round(3)

# Display the correlation matrix 
print(correlation_matrix)