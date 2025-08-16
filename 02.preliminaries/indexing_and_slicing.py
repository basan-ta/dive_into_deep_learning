import torch
x = torch.arange(12, dtype=torch.float32)
x = x.reshape(-1,4)
#last row of the tensor
print(x[-1])

#to print specific row
print(x[1])

#to print all rows and  specific column
print(x[:2])

#to print specific element
print(x[1,3]) 

#remove second row and replace it with 22
x[1] = 22

#to replace first two rows with 88
x[:2,:] = 88
print(x)