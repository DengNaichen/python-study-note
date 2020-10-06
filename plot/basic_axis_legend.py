
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-3, 3, 50)
y1 = 2 * x + 1
y2 = x **2 + 1


# plot two figure
plt.figure()
plt.plot(x, y1)

# set lengend
plt.figure(num=3, figsize=(8, 5))
l1, = plt.plot(x, y1, label='up')
l2, = plt.plot(x, y2, c='red', linewidth=1, linestyle="--", label='down')
plt.legend(handles=[l1, l2], labels=['aaa', 'bbb'], loc='best') # don't need , here

# handles is to choose which lines or parameters we want show in legend

# set limit of axis
plt.xlim((-1, 3))
plt.ylim((0, 10))

# set label of axis
plt.xlabel("I am x")
plt.ylabel("I am y")

# set ticks
new_ticks = np.linspace(-1, 2, 5)
print (new_ticks)
plt.xticks(new_ticks)

# set y axis ticks, and corresponding words
plt.yticks([-2, 1, 3, 5],
           [r"$very\ bad$", r'$bad$', r"$normal$", r"$good$"])

# gca = "get current axis"
ax = plt.gca()
# delete (don't show) right and top axis
ax.spines["right"].set_color("none")
ax.spines["top"].set_color("none")
ax.xaxis.set_ticks_position("bottom")
ax.yaxis.set_ticks_position('left')

# todo
ax.spines['bottom'].set_position(('data', 0))
ax.spines['left'].set_position(('data', 0))

# legend


plt.show()
