import matplotlib.pyplot as plt
import numpy as np
import random



def aizawa(xyz,*,a = 0.95, b = 0.7, cc = 0.65, d = 3.5, e = 0.25, f = 0.1):
   
    x, y, z = xyz
    x_dot = (z-b)*x - d*y
    y_dot = d*x + (z-b)*y
    z_dot = cc + a*z - z*z*z/3 - (x*x + y*y)*(1+e*z) + f*z*x*x*x

    return np.array([x_dot, y_dot, z_dot])

plt.style.use('dark_background')
ax = plt.figure(dpi=200).add_subplot(projection='3d')
dt = 0.05 # best not go bigger than 0.1
num_steps = 10000
particlenumber = 100
xyzs = np.empty((num_steps + 1, 3))
for particles in range(particlenumber):
    print("Calculating attractor shape for particle nr. ",particles+1)
    x_vals = []
    y_vals = []
    z_vals = []    
    xyzs[0] = (random.uniform(-1, 1),random.uniform(-1, 1),random.uniform(-1, 1)) 
    #cmap = hsv #(random.uniform(0.3, 1), random.uniform(0.3, 1), random.uniform(0.3, 1))
    cmap = plt.cm.hsv((2*particles+1)/(2*particlenumber))
    #print (xyzs[0])
    for i in range(num_steps):
        xyzs[i + 1] = xyzs[i] + aizawa(xyzs[i]) * dt
        if i > 50:
            x_vals.append(xyzs[i-51][0])
            y_vals.append(xyzs[i-51][1])
            z_vals.append(xyzs[i-51][2])
                
    plt.plot(x_vals,y_vals, z_vals,c=cmap, linewidth=0.01)

# Plot
ax.axis('equal')
ax.axis(False)
#ax.set_xlabel("X Axis")
#ax.set_ylabel("Y Axis")
#ax.set_zlabel("Z Axis")

ax.set_facecolor('black')
ax.grid(False)
ax.xaxis.set_pane_color((0.0, 0.0, 0.0, 0.0))
ax.yaxis.set_pane_color((0.0, 0.0, 0.0, 0.0))
ax.zaxis.set_pane_color((0.0, 0.0, 0.0, 0.0))

ax.set_title("Aizawa Attractor")
filename = "/Users/Holtmanns/Desktop/aizawa_attractor.png"
plt.savefig(filename, dpi=1200)
plt.show()
