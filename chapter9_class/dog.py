# -*- coding: utf-8 -*-
# @Author       : tongyuze
# @Date & Time  : 2019/3/19 19:38
# @FileName     : dog.py
# @Software     : PyCharm
# --------------


class Dog:
    """一次模拟小狗的简单尝试"""

    def __init__(self, name, age):
        """初始化属性 name & age"""
        self.name = name
        self.age = age

    def sit(self):
        """模拟小狗蹲下"""
        print(self.name.title() + " is now sitting.")

    def roll_over(self):
        """模拟小狗打滚"""
        print(self.name.title() + " rolled over!")


my_dog = Dog('willie', 6)
# 访问属性
print("My dog's name is " + my_dog.name.title() + ".")
print("My dog is " + str(my_dog.age) + " years old.")
# 调用方法
my_dog.sit()
my_dog.roll_over()

your_dog = Dog('lucy', 3)
# 访问属性
print("\nYour dog's name is " + your_dog.name.title() + ".")
print("Your dog is " + str(your_dog.age) + " years old!")
# 调用方法
your_dog.sit()
your_dog.roll_over()
