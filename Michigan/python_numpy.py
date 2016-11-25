# a python script showing the essentials of numpy, pandas
import numpy as np
import pandas as pd

print('numpy basics')
cvalues = [25.3, 24.8, 26.9, 23.9]
C = np.array(cvalues)
print(C)
# we can directly do scalar element wise operations on numpy arrays
F = C *(9/5) + 32  # conventional way of doing this in python fvalues = [x * (9/5) + 32 for x in cvalues]
print(F)
# we can get the no of dimensions in an array using ndim
print('no of dimensions of C = ' + str(np.ndim(C)))
C2 = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
print(C2, 'ndim = ' + str(np.ndim(C2)), 'shape = ' + str(np.shape(C2)))

# creation of evenly spaced values, similar to range function in python but faster
# syntax is arange(start, end, step, dtype), step and dtype are optional
print('numpy arange')
a_range = np.arange(10, 20, 2, 'int8')
b_range = np.arange(10, 20)
print(a_range, b_range)

# another function similar to arange is linspace
# syntax is np.linsapce(start, end, no_of_points, endpoint = True, retstep = False), where endpoint decides whether we have
# an open or a closed interval, retstep if set to True, returns a tuple of the array and the step size
a_linspace = np.linspace(10, 20, 20, endpoint = True)
b_linspace = np.linspace(10, 20, 20, endpoint = False)
print(a_linspace, b_linspace) # see how the returned arrays are different

# axis 1 is the axis along the columns (horizontal axis)
# axis 0 is the axis along the rows (vertical axis)
print('array shapes')
x = np.array([ [67, 63, 87],
               [77, 69, 59],
               [85, 87, 99],
               [79, 72, 71],
               [63, 89, 93],
               [68, 92, 78]])
print(x)
print('shape of x is ' + str(x.shape))
# we can directly change the shape, make sure to maintain the same no of elements
x.shape = (3, 6)
print(x)
print('shape of x is ' + str(x.shape))

# indexing is similar to list indexing in core python
# but, instead of referring to an element like arr[x][y], we can also refer by arr[x, y]
# prefer the second method way [x, y] as the first way creates a temporary intermediate 'list' first and is thus slow
# slicing also works in [::, ::] format, start:stop:steps
# note that all the above are a view into the original array, 
# and hence modifying them modifies the original array in the first place
print('arry slicing')
print("x[1][2] is " + str(x[1][2]) ,"x[1, 2] is " + str(x[1, 2]))

# arrays of ones and zeros
# syntax is np.ones((d1, d2), dtype = 'float32'), np.zeros((d1, d2), dtype = 'float32'), dtype is optional
print('arrays of ones and zeros')
print('an array of 1s ' + str(np.ones((2, 3))))
print('an array of 0s ' + str(np.zeros((2, 3))))
# similarly, there are ones_like and zeros_like to create arrays of 1s and 0s with shape similar to existing arrays

# np.copy() is a useful function to copy an existing object as an array

# identity matrix
# can be created using np.identity(size, dtype)
# np.eye() is a more sophisticted version
# syntax is np.eye(N, M = None, k = 0, dtype) where M, k, dtype are optional
# M is the no of columns, N by default, k is the diagonal, +ve values move the main diagonal upwards and vice versa


# scalar operations in numpy, the operations are not inplace, a new array is returned
# use these operations instead of list comprehensions as these are very very fast
print('scalars on arrays')
a_scalar = np.array([1, 3, 5, 7, 9])
print(a_scalar)
a_scalar = a_scalar + 2
print(a_scalar)
print(a_scalar**2)

# operations on multiple arrays
# if we add to arrays of same shape, or multiply them, the operations are performed elements wise
print('scalar operations on multiple arrays')
x_array = np.array([[1, 2, 3], [7, 8, 9]])
y_array = np.ones((2, 3)) * 2
print('x = ' + str(x_array), 'y = ' + str(y_array), 'x * y = ' + str(x_array * y_array))

# matrix multiplication, use np.dot(A, B)
print('matrix multiplication np.dot()')
A = np.array([1, 2])
B = np.array([[3], [4]])
print('A = ' + str(A), 'B = ' + str(B), 'A * B = ' +str(np.dot(A, B)))
# ensure that the matrices are of the size x X y and y X z
# the same logic can be extended to 3 dimensional arrays, aXbXc and bXcXd resulting array is of size aXbXcXd


# numpy has actual matrices also, can be made using np.mat() function.
# also, multiplication of these matrices provides a new matrix as results using actual matrix multiplication
# and not element wise multiplication
print('actual matrices in numpy')
MA = np.mat(A)
MB = np.mat(B)
print('A*B is ' + str(A * B))
print('MA * MB is ' + str(MA * MB))

# broadcasting, 3x3 and 1x3 is multiplied as if the 1x3 matrix was actually 3x3, the same row is repeated 3 times
# the case can be similarly extended for other type like 1x3 and 3x1, or 1x3 and 3x3, or 3x1 and 1x3 etc
print('numpy broadcasting')
A_b = np.array([[1, 2, 3]])
B_b = np.array([[4], [5], [6]])
print('A_b is ' + str(A_b))
print('B_b is ' + str(B_b))
print('A_b * B_b is ' + str(A_b * B_b))

# numpy random no, numpy gives the flexibility to directly create arrays of any size, made up of random nos
# np.random.randint is half closed interval unlike the randint function in python
print('numpy random no')
outcome = np.random.randint(1, 7, size = (3, 3))
print(outcome)

# numpy boolean masking and fancy indexing
print('boolean masking and fancy indexing')
A_bool = np.array([[1, 2, 3, 4, 5, 6, 7, 8, 9]])
B_bool = A_bool * 2
print(A_bool, B_bool)
print('less than 5 ' + str(A_bool < 5))
print(np.array(A_bool < 5).astype(np.int))
print(B_bool[A_bool < 5])



# pandas
# A Series is a one-dimensional array-like object containing an array of data, which can be any NumPy data type, 
# and an associated array of data labels, functioning as its index.
# we can do regular scalar operations on series similar to numpy arrays
print('pandas series')
S = pd.Series([11, 28, 72, 3, 5, 8])
print(S, S.index, S.values)

# its possible to add our own custom indexes also
print('pandas custom index')
fruits = ['apples', 'oranges', 'cherries', 'pears']
quantities = [20, 33, 52, 10]
S = pd.Series(quantities, index=fruits)
print(S)

# The underlying idea of a DataFrame is based on spreadsheets. We can see the data structure of a DataFrame as tabular and 
# spreadsheet-like. It contains an ordered collection of columns. Each column consists of a unique data typye, 
# but different columns can have different types, e.g. the first column may consist of integers, 
# while the second one consists of boolean values and so on.
# can do sum() and cumusum() operation on either a single column or the whole dataframe
# df['col_name'].sum(), df['col_name'].cumsum()
# city_frame = city_frame.sort(columns="area", ascending=False)

