import torch 
x = torch.arange(12, dtype=torch.float32)
#unary operations like e*x 
x = torch.exp(x)
print(x)