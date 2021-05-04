# arr_op.py
#!/usr/bin/env python3
"""Example of a numpy array operation.   Specifically elu and eluprime.

See:  https://en.wikipedia.org/wiki/Rectifier_(neural_networks)#ELU
"""

import numpy as np
x = np.array([[-1, 2], [3, 4]])

elu = lambda Z: np.where(Z>0, Z, np.exp(Z)-1)
eluprime = lambda Z: np.where(Z>0, 1, np.exp(Z))

output1=elu(x)
output2=eluprime(x)
print(f'elu=\n{output1}')
print(f'eluprime=\n{output2}')
