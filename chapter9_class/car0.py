# -*- coding: utf-8 -*-
# @Author       : tongyuze
# @Date & Time  : 2019/3/19 22:38
# @FileName     : car0.py
# @Software     : PyCharm
# --------------


# 创建父类Car
class Car:
    """一次模拟汽车的简单尝试"""

    def __init__(self, make, model, year):
        """初始化描述汽车的属性"""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0   # 指定默认值

    def get_descriptive_name(self):
        """返回整洁的描述性信息"""
        long_name = str(self.year) + " " + self.make + " " + self.model
        return long_name.title()

    def read_odometer(self):
        """读取汽车里程"""
        print("This car has " + str(self.odometer_reading) + " miles on it.")

    def update_odometer(self, mileage):
        """将里程表读数设置为指定的值"""
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")

    def increment_odometer(self, miles):
        """将里程表读数增加指定的量"""
        if miles >= 0:
            self.odometer_reading += miles
        else:
            print("You can't roll back an odometer!")


# 创建子类ElectricCar
class ElectricCar(Car):
    """电动汽车的独特之处"""

    def __init__(self, make, model, year, battery_size):
        """初始化父类的属性"""
        super().__init__(make, model, year)
        self.batter_size = battery_size

    def describe_battery(self):
        """描述电动汽车的电池容量"""
        print("This electric car has a " + str(self.batter_size) + "-kWh battery.")


# 实例化父类Car
my_new_car = Car('Audi', 'A4', 2016)
print(my_new_car.get_descriptive_name())
my_new_car.update_odometer(23)
my_new_car.read_odometer()
my_new_car.update_odometer(14)
my_new_car.read_odometer()
my_new_car.increment_odometer(1500)
my_new_car.read_odometer()
my_new_car.increment_odometer(-100)
my_new_car.read_odometer()

# 实例化子类ElectricCar
my_tesla = ElectricCar('tesla', 'model s', '2106', '100')
print(my_tesla.get_descriptive_name())
my_tesla.update_odometer(600)
my_tesla.read_odometer()
my_tesla.increment_odometer(90)
my_tesla.read_odometer()
my_tesla.describe_battery()
