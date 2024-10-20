import numpy as np
import matplotlib.pyplot as plt

if __name__ == '__main__':
    t = float(input("Input the time you want to plot: "))
    h = np.array([1, 0.1, 0.01, 0.001, 0.0001], dtype=float)
    def function(t,h):
        return 9.8*t+4.9*h
# Calculate the derivative using the forward difference method
    dy_dx = function(t,h)
    plt.plot(h, dy_dx, label='Derivative of y = 4.9x^2', color='b')
    plt.title('Numerical Derivative of y = 4.9x^2')
    plt.xlabel('h (time interval)')
    plt.ylabel("dy/dx (derivative)")
    plt.legend()
    plt.grid(True)
    plt.show()