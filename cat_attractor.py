import matplotlib.pyplot as plt
import numpy as np
import random

# http://www.3d-meier.de/tut19/Seite206.html

fig, ax = plt.subplots()

num_steps = 20000
x_vals = []
y_vals = []

x,y = round(random.uniform(-1., 1), 2),round(random.uniform(-1.,1.), 2) # round(random.uniform(33.33, 66.66), 2)
k = 0.05
for i in range(num_steps):
   xx = (x + y) % 1
   yy = (x + k*y) % 1
   x=xx
   y=yy
   x_vals.append(xx)
   y_vals.append(yy)
   

# Plot
ax.scatter(x_vals,y_vals,c='red', s=0.1)
ax.set(xlabel='x', ylabel='y')
plt.title("Arnold Cat Attractor")

plt.show()
