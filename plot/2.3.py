
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-3, 3, 100)
y = x **3 + 3

plt.figure(num=1, figsize=(8, 5),)
plt.plot(x, y,)

ax = plt.gca()
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
ax.spines['top'].set_color('none')
ax.xaxis.set_ticks_position('bottom')
ax.spines['bottom'].set_position(('data', 0))
ax.yaxis.set_ticks_position('left')
ax.spines['left'].set_position(('data', 0))


# 绘制线上的一个点
x0 = 1
y0 = x0 **3 + 3
plt.scatter(x0, y0, s=50, c="red")

# 绘制一条竖线
plt.plot([x0, x0], [y0, 0])

plt.annotate(r"$x^{3} + 3 = $")


plt.show()
