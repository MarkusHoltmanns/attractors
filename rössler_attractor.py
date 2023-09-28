import matplotlib.pyplot as plt
import numpy as np



def rössler(xyz,*,a=0.2, b=0.2, c=5.7):
   
    x, y, z = xyz
    x_dot = - y - z
    y_dot = x + a*y
    z_dot = b + z*(x-c)
    return np.array([x_dot, y_dot, z_dot])


dt = 0.001
num_steps = 100000

xyzs = np.empty((num_steps + 1, 3))
xyzs[0] = (0., 1., 1.05)
for i in range(num_steps):
    xyzs[i + 1] = xyzs[i] + rössler(xyzs[i]) * dt

# Plot
ax = plt.figure().add_subplot(projection='3d')
ax.plot(*xyzs.T, lw=0.5)
ax.set_xlabel("X Axis")
ax.set_ylabel("Y Axis")
ax.set_zlabel("Z Axis")
ax.set_title("Rössler Attractor")
plt.axis('square')
plt.axis('scaled')
plt.show()