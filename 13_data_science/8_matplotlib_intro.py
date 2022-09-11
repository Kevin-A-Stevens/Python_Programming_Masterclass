"""
Matplotlib is plotting library
works well with numpy arrays and pandas
install with pip3 install matplotlib

https://matplotlib.org/stable/gallery/index
"""
import matplotlib.pyplot as plt

"""
If in Jupyter Notebook use:
%matplotlib inline

Use plt.show() if using your IDE
"""

import numpy as np

x = np.linspace(0,5,11)
y = x ** 2

print(x)
print(y)

# FUNCTIONAL
# plt.plot(x,y)
# plt.xlabel('X Label')
# plt.ylabel('Y Label')
# plt.title('Title')
# plt.show()

# plt.subplot(1, 2, 1)  # rows, columns, figure
# plt.plot(x,y, 'r')
# plt.subplot(1,2,2)
# plt.plot(y,x,'b')
# plt.show()

# OBJECT ORIENTED
# fig = plt.figure()
# axes = fig.add_axes([0.1,0.1,0.8,0.8])  # List = Left, Bottom, Width, Height
# axes.plot(x,y)
# axes.set_xlabel('X_Label')
# axes.set_ylabel('Y Label')
# axes.set_title('Set Title')
# plt.show()

# fig = plt.figure()
# axes1 = fig.add_axes([0.1,0.1,0.8,0.8])
# axes2 = fig.add_axes([0.2,0.5,0.4,0.3])
#
# axes1.plot(x,y)
# axes2.plot(y,x)
# axes2.set_title('Small Plot')
# axes1.set_title('Large Plot')
# plt.show()

# fig,axes = plt.subplots(nrows=1,ncols=2)
# plt.tight_layout()  # fixes overlaps
# axes.plot(x,y)

# for current_ax in axes:
#     current_ax.plot(x,y)
#
# axes[0].plot(x,y)
# axes[0].set_title('First Plot')
# axes[1].plot(y,x)
# axes[1].set_title('Second Plot')
# plt.show()

# fig,axes = plt.subplots(nrows=2, ncols=1, figsize=(8,2))
# axes[0].plot(x,y)
# axes[1].plot(y,x)
# plt.tight_layout()

# ax = fig.add_axes([0,0,1,1])
# ax.plot(x,y)
# fig.savefig('my_picture.png', dpi=200)
# plt.show()

fig = plt.figure()
ax = fig.add_axes([0,0,1,1])
ax.plot(x,y,color='#FF8C00',
        linewidth=3,
        alpha=0.5,
        linestyle='--'
        ,marker='o',
        markersize=10,
        markerfacecolor='yellow',
        markeredgewidth=3,
        markeredgecolor='green')  # alpha = transparency
plt.show()


