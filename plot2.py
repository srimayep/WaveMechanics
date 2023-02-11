import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-10, 10, 1000)
y = 1/np.sqrt(3*np.pi) * np.exp(-x**2/3)

plt.plot(x, y)
plt.xlabel('x')
plt.ylabel(r'$\psi(x)$')
plt.title(r'Plot of $\psi(x) = \frac{1}{\sqrt{3\pi}} \cdot e^\frac{-x^2}{3}$')
plt.show()
