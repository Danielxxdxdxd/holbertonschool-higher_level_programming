#!/usr/bin/python3
from sys import argv


def run():
    if len(argv) == 1:
        print("0 arguments.")
    elif len(argv) == 2:
        print("1 argument:\n1: {}".format(argv[1]))
    elif len(argv) > 2:
        print("{} arguments:".format(len(argv) - 1))
        for indx in range(1, len(argv)):
            print("{}: {}".format(indx, argv[indx]))


if __name__ == "__main__":
    run()
