import numpy as np
data = np.arange(6)*2 + np.random.random((8,6)) 
data[2,3] *= 12
data[7,4] *= 12
data[6,0] *= 12
data[5,1] *= 11
data *= 1000
data.T[0][-1] /=10
data.T[0][-1] /= 10
data.T[1][2] /= 10
data = data.astype(int)
data = data.T

data = data[[1,4,2,3,5,0]]
data = data.astype(float)
with open('data.txt', 'w') as output:
    for line in data:
        print >>output, '\t'.join(['{:}'.format(v) for v in line])
