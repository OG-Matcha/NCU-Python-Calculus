import pylab

# define required variables
xs, step = pylab.linspace(1, 2, 101, retstep=True)
ys = xs * pylab.sqrt(2 * xs - 1)

# calculate real result
real_area = -4 / 15 + 7 * pylab.sqrt(3) / 5

# calculate square & up_square & down_square
square_area, up_square_area, down_square_area = 0, 0, 0
y1 = ys[0]

# loop
for y2 in ys[1:]:
    square_area += y1
    if y1 < y2:
        up_square_area += y2
        down_square_area += y1
    else:
        up_square_area += y1
        down_square_area += y2
    y1 = y2

# multiply heights with width
square_area, up_square_area, down_square_area = map(step.__mul__, (square_area, up_square_area, down_square_area))

# print results
print(f"數學積分     : {real_area:.9f}", end="\n\n")

print("迴圈求積:")
print(f"矩形積分     : {square_area:.9f} 誤差: {abs(real_area - square_area):.10f}")
print(f"上矩形積分   : {up_square_area:.9f} 誤差: {abs(real_area - up_square_area):.10f}")
print(f"下矩形積分   : {down_square_area:.9f} 誤差: {abs(real_area - down_square_area):.10f}")