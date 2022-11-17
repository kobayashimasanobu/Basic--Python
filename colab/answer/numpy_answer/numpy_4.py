import matplotlib.pyplot as plt
import numpy as np

np.random.seed(0)

x = np.linspace(0,5,100)
noise = np.random.normal(0,1,100)

def y(x):
    """真の関数"""
    return 3 - 5 * x + x ** 2

t = y(x)+noise

Y = np.array([np.ones(len(x)),x,x**2])
X = Y.T

W = np.linalg.inv(Y @ X) @ Y @ t
w0 = W[0]
w1 = W[1]
w2 = W[2]
pred_y = w0 + w1 * x + w2 * x ** 2

plt.scatter(x, t)
plt.plot(x, pred_y, linewidth=5, color="red", label="pred")
plt.plot(x, y(x), linewidth=5, color="green", label="true")
plt.legend()
