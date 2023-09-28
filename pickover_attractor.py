import matplotlib.pyplot as plt
import numpy as np


fig, ax = plt.subplots()
num_steps = 1000000
#a,b,cc,d = -1.24458046630025,-1.25191834103316,-1.81590817030519,-1.90866735205054
a,b,cc,d = -0.95,2.87,0.76,0.74

x_vals = []
y_vals = []
x_vals,y_vals = [0.],[0.] # [-0.72],[-0.64]
for i in range(num_steps):
   x = x_vals[i]
   y = y_vals[i]
   xx = np.sin(b*y) + cc*np.cos(b*x)
   yy = np.sin(a*x) + d*np.cos(a*y)
   # expanding in z-direction with zz = x*sin(a)
   x_vals.append(xx)
   y_vals.append(yy)
   

# Plot
ax.scatter(x_vals,y_vals,c='red', s=0.01)
ax.set(xlabel='x', ylabel='y')
plt.title("Pickover/Clifford Attractor")
plt.axis('square')
plt.show()
