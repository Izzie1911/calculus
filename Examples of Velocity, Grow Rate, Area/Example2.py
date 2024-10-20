import numpy as np
import matplotlib.pyplot as plt
"""
This program calculates the derivative of the function y = 4.9 * x^2
with respect to time in the interval [t1, t1 + h].
@:parameter t1 is the time at which we want to calculate the derivative.
@:parameter array h is the array of small time intervals.
"""
if __name__ == '__main__':
    t = float(input("Input the time you want to plot: "))
    h = np.array([1, 0.1, 0.01, 0.001, 0.0001], dtype=float)
    def function(X):
        return 4.9 * (X ** 2)
# Calculate the derivative using the forward difference method
    dy_dx = (function(t + h) - function(t)) / h
    print(dy_dx)
    plt.plot(h, dy_dx, label='Derivative of y = 4.9x^2', color='b')
    plt.title('Numerical Derivative of y = 4.9x^2')
    plt.xlabel('h (time interval)')
    plt.ylabel("dy/dx (derivative)")
    plt.legend()
    plt.grid(True)
    plt.show()