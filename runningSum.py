# -*- coding: utf-8 -*-
"""
Created on Mon Jun 19 04:55:21 2017

@author: Win Htet Aung
"""

st = input()
a = []
for i in st.split(' '):
    a.append(int(i))

for i in range(1, len(a)):
    a[i] = a[i] + a[i - 1]
    
print(a)
