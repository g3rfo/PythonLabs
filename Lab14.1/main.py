import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 10, 1000)
y = - (x ** np.cos(5 * x))

plt.figure(figsize=(8, 6))
plt.plot(x, y, label=r"Y(x)=-x^cos(5*x), x=[0...10]", color='red')
plt.axhline(0, color='black', linewidth=0.5, linestyle='-')
plt.axvline(0, color='black', linewidth=0.5, linestyle='-')
plt.title("Графік функції Y(x)=-x^cos(5*x), x=[0...10]")
plt.xlabel("x")
plt.ylabel("Y(x)")
plt.legend()
plt.grid(True)
plt.show()