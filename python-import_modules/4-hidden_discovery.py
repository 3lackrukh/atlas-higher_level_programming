#!/usr/bin/python3
import hidden_4

if __name__ == "__main__":
    names = dir(hidden_4)
    srt_names = sorted(name for name in names if not name.startswith("__"))
    for name in srt_names:
        print(name)
