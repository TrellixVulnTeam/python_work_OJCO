# -*- coding: utf-8 -*-
# @Author       : tongyuze
# @Date & Time  : 2019/4/3 22:01
# @FileName     : different_dice.py
# @Software     : PyCharm
# --------------
import pygal
import die

die_1 = die.Die()
die_2 = die.Die(10)

results = []
for roll_num in range(50000):
    result = die_1.roll() + die_2.roll()
    results.append(result)

# frequencies = []
# for value in range(2, die_1.num_side + die_2.num_side + 1):
#     frequency = results.count(value)
#     frequencies.append(frequency)

# 列表解析
frequencies = [results.count(value) for value in range(2, die_1.num_side + die_2.num_side + 1)]

hist = pygal.HorizontalBar()
hist.title = "Results of rolling a D6 and a D10 50000 times"
hist.x_title = "Results"
hist.y_title = "Frequency of Results"
# hist.x_labels = ['2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16']
hist.x_labels = [str(x) for x in range(2, die_1.num_side + die_2.num_side + 1)]

hist.add("D6+D10", frequencies)
hist.render_to_file('dif_dice_visual.svg')



