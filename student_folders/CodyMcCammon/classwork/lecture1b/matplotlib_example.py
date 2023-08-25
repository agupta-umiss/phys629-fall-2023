import matplotlib.pyplot as plt 
import numpy as np

x = np.linspace(0, 3*np.pi, 300)

y = np.sin(x)
y2 = np.sin(x**2)
y3 = np.cos(3*x)

plt.plot(x, y, label=r'$\sin(x)$', color = "red")
plt.plot(x, y2, label=r'$\sin(x^2)$', color = "orange")
plt.plot(x, y3, label=r'$\cos(3x)$', color = "blue")
plt.title('Some functions')
plt.xlabel('x')
plt.ylabel('y')

plt.grid(which='major')
plt.legend(loc='lower left');

## optional extras
plt.minorticks_on()
plt.tick_params(which='both', direction='in', tick2On=True)

plt.show()
