#!/usr/bin/python3
import sys
if __name__ == "__main__":
    arg_ct = len(sys.argv) - 1
    if arg_ct == 0:
        print(arg_ct)
    elif arg_ct == 1:
        print(sys.argv[2])
    else:
        result = 0
        for i in range(1, len(sys.argv)):
            result = result + int(sys.argv[i])
        print(result)
