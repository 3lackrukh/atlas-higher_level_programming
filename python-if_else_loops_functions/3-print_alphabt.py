#!/usr/bin/python3
ascii_value = 96
while ascii_value < 122:
    ascii_value += 1
    if (ascii_value == 101 or ascii_value == 113):
        pass
    else:
        print("{}".format(chr(ascii_value)), end='')
