import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-10, 10, 1000)
y = 1/np.sqrt(10) * 1/np.cosh(x/5)

plt.plot(x, y)
plt.xlabel('x')
plt.ylabel(r'$\psi(x)$')
plt.title(r'Plot of $\psi(x) = \frac{1}{\sqrt{10}} \cdot \sech{x/5}$')
plt.show()
