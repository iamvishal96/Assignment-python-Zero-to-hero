# -*- coding: utf-8 -*-
"""day2.py

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1BXeVLj0CXOOEqdWxptLv9RLNHgc9Y5Gi
"""

lottery = "hello coders"
# 'h' or 'e' or 'o' or 'c' or 'd'

print("Choose correct character of the word '",lottery,"' to win the lottery")

inputs = input(" ").lower()

if inputs == lottery[0] or inputs == lottery[1] or inputs == lottery[4] or inputs == lottery[6] or inputs == lottery[8]:
    print("congratulation, you are a winner")
else:
    print ("Sorry, better luck next time")