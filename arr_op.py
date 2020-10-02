import numpy as np
x = np.array([[-1, 2], [3, 4]])

elu = lambda Z: np.where(Z>0, Z, np.exp(Z)-1)
eluprime = lambda Z: np.where(Z>0, 1, np.exp(Z))

output1=elu(x)
output2=eluprime(x)
print(f'elu=\n{output1}')
print(f'eluprime=\n{output2}')
