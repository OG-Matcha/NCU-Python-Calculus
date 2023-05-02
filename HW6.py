import pylab
import numpy


def fn(x, y):
    return numpy.cos(numpy.sqrt(x))


def f(x):
    return 2 * (numpy.sqrt(x) * numpy.sin(numpy.sqrt(x)) + numpy.cos(numpy.sqrt(x))) - 1


a, b, n = 0, 2 * numpy.pi, 100

xs = numpy.linspace(a, b, n + 1)
h = (b - a) / n

ys = [None] * (n + 1)

ys[0] = f(a)
for i in range(n):
    ys[i + 1] = ys[i] + h * fn(xs[i], ys[i])

pylab.rcParams["figure.figsize"] = (10, 5)
pylab.grid()
pylab.plot(xs, ys, color='blue')

pylab.plot(xs, f(xs), color='green')

pylab.title(("y' = cos(sqrt(x)) with y(0) = 1"))
pylab.xlabel("X")
pylab.ylabel("Y")
pylab.show()
