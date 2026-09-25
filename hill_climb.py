import matplotlib.pyplot as plt

def f(x):
    return -x**2 + 10*x + 5

x = 2
while True:
    cur = f(x)
    L = f(x - 1)
    R = f(x + 1)

    best = x - 1 if L > R else x + 1

    print("x =", x, "f(x) =", cur)
    if cur >= max(L, R):
        break

    x = best


print("\nFinal:")
print("x =", x)
print("f(x) =", f(x))


# Plot
xs = list(range(0, 11))
ys = [f(i) for i in xs]

plt.plot(xs, ys, marker='o')
plt.scatter([x], [f(x)], s=100)

plt.xlabel("x")
plt.ylabel("f(x)")
plt.title("Hill Climbing")
plt.grid(True)
plt.show()