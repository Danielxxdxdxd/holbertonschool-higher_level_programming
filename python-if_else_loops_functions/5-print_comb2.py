#!/usr/bin/python3
for numbers in range(00, 100):
    if numbers != 99:
        print("{:02}, ".format(numbers), end="")
    if numbers == 99:
        print("{:02}".format(numbers))
