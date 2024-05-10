# Student ID  : 2604619
# Project Name: Taylor Expansion
# Project ID  : S-Taylor
# Description : This script calculates the exponential of a float number numerically by utilizing the Taylor expansion

import math
import random
from matplotlib import pyplot as plt

# The number of expansion terms
N = int(input())

# The value for which the exponential is computed
x = round(random.uniform(-2, 5), 2)

def factorial(n):
    """
    Calculates the factorial of a number n

    :param n: the number for which the factorial is computed
    :type n: int
    :return: the factorial of n
    :rtype: int
    """
    factorial = 1
    for i in range(1, n+1):
        factorial *= i
    return factorial

def linspace(start, stop, n):
    """
    Returns a list of evenly spaced numbers over a specified interval

    :param start: the starting value of the sequence
    :type start: float
    :param stop: the end value of the sequence
    :type stop: float
    :param n: number of samples to generate
    :type n: int
    :return: n evenly spaced samples, calculated over the interval [start, stop]
    :rtype: list
    """
    if n < 2:
        return [stop]
    else:
        h = (stop - start) / (n - 1)
        return [start + h * i for i in range(n)]

def taylor(x, N):
    """
    Approximates the value of the exponential at x using Taylor series

    :param x: the argument of exp operator
    :type x: float
    :param N: the number of expansion terms in the series
    :type N: int
    :return: approximate value of the exponential at x
    :rtype: float
    """
    e = 0
    for i in range(N):
        e = e + (x**i) / factorial(i)
    return e

# The list of values of x
xl = linspace(-2, 5, 1000)

# The values of the exp() method for values in xl
exp = [math.exp(xl[i]) for i in range(len(xl))]

# The values of taylor() function for values in xl for the specified N
Taylor = [taylor(xl[i], N) for i in range(len(xl))]

# The values of taylor() function for values in xl
# for the number of expansion terms from 0 to N
TaylorN = [taylor(x, i) for i in range(N+1)]

# The percentage error
error = [abs((math.exp(x)-TaylorN[i])/math.exp(x))*100 for i in range(N+1)]

fig, axs = plt.subplots(1, 2)

# The first plot
axs[0].plot(xl, exp, label=r'$e^x$', color='blue')
axs[0].plot(xl, Taylor, label='Taylor', color='red', linestyle='--')
axs[0].plot([], [], label=f'N = {N}', linestyle=' ')
axs[0].plot([], [], label=f'x = {x}', linestyle=' ')
axs[0].legend(loc='upper left')
axs[0].set_xlabel('x')
axs[0].set_ylabel('f(x)')
axs[0].set_xlim(-2, 5)
axs[0].set_ylim(0)
axs[0].hlines(y=math.exp(x), xmin=-2, xmax=x, color='black', linestyles='--')
axs[0].vlines(x=x, ymin=0, ymax=math.exp(x), color='black', linestyles='--')
axs[0].grid()

# The second plot
axs[1].plot(error, color='blue')
axs[1].set_xlabel('N')
axs[1].set_ylabel(r'$\%_{error}$')
axs[1].set_xlim(0, N)
axs[1].axhline(0, linestyle='--', color='black')
axs[1].grid()

# Show the plots
plt.show()
