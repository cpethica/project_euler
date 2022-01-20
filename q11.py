# question 11

import pdb

#  read data and convert to long list of numbers:
lines = []
with open('q11_data.txt') as f:
    #Content_list is the list that contains the read lines.
    for line in f:
        lines.append(line.rstrip().split())

flat_list = [item for sublist in lines for item in sublist]

nums = [int(i) for i in flat_list]

#  convert to numpy matrix
import numpy as np
mat = np.reshape(nums,(20,20))

# array to store products
products = []

# get sequential 4x4 matrices to calculate products from
# rows
for i in range(0,17):    
# columns
    for k in range(0,17):
        fourbyfour = mat[i:i+4,k:k+4]
#         products of each 4 rows and columns for the selected matrix
        for x in range(0,4):
            products.append(np.prod(fourbyfour[x,:]))
            products.append(np.prod(fourbyfour[:,x]))
#       diagonals
        products.append(fourbyfour[0,0]*fourbyfour[1,1]*fourbyfour[2,2]*fourbyfour[3,3])
        products.append(fourbyfour[0,3]*fourbyfour[1,2]*fourbyfour[2,1]*fourbyfour[3,0])

print(max(products))
