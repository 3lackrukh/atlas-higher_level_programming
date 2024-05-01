#!/usr/bin/python3
for i in range(1,90):
    if (i / 10 % 10 > i % 10):
        pass
    elif (i == 90 - 1):
        print("{:02d}".format(i))
    else:
        print("{:02d}".format(i), end=', ')
