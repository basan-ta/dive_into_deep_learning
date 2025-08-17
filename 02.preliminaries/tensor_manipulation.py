import torch 
x = torch.arange(12, dtype=torch.float32)
#unary operations like e*x 
x = torch.exp(x)
print(x)

#binary scalar operations
a = torch.tensor([1, 2, 3,4,5,6,7,8,9,10])
b = torch.tensor([10, 9, 8,7,6,5,4,3,2,1])

# operations 
a+b, a-b, a*b, a/b, a**2

print("addition:", a + b)
print("subtraction:", a - b)
print("multiplication:", a * b)
print("division:", a / b)
print("power:", a ** 2) 


p = torch.arange(12, dtype=torch.float32).reshape(3, 4)
q = torch.tensor([[1, 2, 3, 4],
                  [5, 6, 7, 8],
                  [9, 10, 11, 12]])

'''Concatenate along the first dimension, 
dim=0 --> stack rows vertically (row direction).
Both tensors have 3 rows, so result = 6 rows × 4 columns.'''
print(torch.cat((p, q), dim=0))

''' Concatenate along the second dimension  
dim=1 --> stack columns horizontally.
Both tensors have 4 columns, so result = 3 rows × 8 columns.'''
print(torch.cat((p, q), dim=1))


#conversion between numpy and torch
import numpy as np
a = np.array([[1, 2, 3], [4, 5, 6]])
b = torch.from_numpy(a)  
print(type(a), type(b))

# Converting back to numpy
c = b.numpy()
print("Converted back to Numpy array:\n", c)    