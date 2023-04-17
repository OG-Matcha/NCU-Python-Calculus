import pylab

a, b = -10 * pylab.pi, 10 * pylab.pi
n = 200
dx = (b - a) / (n - 1)

xs = [a + i * dx for i in range(n)]
ys = [pylab.sin(x) / abs(2*x) for x in xs]

pylab.plot(xs, ys)
pylab.grid()
pylab.xlabel("X")
pylab.ylabel("Y")
pylab.title("f(x) = sin(x)/|2x|")

pylab.show()