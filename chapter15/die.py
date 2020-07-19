# -*- coding: utf-8 -*-
# @Author       : tongyuze
# @Date & Time  : 2019/4/3 9:40
# @FileName     : die.py
# @Software     : PyCharm
# --------------
from random import  randint


class Die:
    """表示一个骰子的类"""

    def __init__(self, num_sides=6):
        """骰子默认6个面"""
        self.num_side = num_sides

    def roll(self):
        """返回一个位于1和骰子面数之间的随机值"""
        return randint(1, self.num_side)
