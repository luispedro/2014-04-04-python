import numpy
from matplotlib import pyplot
data = numpy.loadtxt('data.txt')
pyplot.plot(data.max(0))
pyplot.savefig('max.pdf')
pyplot.show()

pyplot.clf()
pyplot.boxplot(numpy.transpose(data))
pyplot.savefig('boxplots.pdf')
pyplot.show()
