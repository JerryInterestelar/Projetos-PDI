import numpy as np
n = 1
x = 3
a, b = np.meshgrid(np.linspace(-n, n, x), np.linspace(-n, n, x))
d = np.sqrt(a*a+b*b)

sigma, mu = 1, 0
g = np.exp(-(d - mu)**2/(2*sigma**2))
print(g)

