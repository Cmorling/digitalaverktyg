import numpy as np
import matplotlib.pyplot as plt


ax = plt.figure().add_subplot()
ax.set_xlim(-10, 10); ax.set_ylim(-10, 10)

# Prepare arrays x, y, z
x = np.linspace(-10, 10, 100)
y = x**2
print(y.shape)
ax.plot(x, y, label='Andra gradare')
ax.legend()

plt.show()