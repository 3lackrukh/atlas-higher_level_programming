#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last_digit = abs(number) % 10
str1 = "Last digit of"
str2 = "is"
str3 = "and is greater than 5"
str4 = "and is less than 6 and not 0"
str5 = "and is 0"
if number < 0:
    if last_digit == 0:
        print (str1, number, str2, (last_digit * -1), str5, sep=' ')
    else:
        print (str1, number, str2, (last_digit * -1) ,str4, sep=' ')
else:
    print (str1, number, str2, last_digit, sep=' ')
