import matplotlib as plt
import numpy as np

np.random.seed(0)

x1 = np.random.randint(10, size = 6)

x2 = np.random.randint(10, size = (3, 4))

x3 = np.random.randint(10, size = (3, 4, 5))


print("x1 ndim:", x1)

print("x2 ndim:", x2)

print("x3 ndim:", x3)

print("x1 ndim:", x1.ndim)

print("x2 ndim:", x2.shape)

print("x3 ndim:", x3.size)


