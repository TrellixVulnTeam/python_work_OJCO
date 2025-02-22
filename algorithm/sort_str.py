# !/usr/bin/python3
# -*- coding: utf-8 -*-

"""
@ Author       : tongyuze
@ Project      : algorithm
@ Date & Time  : 2020/8/11 22:51
@ FileName     : sort_str.py
@ Description  : 字符串排序
"""
"""
规则 1 ：英文字母从 A 到 Z 排列，不区分大小写。如，输入： Type 输出： epTy
规则 2 ：同一个英文字母的大小写同时存在时，按照输入顺序排列。如，输入： BabA 输出： aABb
规则 3 ：非英文字母的其它字符保持原来的位置。如，输入： By?e 输出： Be?y
"""
xin = input()

alpha, arg_other = [], []
for i, v in enumerate(xin):
    if v.isalpha():
        alpha.append(v)
    else:
        arg_other.append(i)
alpha.sort(key=lambda x: x.lower())

xout = []
for i in range(len(xin)):
    if i in arg_other:
        xout.append(xin[i])
    else:
        xout.append(alpha[0])
        alpha.pop(0)

print(''.join(xout))
