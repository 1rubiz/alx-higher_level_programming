#!/usr/bin/python3

if __name__ == "__main__":
import sys


length = len(sys.argv)
if length > 0:
    print(f"{length - 1} arguments:")
    for i in range(1, length):
        print(f"{i}: {sys.argv[i]}")

else:
    print(f"0 arguments.")
