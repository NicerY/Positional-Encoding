import matplotlib.pyplot as plt
import numpy as np
import math

max = 4*math.pi
# 生成数据
t = np.linspace(0, max, 1000)  # 生成自变量 t 的范围
x = np.sin(t)
y = np.sin(t / 2)
z = np.sin(t / 4)

# 计算颜色值
colors = t / max  # 将 t 映射到 [0, 1] 之间，作为颜色值

# 创建三维图形对象
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# 绘制三维点，并添加颜色映射
sc = ax.scatter(x, y, z, c=colors, cmap='viridis', marker='o')

# 设置颜色映射条
cbar = fig.colorbar(sc, ax=ax, orientation='vertical')
cbar.set_label('Color Map')

# 设置图形属性
ax.set_xlabel('X Label')
ax.set_ylabel('Y Label')
ax.set_zlabel('Z Label')
ax.set_title('3D Points Visualization with Color Map')

# 显示图形
plt.show()