# Student ID  : #######
# Project Name: Pi Monte Carlo
# Project ID  : S-PiMonteCarlo
# Description : This code approximates pi using the Monte Carlo method

import math
import random
from matplotlib import pyplot as plt

# Request the number of points from the user
N = int(input())


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


# The coordinates of all points
x = []
y = []

# The coordinates of points within the arc of the circle
in_x = []
in_y = []

# The coordinates of points outside the arc of the circle
out_x = []
out_y = []

for i in range(1, N + 1):
    randx = random.random()
    randy = random.random()

    if (randx ** 2 + randy ** 2) < 1:
        in_x.append(randx)
        in_y.append(randy)
    else:
        out_x.append(randx)
        out_y.append(randy)

    x.append(randx)
    y.append(randy)

# The values of x of the plot of the arc of the circle
cx = linspace(0, 1, 10000)

# The values of y of the plot of the arc of the circle
cy = [math.sqrt(1 - cx[i] ** 2) for i in range(10000)]

fig, axs = plt.subplots(1, 2)

# The first plot
axs[0].scatter(in_x, in_y, color='blue', marker='o', s=5)
axs[0].scatter(out_x, out_y, color='red', marker='^', s=5)
axs[0].plot(cx, cy, color='black')
axs[0].set_xlim([0, 1])
axs[0].set_ylim([0, 1])
axs[0].set_box_aspect(1)

error_list = []

for i in range(1, N + 1):
    x = []
    y = []

    in_x = []
    in_y = []

    out_x = []
    out_y = []

    for j in range(i):
        randx = random.random()
        randy = random.random()

        if (randx ** 2 + randy ** 2) < 1:
            in_x.append(randx)
            in_y.append(randy)
        else:
            out_x.append(randx)
            out_y.append(randy)

        x.append(randx)
        y.append(randy)

    pi = 4 * len(in_x) / len(x)
    error = abs((pi - math.pi) / math.pi * 100)
    error_list.append(error)

# The second plot
axs[1].plot(error_list, color='green')
axs[1].axhline(0, linestyle='--', color='black')
axs[1].set_xlim(0, N)
axs[1].set_box_aspect(1)
axs[1].set_xlabel('N')
axs[1].set_ylabel(r'$\%_{error}$')
axs[1].grid()

# Show the plots
plt.show()
