import matplotlib.pyplot as plt
import numpy as np

# http://www.3d-meier.de/tut19/Seite206.html

fig, ax = plt.subplots()
num_steps = 10000

# with [-0.72],[-0.64]
# 0.9,-0.601,2.0,0.5
# 0.9,-0.5,2.0,0.706
# 0.9,-0.2,2.0,0.5
# 0.86,-0.2,2.0,0.5
# 0.9,0.5,2.018,0.5
# 0.9,-0.5,2.15,0.5

a,b,cc,d = 0.9,-0.2,2.0,0.5

x_vals = []
y_vals = []
x_vals,y_vals = [-0.72],[-0.64]
for i in range(num_steps):
   x = x_vals[i]
   y = y_vals[i]
   xx = x*x - y*y + a*x + b*y
   yy = 2.0*x*y + cc*x + d*y
   x_vals.append(xx)
   y_vals.append(yy)
   

# Plot
ax.scatter(x_vals,y_vals,c='red', s=0.01)
ax.set_aspect('equal', adjustable='box')
ax.set(xlabel='x', ylabel='y')
plt.axis('square')
plt.axis('scaled')
plt.title("Tinkerbell Attractor")

plt.show()
