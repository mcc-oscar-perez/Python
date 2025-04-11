# How to create a numpy array and print some properties of the array

import numpy as np 

lista = [1,2,3,4,5]
array = np.array(lista)
print(array)
print(type(array))
print(array.shape)

#%%
# Create a 2D numpy array (matrix) with 2 rows and 3 columns
# pritnt some properties of the matrix
# and print some specific elements of the matrix 

import numpy as np

matriz = np.array([[1,2,3],[4,5,6]])
print(matriz)
print(matriz.shape)
print(f" first row is: {matriz[0]}")
print(f" last row is: {matriz[1]}")
print(f" Specific element is: {matriz[0,1]}") # 0 is the row and 1 is the column
print(f"Whole column is: {matriz[ : , 2]}") # 2 is the column
# %%

# Do mathematical operations with numpy arrays

import numpy as np 

array1 = np.array([1,2,3])
array2 = np.array([4,5,6])

print(array1 + array2) # sum of the two arrays
print(array1 - array2) # subtraction of the two arrays
print(array1 * array2) # multiplication of the two arrays
print(array1 / array2) # division of the two arrays
print(array1 ** 2) # square of the first array
print(array1 * 2) # multiplication of the first array by 2
print(array1 + 2) # sum of the first array by 2
print(array1 * array2 + 2) # multiplication of the two arrays and sum by 2
print(array1 * array2 - 2) # multiplication of the two arrays and subtraction by 2
print(array1 * array2 / 2) # multiplication of the two arrays and division by 2
print(array1 * array2 ** 2) # multiplication of the first array by the square of the second array
print(array1 * array2 + 2) # multiplication of the two arrays and sum by 2


# %%
