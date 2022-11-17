import matplotlib.pyplot as plt
import numpy as np

np.random.seed(0)

x = np.linspace(0,5,100)
noise = np.random.normal(0,1,100)

def y(x):
    """真の関数"""
    return 3 - 5 * x + x ** 2

t = y(x)+noise
plt.scatter(x,t)
