#!/usr/bin/python3

if __name__ == "__main__":
    import sys

    length = len(sys.argv)
    if length > 0:
        print("{:d} arguments:".format(length - 1))
        for i in range(1, length):
            print("{:d}: {:s}".format(i, sys.argv[i]))

    else:
        print("0 arguments.")
