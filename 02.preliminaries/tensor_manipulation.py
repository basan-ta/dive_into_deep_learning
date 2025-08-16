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