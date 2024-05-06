#!/usr/bin/python3
def roman_to_int(roman_string):
    rom_num = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    int_num = 0
    if not roman_string or not isinstance(roman_string, str):
        return 0
    prev = rom_num[roman_string[0]]
    for i in roman_string:
        int_num += rom_num[i]
        if prev < rom_num[i]:
            int_num -= prev * 2
        prev = rom_num[i]
    return int_num
