import os
import pandas as pd
import torch

# Make directory
os.makedirs(os.path.join('..', 'data'), exist_ok=True)
# File path
data_file = os.path.join("..", 'data', 'house_tiny.csv')

with open(data_file, 'w') as f:
    f.write("""NumRooms,RoofType,Price
1,Gable,50000
2,Hip,65000
3,Gambrel,70000
2,Flat,55000
4,Mansard,120000
3,Gable,85000
5,Hip,150000
2,Gambrel,60000
6,Flat,200000
4,Gable,130000
3,Hip,95000
1,Flat,40000
2,Mansard,70000
3,Gable,80000
,Gambrel,125000
,Flat,160000
2,Gable,62000
6,Hip,210000
3,Mansard,100000
4,Flat,140000
""")
    
data = pd.read_csv(data_file)

'''inputs: all rows of the first two columns (features)
targets: all rows of the third column (labels)'''
inputs, targets = data.iloc[:, 0:2], data.iloc[:,2]
inputs = pd.get_dummies(inputs, dummy_na=True)
print("Inputs:\n", inputs)

#two field in NaN so filling it with mean value of corresponding column
inputs = inputs.fillna(inputs.mean())
print("Inputs after filling NaN with mean:\n", inputs)

#loading into tensor 
x = torch.tensor(inputs.to_numpy(dtype=float))
y = torch.tensor(targets.to_numpy(dtype=float))
print(x)
print(f"Targets into tenor:\n",y)