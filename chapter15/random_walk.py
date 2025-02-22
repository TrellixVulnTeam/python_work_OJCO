# -*- coding: utf-8 -*-
# @Author       : tongyuze
# @Date & Time  : 2019/4/2 23:37
# @FileName     : random_walk.py
# @Software     : PyCharm
# --------------
from random import choice


class RandomWalk:
    """一个生成随机漫步数据的类"""

    def __init__(self, num_points=5000):
        """初始化随机漫步的属性"""
        self.num_points = num_points

        # 所有随机漫步都起始于（0，0）
        self.x_value = [0]
        self.y_value = [0]

    def fill_walk(self):
        """计算随机漫步包含的所有点"""

        # 不断漫步，直到达到列表指定的长度
        while len(self.x_value) < self.num_points:
            # 决定前进的方向和前进的距离
            x_direction = choice([-1, 1])
            x_distance = choice([0, 1, 2, 3, 4])
            x_step = x_direction * x_distance

            y_direction = choice([-1, 1])
            y_distance = choice([0, 1, 2, 3, 4])
            y_step = y_direction * y_distance

            # 拒绝原地踏步
            if x_step == 0 and y_step == 0:
                continue

            # 计算下一个点的x和y值
            next_x = self.x_value[-1] + x_step
            next_y = self.y_value[-1] + y_step
            self.x_value.append(next_x)
            self.y_value.append(next_y)
