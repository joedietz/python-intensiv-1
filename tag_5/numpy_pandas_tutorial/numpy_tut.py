import numpy as np
import matplotlib.pyplot as plt

v = np.array([1, 2, 3, 4, 5, 3])
# v = v.astype(np.int8)
print(f"Shape: {v.shape} Datentyp: {v.dtype}")
print(v)

v3 = v**2  # SIMD (Single Instruction, Multiple Data)
print(v)

w = v + v3
print(w)


x = np.linspace(0, 10, num=100)
y = x**2

plt.plot(x, y)
plt.title("Toller Plot")
plt.show()
