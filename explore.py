# Self Assessment 1: A boolean filter determines which rows will be selected based of specific conditions. 
# Self Assessment 2: df["revenue"] = a coulumn while df[["revenue"]] = a table. This matters because if you need it to be a table so you can take rows and add a header you need to use double brackets.
# Self Assessment 3: I would say pandas are better than excel because they are so much more efficent both in speed and in the amount of data you can handle.

print("---Exercise 1---")

import pandas as pd
import os
df = pd.read_csv('data/retail_sales.csv')

print(df.head())
print(df.shape)
print(df.columns.tolist())
print(df.dtypes)

print("---Exercise 2---")

south = df[df['region'] == 'South']

print(len(south))
print(south.head())

print("---Exercise 3---")

top5 = df.sort_values('revenue', ascending=False).head(5)

print(top5)

print("---Exercise 4---")

big_south = df[(df['region'] == 'South') & (df['revenue'] > 1000)]

print(len(big_south))
print(big_south.head())

print("---Exercise 5---")

df['per_unit'] = df['revenue'] / df['quantity']

print(df.head())
print(df['per_unit'].mean())

print("---Exercise 6---")

print(df['region'].unique())
print(df['region'].value_counts())

print("---Exercise 7---")

subset = df[['region', 'product', 'revenue']]

print(subset.shape)

print("---Exercise 8---")

df.to_csv('data/explored.csv', index=False)
print(os.path.exists('data/explored.csv'))