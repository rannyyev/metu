# Student ID  : #######
# Project Name: Make Graphene
# Project ID  : S-GEN-MakeGraphene
# Description : This script generates a graphene sheet whose size is determined by the user

import math
from matplotlib import pyplot as plt

# The number of atoms on the horizontal and vertical axes
N1 = int(input())
N2 = int(input())

# The length of the bond between atoms
d = 2

# Open the file to write coordinates
with open('coordinates.txt', 'w') as coordinates:

  x = [(math.sqrt(3) * d) * i for i in range(N1)]
  y = [] * N1

  # Write the initial coordinates of the atoms to the file
  for j in range(N1):
      coordinates.write('{}, {}\n'.format(x[j], y[j]))

  # Plot the initial coordinates of the atoms
  plt.scatter(x, y, marker='*', color='green')

  # Calculate and write the coordinates for the remaining atoms
  for _ in range(N2 - 1):
      for j in range(N1):
          x[j] = x[j] + d * math.sqrt(3) / 2
          y[j] = y[j] + d / 2
          coordinates.write('{}, {}\n'.format(x[j], y[j]))

      plt.scatter(x, y, marker='*', color='green')

      for j in range(N1):
          y[j] = y[j] + d
          coordinates.write('{}, {}\n'.format(x[j], y[j]))

      plt.scatter(x, y, marker='*', color='green')

# Display the plot
plt.show()