import numpy as np
import matplotlib.pyplot as plt

# 行星的质量
M = 1.989e30  # 太阳质量
m = 5.972e24  # 地球质量

# 初始位置和速度
r0 = np.array([1.496e11, 0])  # 地球的初始位置（以太阳为原点）
v0 = np.array([0, 29783])  # 地球的初始速度（以轨道速度为基准）

# Gravitational constant
G = 6.67430e-11

# 时间步长和总时间
dt = 3600  # 步长为1小时
total_time = 365 * 24 * 3600  # 模拟一年

# 计算轨道
r = [r0]
v = [v0]

for t in range(0, total_time, dt):
    r_mag = np.linalg.norm(r[-1])  # 计算当前位置的距离
    a = -G * M * r[-1] / r_mag**3  # 计算加速度
    v_new = v[-1] + a * dt  # 更新速度
    r_new = r[-1] + v_new * dt  # 更新位置
    v.append(v_new)
    r.append(r_new)

# 提取轨道数据
x = [pos[0] for pos in r]
y = [pos[1] for pos in r]

# 绘制轨道图
plt.plot(x, y)
plt.scatter(0, 0, color='orange', label='Sun')
plt.scatter(x[-1], y[-1], color='blue', label='Earth')
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Earth Orbit')
plt.legend()
plt.axis('equal')
plt.show()
