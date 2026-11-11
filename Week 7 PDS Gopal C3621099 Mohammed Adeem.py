# using list
import pandas as pd
product_data=[['e-book', 2000], ['plants', 6000], ['Pencil', 3000]] #
#2d list, similar to 2d array
indexes=[1,2,3]
columns_name=['product', 'unit_sold']
product_df = pd.DataFrame(data=product_data, index=indexes,
columns=columns_name)
# print(product_df)

# using dictionaries
product_data={'product': ['e-book', 'plants', 'Pencil'], 'unit_sold': [2000, 5000, 3000]}
product_df = pd.DataFrame(data=product_data)
# print(product_df)

# using numpy array
import numpy as np
products = np.array([['','product','unit_sold'], [1, 'E-book',2000],
                     [2, 'Plants', 6000], [3, 'Pencil',  3000]])

product_pf = pd.DataFrame(data=products[1:,1:],index=products[1:,0 ],
                          columns=products[0,1:])
# print(product_pf) # output is same as of first case

# Part 2 - Importing and cleaning CSV data
import pandas as pd
df = pd.read_csv('data/dirtydata.csv')
# print(df.head(10))

#Print information about the data:
# print(df.info())
# print(df.isna().sum())
# print(df.duplicated())

# Remove rows
import pandas as pd
df = pd.read_csv('data/dirtydata.csv')
new_df = df.dropna()
# print(new_df.to_string())

# Replace empty values
import pandas as pd
df = pd.read_csv('data/dirtydata.csv')
new_df = df.copy()
new_df["Calories"] = new_df["Calories"].fillna(130)

print(new_df)
# print('new_df')

# Replace only for specified columns
import pandas as pd
df = pd.read_csv("data/dirtydata.csv")
# print.df = ("Calories")
new_df = df['Calories'].fillna(130)

# numeric_cols = df.select_dtypes(include="number").columns
# new_df = df.copy()
# new_df[numeric_cols] = new_df[numeric_cols].fillna(130)


#print(new_df)
# Calculating the mean and replacing any empty values
import pandas as pd

df = pd.read_csv("data/dirtydata.csv")
print("Before cleaning:")
print(df["Calories"].isna().sum())
df["Calories"] = df["Calories"].fillna(130)
print("After cleaning:")
print(df["Calories"].isna().sum())
print(df)


