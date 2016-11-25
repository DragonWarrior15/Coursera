from pandas import Series, DataFrame
import pandas as pd
import numpy as np

# pandas
# A Series is a one-dimensional array-like object containing an array of data, which can be any NumPy data type, 
# and an associated array of data labels, functioning as its index.
# we can do regular scalar operations on series similar to numpy arrays
print('pandas series')
S = Series([11, 28, 72, 3, 5, 8])
print(S, S.index, S.values)

# its possible to add our own custom indexes also
print('pandas custom index')
fruits = ['apples', 'oranges', 'cherries', 'pears']
quantities = [20, 33, 52, 10]
S = Series(quantities, index=fruits)
print(S)

# The underlying idea of a DataFrame is based on spreadsheets. We can see the data structure of a DataFrame as tabular and 
# spreadsheet-like. It contains an ordered collection of columns. Each column consists of a unique data typye, 
# but different columns can have different types, e.g. the first column may consist of integers, 
# while the second one consists of boolean values and so on.
# can do sum() and cumusum() operation on either a single column or the whole dataframe
# df['col_name'].sum(), df['col_name'].cumsum()
# city_frame = city_frame.sort(columns="area", ascending=False)

# NumPy array operations, such as filtering with a boolean array, scalar multiplication,
# or applying math functions, will preserve the index-value link
print('Scalar operations on series')
obj2 = Series([4, 7, -5, 3], index=['d', 'b', 'a', 'c'])
print(obj2)
print(obj2[obj2 > 0])
print(obj2 * 2)
print(np.exp(obj2))

# can search for index in the series object, think of it as a key value mapping
print('Pandas check for index')
print('a in obj2 ', 'a' in obj2)

# can create a series from dictionary
sdata = {'Ohio': 35000, 'Texas': 71000, 'Oregon': 16000, 'Utah': 5000}
sdata = Series(sdata)
print(sdata)

# When only passing a dict, the index in the resulting Series will have the dict’s keys in sorted order 
states = ['California', 'Ohio', 'Oregon', 'Texas']
sdata = Series(sdata, index=states)
print(sdata)

# can check for missing values using isnull and notnull functions
print('Pandas checking for missing values')
print('pd.isnull ', pd.isnull(sdata))
print('pd.notnull ', pd.notnull(sdata))

# Both the Series object itself and its index have a name attribute, which integrates with
# other key areas of pandas functionality
print("Pandas name attributes")
sdata.name = "Population"
sdata.index.name = "States"
print(sdata)

# one of the most common ways to create dataframe is from a dict of equal-length lists or NumPy arrays
# columns are places in sorted order
data = {'state': ['Ohio', 'Ohio', 'Ohio', 'Nevada', 'Nevada'],
        'year': [2000, 2001, 2002, 2001, 2002],
        'pop': [1.5, 1.7, 3.6, 2.4, 2.9]}
frame = DataFrame(data)
print('Pandas DataDrame created using lists of equal lengths')
print(frame)

# can print the column using column attribute
print('Pandas columns')
print(frame.columns)

# a column can be retrieved using a dict like notation or attribute
print("Pandas ways to retrieve a column")
print(frame['state'])
print(frame.state)

# Assigning a column that doesn’t exist will create a new column. 
print('Pandas DataFrame creating a new column')
frame['eastern'] = (frame.state == 'Ohio')
print(frame)

# The del keyword will delete columns as with a dict
print('Pandas deleting a column')
del frame['eastern']
print(frame)

# The column returned when indexing a DataFrame is a view on the underlying data, not a copy. 
# Thus, any in-place modifications to the Series will be reflected in the DataFrame. 
# The column can be explicitly copied using the Series’s copy method.

