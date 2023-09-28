import matplotlib.pyplot as plt
import numpy as np


fig, ax = plt.subplots()
num_steps = 100000
#a,b,cc,d = -1.24458046630025,-1.25191834103316,-1.81590817030519,-1.90866735205054
a,b,cc,d = -0.709,1.638,0.452,1.740

x_vals = []
y_vals = []
x_vals,y_vals = [0.],[0.] # [-0.72],[-0.64]
for i in range(num_steps):
   x = x_vals[i]
   y = y_vals[i]
   xx = np.sin(a*y) + np.cos(b*x)
   yy = np.sin(cc*x) + np.cos(d*y)
   x_vals.append(xx)
   y_vals.append(yy)
   

# Plot
ax.scatter(x_vals,y_vals,c='red', s=0.01)
ax.axis('equal')
ax.set(xlabel='x', ylabel='y')
plt.title("Peter de Jong Attractor")

plt.show()
