import numpy
import robust

data = numpy.loadtxt('data.txt')
avg =[]
for line in data:
    print robust.average(line)

