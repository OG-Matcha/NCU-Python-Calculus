import pylab

def f(x):
    return (2 + pylab.sin(x / pylab.pi)) / (2 - pylab.sin(x / pylab.pi))

def f_diff(x):
    return 4 * pylab.cos(x / pylab.pi) / (pylab.pi * (pylab.sin(x / pylab.pi) - 2) ** 2)

a, b = 0, 50
n = 200
dx = (b - a) / (n - 1)

xs1 = [a + i * dx for i in range(n)]
ys1 = [f(x) for x in xs1]

xs2 = [a + i * dx for i in range(n)]
ys2 = [f_diff(x) for x in xs2]

pylab.rcParams["figure.figsize"] = (10,5)
pylab.plot(xs1, ys1)
pylab.plot(xs2, ys2)
pylab.grid()
pylab.xlabel("X")
pylab.ylabel("Y")
pylab.title("f(x) = (2 + sin(x/pi)) / (2 - sin(x/pi)) and computed derivative")

pylab.show()