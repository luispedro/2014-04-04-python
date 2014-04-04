import numpy as np
from matplotlib import pyplot
data = np.loadtxt('data.txt')
pyplot.plot(data.max(0))
pyplot.savefig('max.pdf')
pyplot.show()
