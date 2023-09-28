import matplotlib.pyplot as plt
import numpy as np



def thomas(xyz,*,b=0.1998): # b = 0.208186 or 0.32899 or 0.1225 or else
    
    x, y, z = xyz
    x_dot = np.sin(y) - b*x
    y_dot = np.sin(z) - b*y
    z_dot = np.sin(x) - b*z
    return np.array([x_dot, y_dot, z_dot])


dt = 0.05
num_steps = 100000

xyzs = np.empty((num_steps + 1, 3))
xyzs[0] = (0.1, 1., 1.05) 

for i in range(num_steps):
    xyzs[i + 1] = xyzs[i] + thomas(xyzs[i]) * dt

# Plot
ax = plt.figure().add_subplot(projection='3d')
ax.plot(*xyzs.T, lw=0.5)

ax.set_xlabel("X Axis")
ax.set_ylabel("Y Axis")
ax.set_zlabel("Z Axis")
ax.set_title("Thomas Attractor")
plt.axis('square')
plt.axis('scaled')
plt.show()
