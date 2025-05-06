#!/usr/bin/python3

from sys import argv

if __name__ == "__main__":
    if len(argv) == 1:
        print("0 arguments.")
    else:
        count = len(argv) - 1
        print("{:d} argument{:s}:".format(count, ("" if count == 1 else "s")))
        for i in range(1, len(argv)):
            print("{:d}: {:s}".format(i, argv[i]))
