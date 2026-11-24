import pandas as pd
import numpy as np

# Creating the pandas series
practicePandas = pd.Series([10,20,30,20, np.nan])

# Displaying the original series
print(practicePandas)
print()

# Displays the mean
print("The mean is:", practicePandas.mean())

# Displays the sum
print("The Sum is:", practicePandas.sum())

# Displays the max value
print("The Max is:", practicePandas.max())

# Displays the Min value
print("The Min is:", practicePandas.min())
print()

# Displays the first 3 values
print("The first 3 valaues are:\n", practicePandas.head(3))
print()

# Displays the Index null values
print("The null values are:", practicePandas.isnull())
print()

# Replacing the null values with 0
print("Replacing the values:\n", practicePandas.fillna(0))
print()

# Sorting the values
print("Sorting the values:\n", practicePandas.sort_values())
print()

# Counting values
print("Counting the values:\n", practicePandas.value_counts())



