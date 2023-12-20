import matplotlib.pyplot as plt

def f(x):
    return x**2 - 3

x = list(range(-100, 101))

y = [f(n) for n in x]

plt.plot(x, y, label='f(x) = x^2 - 3')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.title('Graph of f(x) = x^2 - 3')
plt.axhline(0, color='black',linewidth=0.5)
plt.axvline(0, color='black',linewidth=0.5)
plt.grid(color = 'gray', linestyle = '--', linewidth = 0.5)
plt.legend()
plt.show()