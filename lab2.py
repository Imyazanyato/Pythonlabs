# -*- coding: utf-8 -*-
"""Untitled1.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1_jBPxFZ3mqGtq75xIx6Si-4t_9Hn_vgP
"""

a = True
b = False
print (a & b)
print((a & b)| b)
print((a & b)^(a & b))
print((a & b ^(a & b)| b))
print(b & b ^ a & (a | b | a) ^ (a | b))
print(1 << 2)
print(1 & 0 | 1 >> 1)
print(0b101 & 0b111 ^ 0b111 | 0b010)

a, b = int(input()), int(input())
if a > b:
    print(b)
else:
    print(a)



a, b, c = int(input()), int(input()), int(input())
if (a > b) and (a > c):
 print(a)
elif (b > a) and (b > c):
 print(b)
else:
 print(c)

a, b, c = int(input()), int(input()), int(input())
q ={a, b, c}
print(len(q))


