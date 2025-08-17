import torch 
#scalars
x = torch.tensor(3.0)
y = torch.tensor(7)
print(x+y)

#vectors (in L.algebra it is known as one-based indexing)
a = torch.arange(3)
print(f"vector a ",a)

#access via indexing
print(a[2]) #access second element of a ("2")

#len and shape 
print(f"length\n ",len(a))
print(f"shape\n", a.shape)