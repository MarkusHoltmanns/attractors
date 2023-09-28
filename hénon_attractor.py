import matplotlib.pyplot as plt
import numpy as np



fig, ax = plt.subplots()
num_steps = 1000

a = 1.4 
b = 0.3
x = 0.5 
y = 0.5
for i in range(num_steps):
   xx = y + 1. - a*x*x
   yy = b*x
   x=xx
   y=yy
   ax.scatter(xx,yy,c='red', s=0.1)

# Plot
ax.set(xlabel='x', ylabel='y')
plt.title("Hénon Attractor")
plt.axis('square')
#plt.axis('scaled')
plt.show()
