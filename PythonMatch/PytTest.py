# -*- coding: utf-8 -*-
"""
Created on Wed Sep 20 11:48:03 2023

@author: sbeskhmelnitsyn
"""


import matplotlib.pyplot as plt

# Создаем новую фигуру и оси
fig, ax = plt.subplots()

# Определяем координаты начала и конца вектора

vx, vy = -2, 2


ix, iy = 1, 0

jx, jy = 0, 1

pix_start, piy_start = ix, 0
pix_end, piy_end = 0, jy

pjx_start, pjy_start = 0, jy
pjx_end, pjy_end = ix, 0


# Рисуем вектор
ax.quiver(vx, vy, angles='xy', scale_units='xy', scale=1, color='b')

ax.quiver(ix, iy, angles='xy', scale_units='xy', scale=1, color='grey')

ax.quiver(jx, jy, angles='xy', scale_units='xy', scale=1, color='grey')

ax.quiver(pix_start, piy_start, pix_end, piy_end, angles='xy', scale_units='xy', 
          scale=1, color='grey')

ax.quiver(pjx_start, pjy_start, pjx_end, pjy_end, angles='xy', scale_units='xy', 
          scale=1, color='grey')

nix, niy = 1, 2
njx, njy = -2, -1

ax.quiver(nix, niy, angles='xy', scale_units='xy', 
          scale=1, color='r')

ax.quiver(njx, njy, angles='xy', scale_units='xy', 
          scale=1, color='y')

ax.quiver (vx*nix+vy*niy, vx*njx+jy*njy, angles='xy', scale_units='xy', 
          scale=1, color='black')







# Настройка осей
ax.set_xlim(-7, 7)
ax.set_ylim(-7, 7)
ax.axhline(0, color='black',linewidth=0.5)
ax.axvline(0, color='black',linewidth=0.5)
ax.grid(color = 'gray', linestyle = '--', linewidth = 0.5)

# Добавляем метки к осям
ax.set_xlabel('X-ось')
ax.set_ylabel('Y-ось')

# Добавляем заголовок
ax.set_title('Вектор на координатных осях')

# Добавляем легенду
ax.legend()

# Отображаем изображение на экране
plt.show()