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