import numpy as np
import matplotlib.pyplot as plt

def f(x, y):
    return (x - 3)**2 + (y - 2)**2

def gradient(x, y):
    dx = 2 * (x - 3)
    dy = 2 * (y - 2)
    return dx, dy

x = 0.0
y = 0.0
eta = 0.1

x_values = [x]
y_values = [y]

for i in range(10):
    dx, dy = gradient(x, y)

    x = x - eta * dx
    y = y - eta * dy

    x_values.append(x)
    y_values.append(y)

    print(i + 1, "x =", x, "y =", y, "f(x,y) =", f(x,y))

# Plot
X = np.linspace(-1, 5, 100)
Y = np.linspace(-1, 4, 100)

X, Y = np.meshgrid(X, Y)
Z = f(X, Y)

plt.contour(X, Y, Z)

plt.plot(x_values, y_values, marker='o')

plt.xlabel("x")
plt.ylabel("y")
plt.title("Two Variable Gradient Descent")
plt.grid(True)
plt.show()