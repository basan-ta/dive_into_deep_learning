import torch 
x = torch.arange(12, dtype=torch.float32)

#to see total number of elements
print(x.numel())

#reshaping the tensor 
x = x.reshape(3, 4)
#we can alse use -1 to infer the size of one dimension
#x = x.reshape(3, -1)

# mean if you have 1200 elements --> x.reshape(10, -1)  which mean size → (10, 120)


#for shape of the tensor
print(x.shape)

print(x) 

#create y tensor with zeros as all elements
y = torch.zeros((2,3,4))   
print(y)

''' First dimension = 2 →  2 blocks 
    second dimension = 3 → each block has 3 rows
    Third dimension = 4 → each row has 4 columns 
    '''
#create z tensor with ones as all elements
z = torch.ones((2,3,4))
print(z)