import matplotlib.pyplot as plt
import numpy as np
import random

# http://www.3d-meier.de/tut19/Seite206.html

fig, ax = plt.subplots()

num_steps = 20000
x_vals = []
y_vals = []

x,y = round(random.uniform(-10., 10), 2),round(random.uniform(-10.,10.), 2) # round(random.uniform(33.33, 66.66), 2)
sigma = 0.5
for i in range(num_steps):
   xx = (x + y + sigma*np.cos(2.0*np.pi*y)) % 1
   yy = (x + 2.0*y) % 1
   x=xx
   y=yy
   x_vals.append(xx)
   y_vals.append(yy)
   

# Plot
ax.scatter(x_vals,y_vals,c='red', s=0.1)
ax.set(xlabel='x', ylabel='y')
plt.title("Sinai Attractor")
plt.axis('square')
plt.axis('scaled')
plt.show()
