import numpy
import robust

data = numpy.loadtxt('data.txt')
for line in data:
    print robust.average(line)

