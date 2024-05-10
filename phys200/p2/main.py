# Student ID  : #######
# Project Name: Planck's Law
# Project ID  : S-GEN-PlancksLaw
# Description : This script calculates the total power emitted by a black-body using the Simpson's rule

import math
from scipy.constants import h, k, c
from matplotlib import pyplot as plt

# The absolute temperature of a black-body
T = 4000


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
        return stop
    else:
        h = (stop - start) / (n - 1)
        list = [start + h * i for i in range(n)]
        return list


def simpson_integrate(func, T, a, b, n):
    """
    Approximates the area under the graph of function of spectral radiance
    from a to b with n intervals using composite Simpson's 1/3 rule

    :param func: the function of spectral radiance
    :param T: the absolute temperature
    :type T: float
    :param a: the starting value
    :type a: float
    :param b: the end value
    :type b: float
    :param n: an even number of intervals between a and b
    :type n: integer
    :return: the area under the graph of function of spectral radiance
    :rtype: float
    """
    if n % 2 == 1:
        raise ValueError("n must be an even integer.")

    h = (b - a) / n
    result = func(a, T) + func(b, T)

    for i in range(1, n):
        x = a + i * h
        if i % 2 == 0:
            result = result + 2 * func(x, T)
        else:
            result = result + 4 * func(x, T)

    return h / 3 * result


def func_planck(f, T):
    """
    Calculates the value of spectral radiance of a black-body with frequency f
    and absolute temperature T

    :param f: the frequency of the black-body
    :type f: function
    :param T: the absolute temperature
    :type T: float
    :return: the spectral radiance of the black-body
    :rtype: float
    """
    exponent = math.exp(h * f / (k * T))
    result = (2 * h * f**3 / c**2) * (1 / (exponent - 1))
    return result


# The values of frequency of a black-body
fr_list = linspace(1, 1e15, 100000)

# The values of the spectral radiance for values of frequency in fr_list
func_planck_list = [func_planck(i, T) for i in fr_list]

# The area under the graph
area = simpson_integrate(func_planck, T, 1, 1e15, 100000)

# The plot
plt.plot(fr_list, func_planck_list, label=f'T = {T} + K')
plt.legend(loc='upper left')
plt.title('Planck\'s law of black-body radiation')
plt.xlabel(r'$\nu$, [Hz]')
plt.ylabel(r'$B_{\nu}(\nu, T)$')
plt.grid()

# Display the plot
plt.show()
