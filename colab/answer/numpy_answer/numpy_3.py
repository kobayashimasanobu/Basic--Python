import numpy as np
import matplotlib.pyplot as plt

np.random.seed(0)
x = np.linspace(0,5,100)

Y = np.array([np.ones(len(x)),x,x**2])
X = Y.T
