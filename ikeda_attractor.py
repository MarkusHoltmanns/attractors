import matplotlib.pyplot as plt
import numpy as np
import random
from matplotlib import colors


fig, ax = plt.subplots()

num_steps = 2000
particlenumber = 1000
u = 0.918 # ikeda parameter


for particles in range(particlenumber):
   x,y = round(random.uniform(-10., 10), 2),round(random.uniform(-10.,10.), 2) # round(random.uniform(33.33, 66.66), 2)
   x_vals = []
   y_vals = []
   cmap = (random.uniform(0, 1), random.uniform(0, 1), random.uniform(0, 1))
   
   for i in range(num_steps):
      t = 0.4 - 6/(1+x*x+y*y)
      xx = 1 + u*(x*np.cos(t) - y*np.sin(t))
      yy = u*(x*np.sin(t) + y*np.cos(t))
      x=xx
      y=yy
      #if i > 0.5*num_steps:
      x_vals.append((xx))
      y_vals.append((yy))
      
   plt.plot(x_vals,y_vals,c=cmap, linewidth=0.2)
        

# Plot
ax.set(xlabel='x', ylabel='y')
plt.title("Ikeda Attractor")
plt.axis('square')
plt.axis('scaled')
filename = "/Users/Holtmanns/Desktop/ikeda_attractor.png"
plt.savefig(filename, dpi=1200)
plt.show()
