#!/usr/bin/python3
import sys
if __name__ == "__main__":
    arg_ct = len(sys.argv)
    if arg_ct == 1:
        print("0 arguments.")
    elif arg_ct == 2:
        print("1 argument:")
        print(f"1: {sys.argv[1]}")
    else:
        print(f"{arg_ct - 1} arguments:")
        for i, arg in enumerate(sys.argv[1:], start=1):
            print(f"{i}: {arg}")
