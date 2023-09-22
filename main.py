# -*- coding: utf-8 -*-
"""
Created on Wed Sep 20 11:48:03 2023

@author: sbeskhmelnitsyn
"""

import matplotlib.pyplot as plt

# Создаем новую фигуру и оси
fig, ax = plt.subplots()

# Определяем координаты начала и конца вектора


# i

ix, iy = 1, 0

# j

jx, jy = 0, 1

# v
vx, vy = -2, 2

# vector v
ax.quiver(vx, vy, angles='xy', scale_units='xy', scale=1, color='b', label='v')

# i1
nix, niy = 1, 2

# j1
njx, njy = -2, -1

# vector i1
ax.quiver(nix, niy, angles='xy', scale_units='xy',
          scale=1, color='green', label='i1')

# vector j1
ax.quiver(njx, njy, angles='xy', scale_units='xy',
          scale=1, color='grey', label='j1')

# vector v1

ax.quiver(vx * nix + vy * njx, vx * niy + vy * njy, angles='xy', scale_units='xy',
          scale=1, color='y', label='v1')

# Настройка осей
ax.set_xlim(-7, 7)
ax.set_ylim(-7, 7)
ax.axhline(0, color='black', linewidth=0.5)
ax.axvline(0, color='black', linewidth=0.5)
ax.grid(color='gray', linestyle='--', linewidth=0.5)

# Добавляем метки к осям
ax.set_xlabel('X-ось')
ax.set_ylabel('Y-ось')

# Добавляем заголовок
ax.set_title('Вектор на координатных осях')

# Добавляем легенду
ax.legend()

# Отображаем изображение на экране
plt.show()

print (vx * nix + vy * njx, vx * niy + vy * njy)
