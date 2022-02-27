import numpy as np
import matplotlib.pyplot as plt

t = np.arange(0., 5., 0.2)

plt.plot(t, t, color = 'red', linestyle = 'dashed')
plt.plot(t, t**2, color = 'white', marker = 's', mec = 'green', mfc = 'green' )
plt.plot(t, t**3, color = 'white', marker = '^', mec = 'blue', mfc = 'blue' )
plt.show()