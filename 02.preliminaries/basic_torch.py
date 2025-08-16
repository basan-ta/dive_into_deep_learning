import torch 
x = torch.arange(12, dtype=torch.float32)

#to see total number of elements
print(x.numel())



#reshaping the tensor 
x = x.reshape(3, 4)

#for shape of the tensor
print(x.shape)

print(x)    