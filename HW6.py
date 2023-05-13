import pylab
from numpy import sin, cos, sqrt, pi, linspace

# derivative function


def fn(x, y):
    return cos(sqrt(x))

# original function


def f(x):
    return 2 * (sqrt(x) * sin(sqrt(x)) + cos(sqrt(x))) - 1


# from 0 to 2π, take 100 points
a = 0
b = 2 * pi
n = 100

# separate the space and calculate the distance between two points
xs = linspace(a, b, n + 1)
h = (b - a) / n

# set a default list to store values
ys = [None] * (n + 1)

# set y(0) to 1 and fill the list with Euler method
ys[0] = 1
for i in range(n):
    ys[i + 1] = ys[i] + h * fn(xs[i], ys[i])

# set the window size
pylab.rcParams["figure.figsize"] = (10, 5)

# plot the lines
pylab.plot(xs, ys, color="blue", label="Euler method")
pylab.plot(xs, f(xs), color="green", label="exact")

# set the coordinates
pylab.xlim(left=0, right=7)
pylab.ylim(bottom=0, top=2.5)

# Add title, labels, grid and legend
pylab.title("y' = cos(sqrt(x)) with y(0) = 1")
pylab.xlabel("X")
pylab.ylabel("Y")
pylab.grid()
pylab.legend()

# show the window
pylab.show()
