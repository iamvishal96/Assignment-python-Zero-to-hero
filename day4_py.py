# -*- coding: utf-8 -*-
"""day4.py

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1BXeVLj0CXOOEqdWxptLv9RLNHgc9Y5Gi
"""

Tv = {'BreakingBad':100, 'GameOfThrones':12, 'mirzapur' : 88}
 
Keymax = max(Tv, key= lambda x: Tv[x])
print(Keymax)