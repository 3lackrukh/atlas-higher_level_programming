#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last_digit = abs(number) % 10
str1 = "Last digit of"
str2 = "is"
neg = "-"
if number < 0:
    print (str1, number, str2, neg, last_digit, sep=' ')
else:
    print (str1, number, str2, last_digit, sep=' ')
