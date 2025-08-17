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

'''scalars are 0-th order tensor, vector are 1-st order tensor and matrices are the 2-nd order tensor  '''

A = torch.arange(6).reshape(3,2)
print(A)
#transpose of matrix 
print(A.T)

#symmetric matrix
B = torch.tensor([[1,2,3],[2,0,4],[3,4,5]])
print(B)
#condition to be symmetric is B.T = B 
print(B == B.T)

#tensor with higher order
P = torch.arange(24).reshape(2,3,4)
print(P)

#copy the tensor and perform Tensor Arithmetic 
A = torch.arange(6, dtype = torch.float32).reshape(3,2)
B = A.clone()
print(A)
print(A+B)
print(A*B)

#multiplying tensor with scalar
o = 2
print(o + A)
print(o * A)
print((o*A).shape)