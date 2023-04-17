import sympy

# enable the best printer
sympy.init_printing()

# define the variable and function
sympy.var("x, y")
func = x * sympy.sin(y) * sympy.cos(x)

# integrate with respect to x first and then integrate with respect to y for three times
for i in range(3):
    ifn = sympy.Integral(func, x, y)
    func = ifn.doit()
    sympy.pprint(ifn)
    print("=")
    sympy.pprint(func)
    print()

# redefine the function
func = x * sympy.sin(y) * sympy.cos(x)

# integrate with respect to y first and then integrate with respect to x for three times
for i in range(3):
    ifn = sympy.Integral(func, y, x)
    func = ifn.doit()
    sympy.pprint(ifn)
    print("=")
    sympy.pprint(func)
    print()
