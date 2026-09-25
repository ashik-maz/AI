import matplotlib.pyplot as plt

def f(x):
    return (x - 3)**2

def gradient(x):
    return 2 * (x - 3)

x = 0.0
eta = 0.1

x_values = [x]
y_values = [f(x)]

for i in range(10):
    x = x - eta * gradient(x)

    x_values.append(x)
    y_values.append(f(x))

    print(i + 1, "x =", x, "f(x) =", f(x))

# Plot
xs = [i / 10 for i in range(61)]
ys = [f(i) for i in xs]

plt.plot(xs, ys)
plt.scatter(x_values, y_values)

plt.xlabel("x")
plt.ylabel("f(x)")
plt.title("Gradient Descent")
plt.grid(True)
plt.show()